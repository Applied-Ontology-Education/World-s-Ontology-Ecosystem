from dataclasses import dataclass
from pathlib import Path

from pyshacl import validate
from rdflib import RDF, SH, Graph, URIRef


@dataclass(frozen=True)
class ValidationViolation:
    shape_id: str
    focus_node: str
    message: str
    path: str | None


@dataclass(frozen=True)
class ValidationReport:
    conforms: bool
    violations: list[ValidationViolation]
    report_graph: Graph


def validate_graph(data_graph: Graph, shapes_path: Path) -> ValidationReport:
    """Validate one concrete RDF graph and return compact SHACL feedback."""
    shapes_graph = Graph().parse(shapes_path, format="turtle")
    conforms, report_graph, _ = validate(
        data_graph=data_graph,
        shacl_graph=shapes_graph,
        inference="rdfs",
        abort_on_first=False,
        allow_infos=True,
        allow_warnings=True,
    )

    violations = []
    for result in report_graph.subjects(RDF.type, SH.ValidationResult):
        shape = report_graph.value(result, SH.sourceShape)
        focus = report_graph.value(result, SH.focusNode)
        message = report_graph.value(result, SH.resultMessage)
        path = report_graph.value(result, SH.resultPath)
        violations.append(
            ValidationViolation(
                shape_id=shape_name(shapes_graph, shape),
                focus_node=local_name(focus),
                message=str(message or "SHACL constraint failed"),
                path=local_name(path) if path else None,
            )
        )

    return ValidationReport(bool(conforms), violations, report_graph)


def local_name(value) -> str:
    text = str(value or "")
    return text.rsplit("#", 1)[-1].rsplit("/", 1)[-1]


def shape_name(shapes_graph: Graph, shape) -> str:
    """Resolve a nested blank-node constraint to its named NodeShape."""
    if isinstance(shape, URIRef):
        return local_name(shape)

    pending = [shape]
    visited = set()
    while pending:
        current = pending.pop()
        if current in visited:
            continue
        visited.add(current)
        for parent in shapes_graph.subjects(object=current):
            if isinstance(parent, URIRef) and (parent, RDF.type, SH.NodeShape) in shapes_graph:
                return local_name(parent)
            pending.append(parent)
    return local_name(shape)
