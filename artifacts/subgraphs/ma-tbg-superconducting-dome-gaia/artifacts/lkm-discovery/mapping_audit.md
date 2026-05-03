# Mapping audit log -- ma-tbg-superconducting-dome-gaia

## 9-step batch checklist

| step | status | audit note |
|---|---|---|
| 1. Bootstrap | done | Loaded only `input/evidence_gcn_006f88d8df3548fa.json`; root `gcn_006f88d8df3548fa` has one evidence chain and one factor `gfac_1433dc8665164d11`. |
| 2. Refine self-contained | done | Rewrote both distinct `gcn_*` claims to include MA-TBG, device/twist-angle context where available, density/temperature conditions, and provenance metadata with verbatim `lkm_original`. |
| 3. Decompose compound root | done | Preserved the selected root and added three grounded helper conclusions for dome adjacency, zero-resistance/base-temperature behavior, and the half-filling insulating temperature window. |
| 4. Hunt open problems | done | Checked the selected claim texts and factor steps for internally grounded contradictions; no pair was promoted to `contradiction()` because cautions are scope/interpretation limits rather than mutually exclusive claims. |
| 5. Mark suspicions | done | Logged the Mott-like interpretation caution and the hole-side measurement wording as dismissed false alarms in `dismissed/open_problem_false_alarms.md`; prior text carries `TODO:review`. |
| 6. Compile + infer | done | `gaia compile .`, `gaia check --brief .`, `gaia check --hole .`, and `gaia infer .` all passed from the subgraph package directory; IR hash `sha256:f49d9cc8c558d9774a0ba9853558f8304ec98346b1e24b3c1e53b60d07f66ffd`. |
| 7. Review obligations/holes | done | `gaia check --hole .` reported 0 holes / 1 independent claim; `gaia inquiry obligation list` reported no open obligations and `gaia inquiry hypothesis list` reported no hypotheses. |
| 8. Search supports | closed by scope | No new LKM retrieval was performed: this audited subgraph is constrained to the selected root evidence JSON and `data.papers`. |
| 9. Repeat / exit rationale | done | The single selected root chain is fully mapped, all required Gaia checks passed, and remaining issues are parent-synthesis cautions rather than subgraph blockers. |

## Claims

| LKM id / helper | Gaia label | source paper | mapping decision |
|---|---|---|---|
| `gcn_ffd6d31f7b2642e6` | `gcn_ffd6d31f_correlated_insulator_phenomenology` | `paper:813052701314121729` | Refined premise: half-filling insulating temperature dependence in MA-TBG is treated as correlated/Mott-like phenomenology, with the LKM caution that this is not microscopic proof. |
| `gcn_006f88d8df3548fa` | `gcn_006f88d8_ma_tbg_superconducting_domes` | `paper:813052701314121729` | Preserved selected root with explicit M1/M2 twist angles, half-filling density definition, superconducting dome adjacency, 70 mK resistance suppression, and 1-4 K insulating window. |
| helper | `helper_ma_tbg_domes_adjacent_to_correlated_insulator` | `paper:813052701314121729` | Decomposition helper for superconducting domes adjacent to the correlated insulator. |
| helper | `helper_ma_tbg_resistance_suppressed_at_70_mk` | `paper:813052701314121729` | Decomposition helper for resistance suppressed below the measurement floor at 70 mK. |
| helper | `helper_ma_tbg_half_filling_insulating_window` | `paper:813052701314121729` | Decomposition helper for insulating temperature dependence over roughly 1-4 K at nominal half filling. |

## Factors -> deductions

| factor_id | source_paper | premises | conclusion | dsl_kind | prior |
|---|---|---|---|---|---:|
| `gfac_1433dc8665164d11` | `paper:813052701314121729` | `gcn_ffd6d31f7b2642e6` | `gcn_006f88d8df3548fa` | `deduction` with five numbered LKM steps | 0.95 |

## Decomposition helpers

| helper | source evidence | DSL action |
|---|---|---|
| `helper_ma_tbg_domes_adjacent_to_correlated_insulator` | Root text plus factor steps 2-3 | `support([root], helper, prior=0.90)`; helper is downstream of the root to avoid double-counting the same chain as independent evidence. |
| `helper_ma_tbg_resistance_suppressed_at_70_mk` | Root text plus factor step 3 | `support([root], helper, prior=0.90)`. |
| `helper_ma_tbg_half_filling_insulating_window` | Root text plus factor step 4 | `support([root], helper, prior=0.90)`. |

## Open-problem and contradiction pass

| candidate | origin | decision | rationale |
|---|---|---|---|
| Correlated/Mott-like interpretation vs lack of microscopic proof | `gcn_ffd6d31f7b2642e6` | dismissed as review caution | The LKM premise explicitly qualifies the interpretation as plausible phenomenology rather than rigorous proof, so this is not a separately grounded incompatible claim. |
| Dome regions on both sides of correlated insulator vs hole-side density wording in factor step 3 | root/factor wording | dismissed as scope detail | The selected root states the broader phase-diagram claim; step 3 describes the shown measurements around `-n_s/2`, not an incompatible alternative. |
| Superconducting domes adjacent to correlated insulator vs cuprate analogy | factor step 5 | no contradiction | The analogy is interpretive support and does not assert a same-system competing value or mechanism. |

## Equivalences

| pair | decision | dsl_action |
|---|---|---|
| none | No same-proposition duplicate among the two distinct `gcn_*` claims in the selected evidence chain. | none |

## Leaves and priors

| leaf claim | prior | rationale |
|---|---:|---|
| `gcn_ffd6d31f_correlated_insulator_phenomenology` | 0.78 | Grounded in transport phenomenology and interaction-scale context, but capped below 0.90 because the LKM text itself says the Mott mechanism is not microscopically proven. |

## Inference summary

| label | posterior |
|---|---:|
| `gcn_ffd6d31f_correlated_insulator_phenomenology` | 0.78 |
| `gcn_006f88d8_ma_tbg_superconducting_domes` | 0.869759 |
| `helper_ma_tbg_domes_adjacent_to_correlated_insulator` | 0.8906087669 |
| `helper_ma_tbg_resistance_suppressed_at_70_mk` | 0.8906087669 |
| `helper_ma_tbg_half_filling_insulating_window` | 0.8906087669 |

## Gaia CLI verification

| command | status | note |
|---|---|---|
| `uv run --project /home/rsw/ThisIsDP/dev/test_lkm2gaia gaia compile .` | pass | Compiled 9 knowledge, 4 strategies, 0 operators; IR hash `sha256:f49d9cc8c558d9774a0ba9853558f8304ec98346b1e24b3c1e53b60d07f66ffd`. |
| `uv run --project /home/rsw/ThisIsDP/dev/test_lkm2gaia gaia check --brief .` | pass | 1 independent premise with prior, 4 derived conclusions, and 4 Gaia-generated orphan helper claims. |
| `uv run --project /home/rsw/ThisIsDP/dev/test_lkm2gaia gaia check --hole .` | pass | 0 holes / 1 independent claim. |
| `uv run --project /home/rsw/ThisIsDP/dev/test_lkm2gaia gaia infer .` | pass | Inferred 5 beliefs using exact JT; converged after 2 iterations. |
| `uv run --project /home/rsw/ThisIsDP/dev/test_lkm2gaia gaia inquiry obligation list` | pass | No open obligations. |
| `uv run --project /home/rsw/ThisIsDP/dev/test_lkm2gaia gaia inquiry hypothesis list` | pass | No hypotheses. |

## Exit rationale

The standalone package maps every distinct `gcn_*` claim and every `gfac_*` factor in the selected root evidence chain and preserves the raw root JSON. No unselected LKM root, external paper text, or web evidence was imported; parent-package synthesis can later decide whether to connect this branch to other MA-TBG mechanisms.
