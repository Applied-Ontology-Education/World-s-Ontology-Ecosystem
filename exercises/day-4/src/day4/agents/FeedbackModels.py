from typing import Annotated, Literal

from pydantic import BaseModel, ConfigDict, Field

AxiomId = Annotated[str, Field(pattern=r"^(S\d{2}|Z\d{2})$")]
ResidentId = Annotated[str, Field(pattern=r"^Resident_[A-E]$")]
ReasoningStep = Annotated[str, Field(min_length=1)]


class HypothesisFeedback(BaseModel):
    """Validated final report submitted by the hypothesis agent."""

    model_config = ConfigDict(extra="forbid")

    leading_hypothesis: ResidentId
    confidence: int = Field(ge=0, le=100)
    supporting_axiom_ids: list[AxiomId]
    reasoning_steps: list[ReasoningStep] = Field(min_length=1)
    unstated_assumptions: list[str]
    best_competing_hypothesis: ResidentId
    most_useful_missing_information: str = Field(min_length=1)
    status: Literal["possible", "plausible", "inconsistent", "entailed"]


class CriticFeedback(BaseModel):
    """Validated final report submitted by the critic agent."""

    model_config = ConfigDict(extra="forbid")

    absent_axiom_ids: list[AxiomId]
    unsupported_inferences: list[str]
    hidden_assumptions: list[str]
    ontology_conflicts: list[str]
    assessment: Literal[
        "inconsistent",
        "currently_possible",
        "comparatively_well_supported",
        "entailed",
    ]
    highest_value_additional_axiom_or_query: str = Field(min_length=1)
    revision_required: bool
    summary: str = Field(min_length=1)
