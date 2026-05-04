# TBG magic-angle Gaia candidate checkpoint -- May 4 regeneration

Topic: single-root TBG magic-angle graph grown from BM velocity suppression through connected, chain-backed Turn-2 extensions.

Discovery inputs:

- Existing raw discovery files under `artifacts/lkm-discovery/input/`.
- `may4_match_bm_velocity_extensions.json`
- `may4_match_bm_many_body_extensions.json`
- `may4_match_bm_abinitio_bridge_retry.json`
- May 4 evidence files prefixed `may4_evidence_*.json`

Only candidates with `total_chains > 0` are eligible roots or extensions.

## Starting Root

1. `gcn_7bca73ad98eb4ed4` | BM velocity suppression in TBG | The BM continuum model strongly suppresses the noninteracting Dirac-point velocity near the largest magic angle and admits an empirical linear fit for `0 < theta < 3 deg`. | `total_chains=1` | selected as the exact single starting root.

Selection rationale: this root is central to the recommended strategy, is chain-backed, and its evidence chain explicitly connects `v_F*(theta)` to low-energy many-body and electron-phonon calculations.

## Accepted Connected Extensions

| pass | extension root | path to current graph | status |
|---|---|---|---|
| Turn-2.1 | `gcn_93c279f20f364a40` | Chain-backed continuum moire Hamiltonian derives suppressed `v_F*(theta)` near `theta_magic ~ 1.025 deg` and electron-phonon form factor `F(theta)`, directly supporting the BM velocity root's velocity-suppression mechanism. | accepted |
| Turn-2.2 | `gcn_feace4c9a0154885` | Chain-backed BM velocity premise states `v_F*/v_F ~ 1/4` at `theta=1.5 deg` and uses `1/v_F*^2` scaling for phonon-limited resistivity; connected to the BM velocity root and `gcn_93c279f20f364a40`. | accepted |
| Turn-2.3 | `gcn_a0ab3201de0e41ad` | Chain-backed MATBG finite-pairing-momentum BdG calculation remains in the continuum-model/phonon-mediated branch connected through `v_F*`, optical phonon attraction, and flat-band VHSs. The support edge is intentionally moderate and model-family scoped. | accepted |
| Turn-2.4 | `gcn_848085b12d384915` | Chain-backed Kohn-Sham calculation independently finds vanishing Fermi velocity and flat bands near `theta_M ~ 1.08 deg`, supporting the same velocity-collapse phenomenon by a different method. | accepted |
| Turn-2.5 | `gcn_5f58746bcc0b4098` | Chain-backed ab initio Wannier/TB workflow finds low-dispersion TBG bands near `theta* ~ 1.1 deg`; connected through the accepted Kohn-Sham flat-band/velocity root. | accepted |
| Turn-2.6 | `gcn_de1d329f326f4e75` | Chain-backed DFT relaxation claim concerns `theta=1.08 deg` first-magic-angle TBG flat bands and gaps; connected through ab initio/Kohn-Sham flat-band roots. | accepted |
| Turn-2.7 | `gcn_c220df1acc8b476a` | Chain-backed lattice-reconstruction claim concerns magic-angle TBG relaxation effects on flat-band bandwidth and isolation; connected through the accepted DFT relaxation root. | accepted |
| Turn-2.8 | `gcn_afdfbd0c013048d8` | Chain-backed magnetic Bloch root explicitly starts from the BM continuum model at magic-angle parameters; connected to the starting BM root with flux/topology scope preserved. | accepted |
| Turn-2.9 | `gcn_8159f32dda354258` | Chain-backed merged-Dirac root proposes a same-system small-angle mechanism for vanishing Dirac velocity and nearly flat bands; connected through BM and Kohn-Sham velocity-collapse roots. | accepted |

## Rejected Or Deferred Candidates

| candidate | decision | reason |
|---|---|---|
| `gcn_006f88d8df3548fa` Cao MA-TBG superconducting domes | rejected for this executable graph | Chain-backed as an observation, but no chain-backed bridge was found that makes BM velocity suppression or phonon/BdG calculations support the specific experimental dome/insulator phase diagram without an agent-authored synthesis claim. |
| `gcn_105d2fc961f949b6` pressure-tuned large-angle TBG | rejected | Same material family, but large-angle pressure tuning is a different control route; May 4 bridge searches did not find a direct chain-backed path from the active first-magic-angle BM graph. |
| `gcn_f23eff9c755840f2` twisted few-layer graphite | rejected | Nearby flat-band theme but different few-layer graphite system; no chain-backed path to the active bilayer TBG graph without generic moire-family synthesis. |
| `gcn_2cf09f115b814154`, `gcn_225da7b340cb47b8`, `gcn_14a55aff3de24a3a`, `gcn_b4e3bdff3c0c439a` multilayer/trilayer/quadrilayer/MATTG roots | rejected | Different layer count or stacking; no accepted LKM chain-backed bridge to the active bilayer TBG graph under the May 4 no-synthesis rule. |
| `gcn_584669e24c6145a7`, `gcn_9f7dbaf8f0014316` hBN/TMD substrate roots | deferred | They are TBG substrate perturbation roots, but adding them would require topology/substrate scope bridges. The current run stops before substrate branches to keep the graph focused and connected by stronger BM/velocity/flat-band evidence. |

## Bridge Search Outcome

May 4 LKM searches found enough connected roots for a coherent BM velocity/flat-band/phonon/relaxation graph, but not enough honest bridge evidence to keep expanding to about 100 nodes without adding pressure, superconducting-observation, substrate, or multilayer branches through generic agent synthesis. The final package therefore stops at the largest coherent connected graph found in this pass.
