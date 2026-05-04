# Merge audit log -- tbg-magic-angle-gaia

Regeneration date: 2026-05-04

## Duplicate and equivalence decisions

| pair/group | verdict | reason | action |
|---|---|---|---|
| `gcn_7bca73ad98eb4ed4` vs `gcn_93c279f20f364a40` | keep distinct | Both involve continuum velocity suppression near the magic angle, but the starting root states the Das Sarma 2020 empirical linear fit for `0 < theta < 3 deg`, while Wu 2018 derives a continuum Hamiltonian plus electron-phonon form factor with different parameters. | no merge; support edge only |
| `gcn_7bca73ad98eb4ed4` vs `gcn_feace4c9a0154885` | keep distinct | The strange-metallicity root includes a specific phonon-limited resistivity consequence through `1/v_F*^2`; the starting root is a velocity-fit claim. | no merge; support edge only |
| `gcn_93c279f20f364a40` vs `gcn_feace4c9a0154885` | keep distinct | Both share `v_F*` and electron-phonon context, but one derives `F(theta)` and one derives resistivity enhancement. | no merge |
| `gcn_a0ab3201de0e41ad` vs experimental superconducting dome claims | keep distinct | Qin 2021 is a phonon-mediated mean-field BdG theory root; Cao 2018 is an experimental phase-diagram root. No same-proposition equivalence or direct bridge was found. | no merge; Cao root rejected from executable graph |
| `gcn_848085b12d384915`, `gcn_5f58746bcc0b4098`, `gcn_de1d329f326f4e75`, `gcn_c220df1acc8b476a` | keep distinct | All concern near-first-magic-angle TBG flat bands, but methods differ: Kohn-Sham corrugated geometry, ab initio Wannier/TB screening over commensurate cells, DFT full relaxation, and relaxation-aware continuum/STS modeling. | no equivalence; scoped support edges |
| `gcn_afdfbd0c013048d8` vs BM velocity root | keep distinct | Magnetic-Bloch root starts from BM but adds flux `phi=2pi`, Landau-level basis, and topology; not the same proposition as zero-field velocity suppression. | no merge; support edge only |
| `gcn_8159f32dda354258` vs BM/Kohn-Sham velocity roots | keep distinct | Merged-Dirac root is a conjectural mechanism for velocity collapse, not an independent measurement of the same empirical fit. | no merge; support edge only |

## Rejected bridge candidates

| candidate/group | verdict | reason |
|---|---|---|
| Cao MA-TBG superconducting domes (`gcn_006f88d8df3548fa`) | rejected for May 4 executable graph | Chain-backed observation, but no LKM chain-backed bridge was found from the active BM/flat-band graph to the specific observed dome/insulator phase diagram without a generic synthesis claim. |
| Pressure-tuned large-angle TBG (`gcn_105d2fc961f949b6`) | rejected | Large-angle external compression is a different flat-band route; no accepted evidence-backed path to the first-magic-angle BM graph. |
| Few-layer graphite and multilayer/trilayer/quadrilayer/MATTG branches | rejected | Different layer count, stacking, or geometry; no chain-backed bridge that preserves bilayer-TBG scope without agent-authored family synthesis. |
| hBN/TMD substrate topology branches | deferred | Direct TBG substrate roots exist, but adding them would move into topological/substrate perturbation scope. This run stopped at the stronger BM/velocity/flat-band/relaxation connected component. |

## Contradiction decisions

No `contradiction()` operator was emitted. Differences among accepted roots are method, parameter, or regime scope distinctions: empirical BM fit, continuum Hamiltonian with electron-phonon form factor, Kohn-Sham/DFT/ab initio workflows, relaxation models, flux `phi=2pi`, and conjectural merged-Dirac mechanism. None asserts mutually exclusive same-system/same-condition values in the accepted executable graph.

## Duplicate audit status

`gaia inquiry review --strict .` on the regenerated package reported 0 warnings, 0 errors, 0 independent claims missing priors, and 0 possible duplicate claims.

Strict review also reported 31 structural holes/orphaned internal generated helper claims (`__conjunction_result_*` / `__implication_result_*`) and 19 unreviewed warrants. These are not science-facing duplicate source claims and are retained as review-work items rather than merge/equivalence actions.
