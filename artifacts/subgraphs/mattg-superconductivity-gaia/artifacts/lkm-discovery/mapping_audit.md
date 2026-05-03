# Mapping audit log - mattg-superconductivity-gaia

## Claims

| lkm_id | label | source_paper | transformation |
|---|---|---|---|
| `gcn_c680c2399704407b` | `gcn_c680c239_mattg_continuum_approximations` | `paper:812508547391684608` | Rewritten as a self-contained premise about Park et al.'s MATTG continuum-model assumptions: omitted top-bottom coupling, fixed interlayer hoppings, empirical relaxation, and non-self-consistent displacement-field modeling; verbatim LKM text preserved in `lkm_original`. |
| `gcn_3618ccee24d94ab2` | `gcn_3618ccee_mattg_theta_over_sqrt2_mapping` | `paper:812508547391684608` | Rewritten as a self-contained premise about the theta/sqrt(2) mirror-sector reduction and larger MATTG magic-angle estimate; approximation limits preserved. |
| `gcn_713147608cae4a93` | `gcn_71314760_mattg_displacement_field_modeling` | `paper:812508547391684608` | Rewritten as a self-contained premise about modeling displacement field as `Delta V=dD/epsilon_0` and the screening caveat; verbatim LKM text preserved in `lkm_original`. |
| `gcn_b4e3bdff3c0c439a` | `gcn_b4e3bdff_mattg_mirror_flat_dirac_control` | `paper:812508547391684608` | Rewritten as a self-contained root conclusion about mirror-protected flat bands, opposite-character Dirac bands, theta/sqrt(2) magic-angle scaling, and finite-D hybridization under the stated approximations. |

## Factors -> deductions

| factor_id | source_paper | premises | conclusion | dsl_kind | prior |
|---|---|---|---|---|---|
| `gfac_170b7417d2e4485f` | `paper:812508547391684608` | `gcn_c680c239_mattg_continuum_approximations`, `gcn_3618ccee_mattg_theta_over_sqrt2_mapping`, `gcn_71314760_mattg_displacement_field_modeling` | `gcn_b4e3bdff_mattg_mirror_flat_dirac_control` | `deduction` | 0.95 |

## Decomposition

| helper_label | source | decision | dsl_action |
|---|---|---|---|
| `helper_mattg_zero_d_mirror_protected_flat_dirac` | `gcn_b4e3bdff3c0c439a` / factor step 2 | Root subclaim about zero-D mirror characters and symmetry-forbidden flat/Dirac hybridization. | `support(root, helper)` with prior 0.90. |
| `helper_mattg_magic_angle_larger_than_matbg` | `gcn_b4e3bdff3c0c439a` / factor step 3 | Root subclaim about theta/sqrt(2) reduction and MATTG magic angle near 1.6 degrees. | `support(root, helper)` with prior 0.90. |
| `helper_mattg_displacement_field_hybridizes_bands` | `gcn_b4e3bdff3c0c439a` / factor step 4 | Root subclaim about finite-D mirror breaking and flat/Dirac hybridization. | `support(root, helper)` with prior 0.90. |

## Equivalences

| pair | decision | dsl_action |
|---|---|---|
| (none in this run) | The selected payload has one source paper and no independent same-proposition claim. | None |

## Contradictions and open problems

| item | decision | dsl_action |
|---|---|---|
| Direct top-bottom coupling and high-order/non-local interlayer terms are omitted. | Scoped modeling assumption and quantitative uncertainty, not a same-payload contradiction. | No `contradiction(...)`; retained in premise with prior 0.76. |
| `theta/sqrt(2)` magic-angle reduction depends on ideal mirror symmetry and neglected terms. | Approximation caveat and review target, not a contradiction in the selected payload. | No `contradiction(...)`; retained in premise with prior 0.80. |
| Non-self-consistent displacement-field treatment omits screening. | Quantitative review target for field scale/hybridization strength, not a contradiction in the selected payload. | No `contradiction(...)`; retained in premise with prior 0.74. |

## Dismissed

| pair | origin | rationale |
|---|---|---|
| (none in this run) | | |
