# Mapping audit log -- tbg-magic-angle-gaia

Regeneration date: 2026-05-04

Policy: May 4 single-root regeneration. The executable package starts from exactly one chain-backed LKM root (`gcn_7bca73ad98eb4ed4`) and adds only connected Turn-2 extensions. No executable claim uses agent-authored synthesis provenance. Scope, non-contradiction, and non-equivalence judgments are logged here and in `merge_audit.md`, not promoted to `claim(...)` nodes.

## Starting root

| root id | module | exported label | evidence file | decision |
|---|---|---|---|---|
| `gcn_7bca73ad98eb4ed4` | `paper_dassarma2020.py` | `gcn_7bca73ad98eb4ed4` | `evidence_gcn_7bca73ad98eb4ed4.json` | selected as the exact single starting root |

## Accepted Turn-2 extensions

| pass | root id | module | factor ids | path to current graph |
|---|---|---|---|---|
| Turn-2.1 | `gcn_93c279f20f364a40` | `paper_wu2018.py` | `gfac_4dfdc41c1d7c4f0b` | LKM chain derives `v_F*(theta)` suppression and electron-phonon `F(theta)` from a continuum moire Hamiltonian; supports BM velocity root. |
| Turn-2.2 | `gcn_feace4c9a0154885` | `paper_dassarma2022.py` | `gfac_80bf41b7112e4d20` | LKM chain uses BM velocity suppression to derive phonon-resistivity enhancement through `1/v_F*^2`; connected to root and Turn-2.1. |
| Turn-2.3 | `gcn_a0ab3201de0e41ad` | `paper_qin2021.py` | `gfac_8e790c60b9c94313` | LKM chain uses MATBG continuum flat bands, optical phonon attraction, and extracted `v_F*(mu)`; accepted as moderate model-family continuation of the phonon branch. |
| Turn-2.4 | `gcn_848085b12d384915` | `paper_uchida2014.py` | `gfac_e7f366dda20d45cf` | Kohn-Sham TBG calculation independently reports velocity collapse and flat bands near `theta_M ~ 1.08 deg`; supports the root without equivalence. |
| Turn-2.5 | `gcn_5f58746bcc0b4098` | `paper_tritsaris2020.py` | `gfac_c4fed52224164214` | Ab initio Wannier/TB flat-band likelihood near `theta* ~ 1.1 deg`; connected through Turn-2.4. |
| Turn-2.6 | `gcn_de1d329f326f4e75` | `paper_cantele2020.py` | `strat_gfac_3a3936eff4a1434c` | DFT relaxation result at `theta=1.08 deg`; connected through first-principles flat-band roots. |
| Turn-2.7 | `gcn_c220df1acc8b476a` | `paper_liu2020.py` | `gfac_e5303e2e42664d99` | Lattice-reconstruction continuum/STS result for MA-TBG flat bands; connected through Turn-2.6 relaxation branch. |
| Turn-2.8 | `gcn_afdfbd0c013048d8` | `paper_herzogarbeitman2022.py` | `gfac_9fc5b7efdef44e14` | Magnetic-Bloch representation explicitly starts from the BM continuum model at magic-angle parameters; connected to root with flux scope preserved. |
| Turn-2.9 | `gcn_8159f32dda354258` | `paper_yamada2020.py` | `strat_gfac_3970f30041424709` | Same-system small-angle mechanism for vanishing Dirac velocity and flat bands; connected through BM/Kohn-Sham velocity roots, marked conjectural. |

## Cross-paper operators

All cross-paper wiring is `support(...)` between LKM-backed claims. No `claim(...)`, `equivalence(...)`, or `contradiction(...)` is emitted in `cross_paper.py`.

| operator | premises | conclusion | prior | audit note |
|---|---|---|---|---|
| `link_wu_velocity_supports_bm_velocity` | `gcn_93c279f20f364a40` | `gcn_7bca73ad98eb4ed4` | 0.82 | independent continuum velocity support, not identical linear-fit equivalence |
| `link_bm_velocity_to_phonon_resistivity` | `gcn_7bca73ad98eb4ed4`, `gcn_93c279f20f364a40` | `gcn_feace4c9a0154885` | 0.78 | connects BM velocity suppression to LKM-backed phonon-resistivity scaling |
| `link_phonon_inputs_to_pairing_calculation` | `gcn_93c279f20f364a40`, `gcn_feace4c9a0154885` | `gcn_a0ab3201de0e41ad` | 0.60 | moderate model-family support; not an experimental superconductivity bridge |
| `link_kohn_sham_velocity_to_bm_velocity` | `gcn_848085b12d384915` | `gcn_7bca73ad98eb4ed4` | 0.72 | independent Kohn-Sham velocity-collapse support |
| `link_kohn_sham_to_abinitio_flat_band` | `gcn_848085b12d384915` | `gcn_5f58746b_magic_angle_flat_band_likelihood` | 0.70 | first-principles flat-band agreement, no workflow equivalence |
| `link_abinitio_to_relaxation_roots` | `gcn_848085b12d384915`, `gcn_5f58746b_magic_angle_flat_band_likelihood` | `gcn_de1d329f326f4e75` | 0.68 | connects first-principles flat-band context to DFT relaxation |
| `link_relaxation_roots` | `gcn_de1d329f326f4e75` | `gcn_c220df1acc8b476a` | 0.70 | relaxation-specific continuation, DFT and continuum/STS kept distinct |
| `link_bm_velocity_to_magnetic_bloch` | `gcn_7bca73ad98eb4ed4` | `gcn_afdfbd0c013048d8` | 0.66 | BM model path with magnetic-flux scope preserved |
| `link_bm_velocity_to_merged_dirac` | `gcn_7bca73ad98eb4ed4`, `gcn_848085b12d384915` | `gcn_8159f32d_merged_dirac_magic_angle_flat_band` | 0.62 | conjectural same-system velocity mechanism, no proof/equivalence |

## Rejected or deferred branches

The following chain-backed roots remain preserved in raw artifacts and/or subgraph artifacts but are not imported by the executable package: Cao superconducting domes, pressure-tuned large-angle TBG, few-layer graphite, trilayer/quadrilayer/monolayer-bilayer/MATTG, hBN-aligned TBG, and TBG-on-TMD substrate topology. Rejection/defer reasons are in `candidates.md` and `merge_audit.md`.

## Per-pass TODO checklist results

### Turn-1 root build (`gcn_7bca73ad98eb4ed4`)

- [x] The package grows from a single starting root in one on-disk package.
- [x] Every science-facing claim is LKM-backed or a direct decomposition of LKM-backed evidence.
- [x] No extension was accepted at this step.
- [x] No executable science-facing claim uses banned synthesis provenance.
- [x] Scope/non-contradiction/non-equivalence judgments remain audit-only.
- [x] Gaia checks scheduled after rebuild.
- [x] Audit files remain current.
- [x] README/analysis scheduled for regeneration and prose repair.

### Turn-2 extension loop

- [x] The package still grows from `gcn_7bca73ad98eb4ed4`.
- [x] New claims come from raw LKM JSON or existing LKM-backed subgraph evidence.
- [x] Every accepted extension has a logged path to the current graph.
- [x] No executable synthesis claim was added.
- [x] Scope judgments for rejected pressure, superconducting-observation, substrate, and multilayer branches are audit-only.
- [x] Gaia checks scheduled after source rebuild.
- [x] `mapping_audit.md`, `merge_audit.md`, `merge_decisions.todo`, and `dismissed/` updated or retained.
- [x] README/analysis will state the connected graph is below 100 because unsupported bridge branches were rejected.

### Final render pass

- [x] `gaia compile .`, `gaia check --hole .`, and `gaia infer .` pass.
- [x] Duplicate review is rerun and logged.
- [x] README, docs, and starmap are regenerated.
