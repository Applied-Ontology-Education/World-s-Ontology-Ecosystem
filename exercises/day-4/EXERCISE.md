# Day 4 Guided Exercise

## Goal

This exercise shows what changes when grounding, agent review, and formal
constraint feedback are added to an AI workflow. You will audit four solutions
to the same Zebra-owner question, then compare their abductive hypotheses with
a deductive OWL reasoner result.

You are not expected to implement ABI agents, RDF serialization, SHACL, or file
logging. The complete experiment is runnable when you receive it.

## The four experiments

| Experiment | Information and feedback available |
|---|---|
| 1. LLM only | The question and candidate IDs; no ontology, Critic, or SHACL |
| 2. Ontology-grounded hypothesis | Hypothesis Agent and the Round 4 ontology snapshot |
| 3. Critic added | The same snapshot plus an LLM review and one possible revision |
| 4. SHACL feedback loop | Hypothesis, Critic, and deterministic arrangement checks across Core and Rounds 1–4 |

Runs 1–3 use the same Round 4 problem so you can isolate the effect of each
added component. Run 4 also exposes the ontology stages successively so you can
observe belief revision as clues become available.

## The one exercise file

Read:

```text
exercise.json
```

It contains the question, candidate IDs, complete Hypothesis prompt, complete
Critic prompt, four experiment configurations, stage selection, revision limits,
final reasoner query, and CSV filename. You may change a prompt or configuration
and rerun after completing the baseline audit, but no Python editing is required.

Everything else is provided framework plumbing.

## Run the exercise

Use macOS, Linux, or WSL on Windows. Copy `.env.example` to `.env`, add an
OpenRouter API key, and run:

```bash
make
```

The default Make target installs the UV environment, validates the ontologies,
ensures `.env` exists, and starts every configured experiment. `make run` is
equivalent. Run `make test` separately when you want the offline workflow test.

To install and verify without making model calls, run `make install
verify-setup test`.

One execution creates a timestamped directory under `runs/` and a consolidated:

```text
agent-run-log.csv
```

The CSV identifies the model, experiment, enabled components, ontology stage,
leading hypothesis, confidence, cited axioms, assumptions, SHACL evidence,
Critic findings, and revision count. `config.yaml` contains a validated
`agent_models` list; adding another registered model repeats all experiments and
appends its rows to the same CSV.

## Audit procedure

1. Read `exercise.json` and predict what each added component can and cannot
   establish.
2. Run all four experiments with `make`.
3. Open `agent-run-log.csv` and compare the first three Round 4 rows.
4. Inspect one ungrounded hypothesis and check whether it disclosed its lack of
   evidence.
5. Inspect one Critic report and decide whether its requested revision was
   justified.
6. Inspect one failed and one conforming SHACL report from Experiment 4.
7. Compare Experiment 4 across Core and Rounds 1–4.
8. Optionally change one prompt instruction and compare a second run.

## Final OWL query

After the audit, open `ontology/zebra-round-4.owl` in Protégé, run an OWL 2 DL
reasoner, and issue:

```text
Resident and livesIn some (hasPet value Zebra)
```

The reasoner result is deliberately separate from the agent feedback loop.
SHACL checks one proposed arrangement for compatibility; the reasoner tests
deductive entailment.

## Discussion questions

Use these questions to guide the final discussion. No written submission is
required.

1. What did the LLM-only result claim, and what evidence was missing?
2. What improved when the ontology snapshot was added?
3. What did the Critic catch, and why is another LLM not a formal validator?
4. What did SHACL establish about a conforming arrangement, and what did it not
   establish?
5. How did the hypothesis change from Core through Round 4?
6. What additional conclusion did the final OWL reasoner provide?
