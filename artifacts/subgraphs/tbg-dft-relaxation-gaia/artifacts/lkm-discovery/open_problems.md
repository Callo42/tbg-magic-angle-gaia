# Open-problem audit -- tbg-dft-relaxation-gaia

The selected evidence was audited for research-worthy tensions using only `turn2_evidence_gcn_de1d329f326f4e75.json` and its `data.papers` entry.

| claim | audit outcome | action |
|---|---|---|
| gcn_6463be97083b44fd | The comparison between vdW-DF2 Kohn-Sham gaps and spectroscopy depends on the assumption that electron-electron correlation and quasiparticle self-energy corrections do not substantially renormalize the 10-30 meV gap scale. The selected JSON contains no counter-evidence quantifying those corrections. | Prior set to 0.62 with `TODO:review`; no contradiction edge. |
| gcn_abaf80790d664630 | The in-plane-only and out-of-plane-only constrained optimizations are useful diagnostics only if nonlinear coupling in the fully relaxed structure does not invalidate the separation. The selected JSON acknowledges the caveat but gives no counter-claim. | Prior set to 0.70 with `TODO:review`; no contradiction edge. |
| gcn_de1d329f326f4e75 | The root conclusion combines DFT gaps, partial-relaxation tests, and TB agreement for the same Cantele et al. geometry. The selected JSON does not include another same-scope result with incompatible gap values. | Derived by `strat_gfac_3a3936eff4a1434c`; no direct prior. |
