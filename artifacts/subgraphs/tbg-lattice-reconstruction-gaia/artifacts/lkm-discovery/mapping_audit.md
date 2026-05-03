# Mapping audit log -- tbg-lattice-reconstruction-gaia

## 9-step batch checklist

| step | status | audit note |
|---|---|---|
| 1. Bootstrap | done | Loaded only `input/turn2_evidence_gcn_c220df1acc8b476a.json`; root `gcn_c220df1acc8b476a` has one evidence chain and one factor `gfac_e5303e2e42664d99`. |
| 2. Refine self-contained | done | Rewrote all three distinct `gcn_*` claims to include system, continuum-model scope, reconstruction geometry, observed/computed spectral trends, heterostrain limitation, and `[@Liu2020]` citation context while preserving verbatim `lkm_original`. |
| 3. Decompose compound root | done | No separate decomposition helper was emitted: the two evidence-grounded aspects are already represented by the two LKM premises, and the selected root remains the chain conclusion supported by `gfac_e5303e2e42664d99`. |
| 4. Hunt open problems | done | Checked the selected claims and factor steps for internally grounded tensions; heterostrain-driven fine splitting was logged as an open modeling limitation, not a `contradiction()`, because the selected evidence contains no incompatible same-scope counterclaim. |
| 5. Mark suspicions | done | Logged model-scope cautions in `dismissed/open_problem_scope_cautions.md`; leaf priors carry `TODO:review`, with lower prior on the heterostrain premise because refs `[54-55]` are not present in `data.papers`. |
| 6. Compile + infer | done | `gaia compile .`, `gaia check --brief .`, `gaia check --hole .`, and `gaia infer .` all passed from the subgraph package directory; IR hash `sha256:a2fa23d90abbe44f603db8bcbf8fb70d115a05edda73107ad888c0c4286a86da`. |
| 7. Review obligations/holes | done | `gaia check --hole .` reported 0 holes / 2 independent claims; `gaia inquiry obligation list` reported no open obligations and `gaia inquiry hypothesis list` reported no hypotheses. |
| 8. Search supports | closed by scope | No new LKM retrieval was performed: this audited subgraph is constrained to the selected root evidence JSON and `data.papers`. |
| 9. Repeat / exit rationale | done | The single selected root chain is fully mapped, all required Gaia checks passed, and remaining issues are synthesis cautions rather than standalone subgraph blockers. |

## Claims

| LKM id | Gaia label | source paper | mapping decision |
|---|---|---|---|
| `gcn_8cd2984a6296435c` | `gcn_8cd2984a6296435c` | `paper:867745366357836075` | Refined premise: Liu et al.'s relaxation-aware continuum calculation uses registry-dependent tunneling/displacement fields and reports broader, more isolated flat bands in reconstructed TBG relative to rigid TBG. |
| `gcn_ed8fa9253ea24982` | `gcn_ed8fa9253ea24982` | `paper:867745366357836075` | Refined premise: spatially non-uniform heterostrain can produce additional DOS fine structure such as three-subpeak splitting, which registry-only relaxation calculations omit. |
| `gcn_c220df1acc8b476a` | `gcn_c220df1acc8b476a` | `paper:867745366357836075` | Preserved selected root as the scoped conclusion: lattice-relaxed continuum modeling reproduces broadening and isolation trends but not heterostrain-induced fine splitting. |

## Factors -> deductions

| factor_id | source_paper | premises | conclusion | dsl_kind | prior |
|---|---|---|---|---|---:|
| `gfac_e5303e2e42664d99` | `paper:867745366357836075` | `gcn_8cd2984a6296435c`, `gcn_ed8fa9253ea24982` | `gcn_c220df1acc8b476a` | `deduction` with five numbered LKM steps | 0.95 |

## Open-problem and contradiction pass

| candidate | origin | decision | rationale |
|---|---|---|---|
| Relaxation-reconstructed geometry reproduces broadening/isolation vs omitted heterostrain fails to reproduce three-subpeak fine splitting | root and both premises | not a formal contradiction | The selected evidence scopes these as complementary explanatory layers: relaxation explains key broadening/isolation trends, while heterostrain may explain additional fine peak splitting. |
| Heterostrain refs `[54-55]` absent from `data.papers` | `gcn_ed8fa9253ea24982` | open provenance caution | The claim is preserved because it is in the selected LKM chain, but its leaf prior is lower and TODO-marked. |
| Reconstructed continuum model vs unreconstructed rigid geometry | factor steps 1-4 | model comparison, not contradiction | The rigid geometry is a comparison baseline; the selected evidence does not claim that both geometries simultaneously describe the same reconstructed sample. |

## Equivalences

| pair | decision | dsl_action |
|---|---|---|
| none | No same-proposition duplicate among the three distinct `gcn_*` claims in the selected evidence chain. | none |

## Leaves and priors

| leaf claim | prior | rationale |
|---|---:|---|
| `gcn_8cd2984a6296435c` | 0.80 | Model-scoped continuum result for relaxation trends; capped below 0.90 pending reviewer audit. |
| `gcn_ed8fa9253ea24982` | 0.72 | Heterostrain limitation and prior-literature attribution preserved from LKM but indirect within the selected `data.papers`; capped below 0.90 pending reviewer audit. |

## Inference summary

| label | posterior |
|---|---:|
| `gcn_8cd2984a6296435c` | 0.8000000000 |
| `gcn_ed8fa9253ea24982` | 0.7200000000 |
| `gcn_c220df1acc8b476a` | 0.7729807444 |

## Gaia CLI verification

| command | status | note |
|---|---|---|
| `uv run --project /home/rsw/ThisIsDP/dev/test_lkm2gaia gaia compile .` | pass | Compiled 5 knowledge, 1 strategy, 0 operators; IR hash `sha256:a2fa23d90abbe44f603db8bcbf8fb70d115a05edda73107ad888c0c4286a86da`. |
| `uv run --project /home/rsw/ThisIsDP/dev/test_lkm2gaia gaia check --brief .` | pass | 2 independent premises with priors, 1 derived conclusion, and 2 Gaia-generated orphan helper claims. |
| `uv run --project /home/rsw/ThisIsDP/dev/test_lkm2gaia gaia check --hole .` | pass | 0 holes / 2 independent claims. |
| `uv run --project /home/rsw/ThisIsDP/dev/test_lkm2gaia gaia infer .` | pass | Inferred 4 beliefs using exact JT; converged after 2 iterations. |
| `uv run --project /home/rsw/ThisIsDP/dev/test_lkm2gaia gaia inquiry obligation list` | pass | No open obligations. |
| `uv run --project /home/rsw/ThisIsDP/dev/test_lkm2gaia gaia inquiry hypothesis list` | pass | No hypotheses. |

## Exit rationale

The standalone package maps every distinct `gcn_*` claim and every `gfac_*` factor in the selected root evidence chain and preserves the raw root JSON. No unselected LKM root, external paper text, or web evidence was imported; parent-package synthesis can later decide whether to connect this lattice-reconstruction branch to other TBG flat-band, relaxation, or spectroscopy mechanisms.
