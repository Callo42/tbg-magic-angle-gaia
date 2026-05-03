# Mapping audit log -- magnetic-bloch-tbg-gaia

Source evidence: `input/evidence_gcn_afdfbd0c013048d8.json`

## Claims

| lkm_id | label | source_paper | mapping decision |
|---|---|---|---|
| `gcn_06caff12a4d84b26` | `gcn_06caff12a4d84b26` | `paper:867760961551860070` | mapped as a self-contained numerical-convergence premise for the Landau-level truncation procedure; original LKM text preserved in `lkm_original` |
| `gcn_fedb8c2683fb48c7` | `gcn_fedb8c2683fb48c7` | `paper:867760961551860070` | mapped as a self-contained physical-interpretation premise covering cutoff, k-mesh, and parameter-grid extrapolation; original LKM text preserved in `lkm_original` |
| `gcn_afdfbd0c013048d8` | `gcn_afdfbd0c013048d8` | `paper:867760961551860070` | mapped as the selected root conclusion; rewritten to expose system, flux, model parameters, gap scale, and Chern-number regimes; original LKM text preserved in `lkm_original` |

## Factors -> deductions

| factor_id | source_paper | premises | conclusion | dsl_kind | warrant_prior |
|---|---|---|---|---|---|
| `gfac_9fc5b7efdef44e14` | `paper:867760961551860070` | `gcn_06caff12a4d84b26`, `gcn_fedb8c2683fb48c7` | `gcn_afdfbd0c013048d8` | `deduction` | `0.95` |

## Decomposition audit

The root LKM claim is conjunctive: it combines the magnetic Bloch representation,
the reentrant flat-band/gap result, and the `(w0,w1)` topology phase diagram.
No additional Gaia contradiction/equivalence decomposition was emitted because
the selected evidence supplies these as parts of one same-paper conclusion under
the same BM-model scope, not as a conflict or independent agreement between two
separable sources. The self-contained root claim keeps the components explicit.

## Contradictions

| pair | origin | decision | dsl_action |
|---|---|---|---|
| `(none)` | discovery flags and selected evidence chain | `contradictions.md` reports no pairs; the single evidence chain does not contain an incompatible same-system value or opposite topological assignment | no `contradiction()` emitted |

## Open-problem audit

| checked label | tension searched within selected evidence | decision |
|---|---|---|
| `gcn_06caff12a4d84b26` | Landau-level cutoff convergence and Wilson-loop/Chern-number numerical tolerance could fail if cutoff scans are insufficient | retained as an assumption-bearing leaf with prior `0.74`; no contrary LKM claim appears in selected evidence |
| `gcn_fedb8c2683fb48c7` | Physical interpretation depends on cutoff, k-mesh, parameter-grid extrapolation, and BM-model approximations | retained as an assumption-bearing leaf with prior `0.68`; no contrary LKM claim appears in selected evidence |
| `gcn_afdfbd0c013048d8` | Gap scale and Chern assignments depend on `(w0,w1)` regime and should not be generalized outside the stated magic-angle BM parameter scope | retained as scoped root conclusion; no open contradiction emitted |

## Dismissed

| pair | origin | rationale |
|---|---|---|
| `(none in this run)` |  |  |
