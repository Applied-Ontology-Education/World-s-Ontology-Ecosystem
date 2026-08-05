# Day 3 Exercise: Evaluating an AI-Generated Ontology

## Purpose

Large language models can generate ontology syntax quickly. This exercise asks whether the resulting artifact is actually a defensible ontology.

You will choose a domain, write your own prompt, and use any large language model you prefer to generate an OWL ontology. You will then use the lessons from Days 1 and 2 to evaluate and repair the generated ontology.

Your evaluation should draw on:

- the seven-step strategy from material entities to information from Day 1;
- ontology design-pattern thinking;
- the definition-writing guidelines from Day 2;
- distinctions among classes, individuals, relations, and literal values;
- appropriate use of OWL axioms and restrictions;
- Protégé and an OWL reasoner; and
- your own domain and ontological judgment.

The goal is not merely to find syntax errors. A generated ontology may open in Protégé and remain logically consistent while still containing poor definitions, category mistakes, unsupported relations, weak modeling decisions, or failures to represent the intended domain.

By the end of the exercise, you should be able to distinguish:

1. problems caused by the prompt;
2. problems caused by the generated model;
3. problems detectable by an OWL reasoner;
4. problems that require domain or ontological judgment; and
5. corrections that improve the ontology rather than merely changing its appearance.

---

## Core Task

Complete the following:

1. choose a narrowly defined domain;
2. write a prompt requesting an OWL ontology for that domain;
3. use any large language model to generate the ontology;
4. open the generated ontology in Protégé;
5. identify at least **five substantive problems**;
6. correct those problems in a revised copy; and
7. run an OWL reasoner before and after revision.

Your five issues must include:

- at least one ontological or category error;
- at least one definition problem;
- at least one logical or OWL modeling problem; and
- at least one problem involving relations.

---

## Step 1: Choose a Domain and Write the Prompt

Choose a domain narrow enough to model and evaluate during the exercise.

Examples include:

- a university course;
- a restaurant reservation;
- a vehicle-maintenance process;
- a conference submission;
- a medical appointment;
- a library-loan process;
- an emergency-response scenario; or
- another domain you understand well.

Write a prompt asking the model to generate an OWL ontology that can be opened in Protégé.

Your prompt should state:

- the domain to be represented;
- the purpose of the ontology;
- the kinds of questions the ontology should support;
- the desired serialization, such as RDF/XML or Turtle;
- whether definitions should be included;
- whether named individuals should be included; and
- any upper ontology, reused terminology, or modeling constraints you want the model to follow.

Do not improve the generated ontology before saving the original output.

Save the prompt as:

```text
prompt.md
```

Save the original generated ontology as:

```text
generated-ontology.owl
```

If the model produces invalid syntax, you may ask it to repair the syntax so that the file opens in Protégé. Record that additional prompt in `prompt.md`. Do not ask the model to correct substantive modeling problems before your evaluation.

---

## Step 2: Record the Intended Model

Before inspecting the generated ontology, record:

- what the ontology is intended to represent;
- what questions it should support;
- which terms appear central to the domain;
- what assumptions your prompt gives the model; and
- what important modeling guidance your prompt omits.

Use your own stated purpose and questions as the basis for evaluating the ontology.

Do not evaluate the ontology only by asking whether its labels sound plausible.

---

## Step 3: Inspect the Ontology Before Reasoning

Open `generated-ontology.owl` in Protégé.

Inspect:

- the class hierarchy;
- object properties;
- data properties;
- named individuals;
- annotations and definitions;
- imported ontologies;
- domain and range axioms;
- restrictions;
- disjointness axioms; and
- equivalent-class axioms.

Look for warning signs, including:

- every noun becoming a class;
- classes and individuals being confused;
- information being confused with what it is about;
- roles being confused with their bearers;
- processes being represented as objects or attributes;
- relations created merely by converting verbs into property names;
- labels being used without definitions;
- invented upper-level categories;
- duplicated terms;
- vague or overly broad classes;
- unsupported domain and range axioms;
- unjustified equivalence axioms; and
- universal claims inferred from examples.

---

## Step 4: Run the Reasoner

Run an OWL reasoner.

Record:

- whether the ontology is consistent;
- whether any classes are unsatisfiable;
- whether unexpected equivalences appear;
- whether expected classifications are inferred; and
- which problems the reasoner fails to detect.

Remember:

> Logical consistency is necessary, but it is not sufficient for ontological adequacy.

A reasoner can determine whether the axioms are formally compatible. It cannot determine whether the ontology represents the domain correctly.

---

## Step 5: Evaluate the Definitions

Use the definition-writing guidelines from Day 2.

For important classes, ask:

- Does the definition use the genus–differentia form?
- Does it begin with one appropriate genus?
- Is the genus the closest appropriate parent class?
- Does it define the entity rather than the label or ontology representation?
- Is it circular?
- Is it too broad or too narrow?
- Does it include examples or encyclopedic information rather than defining information?
- Does it rely on vague expressions such as “usually,” “generally,” or “related to”?
- Does it agree with the logical axioms?

Identify at least one definition that should be revised.

Provide a replacement definition and explain why it is better.

---

## Step 6: Evaluate Classes, Relations, and Axioms

### Classes

Ask:

- Is each class a repeatable type of entity?
- Are sibling classes distinguished clearly?
- Are subclass axioms justified, e.g. for A subclass of B, is every instance of A an instance of B?

### Relations

Ask:

- Does each relation have a clear meaning?
- Are domain and range axioms justified?
- Are vague relations such as `related_to`, `has_data`, or `involves` doing too much work?
- Does the relation connect entities of the appropriate kinds?

### Individuals and Literal Values

Ask:

- Are named individuals truly particular entities?
- Has the model created individuals merely to represent labels or values?
- Are source-specific assertions being treated as universal truths?

---

## Step 7: Repair the Ontology

Create a copy of the ontology named:

```text
revised-ontology.owl
```

Correct the substantive problems you identified.

Possible corrections include:

- moving a class to a more appropriate parent;
- distinguishing a class from an individual;
- distinguishing information from what it is about;
- distinguishing a role from its bearer;
- replacing a vague or circular definition;
- removing an unjustified equivalence;
- correcting a relation;
- adding a missing definition; or
- separating universal claims from source-specific assertions.

After making the corrections:

1. save the ontology;
2. run the reasoner again;
3. inspect the inferred hierarchy; and
4. record whether the corrections introduced unexpected consequences.

---

## Required Submission

Create a folder using your name or group name:

```text
YOUR-NAME/
├── prompt.md
├── generated-ontology.owl
├── revised-ontology.owl
```