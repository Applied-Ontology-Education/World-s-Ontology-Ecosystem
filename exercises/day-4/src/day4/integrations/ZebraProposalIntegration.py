import json
from dataclasses import dataclass
from pathlib import Path
from typing import Literal

from langchain_core.tools import BaseTool, tool
from pydantic import BaseModel, ConfigDict, Field, model_validator
from rdflib import RDF, XSD, Graph, Namespace
from rdflib import Literal as RDFLiteral

from day4.integrations.OntologyValidationIntegration import (
    ValidationReport,
    validate_graph,
)

ZEBRA = Namespace("https://ncor-network.org/course/day4/zebra#")
SHAPES = Path("ontology/zebra-proposal-shapes.ttl")

HouseId = Literal["House1", "House2", "House3", "House4", "House5"]
ResidentId = Literal[
    "Resident_A", "Resident_B", "Resident_C", "Resident_D", "Resident_E"
]
ColorId = Literal["Color_A", "Color_B", "Color_C", "Color_D", "Color_E"]
DrinkId = Literal["Drink_A", "Drink_B", "Drink_C", "Drink_D", "Drink_E"]
PetId = Literal["Pet_A", "Pet_B", "Pet_C", "Pet_D", "Zebra"]
BrandId = Literal["Brand_A", "Brand_B", "Brand_C", "Brand_D", "Brand_E"]


class HouseAssignment(BaseModel):
    model_config = ConfigDict(extra="forbid")

    house: HouseId
    resident: ResidentId
    color: ColorId
    drink: DrinkId
    pet: PetId
    brand: BrandId


class ZebraArrangement(BaseModel):
    model_config = ConfigDict(extra="forbid")

    houses: list[HouseAssignment] = Field(min_length=5, max_length=5)

    @model_validator(mode="after")
    def assignments_are_one_to_one(self):
        for field in ("house", "resident", "color", "drink", "pet", "brand"):
            values = [getattr(assignment, field) for assignment in self.houses]
            if len(set(values)) != 5:
                raise ValueError(f"Each {field} must appear exactly once")
        return self


class ZebraProposal(ZebraArrangement):
    active_round: int = Field(ge=0, le=4)

    @property
    def zebra_owner(self) -> ResidentId:
        return next(house.resident for house in self.houses if house.pet == "Zebra")

    def as_graph(self) -> Graph:
        graph = Graph()
        graph.bind("zebra", ZEBRA)
        graph.add((ZEBRA.CurrentProposal, RDF.type, ZEBRA.ProposedArrangement))
        graph.add(
            (
                ZEBRA.CurrentProposal,
                ZEBRA.activeRound,
                RDFLiteral(self.active_round, datatype=XSD.nonNegativeInteger),
            )
        )

        for assignment in self.houses:
            house = ZEBRA[assignment.house]
            graph.add((house, ZEBRA.hasResident, ZEBRA[assignment.resident]))
            graph.add((house, ZEBRA.hasColor, ZEBRA[assignment.color]))
            graph.add((house, ZEBRA.hasDrink, ZEBRA[assignment.drink]))
            graph.add((house, ZEBRA.hasPet, ZEBRA[assignment.pet]))
            graph.add((house, ZEBRA.hasSmoke, ZEBRA[assignment.brand]))
        return graph


@dataclass(frozen=True)
class ValidationAttempt:
    proposal: ZebraProposal
    report: ValidationReport
    proposal_turtle: str
    report_turtle: str


def validate_proposal(
    proposal: ZebraProposal,
    ontology_path: Path,
    shapes_path: Path = SHAPES,
) -> ValidationReport:
    graph = Graph().parse(ontology_path, format="turtle")
    graph += proposal.as_graph()
    return validate_graph(graph, shapes_path)


def validation_result(attempt: ValidationAttempt) -> dict:
    report = attempt.report
    return {
        "conforms": report.conforms,
        "active_round": attempt.proposal.active_round,
        "zebra_owner": attempt.proposal.zebra_owner,
        "violations": [
            {
                "axiom_id": violation.shape_id.removesuffix("Shape"),
                "focus_node": violation.focus_node,
                "path": violation.path,
                "message": violation.message,
            }
            for violation in report.violations
        ],
        "interpretation": (
            "This concrete arrangement satisfies the active constraints. "
            "It establishes possibility, not deductive entailment."
            if report.conforms
            else "Revise the arrangement to address every reported violation."
        ),
    }


def validation_tool(
    active_round: int,
    ontology_path: Path,
    attempts: list[ValidationAttempt],
    shapes_path: Path = SHAPES,
    max_attempts: int = 3,
) -> BaseTool:
    """Build the non-terminal checker tool for one ontology stage."""

    @tool("validate_arrangement", args_schema=ZebraArrangement)
    def validate_arrangement(**arrangement) -> str:
        """Check a complete five-house arrangement against the active clues.

        Use the returned violated axiom IDs to revise the arrangement. A
        conforming arrangement proves only that the candidate is possible.
        """
        if len(attempts) >= max_attempts:
            return json.dumps(
                {
                    "error": f"Validation limit reached ({max_attempts} attempts).",
                    "instruction": "Submit the best supported hypothesis now.",
                }
            )

        proposal = ZebraProposal(active_round=active_round, **arrangement)
        report = validate_proposal(proposal, ontology_path, shapes_path)
        attempt = ValidationAttempt(
            proposal=proposal,
            report=report,
            proposal_turtle=proposal.as_graph().serialize(format="turtle"),
            report_turtle=report.report_graph.serialize(format="turtle"),
        )
        attempts.append(attempt)
        return json.dumps(validation_result(attempt))

    return validate_arrangement
