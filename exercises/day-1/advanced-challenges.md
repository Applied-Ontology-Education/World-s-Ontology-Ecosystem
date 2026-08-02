# Advanced Challenges: Reasoning Beyond the Core Exercise

## Purpose

These challenges are for participants who complete the required Day 1 exercise early or who already have experience with Protégé and OWL.

Continue working in the ontology you completed during the main exercise. Do not begin from a new starter file unless your working ontology has become inconsistent and you cannot repair it.

Each challenge introduces a distinct feature of OWL reasoning:

1. classification using a value restriction;
2. the distinction between an unsatisfiable class and an inconsistent ontology;
3. the inferential behavior of domain and range axioms;
4. the open-world assumption.

## Before each challenge

For every challenge:

1. Read the task fully.
2. Predict what HermiT will infer before running it.
3. Identify the axioms that support your prediction.
4. Run HermiT.
5. Compare the result with your prediction.
6. Repair or restore the ontology before moving to the next challenge.

Do not merely click through the instructions. The goal is to understand why the reasoner produces each result.

---

# Challenge 1: Classify a measurement by its unit

## Goal

Define a class of speed measurements that use knots, then ask HermiT to classify an existing measurement datum into that class.

You already created:

```text
speed_measurement_01 Type SpeedMeasurementDatum
speed_measurement_01 has measurement unit knot
```

You will now define a class whose members satisfy those conditions.

## Step 1: Create the class

1. Open the **Entities** tab.
2. Select the class hierarchy.
3. Create a new class named:

   ```text
   KnotSpeedMeasurementDatum
   ```

## Step 2: Add an equivalent-class definition

Select `KnotSpeedMeasurementDatum`.

In the **Equivalent To** section, add:

```text
SpeedMeasurementDatum and 'has measurement unit' value knot
```

This definition says:

> Something is a `KnotSpeedMeasurementDatum` if and only if it is a `SpeedMeasurementDatum` and has the individual `knot` as one of its measurement units.

## Step 3: Predict the inference

Before running HermiT, answer:

> Should `speed_measurement_01` be inferred to be a `KnotSpeedMeasurementDatum`?

Identify the assertions that matter:

```text
speed_measurement_01 Type SpeedMeasurementDatum
speed_measurement_01 has measurement unit knot
```

Do not manually assert:

```text
speed_measurement_01 Type KnotSpeedMeasurementDatum
```

## Step 4: Run HermiT

1. Select **Reasoner → HermiT**.
2. Start or synchronize the reasoner.
3. Open **Individuals by class**.
4. Select `speed_measurement_01`.
5. Inspect the **Types** section.

## Expected result

HermiT should infer:

```text
speed_measurement_01 Type KnotSpeedMeasurementDatum
```

The inferred type should appear separately from the asserted types.

## Step 5: Test the dependency

1. Remove:

   ```text
   speed_measurement_01 has measurement unit knot
   ```

2. Synchronize HermiT.
3. Inspect the inferred types of `speed_measurement_01`.

The inferred `KnotSpeedMeasurementDatum` type should disappear.

4. Restore the measurement-unit assertion.
5. Synchronize HermiT.
6. Confirm that the inferred type returns.

---

# Challenge 2: Unsatisfiable class versus inconsistent ontology

## Goal

Create a class whose definition cannot possibly have an instance, then distinguish that result from a fully inconsistent ontology.

## Step 1: Create the class

Create a new class named:

```text
ProcessMeasurement
```

## Step 2: Define the class

Add the following equivalent-class definition:

```text
ActOfMotion and MeasurementDatum
```

This says:

> Something is a `ProcessMeasurement` if and only if it is both an `ActOfMotion` and a `MeasurementDatum`.

## Step 3: Predict the result

Before running HermiT, trace the superclass paths.

For `ActOfMotion`:

```text
ActOfMotion
SubClassOf process
SubClassOf occurrent
```

For `MeasurementDatum`:

```text
MeasurementDatum
SubClassOf generically dependent continuant
SubClassOf continuant
```

BFO declares:

```text
continuant DisjointWith occurrent
```

Ask:

> Can anything instantiate both `ActOfMotion` and `MeasurementDatum`?

## Step 4: Run HermiT

1. Start or synchronize HermiT.
2. Inspect the class hierarchy.
3. Locate `ProcessMeasurement`.

## Expected result

`ProcessMeasurement` should be classified beneath or as equivalent to:

```text
owl:Nothing
```

Protégé normally displays an unsatisfiable class in red.

The ontology itself should still be consistent.

## Why the ontology remains consistent

The ontology currently says only that `ProcessMeasurement` is a class that cannot have any instances.

An ontology can consistently contain an empty class.

The ontology becomes inconsistent only if something is asserted to instantiate that impossible class.

## Step 5: Make the ontology inconsistent

Create an individual named:

```text
impossible_01
```

Assert:

```text
impossible_01 Type ProcessMeasurement
```

Run HermiT again.

## Expected result

The ontology should now be inconsistent.

The axioms jointly require `impossible_01` to be both:

```text
an occurrent
```

and:

```text
a continuant
```

which BFO forbids.

## Step 6: Repair the ontology

Remove:

```text
impossible_01 Type ProcessMeasurement
```

You may delete the individual entirely.

Run HermiT again.

Confirm:

- the ontology is consistent;
- `ProcessMeasurement` remains unsatisfiable.

---

# Challenge 3: Discover what domain and range axioms do

## Goal

Observe that OWL domain and range axioms infer types. They do not operate like ordinary database field constraints.

## Step 1: Add a domain

Select the object property:

```text
has measurement unit
```

Add the domain:

```text
MeasurementDatum
```

The axiom means:

> Anything that bears the relation `has measurement unit` to something is a `MeasurementDatum`.

It does not mean:

> Only allow users to enter this relation when the subject has already been labeled as a `MeasurementDatum`.

## Step 2: Add a range

Add the range:

```text
MeasurementUnit
```

The axiom means:

> Anything that occurs as the object of `has measurement unit` is a `MeasurementUnit`.

## Step 3: Confirm the normal case

Run HermiT.

The ontology should remain consistent because:

```text
speed_measurement_01 has measurement unit knot
```

already fits the intended model.

HermiT may infer types already asserted explicitly.

## Step 4: Add a deliberately incorrect assertion

Add:

```text
motion_01 has measurement unit knot
```

Do not add a new type assertion to `motion_01`.

## Step 5: Predict the reasoner behavior

Ask:

> Will Protégé reject the assertion, ignore it, or infer a new type for `motion_01`?

Trace the domain consequence:

```text
motion_01 has measurement unit knot
```

together with:

```text
Domain of has measurement unit = MeasurementDatum
```

entails:

```text
motion_01 Type MeasurementDatum
```

But you already asserted:

```text
motion_01 Type ActOfMotion
```

Those types lead to disjoint BFO categories.

## Step 6: Run HermiT

Synchronize the reasoner.

## Expected result

The ontology should become inconsistent.

The reasoner infers:

```text
motion_01 Type MeasurementDatum
```

because `motion_01` occurs in the domain position of `has measurement unit`.

This gives two paths:

```text
motion_01
Type ActOfMotion
SubClassOf process
SubClassOf occurrent
```

and:

```text
motion_01
Type MeasurementDatum
SubClassOf generically dependent continuant
SubClassOf continuant
```

Because `continuant` and `occurrent` are disjoint, the ontology is inconsistent.

## Step 7: Repair the ontology

Remove:

```text
motion_01 has measurement unit knot
```

Run HermiT again.

Confirm that the ontology is consistent.

Do not remove the domain or range axioms merely to conceal the incorrect assertion.

---

# Challenge 4: Encounter the open-world assumption

## Goal

Show that the absence of an assertion does not establish that the corresponding relation does not hold.

## Step 1: Create a class

Create:

```text
StationaryPatrolBoat
```

## Step 2: Define the class

Add the equivalent-class definition:

```text
PatrolBoat and ('participates in' max 0 ActOfMotion)
```

This definition says:

> Something is a `StationaryPatrolBoat` if and only if it is a `PatrolBoat` and participates in no instances of `ActOfMotion`.

## Step 3: Remove the known motion assertion

Remove:

```text
patrol_boat_01 participates in motion_01
```

Do not add any negative assertion or maximum-cardinality assertion yet.

## Step 4: Predict the result

Ask:

> Since the ontology no longer states that the boat participates in an act of motion, will HermiT infer that it is stationary?

Run HermiT and inspect the inferred types of `patrol_boat_01`.

## Expected result

HermiT should **not** infer:

```text
patrol_boat_01 Type StationaryPatrolBoat
```

The ontology no longer knows that the boat participates in a motion, but it also does not know that the boat participates in none.

## Why no inference occurs

OWL uses the open-world assumption.

Removing:

```text
patrol_boat_01 participates in motion_01
```

does not entail:

```text
patrol_boat_01 participates in no ActOfMotion
```

It means only that the current ontology does not assert the relation.

## Step 5: Add the missing negative commitment

Select `patrol_boat_01`.

Add the class assertion:

```text
'participates in' max 0 ActOfMotion
```

This is an anonymous class assertion. It explicitly states that `patrol_boat_01` participates in at most zero acts of motion.

Run HermiT.

## Expected result

HermiT should now infer:

```text
patrol_boat_01 Type StationaryPatrolBoat
```

The individual now satisfies both parts of the equivalent-class definition:

```text
patrol_boat_01 Type PatrolBoat
patrol_boat_01 Type ('participates in' max 0 ActOfMotion)
```

## Step 6: Test the contradiction

Restore:

```text
patrol_boat_01 participates in motion_01
```

while retaining:

```text
'participates in' max 0 ActOfMotion
```

Run HermiT.

## Expected result

The ontology should become inconsistent.

You have asserted both:

- that the boat participates in an `ActOfMotion`; and
- that it participates in at most zero `ActOfMotion` instances.

## Step 7: Repair the ontology

For the original exercise model:

1. retain:

   ```text
   patrol_boat_01 participates in motion_01
   ```

2. remove:

   ```text
   'participates in' max 0 ActOfMotion
   ```

3. run HermiT and confirm that the ontology is consistent.

---
