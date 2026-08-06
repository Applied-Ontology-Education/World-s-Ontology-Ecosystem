# Day 4 Exercise: Abductive Agents and the Zebra Puzzle

## Overview

In this exercise, you will compare two forms of automated reasoning:

- **Abductive reasoning with a generative AI model**, which proposes the most plausible answer from incomplete information.
- **Deductive reasoning with an OWL reasoner**, which derives only what follows logically from the axioms encoded in an ontology.

You will model the Zebra Puzzle in Protégé, add its clues in stages, and compare the guesses produced by a generative AI model with the conclusions produced by HermiT.

## Learning Goals

By the end of the exercise, you should be able to:

1. Explain the difference between deductive and abductive reasoning.
2. Encode puzzle constraints as OWL axioms.
3. Use a generative AI model to make abductive guesses from incomplete information.
4. Use HermiT to determine what follows deductively from an OWL ontology.
5. Evaluate how the outputs of a generative AI model change as additional axioms are supplied.

## What You Will Need

- Protégé and the HermiT reasoner
- Access to a generative AI model of your choice
- A copy of this repository

## Important Rule for the AI Model

The Zebra Puzzle is widely known, and its solution is available online. Tell the model:

> Do not search the web, retrieve a memorized solution, or rely on prior knowledge of the Zebra Puzzle. Reason only from the clues supplied in this prompt.

The purpose of the exercise is to observe abductive reasoning from incomplete information. Looking up the known solution undermines the experiment.

---

## Part 1: Create the Ontology

Create a new OWL ontology in Protégé.

Your ontology should represent:

1. There are five houses.
2. The Englishman lives in the red house.
3. The Spaniard owns the dog.
4. Coffee is drunk in the green house.
5. The Ukrainian drinks tea.

Add appropriate domains, ranges, inverses, and cardinality constraints. 

Use classes and restrictions where the identity of an individual is not yet known. The goal is to allow the reasoner to determine instance-level facts from the constraints.

Run HermiT and examine what information - if any - has been inferred (look for lines in yellow in Protege).

---

## Part 2: First Abductive Guess

Give your AI model the OWL file you've created and ask:

> Who owns the zebra? Make the best abductive guess you can from only these clues. Explain your reasoning, identify any assumptions you make, and state how confident you are.

Save the model's response.

At this stage, the model does not have enough information to determine the answer deductively. It may still make a guess.

---

## Part 3: Add the Second Group of Clues

Add these clues to both the ontology:

6. The green house is immediately to the right of the ivory house.
7. The Old Gold smoker owns snails.
8. Kools are smoked in the yellow house.

Run HermiT and examine what information - if any - has been inferred (look for lines in yellow in Protege).

Then ask the AI model to answer the question against your updated OWL file. Tell it not to preserve its earlier answer merely for consistency.

---

## Part 4: Add the Third Group of Clues

Add these clues to your OWL file:

9. Milk is drunk in the middle house.
10. The Norwegian lives in the first house.
11. The person who smokes Chesterfields lives next to the person who owns the fox.

Run HermiT and examine what information - if any - has been inferred (look for lines in yellow in Protege).

Then ask the AI model to answer the question against your updated OWL file. Tell it not to preserve its earlier answer merely for consistency.

---

## Part 5: Complete the Puzzle

Add the remaining clues:

12. Kools are smoked in a house next to the house where the horse is kept.
13. The Lucky Strike smoker drinks orange juice.
14. The Japanese person smokes Parliaments.
15. The Norwegian lives next to the blue house.

Before running HermiT, verify that:

- all five members of each category are represented;
- the five houses are ordered correctly;
- `next to` is represented symmetrically;
- `immediately to the right of` has the intended direction;
- inverse properties are declared where appropriate;
- domains and ranges point in the correct direction;
- one-to-one constraints are represented;
- individuals that must be distinct are declared different;
- none of the clues has been encoded as the desired conclusion.

Run HermiT and inspect the inferred facts. If you've done the exercise correctly, the owner of the zebra will be revealed as a consequence of your assertions. 

Finally, give the AI model the complete set of assertions and ask it to answer one last time.

The OWL reasoner and the AI model should now reach the same answer, although they may reach it in very different ways...or perhaps not at all...

---

## Deliverables

Submit:

1. Your completed OWL file.
2. A prompt-and-response log for all four AI runs.
