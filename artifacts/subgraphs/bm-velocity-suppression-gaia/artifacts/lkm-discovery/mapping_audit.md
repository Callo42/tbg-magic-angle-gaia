# Mapping audit log -- bm-velocity-suppression-gaia

Source root: `gcn_7bca73ad98eb4ed4`
Evidence file: `artifacts/lkm-discovery/input/evidence_gcn_7bca73ad98eb4ed4.json`

## Claims

| lkm_id | label | source_paper | decision |
|---|---|---|---|
| `gcn_d3808439ccf6496b` | `gcn_d3808439ccf6496b` | `paper:812646407474249731` | Mapped as a self-contained premise for the BM continuum velocity fit; original LKM text preserved in metadata. |
| `gcn_671ceef053a64aa7` | `gcn_671ceef053a64aa7` | `paper:812646407474249731` | Mapped as a self-contained premise for the BM model's role as a bare noninteracting input; original LKM text preserved in metadata. |
| `gcn_7bca73ad98eb4ed4` | `gcn_7bca73ad98eb4ed4` | `paper:812646407474249731` | Mapped as the selected root conclusion; original LKM text preserved in metadata. |

## Factors -> deductions

| factor_id | source_paper | premises | conclusion | dsl_kind |
|---|---|---|---|---|
| `gfac_2f2334a945114bf3` | `paper:812646407474249731` | `gcn_d3808439ccf6496b`, `gcn_671ceef053a64aa7` | `gcn_7bca73ad98eb4ed4` | `deduction(..., prior=0.95)` with numbered LKM steps |

## Decomposition

No compound root decomposition was emitted. The selected root is scoped as a single model-result claim: BM continuum velocity suppression plus the empirical fit in the same angular window. The evidence chain does not provide independent same-scope atomic claims that should be split into contradiction or equivalence operators.

## Equivalences

| pair | a | b | decision | dsl_action |
|---|---|---|---|---|
| (none in selected evidence) | | | | |

## Contradictions

| pair | a | b | decision | dsl_action |
|---|---|---|---|---|
| (none promoted) | | | Discovery flags report no pairs; selected one-paper chain provides no incompatible same-system values. | No `contradiction()` emitted. |

## Dismissed

| pair | origin | rationale |
|---|---|---|
| (none) | | |
