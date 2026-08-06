# Day 4 Exercise: Ground, Critique, Validate

## What you will investigate

One question drives this exercise:

**Which resident is the best current candidate for owning `Zebra`?**

You will audit four increasingly constrained ways of answering it, and along
the way answer a deeper question: what does each component add to an
ontology-enabled AI workflow, and how does an abductive hypothesis differ from
a deductively entailed conclusion?

## What you will learn

By the end of the exercise, you should be able to:

- recognize an unsupported LLM answer;
- ground a hypothesis in explicit ontology axioms;
- evaluate the benefits and limits of an LLM Critic;
- use SHACL violations as deterministic revision feedback;
- distinguish plausible, possible, inconsistent, and entailed claims;
- compare an abductive workflow result with an OWL reasoner result.

## The four experiments

| Experiment | Ontology | Critic | SHACL | Stages |
|---|:---:|:---:|:---:|---|
| 1. LLM only | No | No | No | Round 4 question only |
| 2. Ontology-grounded hypothesis | Yes | No | No | Round 4 |
| 3. Critic added | Yes | Yes | No | Round 4 |
| 4. SHACL feedback loop | Yes | Yes | Yes | Core and Rounds 1–4 |

The first three experiments run on the same problem, so you can isolate what
each component contributes. The final experiment shows belief revision over
successively richer ontology states.

```text
Question only
     ↓ add ontology
Grounded hypothesis
     ↓ add Critic
Reviewed reasoning
     ↓ add SHACL
Constraint-checked feedback loop
     ↓ final, separate OWL query
Deductive entailment result
```

Keep one distinction in mind while you audit: SHACL answers whether one
concrete five-house arrangement satisfies the active constraints. It
establishes possibility, not uniqueness or entailment. The final OWL reasoner
query is a separate deductive check.

## Where you will work

You stay in one file:

```text
exercise.json
```

It contains the question, both complete task prompts, four experiment
definitions, selected ontology stages, component switches, revision budgets,
the final reasoner query, and the output filename. It works as provided. Your
job is mainly to read and audit it; if you want a second comparison run, one
optional JSON change is enough.

You do not need to understand or modify:

- `src/day4/exercise.py`: stage sessions and evidence preservation;
- `src/day4/workflows/ExercisePlumbing.py`: ABI calls and run artifacts;
- `src/day4/workflows/StudentExerciseWorkflow.py`: generic JSON-driven loop;
- `src/day4/integrations/`: RDF conversion and SHACL checking;
- `src/day4/agents/`: agent construction and structured tools;
- `scripts/export_current_axioms.py`: ontology-to-text export;
- `main.py`: ABI initialization and dependency wiring.

## Run it locally

Use macOS, Linux, or WSL on Windows. Install
[UV](https://docs.astral.sh/uv/) and run:

```bash
make
```

`make` and `make run` are equivalent. The default target creates the UV
environment, validates the ontologies, ensures `.env` exists, and launches the
exercise. Run `make test` separately for the offline workflow test.

To prepare everything without making model calls:

```bash
make install verify-setup test
```

The `day4.config.agent_models` list in `config.yaml` selects the models used
by the two agents. Each listed model runs every configured experiment and
appends its results to the same CSV. The starter selects Claude Opus 4.8
through OpenRouter.

Every execution creates one timestamped `runs/day4-run-*` directory. Its
`agent-run-log.csv` consolidates every comparison row. Detailed JSON,
Markdown, ontology snapshots, SHACL reports, and Turtle proposals are grouped
by experiment and stage beneath the same directory.

## Files

- `EXERCISE.md`: your step-by-step procedure and audit questions
- `exercise.json`: the complete experiment declaration you will read and audit
- `config.yaml`: provider settings and the agent-model list
- `Makefile`: one-command setup, verification, and execution
- `ontology/zebra-core.owl`: clue-free structural model
- `ontology/zebra-round-1.owl` through `zebra-round-4.owl`: cumulative stages
- `ontology/zebra-proposal-shapes.ttl`: executable arrangement constraints
- `clue-packets/`: new clues introduced at each round
- `templates/`: CSV and analysis templates

The ontology uses masked identifiers such as `Resident_A` and `Color_B`. If
you already know the classic Zebra Puzzle answer, the masking keeps it from
contaminating your results.

## Final deductive check

After Experiment 4, open `ontology/zebra-round-4.owl` in Protégé, run an
OWL 2 DL reasoner, and issue:

```text
Resident and livesIn some (hasPet value Zebra)
```

Compare what the reasoner entails with what the abductive workflow proposed.
