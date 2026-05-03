# Mapping audit log -- ab-initio-twisted-multilayer-gaia

## 9-step batch checklist

| step | status | audit note |
|---|---|---|
| 1. Bootstrap | done | Loaded only `input/evidence_gcn_5f58746bcc0b4098.json` for the chain backbone. |
| 2. Refine | done | Rewrote the root to include explicit system, angle range, workflow, p(theta) quantity, and Fermi-level flat-band outcome. Empty premise texts were reconstructed only from factor steps and marked with `todo` metadata. |
| 3. Decompose | done | No compound conflict/agreement decomposition was emitted; the root is a single workflow-result claim. |
| 4. Hunt open problems | done | The chain itself flags structural relaxation below about 1 degree as a caveat absent from the workflow. This was logged as a dismissed contradiction/scope risk, not promoted to an unsupported `contradiction()` edge. |
| 5. Mark suspicions | done | Scope and premise-content suspicions are recorded through `dismissed/structural_relaxation_scope.md`, `todo` metadata on empty-content premises, and prior justifications. |
| 6. Compile + infer | done | `uv run --project /home/rsw/ThisIsDP/dev/test_lkm2gaia gaia compile .` and `gaia infer .` passed; IR hash `sha256:c3e5e8d555054feb7dc540c95507eee2b1e43ecd2ed3a638eb08cbf65b13363a`. |
| 7. Review obligations/holes | done | `gaia check --brief .` and `gaia check --hole .` passed with 0 holes. Gaia reports two internal generated orphan claims for the deduction, not science-facing LKM claims. |
| 8. Search supports | done | No extra support claims were formalized because this worker is constrained to the selected raw evidence and `data.papers`. |
| 9. Repeat/exit rationale | done | No repair loop was needed after checks passed; remaining risks are TODO-marked premise priors and the structural-relaxation scope caveat. |

## Claims

| label | lkm id | source paper | self-contained transformation | lkm_original preserved |
|---|---|---|---|---|
| `gcn_af432bff_ab_initio_tb_workflow` | `gcn_af432bff1d3e4cf0` | `paper:812643486368006145` | Empty LKM premise reconstructed from factor steps 1 and 3 as the established Wannier-derived TB workflow, 60-k-point path, and detector window used for the survey. | yes, empty string plus `todo` metadata |
| `gcn_be5d1975_detector_interpolation` | `gcn_be5d1975ecac4211` | `paper:812643486368006145` | Empty LKM premise reconstructed from factor step 3 as the detector-output interpolation/blending assumption used to obtain continuous p(theta). | yes, empty string plus `todo` metadata |
| `gcn_5f58746b_magic_angle_flat_band_likelihood` | `gcn_5f58746bcc0b4098` | `paper:812643486368006145` | Root refined to make the 33-cell angle sweep, ab initio Wannier-derived TB workflow, p(theta) maximum near 1.1 degrees, and near-Fermi low-dispersion bands explicit. | yes |

## Factors -> deductions

| factor_id | source_paper | premises | conclusion | dsl_kind | prior |
|---|---|---|---|---|---|
| `gfac_c4fed52224164214` | `paper:812643486368006145` | `gcn_af432bff1d3e4cf0`, `gcn_be5d1975ecac4211` | `gcn_5f58746bcc0b4098` | `deduction` | 0.95 |

## Open-problem and contradiction pass

| candidate | origin | decision | rationale |
|---|---|---|---|
| Structural relaxation below about 1 degree may modify band structures and widen single-particle gaps | factor step 6 | dismissed as formal contradiction; retained as open-problem risk | The selected evidence names an omitted effect but does not provide a counterclaim under the same workflow, angle, relaxation state, and detector definition. |
| Empty LKM premise text for workflow and interpolation assumptions | premises `gcn_af432...`, `gcn_be5...` | retained as audit risk | The chain steps provide enough context to avoid opaque placeholders, but the premise IDs themselves lack verbatim content, so priors are capped and TODO-marked. |

## Equivalences

| pair | decision | dsl_action |
|---|---|---|
| `gcn_af432bff1d3e4cf0` / `gcn_be5d1975ecac4211` | related workflow premises, not the same proposition | none |
| premise IDs / `gcn_5f58746bcc0b4098` | premises support a derived result, not equivalent to it | none |

## Dismissed

| pair | origin | rationale |
|---|---|---|
| See `dismissed/structural_relaxation_scope.md` | selected evidence open-problem audit | Omitted relaxation is a model-scope caveat, not an incompatible LKM-backed claim pair. |

## Gaia CLI verification

All requested local checks passed from the subgraph package directory:

```bash
uv run --project /home/rsw/ThisIsDP/dev/test_lkm2gaia gaia compile .
uv run --project /home/rsw/ThisIsDP/dev/test_lkm2gaia gaia check --brief .
uv run --project /home/rsw/ThisIsDP/dev/test_lkm2gaia gaia check --hole .
uv run --project /home/rsw/ThisIsDP/dev/test_lkm2gaia gaia infer .
```

Summary:

- Compile: 5 knowledge, 1 strategy, 0 operators; IR hash `sha256:c3e5e8d555054feb7dc540c95507eee2b1e43ecd2ed3a638eb08cbf65b13363a`.
- `check --brief`: passed.
- `check --hole`: passed with 0 holes / 2 independent claims; both independent premises have TODO-marked priors.
- `infer`: passed, exact JT inference converged after 2 iterations; exported root belief `0.76616807704`.
