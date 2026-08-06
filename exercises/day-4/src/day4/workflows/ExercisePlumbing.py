import csv
import json
from datetime import UTC, datetime
from pathlib import Path
from uuid import uuid4

from langchain_core.language_models.chat_models import BaseChatModel
from naas_abi_core.models.Model import ChatModel
from naas_abi_core.services.agent.Agent import AgentSharedState

from day4.agents.CriticAgentAgent import CriticAgentAgent
from day4.agents.FeedbackModels import CriticFeedback, HypothesisFeedback
from day4.agents.HypothesisAgentAgent import HypothesisAgentAgent
from day4.integrations.ZebraProposalIntegration import (
    ValidationAttempt,
    validation_result,
    validation_tool,
)


class AgentRuntime:
    """ABI plumbing: invoke each agent with a fresh conversation thread."""

    def __init__(self, chat_model: BaseChatModel | ChatModel | None = None):
        self.chat_model = chat_model
        self.validation_attempts: list[ValidationAttempt] = []

    def hypothesize(
        self,
        prompt: str,
        ontology_path: Path,
        active_round: int,
        use_validation: bool,
        validation_shapes: Path,
        max_validation_attempts: int,
    ) -> HypothesisFeedback:
        self.validation_attempts = []
        tools = []
        if use_validation:
            tools.append(
                validation_tool(
                    active_round,
                    ontology_path,
                    self.validation_attempts,
                    shapes_path=validation_shapes,
                    max_attempts=max_validation_attempts,
                )
            )
        agent = HypothesisAgentAgent.New(
            AgentSharedState(thread_id=f"hypothesis-{uuid4()}"),
            additional_tools=tools,
            chat_model=self.chat_model,
        )
        return HypothesisFeedback.model_validate_json(agent.invoke(prompt))

    def criticize(self, prompt: str) -> CriticFeedback:
        agent = CriticAgentAgent.New(
            AgentSharedState(thread_id=f"critic-{uuid4()}"),
            chat_model=self.chat_model,
        )
        return CriticFeedback.model_validate_json(agent.invoke(prompt))


class RunArtifacts:
    """File plumbing: write exact JSON, readable Markdown, and the CSV summary."""

    def __init__(
        self,
        runs_directory: Path = Path("runs"),
        csv_template: Path = Path("templates/agent-run-log.csv"),
        log_filename: str = "agent-run-log.csv",
    ):
        timestamp = datetime.now(UTC).strftime("%Y%m%d-%H%M%S-%f")
        self.run_directory = runs_directory / f"day4-run-{timestamp}"
        self.run_directory.mkdir(parents=True)
        self.log_path = self.run_directory / log_filename

        with csv_template.open(newline="", encoding="utf-8") as template:
            self.fields = next(csv.reader(template))
        with self.log_path.open("w", newline="", encoding="utf-8") as log:
            csv.DictWriter(log, fieldnames=self.fields).writeheader()

        print(f"Run log: {self.log_path}", flush=True)

    def save_snapshot(self, directory: str, snapshot: str) -> None:
        self._stage_directory(directory).joinpath("ontology-snapshot.md").write_text(
            snapshot, encoding="utf-8"
        )

    def save_feedback(self, directory, stage, attempt, feedback) -> None:
        agent_name = "hypothesis" if isinstance(feedback, HypothesisFeedback) else "critic"
        stem = f"{agent_name}-attempt-{attempt}"
        stage_directory = self._stage_directory(directory)
        stage_directory.joinpath(f"{stem}.json").write_text(
            feedback.model_dump_json(indent=2) + "\n", encoding="utf-8"
        )
        stage_directory.joinpath(f"{stem}.md").write_text(
            feedback_markdown(stage, attempt, feedback), encoding="utf-8"
        )

    def save_validation_attempts(
        self,
        directory: str,
        hypothesis_attempt: int,
        attempts: list[ValidationAttempt],
        enabled: bool,
    ) -> None:
        stage_directory = self._stage_directory(directory)
        summary = [
            "# Arrangement Validation",
            "",
            f"- Hypothesis attempt: {hypothesis_attempt}",
            f"- Checker calls: {len(attempts)}",
            "",
        ]

        if not enabled:
            summary.append("SHACL validation was disabled for this experiment.\n")
        elif not attempts:
            summary.append("The Hypothesis Agent did not call `validate_arrangement`.\n")

        for check, attempt in enumerate(attempts, 1):
            stem = f"hypothesis-attempt-{hypothesis_attempt}-check-{check}"
            result = validation_result(attempt)
            stage_directory.joinpath(f"{stem}-proposal.ttl").write_text(
                attempt.proposal_turtle, encoding="utf-8"
            )
            stage_directory.joinpath(f"{stem}-report.ttl").write_text(
                attempt.report_turtle, encoding="utf-8"
            )
            stage_directory.joinpath(f"{stem}-result.json").write_text(
                json.dumps(result, indent=2) + "\n", encoding="utf-8"
            )
            stage_directory.joinpath(f"{stem}-result.md").write_text(
                validation_markdown(hypothesis_attempt, check, result),
                encoding="utf-8",
            )
            summary.extend(
                [
                    f"## Check {check}",
                    "",
                    f"- Zebra owner: {result['zebra_owner']}",
                    f"- Conforms: {'yes' if result['conforms'] else 'no'}",
                    "",
                    result["interpretation"],
                    "",
                ]
            )

        stage_directory.joinpath(
            f"hypothesis-attempt-{hypothesis_attempt}-validation-summary.md"
        ).write_text("\n".join(summary), encoding="utf-8")

    def record_stage(
        self,
        model,
        experiment,
        components,
        stage,
        ontology_supplied,
        critic_enabled,
        validation_enabled,
        snapshot,
        hypothesis,
        model_checker_evidence,
        critique,
        revision_count,
    ) -> None:
        row = {
            "Model": model,
            "Experiment": experiment,
            "Components": components,
            "Stage": stage,
            "Ontology supplied": "yes" if ontology_supplied else "no",
            "Critic enabled": "yes" if critic_enabled else "no",
            "SHACL enabled": "yes" if validation_enabled else "no",
            "Ontology snapshot": snapshot,
            "Leading hypothesis": hypothesis.leading_hypothesis,
            "Confidence": hypothesis.confidence,
            "Supporting axioms": "; ".join(hypothesis.supporting_axiom_ids),
            "Reasoning steps": "\n".join(
                f"{index}. {step}"
                for index, step in enumerate(hypothesis.reasoning_steps, 1)
            ),
            "Unstated assumptions": "; ".join(hypothesis.unstated_assumptions),
            "Best alternative": hypothesis.best_competing_hypothesis,
            "Most useful missing information": (
                hypothesis.most_useful_missing_information
            ),
            "Status claimed": hypothesis.status,
            "Model-checker evidence": model_checker_evidence,
            "Critic findings": (
                critic_markdown(critique)
                if critique is not None
                else "Critic Agent not used in this experiment."
            ),
            "Revision count": revision_count,
        }
        with self.log_path.open("a", newline="", encoding="utf-8") as log:
            csv.DictWriter(log, fieldnames=self.fields).writerow(row)

    def _stage_directory(self, directory: str) -> Path:
        path = self.run_directory / directory
        path.mkdir(parents=True, exist_ok=True)
        return path


def feedback_markdown(stage, attempt, feedback) -> str:
    if isinstance(feedback, HypothesisFeedback):
        return f"""# Hypothesis Agent Output

- Stage: {stage}
- Attempt: {attempt}

## Leading hypothesis

{feedback.leading_hypothesis}

## Confidence

{feedback.confidence}

## Supporting axioms

{bullet_list(feedback.supporting_axiom_ids)}

## Reasoning steps

{numbered_list(feedback.reasoning_steps)}

## Unstated assumptions

{bullet_list(feedback.unstated_assumptions)}

## Best competing hypothesis

{feedback.best_competing_hypothesis}

## Most useful missing information

{feedback.most_useful_missing_information}

## Status

{feedback.status}
"""

    return f"""# Critic Agent Output

- Stage: {stage}
- Attempt: {attempt}

{critic_markdown(feedback)}
"""


def critic_markdown(critique) -> str:
    return "\n".join(
        [
            f"Assessment: {critique.assessment.replace('_', ' ')}",
            f"Revision required: {'yes' if critique.revision_required else 'no'}",
            "",
            f"Summary: {critique.summary}",
            "",
            critic_section("Absent axiom IDs", critique.absent_axiom_ids),
            "",
            critic_section("Unsupported inferences", critique.unsupported_inferences),
            "",
            critic_section("Hidden assumptions", critique.hidden_assumptions),
            "",
            critic_section("Ontology conflicts", critique.ontology_conflicts),
            "",
            "Highest-value additional axiom or query:",
            critique.highest_value_additional_axiom_or_query,
        ]
    )


def validation_markdown(hypothesis_attempt, check, result) -> str:
    violations = result["violations"]
    violation_lines = (
        "- None"
        if not violations
        else "\n".join(
            f"- {item['axiom_id']}: {item['message']}" for item in violations
        )
    )
    return f"""# Arrangement Validation Result

- Hypothesis attempt: {hypothesis_attempt}
- Check: {check}
- Active round: {result['active_round']}
- Zebra owner: {result['zebra_owner']}
- Conforms: {'yes' if result['conforms'] else 'no'}

## Violated axioms

{violation_lines}

## Interpretation

{result['interpretation']}
"""


def critic_section(title, values) -> str:
    return f"{title}: None" if not values else f"{title}:\n{bullet_list(values)}"


def bullet_list(values) -> str:
    return "- None" if not values else "\n".join(f"- {value}" for value in values)


def numbered_list(values) -> str:
    return "\n".join(f"{index}. {value}" for index, value in enumerate(values, 1))
