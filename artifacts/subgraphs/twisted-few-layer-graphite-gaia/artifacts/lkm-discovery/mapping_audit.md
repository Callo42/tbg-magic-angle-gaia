# Mapping audit log -- twisted-few-layer-graphite-gaia

## 9-step batch checklist

| step | status | audit note |
|---|---|---|
| 1. Bootstrap | done | Loaded only `input/evidence_gcn_f23eff9c755840f2.json`; root `gcn_f23eff9c755840f2` has one evidence chain and one factor `gfac_6988d3b9bea84c0f`. |
| 2. Refine self-contained | done | Rewrote all three distinct `gcn_*` claims to include system, continuum-model scope, values, parameters, omitted effects, and `[@Ma2020]` citation context while preserving verbatim `lkm_original`. |
| 3. Decompose compound root | done | No separate decomposition helper was emitted: the root can be made self-contained as one scoped proposition about the principal two-band pair and the same-formalism TBG numerical correspondence. |
| 4. Hunt open problems | done | Checked the selected claims and factor steps for internally grounded tensions; modeling limitations were logged as scope cautions, and no pair was promoted to `contradiction()` because the selected evidence contains no incompatible counterclaim. |
| 5. Mark suspicions | done | Logged rigid-structure assumptions, remote-hopping sensitivity, primary-two-band scope, and TBG-comparison scope in `dismissed/open_problem_scope_cautions.md`; leaf priors carry `TODO:review`. |
| 6. Compile + infer | done | `gaia compile .`, `gaia check --brief .`, `gaia check --hole .`, and `gaia infer .` all passed from the subgraph package directory; IR hash `sha256:0552767ceb59065282b105d7316f0b3f4b329ba55fa7247ee013e76e1683f3b3`. |
| 7. Review obligations/holes | done | `gaia check --hole .` reported 0 holes / 2 independent claims; `gaia inquiry obligation list` reported no open obligations and `gaia inquiry hypothesis list` reported no hypotheses. |
| 8. Search supports | closed by scope | No new LKM retrieval was performed: this audited subgraph is constrained to the selected root evidence JSON and `data.papers`. |
| 9. Repeat / exit rationale | done | The single selected root chain is fully mapped, all required Gaia checks passed, and remaining issues are synthesis cautions rather than standalone subgraph blockers. |

## Claims

| LKM id | Gaia label | source paper | mapping decision |
|---|---|---|---|
| `gcn_2fcfd55afc454c94` | `gcn_2fcfd55afc454c94` | `paper:867748811072602427` | Refined premise: Ma et al.'s continuum calculation treats the tFL graphite slabs as rigid and uniformly twisted, excluding relaxation, corrugation, and spatial twist inhomogeneity. |
| `gcn_2ceab67f16f34d1e` | `gcn_2ceab67f16f34d1e` | `paper:867748811072602427` | Refined premise: the 1.05 degree estimate comes from the N=3 minimal-model scan with listed continuum parameters, while full-parameter calculations with remote hoppings make the bands more dispersive and parameter-sensitive. |
| `gcn_f23eff9c755840f2` | `gcn_f23eff9c755840f2` | `paper:867748811072602427` | Preserved selected root as a scoped conclusion: within Ma et al.'s continuum description, the primary two moire bands in tFL graphite become nearly flat near 1.05 degrees, matching the principal TBG magic-angle value in the same formalism. |

## Factors -> deductions

| factor_id | source_paper | premises | conclusion | dsl_kind | prior |
|---|---|---|---|---|---:|
| `gfac_6988d3b9bea84c0f` | `paper:867748811072602427` | `gcn_2fcfd55afc454c94`, `gcn_2ceab67f16f34d1e` | `gcn_f23eff9c755840f2` | `deduction` with three numbered LKM steps | 0.95 |

## Open-problem and contradiction pass

| candidate | origin | decision | rationale |
|---|---|---|---|
| Rigid uniformly twisted slabs vs relaxation, corrugation, or twist inhomogeneity | `gcn_2fcfd55afc454c94` | dismissed as modeling-scope caution | The selected evidence states these effects are omitted; it does not provide a counterclaim quantifying how including them changes the 1.05 degree estimate. |
| Minimal-model magic angle vs full-parameter dispersive bands | `gcn_2ceab67f16f34d1e` | dismissed as internal scope qualifier | The same LKM premise explicitly says full-parameter calculations make the flat bands dispersive and parameter-dependent. This qualifies the root claim rather than contradicting it. |
| Principal two moire bands flatten vs remaining moire bands stay dispersive | factor step 3 | dismissed as scope qualifier | The evidence limits flatness to the primary two-band pair. It does not assert that all moire bands become flat at 1.05 degrees. |
| Same numerical value as TBG principal magic angle vs tFL graphite having richer multilayer spectra | root claim and factor step 3 | no formal contradiction | Equality is asserted only for the principal numerical angle within the same continuum formalism. |

## Equivalences

| pair | decision | dsl_action |
|---|---|---|
| none | No same-proposition duplicate among the three distinct `gcn_*` claims in the selected evidence chain. | none |

## Leaves and priors

| leaf claim | prior | rationale |
|---|---:|---|
| `gcn_2fcfd55afc454c94` | 0.82 | Modeling-assumption premise from the selected LKM chain; capped below 0.90 pending reviewer audit. |
| `gcn_2ceab67f16f34d1e` | 0.80 | Minimal-model parameter and sensitivity premise from the selected LKM chain; capped below 0.90 because it explicitly contains parameter-dependence caveats. |

## Inference summary

| label | posterior |
|---|---:|
| `gcn_2fcfd55afc454c94` | 0.82 |
| `gcn_2ceab67f16f34d1e` | 0.80 |
| `gcn_f23eff9c755840f2` | 0.8108288964 |

## Gaia CLI verification

| command | status | note |
|---|---|---|
| `uv run --project /home/rsw/ThisIsDP/dev/test_lkm2gaia gaia compile .` | pass | Compiled 5 knowledge, 1 strategy, 0 operators; IR hash `sha256:0552767ceb59065282b105d7316f0b3f4b329ba55fa7247ee013e76e1683f3b3`. |
| `uv run --project /home/rsw/ThisIsDP/dev/test_lkm2gaia gaia check --brief .` | pass | 2 independent premises with priors, 1 derived conclusion, and 2 Gaia-generated orphan helper claims. |
| `uv run --project /home/rsw/ThisIsDP/dev/test_lkm2gaia gaia check --hole .` | pass | 0 holes / 2 independent claims. |
| `uv run --project /home/rsw/ThisIsDP/dev/test_lkm2gaia gaia infer .` | pass | Inferred 4 beliefs using exact JT; converged after 2 iterations. |
| `uv run --project /home/rsw/ThisIsDP/dev/test_lkm2gaia gaia inquiry obligation list` | pass | No open obligations. |
| `uv run --project /home/rsw/ThisIsDP/dev/test_lkm2gaia gaia inquiry hypothesis list` | pass | No hypotheses. |

## Exit rationale

The standalone package maps every distinct `gcn_*` claim and every `gfac_*` factor in the selected root evidence chain and preserves the raw root JSON. No unselected LKM root, external paper text, or web evidence was imported; parent-package synthesis can later decide whether to connect this tFL-graphite branch to other TBG or multilayer-graphene mechanisms.
