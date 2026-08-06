#!/usr/bin/env python3
"""Parse all supplied ontology files and report the number of active clue records."""
from pathlib import Path
from rdflib import Graph, Namespace
from rdflib.namespace import RDF

Z = Namespace("https://ncor-network.org/course/day4/zebra#")
root = Path(__file__).resolve().parents[1] / "ontology"
failed = False
for path in sorted(root.glob("*.owl")):
    try:
        graph = Graph(); graph.parse(path, format="turtle")
        count = sum(1 for _ in graph.subjects(RDF.type, Z.ClueRecord))
        print(f"OK  {path.name}: {count} active clue records; {len(graph)} RDF triples")
    except Exception as exc:
        failed = True
        print(f"FAIL {path.name}: {exc}")
raise SystemExit(1 if failed else 0)
