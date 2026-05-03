# Mapping audit log -- alternating-twist-quadrilayer-gaia

## 9-step batch checklist

| step | status | audit note |
|---|---|---|
| 1. Bootstrap | done | Loaded only `input/evidence_gcn_225da7b340cb47b8.json`; root `gcn_225da7b340cb47b8` has one evidence chain and one factor `gfac_b160d54c5fb34e43`. |
| 2. Refine self-contained | done | Rewrote both distinct `gcn_*` claims to include ATQG/TBG mapping context, device twist angles, magic-angle comparison, transport observations, and provenance metadata with verbatim `lkm_original`. |
| 3. Decompose compound root | done | Preserved the selected root and added four grounded helper conclusions for the 1.96 deg device, 1.52 deg device, asymmetric angle dependence, and TBG-equivalent angle context. |
| 4. Hunt open problems | done | Checked the selected claim texts and factor steps for internally grounded tensions; no pair was promoted to `contradiction()` because identified issues are scope cautions or parent-bridge needs rather than mutually exclusive claims inside the selected evidence. |
| 5. Mark suspicions | done | Logged heuristic mapping, transport-signature wording, two-device scope, and TBG-comparison bridge cautions in `dismissed/open_problem_false_alarms.md`; prior text carries `TODO:review`. |
| 6. Compile + infer | done | `gaia compile .`, `gaia check --brief .`, `gaia check --hole .`, and `gaia infer .` all passed from the subgraph package directory; IR hash `sha256:90f2b597ed7504d6fa5d2909602a6be7bdabe5967b60782c90e5040533c3d100`. |
| 7. Review obligations/holes | done | `gaia check --hole .` reported 0 holes / 1 independent claim; `gaia inquiry obligation list` reported no open obligations and `gaia inquiry hypothesis list` reported no hypotheses. |
| 8. Search supports | closed by scope | No new LKM retrieval was performed: this audited subgraph is constrained to the selected root evidence JSON and `data.papers`. |
| 9. Repeat / exit rationale | done | The single selected root chain is fully mapped, all required Gaia checks passed, and remaining issues are parent-synthesis cautions rather than subgraph blockers. |

## Claims

| LKM id / helper | Gaia label | source paper | mapping decision |
|---|---|---|---|
| `gcn_51a6d18a02c4407d` | `gcn_51a6d18a_atqg_tbg_angle_mapping` | `paper:867774235207008693` | Refined premise: ATQG twist angles are heuristically mapped to TBG-like angles by dividing by the golden ratio, with explicit non-equivalence caution. |
| `gcn_225da7b340cb47b8` | `gcn_225da7b3_atqg_angle_phase_decoupling` | `paper:867774235207008693` | Preserved selected root with explicit 1.96 deg / 1.52 deg device comparison, 1.68 deg magic angle, no superconductivity down to 160 mK in the larger-angle device, and superconducting-like transport in the smaller-angle device. |
| helper | `helper_atqg_196_correlated_insulator_no_sc` | `paper:867774235207008693` | Decomposition helper for the larger-angle device's correlated-insulator-dominant behavior and absence of observed superconductivity. |
| helper | `helper_atqg_152_superconducting_like_transport` | `paper:867774235207008693` | Decomposition helper for the smaller-angle device's superconducting-like transport signatures and weaker correlated-insulator signatures. |
| helper | `helper_atqg_asymmetric_angle_dependence` | `paper:867774235207008693` | Decomposition helper for the asymmetric twist-angle dependence across the two devices. |
| helper | `helper_atqg_tbg_equivalent_angle_context` | `paper:867774235207008693` | Decomposition helper for the 1.21 deg / 0.94 deg TBG-like angle context and its heuristic scope. |

## Factors -> deductions

| factor_id | source_paper | premises | conclusion | dsl_kind | prior |
|---|---|---|---|---|---:|
| `gfac_b160d54c5fb34e43` | `paper:867774235207008693` | `gcn_51a6d18a02c4407d` | `gcn_225da7b340cb47b8` | `deduction` with five numbered LKM steps | 0.95 |

## Decomposition helpers

| helper | source evidence | DSL action |
|---|---|---|
| `helper_atqg_196_correlated_insulator_no_sc` | Root text plus factor step 1 | `support([root], helper, prior=0.90)`; helper is downstream of the root to avoid double-counting the same chain as independent evidence. |
| `helper_atqg_152_superconducting_like_transport` | Root text plus factor step 2 | `support([root], helper, prior=0.90)`. |
| `helper_atqg_asymmetric_angle_dependence` | Root text plus factor steps 3 and 5 | `support([root], helper, prior=0.90)`. |
| `helper_atqg_tbg_equivalent_angle_context` | Premise text plus factor step 4 | `support([mapping premise], helper, prior=0.90)`. |

## Open-problem and contradiction pass

| candidate | origin | decision | rationale |
|---|---|---|---|
| Heuristic ATQG-to-TBG mapping vs exact magic-angle equivalence | `gcn_51a6d18a02c4407d` and factor step 4 | dismissed as scope caution | The selected LKM evidence already denies quantitative equivalence, so no incompatible claim is asserted. |
| Superconducting-like transport signatures vs definitive superconductivity | root/factor wording | dismissed as wording caution | The selected evidence does not assert a competing thermodynamic criterion, only transport signatures and transition scales. |
| Two-device comparison vs possible device-to-device variation | root/factor wording | dismissed as synthesis risk | The selected root scopes the conclusion to the presented devices; parent synthesis should avoid overgeneralizing beyond those samples without more evidence. |
| ATQG departure from some TBG trends | root/factor wording | no formal contradiction | The selected JSON contains no specific TBG counterclaim to pair with the ATQG claim in a formal `contradiction()` operator. |

## Equivalences

| pair | decision | dsl_action |
|---|---|---|
| none | No same-proposition duplicate among the two distinct `gcn_*` claims in the selected evidence chain. | none |

## Leaves and priors

| leaf claim | prior | rationale |
|---|---:|---|
| `gcn_51a6d18a_atqg_tbg_angle_mapping` | 0.76 | Grounded in the selected Burg et al. theoretical-comparison context, but capped below 0.90 because the LKM text says the mapping is heuristic and not quantitatively exact. |

## Inference summary

| label | posterior |
|---|---:|
| `gcn_51a6d18a_atqg_tbg_angle_mapping` | 0.76 |
| `gcn_225da7b3_atqg_angle_phase_decoupling` | 0.860278 |
| `helper_atqg_152_superconducting_like_transport` | 0.8863508498 |
| `helper_atqg_196_correlated_insulator_no_sc` | 0.8863508498 |
| `helper_atqg_asymmetric_angle_dependence` | 0.8863508498 |
| `helper_atqg_tbg_equivalent_angle_context` | 0.841316 |

## Gaia CLI verification

| command | status | note |
|---|---|---|
| `uv run --project /home/rsw/ThisIsDP/dev/test_lkm2gaia gaia compile .` | pass | Compiled 11 knowledge, 5 strategies, 0 operators; IR hash `sha256:90f2b597ed7504d6fa5d2909602a6be7bdabe5967b60782c90e5040533c3d100`. |
| `uv run --project /home/rsw/ThisIsDP/dev/test_lkm2gaia gaia check --brief .` | pass | 1 independent premise with prior, 5 derived conclusions, and 5 Gaia-generated orphan helper claims. |
| `uv run --project /home/rsw/ThisIsDP/dev/test_lkm2gaia gaia check --hole .` | pass | 0 holes / 1 independent claim. |
| `uv run --project /home/rsw/ThisIsDP/dev/test_lkm2gaia gaia infer .` | pass | Inferred 6 beliefs using exact JT; converged after 2 iterations. |
| `uv run --project /home/rsw/ThisIsDP/dev/test_lkm2gaia gaia inquiry obligation list` | pass | No open obligations. |
| `uv run --project /home/rsw/ThisIsDP/dev/test_lkm2gaia gaia inquiry hypothesis list` | pass | No hypotheses. |

## Exit rationale

The standalone package maps every distinct `gcn_*` claim and every `gfac_*` factor in the selected root evidence chain and preserves the raw root JSON. No unselected LKM root, external paper text, or web evidence was imported; parent-package synthesis can later decide whether to connect this ATQG branch to other TBG or multilayer-graphene mechanisms.
