# Mapping audit log - twisted-trilayer-flat-bands-gaia

## Claims

| lkm_id | label | source_paper | transformation |
|---|---|---|---|
| `gcn_768268d063184cb8` | `gcn_768268d063184cb8` | `paper:867757254252691813` | Rewritten as a self-contained premise about the Ma et al. minimal continuum Hamiltonian and remote-hopping omissions; verbatim LKM text preserved in `lkm_original`. |
| `gcn_ba18ade2bb8145ee` | `gcn_ba18ade2bb8145ee` | `paper:867757254252691813` | Rewritten as a self-contained premise about the gamma_0/gamma_1 parameter choices and parameter sensitivity; verbatim LKM text preserved in `lkm_original`. |
| `gcn_2a4995cfc44a4638` | `gcn_2a4995cfc44a4638` | `paper:867757254252691813` | Rewritten as a self-contained numerical-convergence premise for finite plane-wave and k-point sampling; verbatim LKM text preserved in `lkm_original`. |
| `gcn_4249f998947d4ee0` | `gcn_4249f998947d4ee0` | `paper:867757254252691813` | Rewritten as a self-contained premise about the discrete twist-angle scan resolution; verbatim LKM text preserved in `lkm_original`. |
| `gcn_2cf09f115b814154` | `gcn_2cf09f115b814154` | `paper:867757254252691813` | Rewritten as a self-contained root conclusion about the 1.12 degree largest magic angle and two nearly flat central moire bands; verbatim LKM text preserved in `lkm_original`. |

## Factors -> deductions

| factor_id | source_paper | premises | conclusion | dsl_kind | prior |
|---|---|---|---|---|---|
| `gfac_0046298fbcb144c4` | `paper:867757254252691813` | `gcn_768268d063184cb8`, `gcn_ba18ade2bb8145ee`, `gcn_2a4995cfc44a4638`, `gcn_4249f998947d4ee0` | `gcn_2cf09f115b814154` | `deduction` | 0.95 |

## Decomposition

No decomposition was applied. The selected root is a scoped single-paper model result: under a named minimal continuum parameterization, the largest magic angle is near 1.12 degrees and the two central bands are nearly flat. The evidence does not provide independent atomic sides of a comparison that should become an equivalence or contradiction operator.

## Equivalences

| pair | decision | dsl_action |
|---|---|---|
| (none in this run) | No independent same-proposition pair in selected payload. | None |

## Contradictions and open problems

| item | decision | dsl_action |
|---|---|---|
| Minimal model omits gamma_3, gamma_4, and Delta'. | Scoped as a modeling assumption and parameter-sensitivity caveat, not a contradiction inside this payload. | No `contradiction(...)`; retained as `gcn_768268d063184cb8` / `gcn_ba18ade2bb8145ee`. |
| Finite plane-wave/k-point convergence. | Open review target because no independent convergence chain is present. | Lower-prior leaf `gcn_2a4995cfc44a4638`. |
| Finite twist-angle grid. | Open review target because the payload does not contain a finer-grid countercheck. | Lower-prior leaf `gcn_4249f998947d4ee0`. |

## Dismissed

| pair | origin | rationale |
|---|---|---|
| (none in this run) | | |
