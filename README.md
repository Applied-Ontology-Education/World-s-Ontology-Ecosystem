# The World's Ontology Ecosystem — Exercise Repository

This repository supports the UB + NCOR five-day ontology summer course. It is designed for a mixed audience: observers who want to follow the reasoning, builders who want to complete guided ontology exercises, and experienced reviewers who want to critique models and tests.

The repository treats ontology engineering as a **tradecraft**. Across the week, participants repeatedly:

1. clarify the use case and competency questions;
2. disambiguate candidate terms using the seven-bucket strategy;
3. distinguish entities from information about them;
4. encode the result in RDF/OWL;
5. test syntax and selected structural expectations;
6. explain what the model establishes and what remains unresolved;
7. submit and review work through GitHub.

## Current package status

This starter package contains:

- the full repository infrastructure;
- a pre-event setup check;
- shared templates and review forms;
- a complete Day 1 exercise, including participant files, automated checks, staged hints, an instructor guide, and an instructor solution;
- structured placeholders for Days 2–5.

The Day 1 case is fictional and unclassified. It is inspired by the kinds of distinctions that arise in operational ontology work, but it does not represent an actual Air Force system or mission.

## Start here

1. Read [START-HERE.md](START-HERE.md).
2. Complete [setup-check/README.md](setup-check/README.md) before the event.
3. Review the participation modes in [docs/PARTICIPATION-AT-SCALE.md](docs/PARTICIPATION-AT-SCALE.md).
4. For Day 1, open [day-1-seven-buckets/README.md](day-1-seven-buckets/README.md).

## Repository map

```text
.
├── .github/                 GitHub Actions and contribution templates
├── .vscode/                 Recommended VS Code settings and extensions
├── common/                  Shared worksheets and review templates
├── day-1-seven-buckets/     Complete Day 1 exercise
├── day-2-unreal/            Placeholder for blueprints and fiction
├── day-3-ai-red-team/       Placeholder for AI comparison exercise
├── day-4-clue-validation/   Placeholder for validation/release exercise
├── day-5-zebra/             Placeholder for capstone reasoning exercise
├── docs/                    Facilitation and repository operations
├── scripts/                 Local validation scripts
├── setup-check/             Pre-event GitHub and RDF setup test
├── submissions/             Team work goes here in participant forks
└── tests/                   Repository-level tests
```

## Fast local check

From the repository root:

```bash
python -m pip install -r requirements.txt
python scripts/run_checks.py setup-check/example-submission
python scripts/run_checks.py day-1-seven-buckets/example-submission
pytest -q
```

## Instructor warning

The `day-1-seven-buckets/instructor/` directory contains the preferred solution and facilitation notes. Before publishing the participant repository, move that directory to a private instructor repository or a protected private branch.

## License

Code is provided under the MIT License. Educational text and exercise content are provided under CC BY 4.0; see [LICENSE.md](LICENSE.md).
