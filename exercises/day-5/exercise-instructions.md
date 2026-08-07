# Day 5 Capstone Exercise

## Purpose

The capstone brings together the main themes from the week:

- ontology tradecraft;
- careful modeling and reusable design patterns;
- definitions;
- OWL and reasoning;
- critical use of large language models;
- ontology-enabled applications; and
- the difference between preserving meaning and merely moving data.

The goal is **not** to build a large ontology. Keep the model small, clear, and defensible.

Work individually or in a small group.

---

## Scenario

A maintenance procedure specifies that a pump should be inspected every 30 days.

Technician Alex performs **Inspection 17** on **Pump P-17**.

The inspection produces **Report R-17**.

The report records a vibration measurement of **4.2 mm/s** and states that the pump requires bearing replacement.

**Work Order W-22** requests that replacement.

---

# Part 1: Build the Pattern

Create a small ontology design pattern for the scenario.

Your model should include only what is needed to represent the case clearly.

Aim for approximately:

- 5–10 classes;
- 3–5 relations;
- the named individuals in the scenario;
- relevant literal values; and
- 3 textual definitions.

You should create an OWL model in Protégé.

## Identify

Distinguish:

- classes;
- named individuals;
- relations;
- literal values;
- processes;
- roles;
- information artifacts; and
- qualities or measurements where relevant.

Apply the modeling strategies used throughout the course.

In particular, avoid:

- treating every noun as a class;
- confusing a role with its bearer;
- confusing an information artifact with what it is about;
- confusing a measurement with its numeric value;
- treating a prescription as though it were an observed fact; and
- adding unnecessary classes or relations.

## Your model should make it possible to determine

1. What is the inspection procedure?
2. Who performed Inspection 17?
3. What was inspected?
4. What information resulted from the inspection?
5. What vibration value was recorded?
6. What maintenance action was requested?
7. Which work order requests that action?

---

# Part 2: Write Three Definitions

Choose three important classes or relations from your model and write textual definitions.

Use the definition-writing guidance from Day 2.

For classes, prefer the genus–differentia form:

> A [genus] that [differentia].

For relations, explain clearly when the relation holds between two entities.

Check that each definition:

- defines the entity rather than the word;
- uses an appropriate parent or genus;
- avoids circularity;
- is neither too broad nor too narrow;
- avoids unnecessary examples or commentary; and
- agrees with the OWL model.

---

# Part 3: Ask an AI to Model the Same Scenario

Use any large language model you prefer.

Give it the scenario and ask it to propose an ontology model.

A simple prompt is:

```text
Create an ontology model for the following scenario.

Identify the classes, named individuals, and relations you would use.
Explain the major modeling decisions.

[PASTE SCENARIO]
```

Compare the AI-generated proposal with your model.

Identify **three disagreements or differences**.

For each, decide:

```text
ACCEPT
REJECT
MODIFY
```

Then give a brief reason.

Example:

```text
AI suggestion:
Technician is modeled as a subclass of Person.

Decision:
MODIFY

Reason:
Technician is better modeled as a role that can be borne by a person.
```

The purpose is not to assume that either the human or AI model is automatically correct.

The purpose is to defend the modeling decision.

---

# Part 4: Run the Reasoner

If you created an OWL model, run the configured reasoner.

Record:

- whether the ontology is consistent;
- whether any classes are unsatisfiable;
- whether expected classifications are inferred; and
- whether any unexpected results appear.

Remember:

> A logically consistent ontology can still contain bad modeling decisions.

If you created only a diagram, review it manually for the same kinds of problems.

---

# Part 5: Derive an Operational View

Imagine that a maintenance application needs to display only:

```text
Pump: P-17
Last inspection: Inspection 17
Measured vibration: 4.2 mm/s
Maintenance action: Replace bearing
Work order: W-22
```

For each field, identify where the value comes from in your ontology.

Use a table such as:

| Application field | Ontology source |
|---|---|
| Pump | |
| Last inspection | |
| Measured vibration | |
| Maintenance action | |
| Work order | |

Then answer:

### What information was omitted?

Identify information represented in the ontology that does not appear in the application view.

Examples might include:

- who performed the inspection;
- the procedure governing the inspection;
- the inspection report;
- the distinction between the recommendation and the future repair process;
- the measurement process; or
- provenance information.

### Is the operational view lossy?

```text
YES / NO
```

Explain briefly.

### Is the operational view divergent?

```text
YES / NO
```

Explain briefly.

A simplified operational representation may omit semantic detail.

It should not change the meaning of the authoritative model.

---

# Submission

Create:

```text
YOUR-NAME/
├── capstone-model.owl
└── capstone-notes.md
```

A diagram may be submitted instead of, or in addition to, the OWL file.

Your `capstone-notes.md` should include:

```markdown
# Day 5 Capstone

## Participants

[Names]

## Model

[Link to OWL file]

## Three Definitions

1.
2.
3.

## AI Comparison

### Difference 1

**AI suggestion:**  
**Decision:** ACCEPT / REJECT / MODIFY  
**Reason:**  

### Difference 2

**AI suggestion:**  
**Decision:** ACCEPT / REJECT / MODIFY  
**Reason:**  

### Difference 3

**AI suggestion:**  
**Decision:** ACCEPT / REJECT / MODIFY  
**Reason:**  

## Reasoner Results

- Consistent:
- Unsatisfiable classes:
- Expected inferences:
- Unexpected inferences:

## Operational View

| Application field | Ontology source |
|---|---|
| Pump | |
| Last inspection | |
| Measured vibration | |
| Maintenance action | |
| Work order | |

**Lossy:** YES / NO

**Divergent:** YES / NO

**Explanation:**  

## Most Important Lesson from the Week

[2–3 sentences]
```
