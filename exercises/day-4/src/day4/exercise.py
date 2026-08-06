from dataclasses import dataclass
from pathlib import Path
from typing import Annotated, Literal

from pydantic import BaseModel, ConfigDict, Field, model_validator

from day4.agents.FeedbackModels import CriticFeedback, HypothesisFeedback
from day4.integrations.ZebraProposalIntegration import (
    ValidationAttempt,
    validation_result,
)
from day4.workflows.ExercisePlumbing import AgentRuntime, RunArtifacts
from scripts.export_current_axioms import export_axioms


@dataclass(frozen=True)
class Stage:
    """One cumulative ontology state in the exercise."""

    name: str
    directory: str
    active_round: int
    ontology_path: Path


StageKey = Literal["core", "round-1", "round-2", "round-3", "round-4"]
ResidentId = Annotated[str, Field(pattern=r"^Resident_[A-E]$")]


class PromptConfiguration(BaseModel):
    model_config = ConfigDict(extra="forbid")

    hypothesis: list[str] = Field(min_length=1)
    critic: list[str] = Field(min_length=1)


class StageConfiguration(BaseModel):
    model_config = ConfigDict(extra="forbid")

    name: str
    directory: str = Field(pattern=r"^[a-z0-9][a-z0-9-]*$")
    active_round: int = Field(ge=0, le=4)
    ontology: str


class ValidationConfiguration(BaseModel):
    model_config = ConfigDict(extra="forbid")

    shapes: str
    max_checker_attempts: int = Field(ge=1, le=10)


class Experiment(BaseModel):
    """One JSON-defined combination of grounding and feedback components."""

    model_config = ConfigDict(extra="forbid")

    id: str = Field(pattern=r"^[a-z0-9][a-z0-9-]*$")
    name: str
    learning_question: str
    stages: list[StageKey] = Field(min_length=1)
    use_ontology: bool
    use_critic: bool
    use_shacl: bool
    max_revisions: int = Field(ge=0, le=3)

    @model_validator(mode="after")
    def component_dependencies_are_valid(self):
        if self.use_shacl and not self.use_ontology:
            raise ValueError("SHACL requires an ontology snapshot")
        if self.max_revisions and not self.use_critic:
            raise ValueError("Revisions require the Critic Agent")
        return self

    @property
    def components(self) -> str:
        enabled = ["Hypothesis Agent"]
        if self.use_ontology:
            enabled.append("ontology")
        if self.use_critic:
            enabled.append("Critic Agent")
        if self.use_shacl:
            enabled.append("SHACL checker")
        return " + ".join(enabled)


class ReasonerCheckConfiguration(BaseModel):
    model_config = ConfigDict(extra="forbid")

    execution: Literal["manual"]
    ontology: str
    query: str
    purpose: str


class OutputConfiguration(BaseModel):
    model_config = ConfigDict(extra="forbid")

    csv: str = Field(pattern=r"^[^/\\]+\.csv$")


class ExerciseConfiguration(BaseModel):
    """Validated, student-readable configuration for the entire exercise."""

    model_config = ConfigDict(extra="forbid")

    schema_version: Literal[1]
    title: str
    learning_goal: str
    question: str
    candidates: list[ResidentId] = Field(min_length=2)
    prompts: PromptConfiguration
    stages: dict[StageKey, StageConfiguration]
    validation: ValidationConfiguration
    experiments: list[Experiment] = Field(min_length=1)
    final_reasoner_check: ReasonerCheckConfiguration
    output: OutputConfiguration

    @model_validator(mode="after")
    def identifiers_are_unique(self):
        ids = [experiment.id for experiment in self.experiments]
        if len(ids) != len(set(ids)):
            raise ValueError("Experiment IDs must be unique")
        if len(self.candidates) != len(set(self.candidates)):
            raise ValueError("Candidate IDs must be unique")
        configured_stages = set(self.stages)
        referenced_stages = {
            stage for experiment in self.experiments for stage in experiment.stages
        }
        if missing := referenced_stages - configured_stages:
            raise ValueError(f"Experiments reference missing stages: {sorted(missing)}")
        return self

    @property
    def hypothesis_prompt(self) -> str:
        candidates = ", ".join(f"`{item}`" for item in self.candidates)
        return "\n\n".join(
            [
                "# Hypothesis Agent task",
                f"Question: {self.question}",
                f"Candidate identifiers: {candidates}",
                *self.prompts.hypothesis,
            ]
        )

    @property
    def critic_prompt(self) -> str:
        return "\n\n".join(["# Critic Agent task", *self.prompts.critic])


def load_exercise_configuration(
    path: Path = Path("exercise.json"),
) -> ExerciseConfiguration:
    """Load the single declarative exercise file with clear validation errors."""
    return ExerciseConfiguration.model_validate_json(path.read_text(encoding="utf-8"))


ValidationHistory = list[tuple[int, int, ValidationAttempt]]


class ZebraExercise:
    """Provided agent, ontology, validation, and artifact building blocks."""

    def __init__(
        self,
        configuration: ExerciseConfiguration,
        runtime: AgentRuntime | None = None,
        artifacts: RunArtifacts | None = None,
        model_id: str = "default",
    ):
        self.configuration = configuration
        self.model_id = model_id
        self.runtime = runtime or AgentRuntime()
        self.artifacts = artifacts or RunArtifacts(
            log_filename=configuration.output.csv
        )
        self.hypothesis_prompt = configuration.hypothesis_prompt
        self.critic_prompt = configuration.critic_prompt

    def stages_for(self, experiment: Experiment) -> list[Stage]:
        stages = []
        for key in experiment.stages:
            configured = self.configuration.stages[key]
            stages.append(
                Stage(
                    configured.name,
                    configured.directory,
                    configured.active_round,
                    Path(configured.ontology),
                )
            )
        return stages

    def start(self, experiment: Experiment, stage: Stage) -> "StageSession":
        """Prepare the exact input exposed by one experiment configuration."""
        snapshot = (
            export_axioms(stage.ontology_path)
            if experiment.use_ontology
            else "No ontology snapshot was supplied to the Hypothesis Agent."
        )
        model_directory = (
            self.model_id.replace("/", "-").replace(":", "-").replace(".", "-")
        )
        directory = f"{model_directory}/{experiment.id}/{stage.directory}"
        self.artifacts.save_snapshot(directory, snapshot)
        return StageSession(self, experiment, stage, directory, snapshot)

    def complete(self) -> None:
        print(
            f"\nExperiment complete. Run log: {self.artifacts.log_path}",
            flush=True,
        )


class StageSession:
    """Hypothesize, critique, revise, and record one ontology stage."""

    def __init__(
        self,
        exercise: ZebraExercise,
        experiment: Experiment,
        stage: Stage,
        directory: str,
        snapshot: str,
    ):
        self.exercise = exercise
        self.experiment = experiment
        self.stage = stage
        self.directory = directory
        self.snapshot = snapshot
        self.attempt = 0
        self.revision_count = 0
        self.validation_history: ValidationHistory = []

    def hypothesize(self) -> HypothesisFeedback:
        """Generate the first hypothesis with the configured information/tools."""
        self.attempt = 1
        print(
            f"\n{self.experiment.name} / {self.stage.name}: "
            "generating hypothesis...",
            flush=True,
        )
        return self._run_hypothesis(
            hypothesis_request(
                self.exercise.hypothesis_prompt,
                self.experiment,
                self.snapshot,
            )
        )

    def criticize(self, hypothesis: HypothesisFeedback) -> CriticFeedback:
        """Review a hypothesis using the ontology and all checker evidence."""
        print(
            f"{self.experiment.name} / {self.stage.name}: running critic...",
            flush=True,
        )
        critique = self.exercise.runtime.criticize(
            critic_request(
                self.exercise.critic_prompt,
                self.snapshot,
                hypothesis,
                self.validation_history,
                self.experiment.use_shacl,
            )
        )
        self.exercise.artifacts.save_feedback(
            self.directory,
            f"{self.experiment.name} / {self.stage.name}",
            self.attempt,
            critique,
        )
        return critique

    def revise(
        self,
        hypothesis: HypothesisFeedback,
        critique: CriticFeedback,
    ) -> HypothesisFeedback:
        """Revise the explanation while preserving conforming evidence."""
        self.revision_count += 1
        self.attempt += 1
        print(
            f"{self.experiment.name} / {self.stage.name}: revising hypothesis...",
            flush=True,
        )
        return self._run_hypothesis(
            revision_request(
                self.exercise.hypothesis_prompt,
                self.snapshot,
                hypothesis,
                critique,
                self.validation_history,
                self.experiment.use_shacl,
            )
        )

    def finish(
        self,
        hypothesis: HypothesisFeedback,
        critique: CriticFeedback | None,
    ) -> dict:
        """Write the stage summary after the workflow accepts or stops revising."""
        result = {
            "experiment": self.experiment.name,
            "stage": self.stage.name,
            "ontology": (
                str(self.stage.ontology_path)
                if self.experiment.use_ontology
                else None
            ),
            "hypothesis": hypothesis.model_dump(mode="json"),
            "critique": (
                critique.model_dump(mode="json") if critique is not None else None
            ),
            "revision_count": self.revision_count,
        }
        self.exercise.artifacts.record_stage(
            self.exercise.model_id,
            self.experiment.name,
            self.experiment.components,
            self.stage.name,
            self.experiment.use_ontology,
            self.experiment.use_critic,
            self.experiment.use_shacl,
            self.snapshot,
            hypothesis,
            validation_evidence(
                self.validation_history,
                self.experiment.use_shacl,
            ),
            critique,
            self.revision_count,
        )
        print(
            f"{self.experiment.name} / {self.stage.name}: complete.", flush=True
        )
        return result

    def _run_hypothesis(self, prompt: str) -> HypothesisFeedback:
        hypothesis = self.exercise.runtime.hypothesize(
            prompt,
            self.stage.ontology_path,
            self.stage.active_round,
            self.experiment.use_shacl,
            Path(self.exercise.configuration.validation.shapes),
            self.exercise.configuration.validation.max_checker_attempts,
        )
        validations = list(self.exercise.runtime.validation_attempts)
        remember_validation_attempts(
            self.validation_history,
            self.attempt,
            validations,
        )
        self.exercise.artifacts.save_feedback(
            self.directory,
            f"{self.experiment.name} / {self.stage.name}",
            self.attempt,
            hypothesis,
        )
        self.exercise.artifacts.save_validation_attempts(
            self.directory,
            self.attempt,
            validations,
            self.experiment.use_shacl,
        )
        return hypothesis


def hypothesis_request(
    hypothesis_prompt: str,
    experiment: Experiment,
    snapshot: str,
) -> str:
    checker = (
        "The `validate_arrangement` SHACL tool is available."
        if experiment.use_shacl
        else "No model-checker tool is available in this experiment."
    )
    return f"""{hypothesis_prompt}

## Experiment configuration

- Experiment: {experiment.name}
- Ontology supplied: {str(experiment.use_ontology).lower()}
- SHACL validation supplied: {str(experiment.use_shacl).lower()}
- {checker}

## Current ontology export

{snapshot}

Submit the final report with `submit_hypothesis_feedback`.
"""


def critic_request(
    critic_prompt: str,
    snapshot: str,
    hypothesis: HypothesisFeedback,
    validation_history: ValidationHistory,
    validation_enabled: bool,
) -> str:
    checker_instruction = (
        "Check that conforming evidence supports the leading resident. "
        "Conformance establishes possibility, not entailment."
        if validation_enabled
        else "SHACL validation was not used. Do not imply that the proposed "
        "arrangement or leading resident was formally checked."
    )
    return f"""{critic_prompt}

{snapshot}

## Hypothesis Agent response

{hypothesis.model_dump_json(indent=2)}

## Model-checker evidence

{validation_evidence(validation_history, validation_enabled)}

{checker_instruction}
A later failed experiment does not erase earlier conforming evidence.

Submit the critique with `submit_critic_feedback`.
"""


def revision_request(
    hypothesis_prompt: str,
    snapshot: str,
    hypothesis: HypothesisFeedback,
    critique: CriticFeedback,
    validation_history: ValidationHistory,
    validation_enabled: bool,
) -> str:
    evidence = (
        best_conforming_evidence(
            validation_history,
            hypothesis.leading_hypothesis,
        )
        if validation_enabled
        else "SHACL validation is disabled for this experiment."
    )
    checker_instruction = (
        "Keep the conforming arrangement above when only its explanation needs "
        "correction. Call `validate_arrangement` again only if you change the "
        "arrangement or no conforming evidence is supplied."
        if validation_enabled
        else "No `validate_arrangement` tool is available. Revise only the "
        "ontology-grounded explanation and disclose that it remains unchecked."
    )
    return f"""{hypothesis_prompt}

{snapshot}

## Previous hypothesis

{hypothesis.model_dump_json(indent=2)}

## Critic feedback

{critique.model_dump_json(indent=2)}

## Best conforming evidence preserved from earlier attempts

{evidence}

Revise the hypothesis using only the current ontology. Address every unsupported
inference and preserve sound steps. {checker_instruction} Then call
`submit_hypothesis_feedback` once.
"""


def remember_validation_attempts(
    history: ValidationHistory,
    hypothesis_attempt: int,
    attempts: list[ValidationAttempt],
) -> None:
    history.extend(
        (hypothesis_attempt, check, attempt)
        for check, attempt in enumerate(attempts, 1)
    )


def best_conforming_evidence(
    history: ValidationHistory,
    preferred_owner: str,
) -> str:
    preferred = [
        item
        for item in history
        if item[2].report.conforms
        and item[2].proposal.zebra_owner == preferred_owner
    ]
    if not preferred:
        other_owners = sorted(
            {
                item[2].proposal.zebra_owner
                for item in history
                if item[2].report.conforms
            }
        )
        suffix = (
            f" Conforming evidence exists for: {', '.join(other_owners)}."
            if other_owners
            else ""
        )
        return f"No conforming arrangement supports {preferred_owner}.{suffix}"

    hypothesis_attempt, check, evidence = preferred[-1]
    return f"""- Hypothesis attempt: {hypothesis_attempt}
- Checker call: {check}
- Proposed Zebra owner: {evidence.proposal.zebra_owner}
- Conforms: yes

```json
{evidence.proposal.model_dump_json(indent=2)}
```

This arrangement establishes possibility, not entailment."""


def validation_evidence(
    history: ValidationHistory,
    enabled: bool = True,
) -> str:
    if not enabled:
        return "SHACL validation was disabled for this experiment."
    if not history:
        return "The Hypothesis Agent did not call `validate_arrangement`."

    entries = []
    for hypothesis_attempt, check, evidence in history:
        result = validation_result(evidence)
        violations = ", ".join(
            violation["axiom_id"] for violation in result["violations"]
        ) or "none"
        entries.append(
            f"- Hypothesis attempt {hypothesis_attempt}, check {check}: "
            f"proposed_zebra_owner={result['zebra_owner']}; "
            f"conforms={str(result['conforms']).lower()}; "
            f"violated axioms={violations}"
        )
    return "\n".join(entries)
