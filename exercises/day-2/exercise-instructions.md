# Day 2 Exercises: From Data to Design Patterns to OWL

## Purpose

Day 2 asks you to translate heterogeneous source data into reusable ontology design patterns and then encode those patterns in OWL using Protégé.

The goal is **not** to reproduce each spreadsheet as a collection of labels and values. Your goal is to determine:

1. what the source record is;
2. what the record is about;
3. which entities should be represented as classes, individuals, or literals;
4. which relations are asserted directly and which are convenient shortcuts;
5. which claims apply universally and which concern only a particular individual, process, measurement, or artifact; and
6. how the resulting representation can be checked with a reasoner.

There may be more than one defensible solution. Your submission must make its ontological commitments explicit and apply them consistently.

---

## Before You Begin

Confirm that the Day 2 data files open correctly:
  * `aircraft_data.xlsx`
  * `soc_structure_definitions.xlsx`
  * `employment_wage_May_2024.xlsx`

Confirm that the ontology imports resolve and that the configured reasoner runs on the starter ontology without reporting an inconsistency.

---

## Required Deliverables

Create a folder for your work using your GitHub username:

```text
exercises/day-2/submissions/YOUR-NAME/
```

Submit the following:

```text
YOUR-NAME/
├── case-1-pattern.png
├── case-1.owl
├── case-2-pattern.png
├── case-2.owl
├── case-3-pattern.png
├── case-3.owl
├── case-4-pattern.png
├── case-4.owl
```

PDF or SVG design-pattern diagrams are also acceptable. Use the same file extension consistently.

---

## Design-Pattern Requirements

Each design pattern must be readable without opening the ontology.

Your legend must visually distinguish:

* **classes**;
* **individuals**;
* **string or numeric literals**;
* **object-property relations**;
* **data-property relations**; and
* **shortcut relations**, when used.

You may choose your own shapes and notation, but use them consistently across all four cases.

Do not turn every noun in the spreadsheet into a class. Do not turn every spreadsheet row into a real-world object.

---

# Case 1: Airbus A320 Neo Source Record

## Task

In `aircraft_data.xlsx`, locate the row for the Airbus A320 Neo.

Construct a design pattern and OWL encoding that reflect the contents of columns:

```text
C–G, R–S, and AB
```

## Guidance

Begin by representing the selected column headers and values in a design pattern. Do not rely on the column letters alone.

For each value, determine whether it is:

* a name or model designation;
* a source-specific identifier;
* a manufacturer or organizational reference;
* a category assigned by the dataset;
* a count;
* a physical measurement;
* a unit;
* a characteristic required by a specification; or
* a characteristic observed in an existing aircraft.

The row may combine information about different things. Do not assume that every selected column describes the same entity in the same way.

Your pattern should make it possible to distinguish among at least the following candidates:

* the spreadsheet record;
* the specification or model information expressed by the record;
* the type of aircraft described or prescribed;
* a manufacturer;
* component types;
* qualities and measurements; and
* literal model names, counts, or numeric values.

Ask whether the source is describing a particular aircraft that exists, a type of aircraft, a specification for aircraft, or some combination of these. State and defend your decision.

When a numerical value has a unit, use a measurement pattern or another explicit representation that preserves both.

---

# Case 2: Prescribed and Observed Approach Speeds

## Task

In `aircraft_data.xlsx`, locate the row for the Airbus A321-111.

Represent the following:

* the aircraft is designed to have a maximum approach speed of 142 knots;
* a particular aircraft undergoes five approaches; and
* the average maximum approach speed obtained from those approaches is 139 knots.

Construct a design pattern and OWL encoding that reflect these phenomena.

## Guidance

This case requires you to keep **prescription**, **observation**, and **aggregation** separate.

Do not simply attach both numeric values to one aircraft. Doing so would obscure why the values differ and what each value means.

Your model should distinguish:

1. the source specification or design information;
2. the class expression or type of aircraft to which the specification applies;
3. the particular aircraft involved in the test;
4. the overall test process;
5. the five approach processes;
6. the measurement information associated with the approaches; and
7. the aggregate or average measurement result.

Decide how the five approaches are related to the overall test. Make the relation explicit rather than relying on their names.

Decide what each measurement is about. A measurement result should not be about a number. The number is a value associated with information that is about a quality, process, participant, or other relevant entity.

The exercise supplies the average value. You may assert that supplied result, but your model must preserve its connection to the five contributing approaches or measurements. 

Do not assert that the observed aircraft fails to conform to the specification unless you have modeled enough information to justify that conclusion. Consider what “maximum approach speed” means in the specification and in the observations before adding a conformity claim.

---

# Case 3: SOC Entries Mentioning “Aerospace Engineer”

## Task

In `soc_structure_definitions.xlsx`, locate the three rows whose `SOC_TITLE` contains “Aerospace Engineer.”

Construct a design pattern and OWL encoding that reflect:

* all three SOC entries;
* their SOC codes and titles;
* their location in the SOC hierarchy; and
* their respective `SOC Definition` values.

## Guidance

Read the workbook carefully before treating the three entries as synonyms.

The SOC system distinguishes levels such as:

* major group;
* minor group;
* broad occupation; and
* detailed occupation.

Use the code structure and official documentation to determine the level of each selected entry. Do not infer the level from title wording alone.

Distinguish:

* the SOC code or classification entry;
* the occupational category identified by that entry;
* a job role;
* a person who may bear that role;
* the processes in which the role is realized; and
* the natural-language definition supplied by the source.

A classification code is not itself a person, job role, or occupational process. It is an information artifact used to identify or classify.

---

# Case 4: Employment and Wage Records

## Task

In `employment_wage_May_2024.xlsx`, locate the three rows whose `OCC_TITLE` contains “Aerospace Engineer.”

Construct a design pattern and OWL encoding that reflect each selected title together with columns:

```text
A, H, I, K, and L
```

Include the `OCC_TITLE` value needed to identify each selected row.

## Guidance

Copy the selected column headers and values into your notes before modeling.

This dataset combines classification information with a statistical report. Your model must distinguish those layers.

For each row, determine which fields concern:

* geographic or reporting area;
* ownership scope;
* occupation code;
* occupation grouping level;
* occupation title;
* population or employment estimate; and
* the source record that reports the estimate.

Treat code values as strings unless the source documentation establishes that numerical operations are meaningful. Leading zeros, hyphens, and code formatting may be significant.

Do not model the total employment value as an intrinsic property of the SOC code. The same occupation code may have different employment estimates across areas, ownership scopes, industries, or reporting periods.

Instead, determine:

* which population the estimate concerns;
* how that population is delimited;
* what counting or measurement process produced the result;
* what information artifact records the result; and
* how the reported value is associated with that information.

The three rows may use the same or similar occupation titles while differing in code, grouping level, scope, or reported count. Your model must preserve those distinctions.

Where a row concerns a population, make clear what qualifies an individual for membership in that population. Do not assume that a population is identical to an occupational category.

Preserve the reporting date or dataset edition in provenance annotations even when it is not one of the required spreadsheet columns.

---

## Submission

Commit and push your completed files to your fork.

Use a commit message such as:

```text
Complete Day 2 ontology exercises
```

Open a pull request only when instructed by the course staff. Follow the submission procedure in [GitHub Basics](../../resources/gitub-basics.md).

In the pull-request description, include:

* participant name;
* the four cases completed;
* whether the reasoner completed successfully.
