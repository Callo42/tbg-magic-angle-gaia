# Mapping audit log -- tbg-dft-relaxation-gaia

Source evidence: `input/turn2_evidence_gcn_de1d329f326f4e75.json`

## Claims

| lkm_id | label | source_paper | decision |
|---|---|---|---|
| gcn_6463be97083b44fd | gcn_6463be97083b44fd | paper:812551532191940608 | Mapped as a self-contained leaf assumption about comparing vdW-DF2 Kohn-Sham gaps to spectroscopy; `lkm_original`, `lkm_id`, `source_paper`, and `provenance_source` preserved. |
| gcn_abaf80790d664630 | gcn_abaf80790d664630 | paper:812551532191940608 | Mapped as a self-contained leaf assumption about constrained in-plane-only and out-of-plane-only relaxations as a diagnostic; metadata preserved. |
| gcn_de1d329f326f4e75 | gcn_de1d329f326f4e75 | paper:812551532191940608 | Mapped as selected exported root conclusion summarizing full-relaxation DFT gaps, partial-relaxation failures, and TB agreement; metadata preserved. |

## Factors -> deductions

| factor_id | source_paper | premises | conclusion | dsl_kind |
|---|---|---|---|---|
| gfac_3a3936eff4a1434c | paper:812551532191940608 | gcn_6463be97083b44fd, gcn_abaf80790d664630 | gcn_de1d329f326f4e75 | deduction(prior=0.95) with six numbered LKM steps |

## Decomposition

The root is compound in the ordinary-language sense, but the selected evidence supplies it as one same-paper conclusion rather than as a comparison between two independent claims requiring `equivalence()` or `contradiction()`. I preserved the root as one self-contained conclusion and did not invent extra non-LKM claim nodes.

## Contradictions

| pair | decision | dsl_action |
|---|---|---|
| Kohn-Sham gap comparability assumption vs selected root | weak assumption/open problem, not contradiction | no `contradiction()` emitted; tracked in priors and `open_problems.md` |
| partial-relaxation diagnostic assumption vs selected root | weak assumption/open problem, not contradiction | no `contradiction()` emitted; tracked in priors and `open_problems.md` |

## Dismissed

No contradiction candidate was dismissed as false while mapping; the selected evidence simply lacked a counter-claim to promote.
