# Day 1 Exercise: From Ontology Tradecraft to OWL

## Purpose

In the lecture, we began with a competency question, identified the entities and relations needed to answer it, disambiguated potentially confusing terms, and constructed a design pattern.

In this exercise, you will take the next step: encode a simplified version of that model in OWL using Protégé, then use an automated reasoner to:

1. derive a classification that you did not assert directly; and
2. detect a category mistake involving a process and information about that process.

The exercise uses the patrol-boat example from the lecture.

## Competency question

> At what speed does a patrol boat move, measured in knots, during a one-hour interval?

The model will represent:

- a particular patrol boat;
- a particular act of motion in which the boat participates;
- a speed measurement datum about that act of motion;
- a duration measurement datum about that act of motion;
- the measurement units knot and hour.

The exercise deliberately focuses on a small number of OWL constructs. It is not intended to produce a complete measurement ontology.

## Learning objectives

By the end of the exercise, you should be able to:

- place domain classes beneath appropriate BFO classes;
- distinguish a process from information about that process;
- create individuals and add class assertions;
- add object-property and data-property assertions;
- define a class using necessary and sufficient conditions;
- run HermiT and inspect inferred types;
- produce, diagnose, and repair an inconsistency.

## Files

Use the following files without changing their relative locations:

```text
starter/
├── patrol-boat-starter.ttl
├── catalog-v001.xml
└── imports/
    └── bfo-core.ttl
```

Before beginning, follow the instructions in [`protege-setup.md`](protege-setup.md).

---

## Part 1: Open the starter ontology and save a working copy

1. Open Protégé Desktop.
2. Select **File → Open**.
3. Open:

   ```text
   starter/patrol-boat-starter.ttl
   ```

4. Confirm that the ontology opens without an import error.
5. Select **File → Save As**.
6. Save a working copy with a new name, for example:

   ```text
   patrol-boat-yourname.ttl
   ```

Do not edit `bfo-core.ttl`. BFO is an imported ontology. Your edits belong in the patrol-boat ontology.

### Checkpoint

In the class hierarchy, you should be able to find the imported BFO classes:

- `material entity`
- `process`
- `generically dependent continuant`

You should also be able to find the local classes:

- `PatrolBoat`
- `ActOfMotion`
- `MeasurementDatum`
- `SpeedMeasurementDatum`
- `DurationMeasurementDatum`
- `MeasurementUnit`
- `MovingPatrolBoat`

At this stage, most local classes will still appear directly beneath `owl:Thing`.

---

## Part 2: Complete the class hierarchy

The first task is to place each local class beneath the class that represents the correct kind of entity.

### 2.1 Place `PatrolBoat`

1. Open the **Entities** tab.
2. Select `PatrolBoat`.
3. In the **SubClass Of** section, click **+**.
4. Add:

   ```text
   material entity
   ```

The resulting axiom should be:

```text
PatrolBoat SubClassOf material entity
```

### 2.2 Place `ActOfMotion`

Add:

```text
ActOfMotion SubClassOf process
```

### 2.3 Place `MeasurementDatum`

Add:

```text
MeasurementDatum SubClassOf generically dependent continuant
```

This records the modeling decision that a measurement datum is information, not the process measured.

### 2.4 Place the specialized measurement classes

Add:

```text
SpeedMeasurementDatum SubClassOf MeasurementDatum
DurationMeasurementDatum SubClassOf MeasurementDatum
```

### 2.5 Place `MeasurementUnit`

Add:

```text
MeasurementUnit SubClassOf generically dependent continuant
```

For this exercise, measurement units are treated as informational standards that can be used by measurement data.

### Checkpoint

Your asserted class hierarchy should now include the following paths:

```text
material entity
  └── PatrolBoat

process
  └── ActOfMotion

generically dependent continuant
  └── MeasurementDatum
      └── SpeedMeasurementDatum

generically dependent continuant
  └── MeasurementDatum
      └── DurationMeasurementDatum

generically dependent continuant
  └── MeasurementUnit
```

Do not yet add a superclass or definition for `MovingPatrolBoat`.

---

## Part 3: Create the individuals

Create the following individuals:

| Individual | Asserted type |
|---|---|
| `patrol_boat_01` | `PatrolBoat` |
| `motion_01` | `ActOfMotion` |
| `speed_measurement_01` | `SpeedMeasurementDatum` |
| `duration_measurement_01` | `DurationMeasurementDatum` |
| `knot` | `MeasurementUnit` |
| `hour` | `MeasurementUnit` |

One reliable method is:

1. Select the class in the class hierarchy.
2. In the **Instances** section, click **+**.
3. Create the individual with the exact name shown above.

You may also use the **Individuals by class** tab.

### Checkpoint

Select each individual and inspect its **Types** section. Each individual should have exactly the intended asserted type listed above.

---

## Part 4: Add the object-property assertions

Open the **Individuals by class** tab and select the relevant individual.

### 4.1 Connect the patrol boat to its motion

Select `patrol_boat_01`.

In **Object property assertions**, add:

```text
patrol_boat_01 participates in motion_01
```

Use the imported BFO property labeled `participates in`.

This assertion says that the patrol boat is a participant in the act of motion. It does not say that the boat is identical with the motion.

### 4.2 State what the speed measurement is about

Select `speed_measurement_01`.

Add:

```text
speed_measurement_01 is about motion_01
```

### 4.3 State what the duration measurement is about

Select `duration_measurement_01`.

Add:

```text
duration_measurement_01 is about motion_01
```

### 4.4 Add the measurement units

For `speed_measurement_01`, add:

```text
speed_measurement_01 has measurement unit knot
```

For `duration_measurement_01`, add:

```text
duration_measurement_01 has measurement unit hour
```

### Checkpoint

Your object-property assertions should form this graph:

```text
patrol_boat_01
    participates in
motion_01

speed_measurement_01
    is about
motion_01

duration_measurement_01
    is about
motion_01

speed_measurement_01
    has measurement unit
knot

duration_measurement_01
    has measurement unit
hour
```

---

## Part 5: Add the data-property assertions

### 5.1 Record the speed value

Select `speed_measurement_01`.

In **Data property assertions**, add:

```text
has decimal value 12.0
```

Use the datatype:

```text
xsd:decimal
```

### 5.2 Record the duration value

Select `duration_measurement_01`.

Add:

```text
has decimal value 1.0
```

Use the datatype:

```text
xsd:decimal
```

### Checkpoint

You have now encoded the following claims:

- the patrol boat participates in a particular act of motion;
- a speed measurement datum is about that act of motion;
- the speed measurement has the value `12.0` and uses the unit knot;
- a duration measurement datum is about that act of motion;
- the duration measurement has the value `1.0` and uses the unit hour.

The number `12.0` is not the motion. It is a literal value contained in information about the motion.

---

## Part 6: Define `MovingPatrolBoat`

You will now add a class definition that gives necessary and sufficient conditions for classification as a `MovingPatrolBoat`.

1. Return to the **Entities** tab.
2. Select `MovingPatrolBoat`.
3. In the **Equivalent To** section, click **+**.
4. Enter the following Manchester OWL class expression:

```text
PatrolBoat and 'participates in' some ActOfMotion
```

5. Accept the expression.

The completed definition says:

> Something is a `MovingPatrolBoat` if and only if it is a `PatrolBoat` and participates in at least one `ActOfMotion`.

This is stronger than merely stating:

```text
MovingPatrolBoat SubClassOf PatrolBoat
```

A subclass axiom would say only that every moving patrol boat is a patrol boat. It would not provide enough information for the reasoner to classify a patrol boat as moving.

### Checkpoint

The description of `MovingPatrolBoat` should show:

```text
Equivalent To:
    PatrolBoat and 'participates in' some ActOfMotion
```

---

# Part 7: Reasoner Challenge I — Derive an unasserted classification

## The question

You asserted that:

1. `patrol_boat_01` is a `PatrolBoat`;
2. `patrol_boat_01` participates in `motion_01`;
3. `motion_01` is an `ActOfMotion`.

You did **not** assert:

```text
patrol_boat_01 Type MovingPatrolBoat
```

Ask the reasoner whether that classification follows from the axioms you did assert.

## Run HermiT

1. Select **Reasoner → HermiT**.
2. Select **Reasoner → Start reasoner**, or press:
   - **Ctrl+R** on Windows or Linux;
   - **Command+R** on macOS.
3. Wait for classification to finish.
4. Open the **Individuals by class** tab.
5. Select `patrol_boat_01`.
6. Inspect the **Types** section.

## Expected result

You should see:

```text
MovingPatrolBoat
```

as an **inferred** type. In Protégé, inferred information is normally displayed with a pale yellow background.

The reasoner derived the classification because the individual satisfies both parts of the equivalent-class definition:

```text
patrol_boat_01 Type PatrolBoat
patrol_boat_01 participates in motion_01
motion_01 Type ActOfMotion
```

Therefore:

```text
patrol_boat_01 Type MovingPatrolBoat
```

## Dependency test

Now test whether the inference really depends on the participation assertion.

1. Stop or pause the reasoner if Protégé requires it.
2. Remove:

   ```text
   patrol_boat_01 participates in motion_01
   ```

3. Synchronize or restart HermiT.
4. Inspect the inferred types of `patrol_boat_01`.

The inferred `MovingPatrolBoat` type should disappear.

5. Restore the participation assertion.
6. Synchronize or restart HermiT.
7. Confirm that the inferred type returns.

---

# Part 8: Reasoner Challenge II — Detect and repair a category mistake

The lecture distinguished:

- a process; from
- information about that process.

You correctly modeled:

```text
motion_01 Type ActOfMotion
```

and:

```text
speed_measurement_01 Type SpeedMeasurementDatum
speed_measurement_01 is about motion_01
```

You will now intentionally violate that distinction.

## Introduce the error

1. Select `motion_01`.
2. In the **Types** section, add the additional asserted type:

   ```text
   SpeedMeasurementDatum
   ```

`motion_01` now has both of these asserted types:

```text
ActOfMotion
SpeedMeasurementDatum
```

## Run HermiT again

1. Synchronize or restart the reasoner.
2. Protégé should report that the ontology is inconsistent.

The inconsistency is not caused by the label `motion_01`. It is caused by the combination of the following logical commitments:

```text
motion_01 Type ActOfMotion
ActOfMotion SubClassOf process
process SubClassOf occurrent

motion_01 Type SpeedMeasurementDatum
SpeedMeasurementDatum SubClassOf MeasurementDatum
MeasurementDatum SubClassOf generically dependent continuant
generically dependent continuant SubClassOf continuant

continuant DisjointWith occurrent
```

## Repair the ontology

Repair the error by removing only this assertion:

```text
motion_01 Type SpeedMeasurementDatum
```

Do **not** repair the ontology by:

- deleting BFO's disjointness axiom;
- moving `ActOfMotion` out from under `process`;
- moving `MeasurementDatum` out from under `generically dependent continuant`;
- deleting the distinction between the process and the datum.

Run HermiT again.

## Expected result after repair

- the ontology is consistent;
- `patrol_boat_01` is again inferred to be a `MovingPatrolBoat`;
- `motion_01` is an `ActOfMotion`, not a measurement datum;
- `speed_measurement_01` remains information about `motion_01`.

## Why you are doing this

The challenge connects the modeling recipe to information quality.

The reasoner can detect the error only because the ontology contains explicit commitments about:

- which classes are subclasses of which BFO categories;
- which categories are disjoint;
- which individual instantiates which classes.

The software cannot determine the correct interpretation of the word *speed* for you. That was the tradecraft task. Once the distinction is encoded, however, automated reasoning can help preserve it.

---

## Part 9: Final verification

Before saving, confirm all of the following:

- [ ] `PatrolBoat` is a subclass of `material entity`.
- [ ] `ActOfMotion` is a subclass of `process`.
- [ ] `MeasurementDatum` is a subclass of `generically dependent continuant`.
- [ ] `SpeedMeasurementDatum` and `DurationMeasurementDatum` are subclasses of `MeasurementDatum`.
- [ ] `patrol_boat_01` participates in `motion_01`.
- [ ] `speed_measurement_01` is about `motion_01`.
- [ ] `duration_measurement_01` is about `motion_01`.
- [ ] The speed value is `12.0` with unit `knot`.
- [ ] The duration value is `1.0` with unit `hour`.
- [ ] `MovingPatrolBoat` has the equivalent-class definition given above.
- [ ] HermiT reports the ontology as consistent.
- [ ] `patrol_boat_01` has the inferred type `MovingPatrolBoat`.
- [ ] `motion_01` is not asserted to be a `SpeedMeasurementDatum`.

Save your completed ontology.
