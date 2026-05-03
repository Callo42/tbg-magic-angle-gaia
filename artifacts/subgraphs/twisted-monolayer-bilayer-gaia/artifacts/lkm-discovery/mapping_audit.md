# Mapping audit log -- twisted-monolayer-bilayer-gaia

## 9-step batch checklist

| step | status | audit note |
|---|---|---|
| 1. Bootstrap | done | Loaded only `input/evidence_gcn_14a55aff3de24a3a.json`; root `gcn_14a55aff3de24a3a` has one evidence chain and one factor `gfac_f1d4418da247467d`. |
| 2. Refine self-contained | done | Rewrote the two distinct `gcn_*` claims to include SM-(AB)_2 geometry, relaxed tight-binding context, magic-angle scale, layer-resolved DOS, and TBLG comparison scope; preserved verbatim `lkm_original`. |
| 3. Decompose compound root | done | Preserved the selected root and added three grounded helper conclusions for isolated low-energy flat bands, reduced flatness versus relaxed TBLG, and layer-separated electronic character. |
| 4. Hunt open problems | done | Checked selected claim texts and factor steps for internally grounded tensions; no pair was promoted to `contradiction()` because apparent tensions are scoped comparisons or layer-resolved coexistence. |
| 5. Mark suspicions | done | Logged reduced-flatness scope, layer-localized/delocalized coexistence, and [73]/[74] bridge limitations in `dismissed/open_problem_false_alarms.md`; prior text carries `TODO:review`. |
| 6. Compile + infer | done | `gaia compile .`, `gaia check --brief .`, `gaia check --hole .`, and `gaia infer .` all passed; IR hash `sha256:3d3a930f18b9f35cfc357b18af7a8b1b9bf183a45086b2d4486115c4f86b0844`. |
| 7. Review obligations/holes | done | `gaia check --hole .` reported 0 holes / 1 independent claim; `gaia inquiry obligation list` reported no open obligations and `gaia inquiry hypothesis list` reported no hypotheses. |
| 8. Search supports | closed by scope | No new LKM retrieval was performed: this audited subgraph is constrained to the selected root evidence JSON and `data.papers`. |
| 9. Repeat / exit rationale | done | The single selected root chain is fully mapped, required Gaia checks passed, and remaining issues are parent-synthesis bridge cautions rather than subgraph blockers. |

## Claims

| LKM id / helper | Gaia label | source paper | mapping decision |
|---|---|---|---|
| `gcn_42c7afbd21b5483d` | `gcn_42c7afbd_smab2_layer_resolved_dos` | `paper:867761060289970778` | Refined premise: SM-(AB)_2 layer-decomposed DOS at the magic-angle moire geometry shows top-layer near-zero-energy localization and broadened bottom-bilayer spectral weight. |
| `gcn_14a55aff3de24a3a` | `gcn_14a55aff_smab2_flat_band_localization` | `paper:867761060289970778` | Preserved selected root with explicit isolated flat bands, reduced flatness versus relaxed magic-angle TBLG, and layer-resolved localization/delocalization. |
| helper | `helper_smab2_isolated_low_energy_flat_bands` | `paper:867761060289970778` | Decomposition helper for the isolated low-energy flat bands and zero-energy DOS peak. |
| helper | `helper_smab2_less_flat_than_relaxed_tbg` | `paper:867761060289970778` | Decomposition helper for the larger bandwidth and smaller zero-energy DOS peak relative to relaxed magic-angle TBLG. |
| helper | `helper_smab2_layer_separated_character` | `paper:867761060289970778` | Decomposition helper for top-layer localization and bottom-bilayer broadening/delocalization. |

## Factors -> deductions

| factor_id | source_paper | premises | conclusion | dsl_kind | prior |
|---|---|---|---|---|---:|
| `gfac_f1d4418da247467d` | `paper:867761060289970778` | `gcn_42c7afbd21b5483d` | `gcn_14a55aff3de24a3a` | `deduction` with seven numbered LKM steps | 0.95 |

## Decomposition helpers

| helper | source evidence | DSL action |
|---|---|---|
| `helper_smab2_isolated_low_energy_flat_bands` | Root text plus factor step 3 | `support([root], helper, prior=0.90)`; helper is downstream of the root to avoid double-counting the same chain as independent evidence. |
| `helper_smab2_less_flat_than_relaxed_tbg` | Root text plus factor steps 4-5 | `support([root], helper, prior=0.90)`. |
| `helper_smab2_layer_separated_character` | Premise text plus factor step 6 | `support([premise], helper, prior=0.90)`. |

## Open-problem and contradiction pass

| candidate | origin | decision | rationale |
|---|---|---|---|
| Isolated flat bands versus less-flat-than-TBLG comparison | Root and factor steps 3-5 | dismissed as scope caution | Existence of isolated bands and weaker quantitative flatness relative to TBLG can both be true. |
| Localized versus delocalized flat-band spectral weight | Premise and factor step 6 | dismissed as resolved by layer scope | The selected evidence assigns localization to the top monolayer and broadening/delocalization to the bottom bilayer. |
| Consistency with cited observations [73]/[74] | Factor step 7 | bridge deferred | The selected JSON does not include the separate LKM claims needed for formal `support()` or `equivalence()` to those works. |

## Equivalences

| pair | decision | dsl_action |
|---|---|---|
| none | No same-proposition duplicate among the two distinct `gcn_*` claims in the selected evidence chain. | none |

## Leaves and priors

| leaf claim | prior | rationale |
|---|---:|---|
| `gcn_42c7afbd_smab2_layer_resolved_dos` | 0.82 | Grounded in the selected Nguyen et al. relaxed tight-binding and layer-resolved DOS evidence, but capped below 0.90 because it is model/protocol scoped. |

## Inference summary

| label | posterior |
|---|---:|
| `gcn_42c7afbd_smab2_layer_resolved_dos` | 0.82 |
| `gcn_14a55aff_smab2_flat_band_localization` | 0.888721 |
| `helper_smab2_isolated_low_energy_flat_bands` | 0.8991246011 |
| `helper_smab2_less_flat_than_relaxed_tbg` | 0.8991246011 |
| `helper_smab2_layer_separated_character` | 0.8682620000 |

## Gaia CLI verification

| command | status | note |
|---|---|---|
| `uv run --project /home/rsw/ThisIsDP/dev/test_lkm2gaia gaia compile .` | pass | Compiled 9 knowledge, 4 strategies, 0 operators; IR hash `sha256:3d3a930f18b9f35cfc357b18af7a8b1b9bf183a45086b2d4486115c4f86b0844`. |
| `uv run --project /home/rsw/ThisIsDP/dev/test_lkm2gaia gaia check --brief .` | pass | 1 independent premise with prior, 4 derived conclusions, and 4 Gaia-generated orphan helper claims. |
| `uv run --project /home/rsw/ThisIsDP/dev/test_lkm2gaia gaia check --hole .` | pass | 0 holes / 1 independent claim. |
| `uv run --project /home/rsw/ThisIsDP/dev/test_lkm2gaia gaia infer .` | pass | Inferred 5 beliefs using exact JT; converged after 2 iterations. |
| `uv run --project /home/rsw/ThisIsDP/dev/test_lkm2gaia gaia inquiry obligation list` | pass | No open obligations. |
| `uv run --project /home/rsw/ThisIsDP/dev/test_lkm2gaia gaia inquiry hypothesis list` | pass | No hypotheses. |
| `uv run --project /home/rsw/ThisIsDP/dev/test_lkm2gaia python -m py_compile ...` | pass | Python source parsed successfully. |

## Exit rationale

The standalone package maps every distinct `gcn_*` claim and every `gfac_*` factor in the selected root evidence chain and preserves the raw root JSON. No unselected LKM root, external paper text, web evidence, or parent-package bridge was imported; parent synthesis can later decide whether to connect this branch to other TBG or multilayer-graphene subgraphs using separate chain-backed evidence.
