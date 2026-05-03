# Mapping audit log -- substrate-chern-flat-band-gaia

## 9-step batch checklist

| step | status | audit note |
|---|---|---|
| 1. Bootstrap | done | Loaded only `input/turn2_evidence_gcn_9f7dbaf8f0014316.json`; root `gcn_9f7dbaf8f0014316` has one evidence chain and one factor `gfac_c68ea7fe461d4cd9`. |
| 2. Refine self-contained | done | Rewrote both distinct `gcn_*` claims with explicit TBG-on-TMD system, two-valley BM continuum model, first-magic-angle regime, active-band isolation, and proximity energy scales; preserved `lkm_original`. |
| 3. Decompose compound root | done | Preserved the selected root and added four grounded helper conclusions for Rashba flat pairs, sixteen Dirac points, Chern phase-diagram scope, and away-from-magic-angle failure. |
| 4. Hunt open problems | done | Checked selected claim texts, factor steps, and motivating question for internally grounded tensions; no pair was promoted to `contradiction()` because the apparent tensions are regime boundaries or model-domain cautions. |
| 5. Mark suspicions | done | Logged remote-band / large-bandwidth / outside-magic-angle limitations in `dismissed/open_problem_false_alarms.md`; leaf prior carries `TODO:review`. |
| 6. Compile + infer | done | `gaia compile .`, `gaia check --brief .`, `gaia check --hole .`, and `gaia infer .` all passed; IR hash `sha256:9fa24c8cc6ea22539f46d5c8192ece15123cdfdd0017380d6486eb1b81381800`. |
| 7. Review obligations/holes | done | `gaia check --hole .` reported 0 holes / 1 independent claim; `gaia inquiry obligation list` reported no open obligations and `gaia inquiry hypothesis list` reported no hypotheses. |
| 8. Search supports | closed by scope | No new LKM retrieval was performed: this audited subgraph is constrained to the selected root evidence JSON and `data.papers`. |
| 9. Repeat / exit rationale | done | The single selected root chain is fully mapped, required Gaia checks passed, and remaining issues are parent-synthesis bridge cautions rather than subgraph blockers. |

## Claims

| LKM id / helper | Gaia label | source paper | mapping decision |
|---|---|---|---|
| `gcn_fb78cfd75da34fb5` | `gcn_fb78cfd7_magic_angle_continuum_regime` | `paper:812527076643962881` | Refined premise: two-valley BM continuum model captures TBG-on-TMD flat-band physics only at sufficiently small twist angles near the first magic angle with isolated, narrow active bands and negligible intervalley scattering. |
| `gcn_9f7dbaf8f0014316` | `gcn_9f7dbaf8_substrate_flat_band_topology_regime` | `paper:812527076643962881` | Preserved selected root with explicit Rashba flat pairs, sixteen Dirac points, Chern phase diagrams, and failure away from the near-magic-angle narrow-band regime. |
| helper | `helper_rashba_isolated_flat_pairs` | `paper:812527076643962881` | Decomposition helper for Rashba-induced isolated extremely flat band pairs near K^{+/-}. |
| helper | `helper_single_valley_sixteen_dirac_structure` | `paper:812527076643962881` | Decomposition helper for the single-valley sixteen-Dirac-point structure. |
| helper | `helper_chern_phase_diagram_scope` | `paper:812527076643962881` | Decomposition helper for the Chern-number phase-diagram scope. |
| helper | `helper_away_from_magic_angle_no_reconstruction` | `paper:812527076643962881` | Decomposition helper for the outside-regime failure mode. |

## Factors -> deductions

| factor_id | source_paper | premises | conclusion | dsl_kind | prior |
|---|---|---|---|---|---:|
| `gfac_c68ea7fe461d4cd9` | `paper:812527076643962881` | `gcn_fb78cfd75da34fb5` | `gcn_9f7dbaf8f0014316` | `deduction` with four numbered LKM steps | 0.95 |

## Decomposition helpers

| helper | source evidence | DSL action |
|---|---|---|
| `helper_rashba_isolated_flat_pairs` | Root text plus factor steps 2-4 | `support([root], helper, prior=0.90)`; helper is downstream of the root to avoid double-counting the same chain as independent evidence. |
| `helper_single_valley_sixteen_dirac_structure` | Root text plus factor steps 3-4 | `support([root], helper, prior=0.90)`. |
| `helper_chern_phase_diagram_scope` | Premise plus root text plus factor steps 2-4 | `support([premise, root], helper, prior=0.90)`. |
| `helper_away_from_magic_angle_no_reconstruction` | Root text plus factor step 3 | `support([root], helper, prior=0.90)`. |

## Open-problem and contradiction pass

| candidate | origin | decision | rationale |
|---|---|---|---|
| Near-magic-angle reconstructed topology versus away-from-magic-angle failure | Root and factor step 3 | dismissed as scope boundary | Different twist-angle/bandwidth regimes can both be true. |
| Active-band projection versus remote-band hybridization | Premise and motivating question | dismissed as model-domain caution | The selected evidence states the active-band projection is invalid outside the isolated/narrow-band regime, but does not provide a same-regime counter-claim. |
| Proximity coupling effects versus large kinetic bandwidth | Root and factor step 3 | dismissed as conditional failure mode | The evidence says proximate terms reconstruct bands only when comparable to active bandwidth; large bandwidth is explicitly an outside-regime condition. |

## Equivalences

| pair | decision | dsl_action |
|---|---|---|
| none | No same-proposition duplicate among the two distinct `gcn_*` claims in the selected evidence chain. | none |

## Leaves and priors

| leaf claim | prior | rationale |
|---|---:|---|
| `gcn_fb78cfd7_magic_angle_continuum_regime` | 0.82 | Grounded in selected Wang et al. continuum-model applicability evidence, but capped below 0.90 because it is model- and parameter-regime scoped. |

## Inference summary

| label | posterior |
|---|---:|
| `gcn_fb78cfd7_magic_angle_continuum_regime` | 0.82 |
| `gcn_9f7dbaf8_substrate_flat_band_topology_regime` | 0.888721 |
| `helper_rashba_isolated_flat_pairs` | 0.8991246011 |
| `helper_single_valley_sixteen_dirac_structure` | 0.8991246011 |
| `helper_chern_phase_diagram_scope` | 0.8584372898978 |
| `helper_away_from_magic_angle_no_reconstruction` | 0.8991246011 |

## Gaia CLI verification

| command | status | note |
|---|---|---|
| `uv run --project /home/rsw/ThisIsDP/dev/test_lkm2gaia gaia compile .` | pass | Compiled 12 knowledge, 5 strategies, 0 operators; IR hash `sha256:9fa24c8cc6ea22539f46d5c8192ece15123cdfdd0017380d6486eb1b81381800`. |
| `uv run --project /home/rsw/ThisIsDP/dev/test_lkm2gaia gaia check --brief .` | pass | 1 independent premise with prior, 5 derived conclusions, and 6 Gaia-generated orphan helper claims. |
| `uv run --project /home/rsw/ThisIsDP/dev/test_lkm2gaia gaia check --hole .` | pass | 0 holes / 1 independent claim. |
| `uv run --project /home/rsw/ThisIsDP/dev/test_lkm2gaia gaia infer .` | pass | Inferred 7 beliefs using exact JT; converged after 2 iterations. |
| `uv run --project /home/rsw/ThisIsDP/dev/test_lkm2gaia gaia inquiry obligation list` | pass | No open obligations. |
| `uv run --project /home/rsw/ThisIsDP/dev/test_lkm2gaia gaia inquiry hypothesis list` | pass | No hypotheses. |
| `uv run --project /home/rsw/ThisIsDP/dev/test_lkm2gaia python -m py_compile ...` | pass | Python source parsed successfully. |

## Exit rationale

The standalone package maps every distinct `gcn_*` claim and the `gfac_c68ea7fe461d4cd9` factor in the selected root evidence chain and preserves the raw root JSON. No unselected LKM root, external paper text, web evidence, or parent-package bridge was imported; parent synthesis can later decide whether to connect this branch to other TBG flat-band roots using separate chain-backed evidence.
