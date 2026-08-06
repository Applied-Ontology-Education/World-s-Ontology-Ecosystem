#!/usr/bin/env python3
"""Create a concise, masked snapshot of a staged Zebra ontology."""
from __future__ import annotations

import argparse
from pathlib import Path

from rdflib import Graph, Literal, Namespace
from rdflib.collection import Collection
from rdflib.namespace import OWL, RDF, RDFS

Z = Namespace("https://ncor-network.org/course/day4/zebra#")


def _name(value) -> str:
    """Return the local name of an RDF value."""
    text = str(value)
    return text.rsplit("#", 1)[-1].rsplit("/", 1)[-1]


def _list(graph: Graph, head) -> list:
    return list(Collection(graph, head))


def _enumerated_classes(graph: Graph) -> dict[str, list[str]]:
    """Read exhaustive class members from owl:oneOf declarations."""
    classes = {}
    for class_iri, equivalent_class in graph.subject_objects(OWL.equivalentClass):
        list_head = graph.value(equivalent_class, OWL.oneOf)
        if list_head is not None:
            classes[_name(class_iri)] = [
                _name(member) for member in _list(graph, list_head)
            ]
    return classes


def _all_different_groups(graph: Graph) -> list[set[str]]:
    groups = []
    for declaration in graph.subjects(RDF.type, OWL.AllDifferent):
        list_head = graph.value(declaration, OWL.distinctMembers)
        if list_head is not None:
            groups.append({_name(member) for member in _list(graph, list_head)})
    return groups


def _exact_assignments(graph: Graph, class_iri) -> list[tuple[str, str]]:
    """Return (property, target class) for exact-cardinality-one restrictions."""
    assignments = []
    for restriction in graph.objects(class_iri, RDFS.subClassOf):
        cardinality = graph.value(restriction, OWL.qualifiedCardinality)
        if cardinality is None or int(str(cardinality)) != 1:
            continue
        property_iri = graph.value(restriction, OWL.onProperty)
        target_class = graph.value(restriction, OWL.onClass)
        if property_iri is not None and target_class is not None:
            assignments.append((_name(property_iri), _name(target_class)))
    return assignments


def _relation_is_closed(graph: Graph, subjects: list, property_iri) -> bool:
    """Check that every subject has an OWL closure restriction for a relation."""
    for subject in subjects:
        closed = False
        for restriction in graph.objects(subject, RDF.type):
            if graph.value(restriction, OWL.onProperty) != property_iri:
                continue
            if (
                graph.value(restriction, OWL.allValuesFrom) is not None
                or graph.value(restriction, OWL.maxCardinality) is not None
            ):
                closed = True
                break
        if not closed:
            return False
    return True


def _structural_axioms(graph: Graph) -> list[str]:
    classes = _enumerated_classes(graph)
    different_groups = _all_different_groups(graph)
    houses = classes.get("House", [])

    house_distinct = set(houses) in different_groups
    lines = [
        "- S01: Houses are exactly "
        + ", ".join(houses)
        + ("; they are pairwise distinct." if house_distinct else "."),
        "- S02: Category membership is exhaustive (`owl:oneOf`):",
    ]

    for class_name, members in classes.items():
        if class_name == "House":
            continue
        distinct = set(members) in different_groups
        suffix = "; members are pairwise distinct." if distinct else "."
        lines.append(f"  - {class_name}: {', '.join(members)}{suffix}")

    house_assignments = _exact_assignments(graph, Z.House)
    lines.append(
        "- S03: Every House has exactly one assignment through: "
        + ", ".join(
            f"{property_name} -> {target_class}"
            for property_name, target_class in house_assignments
        )
        + "."
    )

    reverse_assignments = []
    for class_name in classes:
        if class_name == "House":
            continue
        for property_name, target_class in _exact_assignments(
            graph, Z[class_name]
        ):
            if target_class == "House":
                reverse_assignments.append((class_name, property_name))
    lines.append(
        "- S04: Every category member belongs to exactly one House through: "
        + ", ".join(
            f"{class_name} via {property_name}"
            for class_name, property_name in reverse_assignments
        )
        + "."
    )

    house_iris = [Z[house] for house in houses]
    next_to_pairs = {
        tuple(sorted((_name(left), _name(right))))
        for left, right in graph.subject_objects(Z.nextTo)
        if left in house_iris and right in house_iris
    }
    right_of_pairs = [
        (_name(right_house), _name(left_house))
        for right_house, left_house in graph.subject_objects(Z.immediatelyRightOf)
        if right_house in house_iris and left_house in house_iris
    ]
    next_to_label = (
        "The only nextTo pairs are"
        if _relation_is_closed(graph, house_iris, Z.nextTo)
        else "The asserted nextTo pairs are"
    )
    right_of_label = (
        "The only immediatelyRightOf relations are"
        if _relation_is_closed(graph, house_iris, Z.immediatelyRightOf)
        else "The asserted immediatelyRightOf relations are"
    )
    lines.extend(
        [
            "- S05: Houses form the fixed left-to-right order "
            + " < ".join(houses)
            + ".",
            f"- S06: {next_to_label}: "
            + ", ".join(f"{left}--{right}" for left, right in sorted(next_to_pairs))
            + ".",
            f"- S07: {right_of_label}: "
            + ", ".join(
                f"{right} immediately right of {left}"
                for right, left in sorted(right_of_pairs)
            )
            + ".",
            "- S08: Under OWL open-world semantics, an assignment not stated or entailed is unknown, not false.",
        ]
    )
    return lines


def export_axioms(ontology: Path) -> str:
    """Return the agent-readable export for one ontology file."""
    graph = Graph()
    graph.parse(ontology, format="turtle")
    active_round = int(str(next(graph.objects(None, Z.activeRound), Literal(0))))
    clues = []
    for subject in graph.subjects(RDF.type, Z.ClueRecord):
        default_id = Literal(subject.split("#")[-1])
        cid = str(next(graph.objects(subject, Z.axiomId), default_id))
        rnd = int(str(next(graph.objects(subject, Z.clueRound), Literal(0))))
        text = str(next(graph.objects(subject, Z.clueText), Literal("")))
        clues.append((rnd, cid, text))
    clues.sort(key=lambda row: (row[0], row[1]))

    lines = [
        "# Current Zebra Ontology Snapshot",
        "",
        f"Active round: {active_round}",
        "",
        "Only the masked identifiers and active axioms below may be used.",
        "",
        "## Structural axioms",
        "",
    ]
    lines.extend(_structural_axioms(graph))
    lines.extend(["", "## Active clue axioms", ""])
    if clues:
        lines.extend(f"- {cid} (round {rnd}): {text}" for rnd, cid, text in clues)
    else:
        lines.append("- No clue axioms are active.")
    lines.extend(
        [
            "",
            "## Query",
            "",
            "Which resident is the best current candidate for owning Zebra?",
        ]
    )
    return "\n".join(lines) + "\n"


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("ontology", type=Path)
    parser.add_argument("--format", choices=["markdown", "text"], default="markdown")
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()

    output = export_axioms(args.ontology)
    if args.output:
        args.output.write_text(output, encoding="utf-8")
    else:
        print(output)

if __name__ == "__main__":
    main()
