## Exercise

Four cases are available. **Choose two cases to complete.**

Each case is already scoped and serves as a competency question. You do not need to define a new scope or write additional competency questions.

For each selected case, you will:

1. construct a reusable ontology design pattern;
2. encode the pattern in OWL using Protégé;
3. add source-specific individuals and values where needed;
4. write definitions for the classes and relations you create;
5. write identifying descriptions for the named individuals you create;
6. run a reasoner.

There may be more than one defensible solution. Your submission should make its modeling commitments explicit and apply them consistently.

---

## Required Files

Submit the following for each of the two cases you select:

```text
YOUR-NAME/
├── case-N-pattern.png
├── case-N.owl
├── case-M-pattern.png
├── case-M.owl
```

Replace `N` and `M` with the numbers of the cases you completed.

PDF or SVG pattern diagrams are also acceptable.

Definitions should be included as annotations in the OWL files.

---

## Design-Pattern Requirements

For each selected case, create a diagram that distinguishes:

- classes;
- named individuals;
- literal values;
- object-property relations;
- data-property relations.

Do not merely redraw a spreadsheet row using its particular values.

Unless otherwise stated, a class-level arrow from `A` to `B` labeled `R` should be understood as:

```text
A SubClassOf R some B
```

Include only arrows that you intend to encode.

---

## Definition Requirements

Definitions should make explicit the same distinctions represented in the design pattern and OWL model.

### Classes

Write one textual definition for every locally created class.

Use the genus–differentia form:

> **A [genus] that [differentia].**

A class definition should:

- begin with one appropriate genus;
- use the closest appropriate parent class when possible;
- state the characteristics that distinguish the class from sibling classes;
- define the entity rather than the word or ontology label;
- avoid circularity;
- avoid examples and encyclopedic information;
- be neither too broad nor too narrow; and
- agree with the OWL axioms.

### Relations

Write one textual definition for every locally created object property or data property.

A useful form is:

> **A relation that holds between [source] and [target] when [condition].**

A relation definition should explain what must be true when the relation holds. Do not define a relation merely by repeating its label or listing its domain and range.

### Named Individuals

For every locally created named individual, write a brief identifying description.

The description should identify:

- what type of entity it is;
- which case element or source record it represents; and
- what distinguishes it from other individuals in the model.

---