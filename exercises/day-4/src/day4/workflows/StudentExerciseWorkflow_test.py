import csv
import json
from pathlib import Path
from tempfile import TemporaryDirectory
from types import SimpleNamespace

from day4.agents.FeedbackModels import CriticFeedback, HypothesisFeedback
from day4.exercise import (
    ZebraExercise,
    best_conforming_evidence,
    load_exercise_configuration,
    remember_validation_attempts,
    validation_evidence,
)
from day4.workflows.ExercisePlumbing import RunArtifacts
from day4.workflows.StudentExerciseWorkflow import run_experiment


class FakeRuntime:
    def __init__(self):
        self.critic_calls = 0
        self.validation_attempts = []

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
        candidate = "Resident_B" if "Critic feedback" in prompt else "Resident_A"
        has_ontology = "Ontology supplied: true" in prompt
        return HypothesisFeedback(
            leading_hypothesis=candidate,
            confidence=50,
            supporting_axiom_ids=["Z01"] if has_ontology else [],
            reasoning_steps=(
                ["Z01 supports the current candidate."]
                if has_ontology
                else ["No ontology evidence was supplied."]
            ),
            unstated_assumptions=([] if has_ontology else ["The choice is arbitrary."]),
            best_competing_hypothesis="Resident_C",
            most_useful_missing_information="One more pet clue",
            status="possible" if use_validation else "plausible",
        )

    def criticize(self, prompt: str) -> CriticFeedback:
        self.critic_calls += 1
        revision_required = self.critic_calls % 2 == 1
        return CriticFeedback(
            absent_axiom_ids=[],
            unsupported_inferences=(
                ["Step 1 needs correction."] if revision_required else []
            ),
            hidden_assumptions=[],
            ontology_conflicts=[],
            assessment="currently_possible",
            highest_value_additional_axiom_or_query="One more pet clue",
            revision_required=revision_required,
            summary="Revise step 1." if revision_required else "Accepted.",
        )


def test_runs_the_four_comparison_experiments():
    with TemporaryDirectory() as temporary_directory:
        configuration = load_exercise_configuration()
        artifacts = RunArtifacts(
            runs_directory=Path(temporary_directory),
            log_filename=configuration.output.csv,
        )
        exercise = ZebraExercise(
            configuration,
            FakeRuntime(),
            artifacts,
            model_id="test-model",
        )
        results = run_experiment(exercise)

        assert len(results) == 8
        assert [result["experiment"] for result in results[:3]] == [
            experiment.name for experiment in configuration.experiments[:3]
        ]
        assert [result["stage"] for result in results[3:]] == [
            "Core",
            "Round 1",
            "Round 2",
            "Round 3",
            "Round 4",
        ]
        assert results[0]["ontology"] is None
        assert results[0]["critique"] is None
        assert results[1]["critique"] is None
        assert all(result["revision_count"] == 0 for result in results[:2])
        assert all(result["revision_count"] == 1 for result in results[2:])
        assert all(
            result["hypothesis"]["leading_hypothesis"] == "Resident_B"
            for result in results[2:]
        )

        with artifacts.log_path.open(newline="", encoding="utf-8") as log:
            rows = list(csv.DictReader(log))

        assert len(rows) == 8
        assert rows[0]["Model"] == "test-model"
        assert rows[0]["Experiment"] == "1. LLM only"
        assert rows[0]["Ontology supplied"] == "no"
        assert rows[0]["Critic enabled"] == "no"
        assert rows[0]["SHACL enabled"] == "no"
        assert rows[0]["Supporting axioms"] == ""
        assert rows[0]["Critic findings"] == (
            "Critic Agent not used in this experiment."
        )
        assert rows[1]["Experiment"] == "2. Ontology-grounded hypothesis"
        assert rows[1]["Ontology supplied"] == "yes"
        assert rows[2]["Critic enabled"] == "yes"
        assert rows[2]["SHACL enabled"] == "no"
        assert rows[3]["Experiment"] == "4. SHACL feedback loop"
        assert rows[3]["Stage"] == "Core"
        assert rows[3]["SHACL enabled"] == "yes"
        assert "Z01 (round 1)" not in rows[3]["Ontology snapshot"]
        assert "Revision required: no" in rows[3]["Critic findings"]

        core_directory = (
            artifacts.run_directory / "test-model" / "04-shacl-feedback" / "core"
        )
        hypothesis_json = json.loads(
            (core_directory / "hypothesis-attempt-2.json").read_text()
        )
        assert hypothesis_json["leading_hypothesis"] == "Resident_B"
        assert (core_directory / "critic-attempt-2.md").exists()
        assert (
            core_directory
            / "hypothesis-attempt-2-validation-summary.md"
        ).exists()


class FakeProposal:
    def __init__(self, owner):
        self.active_round = 4
        self.zebra_owner = owner

    def model_dump_json(self, indent=2):
        return json.dumps({"zebra_owner": self.zebra_owner}, indent=indent)


def fake_validation(owner, conforms):
    return SimpleNamespace(
        proposal=FakeProposal(owner),
        report=SimpleNamespace(conforms=conforms, violations=[]),
    )


def test_preserves_conforming_evidence_across_hypothesis_revisions():
    resident_e_success = fake_validation("Resident_E", True)
    resident_d_failure = fake_validation("Resident_D", False)
    history = []

    remember_validation_attempts(history, 1, [resident_e_success])
    remember_validation_attempts(history, 2, [resident_d_failure])

    summary = validation_evidence(history)
    preserved = best_conforming_evidence(history, "Resident_E")

    assert "Hypothesis attempt 1, check 1" in summary
    assert "proposed_zebra_owner=Resident_E; conforms=true" in summary
    assert "Hypothesis attempt 2, check 1" in summary
    assert "proposed_zebra_owner=Resident_D; conforms=false" in summary
    assert "Proposed Zebra owner: Resident_E" in preserved
    assert "Conforms: yes" in preserved
