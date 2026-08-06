# Current Zebra Ontology Snapshot

Active round: 3

Only the masked identifiers and active axioms below may be used.

## Structural axioms

- S01: Houses are exactly House1, House2, House3, House4, House5; they are pairwise distinct.
- S02: Category membership is exhaustive (`owl:oneOf`):
  - Resident: Resident_A, Resident_B, Resident_C, Resident_D, Resident_E; members are pairwise distinct.
  - Color: Color_A, Color_B, Color_C, Color_D, Color_E; members are pairwise distinct.
  - Beverage: Drink_A, Drink_B, Drink_C, Drink_D, Drink_E; members are pairwise distinct.
  - Pet: Pet_A, Pet_B, Pet_C, Pet_D, Zebra; members are pairwise distinct.
  - CigaretteBrand: Brand_A, Brand_B, Brand_C, Brand_D, Brand_E; members are pairwise distinct.
- S03: Every House has exactly one assignment through: hasResident -> Resident, hasColor -> Color, hasDrink -> Beverage, hasPet -> Pet, hasSmoke -> CigaretteBrand.
- S04: Every category member belongs to exactly one House through: Resident via livesIn, Color via colorOf, Beverage via drinkOf, Pet via petOf, CigaretteBrand via smokeOf.
- S05: Houses form the fixed left-to-right order House1 < House2 < House3 < House4 < House5.
- S06: The only nextTo pairs are: House1--House2, House2--House3, House3--House4, House4--House5.
- S07: The only immediatelyRightOf relations are: House2 immediately right of House1, House3 immediately right of House2, House4 immediately right of House3, House5 immediately right of House4.
- S08: Under OWL open-world semantics, an assignment not stated or entailed is unknown, not false.

## Active clue axioms

- Z01 (round 1): Resident_A lives in the Color_A house.
- Z02 (round 1): Resident_B owns Pet_A.
- Z04 (round 1): Resident_C drinks Drink_B.
- Z13 (round 1): Resident_E smokes Brand_E.
- Z08 (round 2): Drink_C is consumed in the middle house (House3).
- Z09 (round 2): Resident_D lives in the first house (House1).
- Z14 (round 2): Resident_D lives next to the Color_E house.
- Z03 (round 3): Drink_A is consumed in the Color_B house.
- Z05 (round 3): The Color_B house is immediately to the right of the Color_C house.
- Z07 (round 3): Brand_B is smoked in the Color_D house.

## Query

Which resident is the best current candidate for owning Zebra?
