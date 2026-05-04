# Semantic label audit -- tbg-magic-angle-gaia

Purpose: presentation-only node-label conversion on 2026-05-04. Scientific claim strings, graph logic, priors, LKM IDs, `source_paper`, `provenance_source`, `derived_from_lkm_ids`, and raw evidence artifacts were not changed by the label conversion.

## Metadata-only provenance repair

On 2026-05-04, approved repair #3 restored summarized `lkm_original` fields to exact raw LKM `data.claim.content` or corresponding raw premise content for active claims with non-empty raw evidence. No semantic labels, executable claim strings, priors, or graph operators were changed.

## Science-facing claim labels

| old label | new label | rationale |
|---|---|---|
| `gcn_d3808439ccf6496b` | `bm_velocity_linear_fit` | BM continuum v_F*(theta) linear fit near the magic angle. |
| `gcn_671ceef053a64aa7` | `bm_velocity_bare_input` | BM continuum v_F*(theta) used as the bare low-energy input. |
| `gcn_7bca73ad98eb4ed4` | `bm_magic_angle_velocity_suppression` | BM magic-angle suppression of the low-energy Dirac velocity. |
| `gcn_b411dd99a41e4de2` | `moire_spinor_phonon_form_factor` | Moire spinor-overlap correction F(theta) for electron-phonon matrix elements. |
| `gcn_570f7bfc906e4dbd` | `relaxed_tunneling_magic_angle_velocity` | Relaxed tunneling parameters producing the model magic angle and suppressed v_F*. |
| `gcn_93c279f20f364a40` | `wu_velocity_phonon_form_factor` | Wu-Hwang-Das Sarma continuum velocity plus phonon form-factor result. |
| `gcn_1cb7675d5185405d` | `bm_velocity_suppression_caveated` | BM velocity-suppression premise with relaxation and many-body caveats. |
| `gcn_feace4c9a0154885` | `phonon_resistivity_velocity_enhancement` | v_F* suppression enhancing phonon-limited resistivity through 1/v_F*^2 scaling. |
| `gcn_1b0c5250d2574e24` | `optical_phonons_instantaneous_couplings` | Optical phonons treated as instantaneous static BCS-like couplings. |
| `gcn_4eda4fedb8364912` | `intravalley_coulomb_tuning_parameter` | Intravalley Coulomb parameter u treated as a phenomenological tuning parameter. |
| `gcn_993c306ad37c4dfb` | `intervalley_scattering_neglect` | Intervalley Coulomb scattering neglected relative to intravalley repulsion. |
| `gcn_2bc94d32817142f7` | `continuum_vhs_pairing_band_assumption` | Continuum flat-band VHS structure used for phonon-mediated pairing predictions. |
| `gcn_324b385e04254463` | `vhs_tc_velocity_extrema_coincidence` | Coincidence of T_c maxima and v_F* minima at flat-band VHSs. |
| `gcn_a0ab3201de0e41ad` | `phonon_bdg_vhs_tc_hc2_velocity_extrema` | BdG result tying VHSs to T_c maxima, H_c2 peaks, and v_F* minima. |
| `gcn_159120a419184e9e` | `small_angle_corrugation_extrapolation` | Small-angle corrugation reconstructed by extrapolated Fourier coefficients. |
| `gcn_75a1c2477ca448b0` | `kohn_sham_magic_angle_numerical_scope` | Numerical and methodological scope of the Kohn-Sham magic angle. |
| `gcn_390a496067b94209` | `half_filled_flat_band_magnetism_tendency` | Half-filled flat Kohn-Sham bands interpreted as a possible magnetism tendency. |
| `gcn_848085b12d384915` | `kohn_sham_magic_angle_flat_bands` | Kohn-Sham magic angle where velocity vanishes and flat bands appear. |
| `gcn_af432bff_ab_initio_tb_workflow` | `ab_initio_tb_flat_band_workflow` | Ab initio Wannier-derived tight-binding workflow and flat-band detector setup. |
| `gcn_be5d1975_detector_interpolation` | `flat_band_detector_interpolation` | Detector outputs converted into a continuous flat-band likelihood p(theta). |
| `gcn_5f58746b_magic_angle_flat_band_likelihood` | `ab_initio_magic_angle_flat_band_likelihood` | Ab initio/TB flat-band likelihood maximized near theta about 1.1 degrees. |
| `gcn_8cd2984a6296435c` | `relaxation_broadens_isolates_flat_bands` | Lattice relaxation broadening and isolating the low-energy flat-band manifold. |
| `gcn_ed8fa9253ea24982` | `heterostrain_flat_band_fine_splitting` | Heterostrain-induced fine splitting absent from relaxation-only calculations. |
| `gcn_c220df1acc8b476a` | `relaxation_reproduces_sts_flat_band_trends` | Relaxation reproducing STS trends for broader and more isolated flat bands. |
| `gcn_6463be97083b44fd` | `dft_gap_spectroscopy_comparison_assumption` | Assumption behind comparing DFT gaps with spectroscopy. |
| `gcn_abaf80790d664630` | `relaxation_component_diagnostic_assumption` | Diagnostic separation of in-plane and out-of-plane relaxation effects. |
| `gcn_de1d329f326f4e75` | `full_relaxation_reproduces_flat_band_gaps` | Full relaxation required to reproduce flat-band manifold and Gamma-point gaps. |
| `gcn_06caff12a4d84b26` | `magnetic_bloch_cutoff_convergence` | Landau-level cutoff convergence for the magnetic Bloch BM Hamiltonian. |
| `gcn_fedb8c2683fb48c7` | `reentrant_flat_band_parameter_convergence` | Parameter-grid and convergence assumptions for reentrant flat-band interpretation. |
| `gcn_afdfbd0c013048d8` | `magnetic_bloch_reentrant_flat_bands` | Magnetic-Bloch calculation producing reentrant flat bands and topology regimes. |
| `gcn_7687975d_small_angle_merging_conjecture` | `small_angle_dirac_merging_conjecture` | Small-angle continuation conjecture for four-Dirac-point merging. |
| `gcn_8159f32d_merged_dirac_magic_angle_flat_band` | `merged_dirac_magic_angle_flat_band` | Merged-Dirac mechanism proposed for vanishing velocity and flat bands. |

## Deduction strategy labels

These strategy variables were renamed to avoid displaying raw `gfac_*` fragments in rendered strategy nodes. Factor IDs remain preserved in `mapping_audit.md` and in raw LKM JSON.

| old label | new label | rationale |
|---|---|---|
| `gfac_2f2334a945114bf3` | `derive_bm_magic_angle_velocity_suppression` | Semantic name derived from the unchanged deduction conclusion and LKM factor role. |
| `gfac_4dfdc41c1d7c4f0b` | `derive_wu_velocity_phonon_form_factor` | Semantic name derived from the unchanged deduction conclusion and LKM factor role. |
| `gfac_80bf41b7112e4d20` | `derive_phonon_resistivity_velocity_enhancement` | Semantic name derived from the unchanged deduction conclusion and LKM factor role. |
| `gfac_8e790c60b9c94313` | `derive_phonon_bdg_vhs_tc_hc2_velocity_extrema` | Semantic name derived from the unchanged deduction conclusion and LKM factor role. |
| `gfac_e7f366dda20d45cf` | `derive_kohn_sham_magic_angle_flat_bands` | Semantic name derived from the unchanged deduction conclusion and LKM factor role. |
| `strat_gfac_c4fed52224164214` | `derive_ab_initio_magic_angle_flat_band_likelihood` | Semantic name derived from the unchanged deduction conclusion and LKM factor role. |
| `gfac_e5303e2e42664d99` | `derive_relaxation_reproduces_sts_flat_band_trends` | Semantic name derived from the unchanged deduction conclusion and LKM factor role. |
| `strat_gfac_3a3936eff4a1434c` | `derive_full_relaxation_reproduces_flat_band_gaps` | Semantic name derived from the unchanged deduction conclusion and LKM factor role. |
| `gfac_9fc5b7efdef44e14` | `derive_magnetic_bloch_reentrant_flat_bands` | Semantic name derived from the unchanged deduction conclusion and LKM factor role. |
| `strat_gfac_3970f30041424709` | `derive_merged_dirac_magic_angle_flat_band` | Semantic name derived from the unchanged deduction conclusion and LKM factor role. |

## Labels intentionally left unchanged

- `link_*` support operator labels were already semantic and were left unchanged.
- Compiler-generated internal `.gaia` helper labels such as `__conjunction_result_*` and `__implication_result_*` are regenerated by Gaia and were not manually renamed.
- Raw `gcn_*` IDs remain intentionally in `lkm_id`, `lkm_original`, provenance file names, audit logs, raw LKM JSON, and archived subgraph artifacts.
