# Mapping audit log -- pressure-flat-band-tbg-gaia

Source evidence: `input/evidence_gcn_105d2fc961f949b6.json`

## Claims

| lkm_id | label | source_paper | decision |
|---|---|---|---|
| `gcn_105d2fc961f949b6` | `gcn_105d2fc961f949b6` | `paper:812469412236886018` | Root claim refined to make the angle range, pressure role, flat-band/VHS result, and many-body-status caveat self-contained. |
| `gcn_e83deb9969844b33` | `gcn_e83deb9969844b33` | `paper:812469412236886018` | Premise retained as the pressure-across-large-angles generalization; self-contained with the 9.4 degree, 2.44 Angstrom anchor and 9-27.8 degree scope. |
| `gcn_ba97172fd9264409` | `gcn_ba97172fd9264409` | `paper:812469412236886018` | Premise retained but softened in DSL wording to the chain's audited status: DOS/VHS are suggestive indicators, not direct proof of superconductivity or correlated insulation. |

All mapped claims preserve `lkm_id`, `source_paper`, `provenance_source`, and verbatim `lkm_original` metadata in `src/pressure_flat_band_tbg/paper_ge2021.py`.

## Factors -> Deductions

| factor_id | source_paper | premises | conclusion | dsl_kind | prior |
|---|---|---|---|---|---|
| `gfac_b4366b0e9b4a4f0f` | `paper:812469412236886018` | `gcn_e83deb9969844b33`, `gcn_ba97172fd9264409` | `gcn_105d2fc961f949b6` | `deduction` | `0.95` |

## Decomposition Decisions

| claim | decision | rationale |
|---|---|---|
| `gcn_105d2fc961f949b6` | No separate atomic decomposition emitted. | The selected LKM chain supplies two explicit premises for the broad pressure-engineering conclusion. It does not supply independent atomic evidence for observed many-body phases, and the DSL claim was refined to avoid turning a suggestive sentence into a demonstrated superconductivity/correlated-insulator assertion. |

## Open-Problem Audit

| item | status | rationale |
|---|---|---|
| Broad angle generality of pressure-induced flat bands | Logged as weak premise via prior on `gcn_e83deb9969844b33`. | The chain generalizes from a highlighted 9.4 degree compressed structure to the 9-27.8 degree commensurate range; this is plausible but needs review or additional evidence. |
| Many-body phase inference from DOS/VHS | Logged as weak premise via prior on `gcn_ba97172fd9264409`. | The chain itself says the paper does not perform many-body calculations or experimental verification of superconductivity/correlated insulation. |
| Contradiction candidates | None emitted. | Parent discovery flags reported no pairs. Within the selected evidence, the many-body issue is a scope/strength caveat rather than a direct contradictory claim. |

## Equivalences

| pair | a | b | decision | dsl_action |
|---|---|---|---|---|
| (none in this run) | | | | |

## Contradictions

| pair | a | b | decision | dsl_action |
|---|---|---|---|---|
| (none in this run) | | | | |

## Dismissed

| pair | origin | rationale |
|---|---|---|
| (none in this run) | | |
