# Day 5 Capstone

## Participants
Luay M. Assidmi

## Model
[capstone-model.owl](./capstone-model.owl)

## Three Definitions

1. **MaintenanceProcedure** (class)
   Genus: information artifact (the closest asserted parent in the model — `bfo:GenericallyDependentContinuant`)
   Differentia: specifies a recurring inspection requirement for a piece of equipment

   **Definition:** An information artifact that specifies a recurring inspection requirement for a piece of equipment.

2. **Inspection** (class)
   Genus: process (matches `bfo:Process`, the direct OWL parent — genus proximus)
   Differentia: performed by a person bearing a technician role, evaluates a piece of equipment against a maintenance procedure's requirements, yields a report and measurement data as output

   **Definition:** A process, performed by a person bearing a technician role, that evaluates a piece of equipment against the requirements of a maintenance procedure and yields a report and associated measurement data as output.

   *Note: "examines"/"inspects" were deliberately avoided as the defining verb — those are grammatically-derived synonyms of the definiendum itself, which counts as circularity even when the exact label isn't repeated.*

3. **recommends** (relation)
   Relations take "when does this hold between two entities" phrasing rather than genus-differentia.

   **Definition:** `recommends` holds between an inspection report and a process type when the content of the report states that an instance of that process type ought to be performed, without the report asserting that such a process has already taken place.

## AI Comparison

### Difference 1
**AI suggestion:**
`:Alex rdf:type owl:NamedIndividual, :Technician` — Alex is typed directly as `:Technician`, with `:Technician` declared as a bare class (no `Person` class, no role individual, no `subClassOf` link at all).

**Decision:** MODIFY

**Reason:**
This is a role/bearer conflation: typing Alex straight to `Technician` makes "being a technician" indistinguishable from "being a person," with no way to represent Alex ceasing to be a technician without deleting his type entirely. Reinterpret `:Technician` as a `Role` class (matching `TechnicianRole`), keep a separate `Person` class, and connect Alex to the role via `bearer_of` and a role individual — the AI's naming survives, the conflation doesn't.

### Difference 2
**AI suggestion:**
`:Bearing_Replacement_P17 rdf:type owl:NamedIndividual, :MaintenanceAction` — the recommended/requested bearing replacement is instantiated as a concrete individual, with `:targets_equipment :P_17`, and both `R_17 identifies_need_for` and `W_22 requests` point at that same individual.

**Decision:** REJECT

**Reason:**
`MaintenanceAction` reads as a process/action type, and instantiating it as a real individual asserts that a specific, particular action-entity now exists — treating a recommendation and a request as though they refer to something already underway. This is exactly the prescription-as-fact confusion the model is built to avoid: nothing in the scenario says the bearing replacement occurred, or even that a single particular replacement-plan exists yet — only that it was identified and requested. `BearingReplacement` is kept as a class only, referenced but never instantiated, for exactly this reason.

### Difference 3
**AI suggestion:**
`:has_interval_days rdf:type owl:DatatypeProperty ; rdfs:range xsd:integer .` with `Pump_Inspection_Rule_1 :has_interval_days 30` — the inspection interval is a typed integer with a self-documenting property name, versus `:has_inspection_interval "30 days"` (a plain string).

**Decision:** ACCEPT

**Reason:**
This is a genuine improvement, not just a stylistic difference. A string literal like `"30 days"` is opaque to a reasoner or query — no arithmetic, no comparison across procedures, no validation that it's even numeric without string parsing. The AI's `xsd:integer` value plus a unit-bearing property name (`has_interval_days`) conveys the same information in a machine-usable form, matching the same value/unit split already used correctly for the vibration reading (`has_decimal_value` / `has_measurement_unit`).

## Reasoner Results
- **Consistent:** Yes. HermiT completed with no inconsistency.
- **Unsatisfiable classes:** None. Every class remains distinct from `owl:Nothing`.
- **Expected inferences:** Upward class propagation for every individual, correctly following the asserted subclass hierarchy — none of this was asserted directly on the individuals, only derived from class-level `subClassOf` axioms:
  - `Inspection_17` → also classified as `bfo:Process`
  - `MaintenanceProcedure_1` → also classified as `bfo:GDC`
  - `Report_R17`, `WorkOrder_W22`, `VibrationMeasurementDatum_1` → also classified as `bfo:GDC`
  - `Alex`, `Pump_P17` → also classified as `bfo:MaterialEntity`
  - `PumpVibration_1` → also classified as `bfo:Quality`
  - `Alex_TechnicianRole` → also classified as `bfo:Role`

  All asserted object-property triples (`realizes`, `has_participant`, `has_specified_output`, `recommends`, `based_on`, `requests`, `bearer_of`, `inheres_in`, `is_about`) survived unchanged — no new property assertions were derived.
- **Unexpected inferences:** None. No individuals merged, no unintended reclassification, no class collapsed into another.

## Operational View

| Application field | Ontology source |
|---|---|
| Pump | `:Pump_P17 rdf:type :Pump` — the individual's identity/label |
| Last inspection | `:Inspection_17 rdf:type :Inspection` — reached via `:Inspection_17 has_participant :Pump_P17` |
| Measured vibration | `:VibrationMeasurementDatum_1 has_decimal_value "4.2"^^xsd:decimal ; has_measurement_unit "mm/s"` — reached via `:Inspection_17 has_specified_output :VibrationMeasurementDatum_1` |
| Maintenance action | `:Report_R17 recommends :BearingReplacement` (the class, not an individual) |
| Work order | `:WorkOrder_W22 rdf:type :WorkOrder` — reached via `:WorkOrder_W22 requests :BearingReplacement` and/or `:WorkOrder_W22 based_on :Report_R17` |

**Lossy:** YES

**Divergent:** NO

**Explanation:**
The view is lossy — it drops real, asserted information (who performed the inspection, the governing maintenance procedure, the inspection report's identity as a distinct artifact, the quality/measurement-datum distinction, and the provenance chain tying it all to one inspection event) that exists in the ontology and isn't recoverable from the five displayed fields alone. It is not divergent: every displayed value is a faithful projection of an ontology assertion, and nothing is asserted, invented, or contradicted. The closest edge case is "Maintenance action: Replace bearing," which is built from a *class* (`BearingReplacement`), not an individual — the field is technically displaying a recommendation, not a fact-in-progress. As long as the UI doesn't imply (via phrasing, a status badge, a checkbox) that the replacement is scheduled or underway, the projection stays true to the model. Adding a "status: in progress" affordance would cross into divergence, since it would assert something the ontology deliberately never asserts.

## Most Important Lesson from the Week
The tooling is mechanical, the engineering is architectural. Train for the how to architect (specifically the design pattern) and it will give you the key, compatative edge and blueprint to build and represent anything with any tool.
