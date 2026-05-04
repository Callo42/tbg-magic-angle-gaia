# tbg-magic-angle-gaia

Gaia knowledge package regenerated from one BM velocity root and connected LKM-backed TBG magic-angle extensions.

## Overview

```mermaid
graph LR
    bm_magic_angle_velocity_suppression["bm_magic_angle_velocity_suppression (1.00)"]:::derived
    wu_velocity_phonon_form_factor["wu_velocity_phonon_form_factor (0.92)"]:::derived
    phonon_resistivity_velocity_enhancement["phonon_resistivity_velocity_enhancement (0.98)"]:::derived
    phonon_bdg_vhs_tc_hc2_velocity_extrema["phonon_bdg_vhs_tc_hc2_velocity_extrema (0.83)"]:::derived
    kohn_sham_magic_angle_flat_bands["kohn_sham_magic_angle_flat_bands (0.87)"]:::derived
    ab_initio_magic_angle_flat_band_likelihood["ab_initio_magic_angle_flat_band_likelihood (0.94)"]:::derived
    relaxation_reproduces_sts_flat_band_trends["relaxation_reproduces_sts_flat_band_trends (0.94)"]:::derived
    full_relaxation_reproduces_flat_band_gaps["full_relaxation_reproduces_flat_band_gaps (0.92)"]:::derived
    magnetic_bloch_reentrant_flat_bands["magnetic_bloch_reentrant_flat_bands (0.93)"]:::derived
    merged_dirac_magic_angle_flat_band["merged_dirac_magic_angle_flat_band (0.93)"]:::derived
    ab_initio_magic_angle_flat_band_likelihood --> full_relaxation_reproduces_flat_band_gaps
    bm_magic_angle_velocity_suppression --> magnetic_bloch_reentrant_flat_bands
    bm_magic_angle_velocity_suppression --> merged_dirac_magic_angle_flat_band
    bm_magic_angle_velocity_suppression --> phonon_resistivity_velocity_enhancement
    full_relaxation_reproduces_flat_band_gaps --> relaxation_reproduces_sts_flat_band_trends
    kohn_sham_magic_angle_flat_bands --> ab_initio_magic_angle_flat_band_likelihood
    kohn_sham_magic_angle_flat_bands --> bm_magic_angle_velocity_suppression
    kohn_sham_magic_angle_flat_bands --> full_relaxation_reproduces_flat_band_gaps
    kohn_sham_magic_angle_flat_bands --> merged_dirac_magic_angle_flat_band
    phonon_resistivity_velocity_enhancement --> phonon_bdg_vhs_tc_hc2_velocity_extrema
    wu_velocity_phonon_form_factor --> bm_magic_angle_velocity_suppression
    wu_velocity_phonon_form_factor --> phonon_bdg_vhs_tc_hc2_velocity_extrema
    wu_velocity_phonon_form_factor --> phonon_resistivity_velocity_enhancement

    classDef setting fill:#f0f0f0,stroke:#999,color:#333
    classDef premise fill:#ddeeff,stroke:#4488bb,color:#333
    classDef derived fill:#ddffdd,stroke:#44bb44,color:#333
    classDef question fill:#fff3dd,stroke:#cc9944,color:#333
    classDef background fill:#f5f5f5,stroke:#bbb,stroke-dasharray: 5 5,color:#333
    classDef orphan fill:#fff,stroke:#ccc,stroke-dasharray: 5 5,color:#333
    classDef external fill:#fff,stroke:#aaa,stroke-dasharray: 3 3,color:#333
    classDef weak fill:#fff9c4,stroke:#f9a825,stroke-dasharray: 5 5,color:#333
    classDef contra fill:#ffebee,stroke:#c62828,color:#333
```

## Introduction

#### bm_magic_angle_velocity_suppression ★

📌 `bm_magic_angle_velocity_suppression`   |   Belief: **1.00**

> For twisted bilayer graphene, the noninteracting low-energy Dirac-point band Fermi velocity v_F*(theta) produced by the Bistritzer-MacDonald continuum moire-band model is strongly suppressed as theta approaches the largest magic angle theta_M where that velocity vanishes; for 0 < theta < 3 degrees it is usefully described by v_F*(theta) ~= 0.5 * |theta - theta_M| * v_F, with v_F about 1e8 cm/s [@DasSarma2020].

🔗 **support**([kohn_sham_magic_angle_flat_bands](#kohn_sham_magic_angle_flat_bands))

<details><summary>Reasoning</summary>

The Uchida et al. LKM chain is an independent Kohn-Sham calculation where the Dirac Fermi velocity vanishes near theta about 1.08 degrees and flat bands emerge. It supports the BM root's velocity-suppression phenomenon while preserving the different method and parameter scope.

</details>


#### wu_velocity_phonon_form_factor ★

📌 `wu_velocity_phonon_form_factor`   |   Belief: **0.92**

> In Wu, Hwang, and Das Sarma's continuum moire Hamiltonian calculation for twisted bilayer graphene, v_F*(theta) is strongly suppressed near theta_magic about 1.025 degrees, and a perturbative moire-wavefunction calculation gives the electron-phonon matrix-element form factor F(theta)=(1+beta^2)/(1+beta)^2 with beta=3(alpha_0^2+alpha_1^2), where alpha_j=w_j/(hbar v_F |kappa_{+1}|) for the AA and AB/BA tunneling parameters [@Wu2018].

🔗 **deduction**([moire_spinor_phonon_form_factor](#moire_spinor_phonon_form_factor), [relaxed_tunneling_magic_angle_velocity](#relaxed_tunneling_magic_angle_velocity))

<details><summary>Reasoning</summary>

1. Define the valley +K moire continuum Hamiltonian as a 4x4 block matrix with layer Dirac Hamiltonians and spatially periodic interlayer tunneling.
2. Define h_l(k) with twist angle theta, monolayer velocity v_F about 10^8 cm/s, and layer-shifted Dirac momenta kappa_l.
3. Expand interlayer tunneling in three moire Fourier components with AA and AB/BA tunneling parameters w_0 and w_1.
4. Use w_0=90 meV and w_1=117 meV, diagonalize the continuum Hamiltonian, and obtain strong v_F*(theta) suppression with a largest magic angle theta_magic about 1.025 degrees.
5. Construct perturbative moire wavefunctions from four layer/momentum components near a moire Dirac point.
6. Define alpha_j=w_j/(hbar v_F |kappa_{+1}|) and beta=3(alpha_0^2+alpha_1^2), which also defines v_F* in the Dirac form of the projected Hamiltonian.
7. Derive F(theta)=(1+beta^2)/(1+beta)^2 as the electron-phonon matrix-element form factor, varying from 0.5 near strong interlayer mixing to 1 for vanishing tunneling.
8. Treat v_F*(theta) and F(theta) as known twist-angle inputs for transport and superconductivity calculations.

</details>


#### phonon_resistivity_velocity_enhancement ★

📌 `phonon_resistivity_velocity_enhancement`   |   Belief: **0.98**

> In Das Sarma and Wu's strange-metallicity model for twisted bilayer graphene, the BM continuum calculation predicts strong v_F* suppression near the magic angle and v_F*/v_F about 1/4 at theta=1.5 degrees; because the phonon-limited resistivity and its temperature coefficient scale as 1/v_F*^2, this velocity reduction implies up to about a 16-fold enhancement of phonon-limited resistivity relative to untwisted monolayer graphene in the small-v_F* regime [@DasSarma2022].

🔗 **support**([bm_magic_angle_velocity_suppression](#bm_magic_angle_velocity_suppression), [wu_velocity_phonon_form_factor](#wu_velocity_phonon_form_factor))

<details><summary>Reasoning</summary>

Both source claims are LKM-backed BM/continuum velocity claims used as low-energy inputs for electron-phonon or transport calculations. They support the strange-metallicity extension's narrower statement that suppressed v_F* enhances phonon-limited resistivity through the stated 1/v_F*^2 scaling.

</details>


#### phonon_bdg_vhs_tc_hc2_velocity_extrema ★

📌 `phonon_bdg_vhs_tc_hc2_velocity_extrema`   |   Belief: **0.83**

> Qin, Zou, and MacDonald's mean-field finite-pairing-momentum BdG calculations for MATBG continuum-model flat bands with optical-phonon attraction and intravalley Coulomb repulsion find that T_c(mu) has dome-like maxima at flat-band van Hove singularities, H_c2(mu) peaks at the same chemical potentials, and extracted v_F*(mu)=k_B T_c(mu)/(hbar q_c(mu)) has V-shaped minima there, robust across the explored ranges eta about 0.7-0.85, theta about 1.07-1.15 degrees, and u about 20-40 meV nm^2 [@Qin2021].

🔗 **support**([wu_velocity_phonon_form_factor](#wu_velocity_phonon_form_factor), [phonon_resistivity_velocity_enhancement](#phonon_resistivity_velocity_enhancement))

<details><summary>Reasoning</summary>

The accepted extensions keep the path within LKM-backed MATBG continuum calculations where v_F* and electron-phonon inputs are used for transport or pairing. This supports the Qin-Zou-MacDonald phonon-mediated BdG extension only as a model-family continuation.

</details>


#### kohn_sham_magic_angle_flat_bands ★

📌 `kohn_sham_magic_angle_flat_bands`   |   Belief: **0.87**

> Uchida et al.'s Kohn-Sham band-structure calculations for twisted bilayer graphene find a magic twist angle theta_M about 1.08 degrees where the Dirac Fermi velocity vanishes; near this angle the low-energy Kohn-Sham bands become extremely flat over most of the Brillouin zone, including nearly dispersionless half-filled bands around E_F and about 10 meV splitting between flat bands at Gamma for theta=0.99 degrees [@Uchida2014].

🔗 **deduction**([small_angle_corrugation_extrapolation](#small_angle_corrugation_extrapolation), [kohn_sham_magic_angle_numerical_scope](#kohn_sham_magic_angle_numerical_scope), [half_filled_flat_band_magnetism_tendency](#half_filled_flat_band_magnetism_tendency))

<details><summary>Reasoning</summary>

1. Start from upstream localization and velocity-reduction results in small-angle corrugated twisted bilayer graphene.
2. Define the magic angle as the twist angle where Kohn-Sham Dirac Fermi velocity v_F=(1/hbar) d epsilon / d k vanishes.
3. Report that theta=0.99 degrees has extremely flat bands near E_F and about 10 meV splitting between the flat bands at Gamma.
4. Extract theta_M about 1.08 degrees from the computed velocity-versus-angle curve.
5. Relate AA-region localization to reduced dispersion and half-filled flat bands.
6. Note consistency with earlier continuum and tight-binding predictions while preserving the different numerical method.

</details>


#### ab_initio_magic_angle_flat_band_likelihood ★

📌 `ab_initio_magic_angle_flat_band_likelihood`   |   Belief: **0.94**

> For 33 unique commensurate twisted bilayer graphene supercells spanning 0.88 degrees <= theta <= 21.79 degrees, Tritsaris et al. 2020 use ab initio Wannier-derived tight-binding calculations and automated flat-band detection to find that the blended flat-band likelihood p(theta) is maximized near theta* approximately 1.1 degrees, where low-dispersion near-flat bands emerge near the Fermi level in the single-particle tight-binding band structures [@Tritsaris2020].

🔗 **support**([kohn_sham_magic_angle_flat_bands](#kohn_sham_magic_angle_flat_bands))

<details><summary>Reasoning</summary>

Both LKM-backed claims are first-principles or ab initio-derived TBG calculations near the first magic angle that report flat or low-dispersion bands. The support is scoped to independent agreement on near-1.1-degree flat-band formation, not equivalence of workflows.

</details>


#### relaxation_reproduces_sts_flat_band_trends ★

📌 `relaxation_reproduces_sts_flat_band_trends`   |   Belief: **0.94**

> In Liu et al.'s continuum-model electronic-structure calculation for magic-angle twisted bilayer graphene, adding atomic-registry-driven lattice relaxation produces reconstructed geometry with enlarged AB/BA regions and reduced AA regions; compared with the rigid unreconstructed calculation, this reconstructed geometry reproduces the key STS spectroscopic trends of broader low-energy flat bands and greater energetic isolation from remote bands, while the calculation omits explicit spatially non-uniform heterostrain and therefore does not reproduce extra flat-band peak splitting, such as three-subpeak structure, observed in some spectra [@Liu2020].

🔗 **support**([full_relaxation_reproduces_flat_band_gaps](#full_relaxation_reproduces_flat_band_gaps))

<details><summary>Reasoning</summary>

The Cantele DFT relaxation chain and the Liu continuum/STS chain both concern magic-angle TBG relaxation effects on flat-band isolation. This supports the Liu extension as a connected relaxation-specific continuation while keeping DFT and continuum/STS scopes distinct.

</details>


#### full_relaxation_reproduces_flat_band_gaps ★

📌 `full_relaxation_reproduces_flat_band_gaps`   |   Belief: **0.92**

> For twisted bilayer graphene at the first magic twist angle $\theta=1.08^\circ$, plane-wave DFT with vdW-DF2 reproduces the near-Fermi narrow flat-band manifold and the $\Gamma$-point gaps to higher and lower bands only when full atomic relaxation includes both in-plane and out-of-plane displacements. In the fully relaxed geometry, the reported flat-band bandwidth is about $20\,\mathrm{meV}$, with upper and lower separation gaps of about $26\,\mathrm{meV}$ and $16\,\mathrm{meV}$, and tight-binding calculations on the same relaxed coordinates give consistent low-energy bands. Unrelaxed flat geometries lack or strongly underestimate these gaps; in-plane-only relaxation gives zero gaps, while out-of-plane-only relaxation gives underestimated gaps of about $2\,\mathrm{meV}$ and $14\,\mathrm{meV}$ [@Cantele2020].

🔗 **support**([kohn_sham_magic_angle_flat_bands](#kohn_sham_magic_angle_flat_bands), [ab_initio_magic_angle_flat_band_likelihood](#ab_initio_magic_angle_flat_band_likelihood))

<details><summary>Reasoning</summary>

The accepted ab initio/Kohn-Sham flat-band claims provide the connected TBG first-magic-angle context for Cantele et al.'s more specific DFT result that full atomic relaxation is required to reproduce the narrow flat-band manifold and gaps at theta=1.08 degrees.

</details>


#### magnetic_bloch_reentrant_flat_bands ★

📌 `magnetic_bloch_reentrant_flat_bands`   |   Belief: **0.93**

> The continuum Bistritzer-MacDonald model of magic-angle twisted bilayer
> graphene, after a layer-dependent momentum shift restores moire periodicity,
> can be represented in a magnetic-translation-irrep Landau-level basis at flux
> $\phi=2\pi$ and diagonalized with a finite Landau-level cutoff; for the BM
> interlayer tunneling parameters studied, this calculation produces two
> low-energy reentrant flat bands per valley and spin separated from passive
> bands by a gap of order 40 meV, with topology controlled by $(w_0,w_1)$:
> physical TBG lies in a crystalline regime with vanishing total Chern number for
> the two flat bands, while the first chiral limit $w_0=0$ lies in a
> Landau-level-type regime where each flat band has Chern number -1
> [@HerzogArbeitman2022].

🔗 **support**([bm_magic_angle_velocity_suppression](#bm_magic_angle_velocity_suppression))

<details><summary>Reasoning</summary>

The magnetic-Bloch extension explicitly starts from the BM continuum model at magic-angle parameters. The BM velocity root supplies the connected zero-field magic-angle BM context, while the extension keeps its flux=2pi and topology conditions separate.

</details>


#### merged_dirac_magic_angle_flat_band ★

📌 `merged_dirac_magic_angle_flat_band`   |   Belief: **0.93**

> In sufficiently small-angle twisted bilayer graphene, where the moire-K gap between the $2n_0$th and $(2n_0+1)$th bands is negligibly small and the upper two bands near charge neutrality are nearly degenerate, Yamada and Hasegawa 2020 propose that three moving Dirac points merge with the fixed K-point Dirac point, producing vanishing Dirac velocity at K; this suppression is conjectured to contribute to extremely narrow nearly flat bands at the magic angles [@Yamada2020].

🔗 **support**([bm_magic_angle_velocity_suppression](#bm_magic_angle_velocity_suppression), [kohn_sham_magic_angle_flat_bands](#kohn_sham_magic_angle_flat_bands))

<details><summary>Reasoning</summary>

The merged-Dirac chain is a conjectural same-system mechanism for vanishing Dirac velocity and near-flat bands at small magic angles. The BM and Kohn-Sham velocity roots support it as a connected mechanistic extension, not as a proved equivalence.

</details>



## paper_dassarma2020 -- LKM claims and deduction from Das Sarma and Wu (2020).

<a id="bm_velocity_linear_fit"></a>

#### bm_velocity_linear_fit

📌 `bm_velocity_linear_fit`   |   Prior: 0.82   |   Belief: **0.89**

> For twisted bilayer graphene in the noninteracting Bistritzer-MacDonald continuum moire-band calculation, with twist angle theta and largest magic angle theta_M measured in degrees and monolayer graphene velocity v_F about 1e8 cm/s, the computed low-energy Dirac-point Fermi velocity v_F*(theta) for 0 < theta < 3 degrees is usefully approximated by v_F*(theta) ~= 0.5 * |theta - theta_M| * v_F [@DasSarma2020].


<a id="bm_velocity_bare_input"></a>

#### bm_velocity_bare_input

📌 `bm_velocity_bare_input`   |   Prior: 0.84   |   Belief: **0.90**

> In twisted bilayer graphene, the Bistritzer-MacDonald continuum moire-band model supplies the noninteracting low-energy band structure, and the Dirac-point band Fermi velocity v_F*(theta) from that model is treated as the bare input velocity for subsequent low-energy many-body and phonon-transport calculations [@DasSarma2020].


<a id="bm_magic_angle_velocity_suppression"></a>

#### bm_magic_angle_velocity_suppression ★

📌 `bm_magic_angle_velocity_suppression`   |   Belief: **1.00**

> For twisted bilayer graphene, the noninteracting low-energy Dirac-point band Fermi velocity v_F*(theta) produced by the Bistritzer-MacDonald continuum moire-band model is strongly suppressed as theta approaches the largest magic angle theta_M where that velocity vanishes; for 0 < theta < 3 degrees it is usefully described by v_F*(theta) ~= 0.5 * |theta - theta_M| * v_F, with v_F about 1e8 cm/s [@DasSarma2020].

🔗 **support**([kohn_sham_magic_angle_flat_bands](#kohn_sham_magic_angle_flat_bands))

<details><summary>Reasoning</summary>

The Uchida et al. LKM chain is an independent Kohn-Sham calculation where the Dirac Fermi velocity vanishes near theta about 1.08 degrees and flat bands emerge. It supports the BM root's velocity-suppression phenomenon while preserving the different method and parameter scope.

</details>


## paper_wu2018 -- continuum velocity and electron-phonon form factor in MATBG.

```mermaid
graph TD
    moire_spinor_phonon_form_factor["moire_spinor_phonon_form_factor (0.81)"]:::premise
    relaxed_tunneling_magic_angle_velocity["relaxed_tunneling_magic_angle_velocity (0.83)"]:::premise
    wu_velocity_phonon_form_factor["wu_velocity_phonon_form_factor (0.92)"]:::derived
    strat_1(["deduction"])
    moire_spinor_phonon_form_factor --> strat_1
    relaxed_tunneling_magic_angle_velocity --> strat_1
    strat_1 --> wu_velocity_phonon_form_factor

    classDef setting fill:#f0f0f0,stroke:#999,color:#333
    classDef premise fill:#ddeeff,stroke:#4488bb,color:#333
    classDef derived fill:#ddffdd,stroke:#44bb44,color:#333
    classDef question fill:#fff3dd,stroke:#cc9944,color:#333
    classDef background fill:#f5f5f5,stroke:#bbb,stroke-dasharray: 5 5,color:#333
    classDef orphan fill:#fff,stroke:#ccc,stroke-dasharray: 5 5,color:#333
    classDef external fill:#fff,stroke:#aaa,stroke-dasharray: 3 3,color:#333
    classDef weak fill:#fff9c4,stroke:#f9a825,stroke-dasharray: 5 5,color:#333
    classDef contra fill:#ffebee,stroke:#c62828,color:#333
```

<a id="moire_spinor_phonon_form_factor"></a>

#### moire_spinor_phonon_form_factor

📌 `moire_spinor_phonon_form_factor`   |   Prior: 0.76   |   Belief: **0.81**

> For a moire Dirac point in twisted bilayer graphene, Wu, Hwang, and Das Sarma construct degenerate Dirac-point eigenstates from four layer/momentum spinors with amplitudes set by alpha_j=w_j/(hbar v_F |kappa_{+1}|), define beta=3(alpha_0^2+alpha_1^2), and approximate the deformation-potential electron-phonon spinor-overlap factor as F(theta)=(1+beta^2)/(1+beta)^2, with 0.5 <= F(theta) <= 1 used as a transport matrix-element correction [@Wu2018].


<a id="relaxed_tunneling_magic_angle_velocity"></a>

#### relaxed_tunneling_magic_angle_velocity

📌 `relaxed_tunneling_magic_angle_velocity`   |   Prior: 0.78   |   Belief: **0.83**

> Using continuum-model interlayer tunneling parameters w_0=90 meV and w_1=117 meV to incorporate atomic-relaxation effects, Wu, Hwang, and Das Sarma obtain a largest magic angle theta_magic about 1.025 degrees and a strongly suppressed twist-angle-dependent Dirac velocity v_F*(theta), while noting sample-dependent relaxation and strain can shift theta_magic and v_F* by order tens of percent [@Wu2018].


<a id="wu_velocity_phonon_form_factor"></a>

#### wu_velocity_phonon_form_factor ★

📌 `wu_velocity_phonon_form_factor`   |   Belief: **0.92**

> In Wu, Hwang, and Das Sarma's continuum moire Hamiltonian calculation for twisted bilayer graphene, v_F*(theta) is strongly suppressed near theta_magic about 1.025 degrees, and a perturbative moire-wavefunction calculation gives the electron-phonon matrix-element form factor F(theta)=(1+beta^2)/(1+beta)^2 with beta=3(alpha_0^2+alpha_1^2), where alpha_j=w_j/(hbar v_F |kappa_{+1}|) for the AA and AB/BA tunneling parameters [@Wu2018].

🔗 **deduction**([moire_spinor_phonon_form_factor](#moire_spinor_phonon_form_factor), [relaxed_tunneling_magic_angle_velocity](#relaxed_tunneling_magic_angle_velocity))

<details><summary>Reasoning</summary>

1. Define the valley +K moire continuum Hamiltonian as a 4x4 block matrix with layer Dirac Hamiltonians and spatially periodic interlayer tunneling.
2. Define h_l(k) with twist angle theta, monolayer velocity v_F about 10^8 cm/s, and layer-shifted Dirac momenta kappa_l.
3. Expand interlayer tunneling in three moire Fourier components with AA and AB/BA tunneling parameters w_0 and w_1.
4. Use w_0=90 meV and w_1=117 meV, diagonalize the continuum Hamiltonian, and obtain strong v_F*(theta) suppression with a largest magic angle theta_magic about 1.025 degrees.
5. Construct perturbative moire wavefunctions from four layer/momentum components near a moire Dirac point.
6. Define alpha_j=w_j/(hbar v_F |kappa_{+1}|) and beta=3(alpha_0^2+alpha_1^2), which also defines v_F* in the Dirac form of the projected Hamiltonian.
7. Derive F(theta)=(1+beta^2)/(1+beta)^2 as the electron-phonon matrix-element form factor, varying from 0.5 near strong interlayer mixing to 1 for vanishing tunneling.
8. Treat v_F*(theta) and F(theta) as known twist-angle inputs for transport and superconductivity calculations.

</details>


## paper_dassarma2022 -- BM velocity suppression and phonon-limited resistivity.

```mermaid
graph TD
    bm_magic_angle_velocity_suppression["bm_magic_angle_velocity_suppression (1.00)"]:::external
    wu_velocity_phonon_form_factor["wu_velocity_phonon_form_factor (0.92)"]:::external
    bm_velocity_suppression_caveated["bm_velocity_suppression_caveated (0.87)"]:::premise
    phonon_resistivity_velocity_enhancement["phonon_resistivity_velocity_enhancement (0.98)"]:::derived
    strat_2(["deduction"])
    bm_velocity_suppression_caveated --> strat_2
    strat_2 --> phonon_resistivity_velocity_enhancement
    strat_10(["support"]):::weak
    wu_velocity_phonon_form_factor --> strat_10
    strat_10 --> bm_magic_angle_velocity_suppression
    strat_11(["support"]):::weak
    bm_magic_angle_velocity_suppression --> strat_11
    wu_velocity_phonon_form_factor --> strat_11
    strat_11 --> phonon_resistivity_velocity_enhancement

    classDef setting fill:#f0f0f0,stroke:#999,color:#333
    classDef premise fill:#ddeeff,stroke:#4488bb,color:#333
    classDef derived fill:#ddffdd,stroke:#44bb44,color:#333
    classDef question fill:#fff3dd,stroke:#cc9944,color:#333
    classDef background fill:#f5f5f5,stroke:#bbb,stroke-dasharray: 5 5,color:#333
    classDef orphan fill:#fff,stroke:#ccc,stroke-dasharray: 5 5,color:#333
    classDef external fill:#fff,stroke:#aaa,stroke-dasharray: 3 3,color:#333
    classDef weak fill:#fff9c4,stroke:#f9a825,stroke-dasharray: 5 5,color:#333
    classDef contra fill:#ffebee,stroke:#c62828,color:#333
```

<a id="bm_velocity_suppression_caveated"></a>

#### bm_velocity_suppression_caveated

📌 `bm_velocity_suppression_caveated`   |   Prior: 0.80   |   Belief: **0.87**

> For twisted bilayer graphene, the Bistritzer-MacDonald continuum moire-band model predicts a moire-band Fermi velocity v_F*(theta) at the moire Dirac points; with standard BM parameters it strongly suppresses v_F* toward zero near a magic twist angle around 1 degree and gives v_F*/v_F about 1/4 at theta=1.5 degrees within the noninteracting continuum approximation without lattice relaxation or many-body self-energy corrections [@DasSarma2022].


<a id="phonon_resistivity_velocity_enhancement"></a>

#### phonon_resistivity_velocity_enhancement ★

📌 `phonon_resistivity_velocity_enhancement`   |   Belief: **0.98**

> In Das Sarma and Wu's strange-metallicity model for twisted bilayer graphene, the BM continuum calculation predicts strong v_F* suppression near the magic angle and v_F*/v_F about 1/4 at theta=1.5 degrees; because the phonon-limited resistivity and its temperature coefficient scale as 1/v_F*^2, this velocity reduction implies up to about a 16-fold enhancement of phonon-limited resistivity relative to untwisted monolayer graphene in the small-v_F* regime [@DasSarma2022].

🔗 **support**([bm_magic_angle_velocity_suppression](#bm_magic_angle_velocity_suppression), [wu_velocity_phonon_form_factor](#wu_velocity_phonon_form_factor))

<details><summary>Reasoning</summary>

Both source claims are LKM-backed BM/continuum velocity claims used as low-energy inputs for electron-phonon or transport calculations. They support the strange-metallicity extension's narrower statement that suppressed v_F* enhances phonon-limited resistivity through the stated 1/v_F*^2 scaling.

</details>


## paper_qin2021 -- critical fields and phonon-mediated pairing in MATBG.

```mermaid
graph TD
    wu_velocity_phonon_form_factor["wu_velocity_phonon_form_factor (0.92)"]:::external
    phonon_resistivity_velocity_enhancement["phonon_resistivity_velocity_enhancement (0.98)"]:::external
    optical_phonons_instantaneous_couplings["optical_phonons_instantaneous_couplings (0.74)"]:::premise
    intravalley_coulomb_tuning_parameter["intravalley_coulomb_tuning_parameter (0.71)"]:::premise
    intervalley_scattering_neglect["intervalley_scattering_neglect (0.76)"]:::premise
    continuum_vhs_pairing_band_assumption["continuum_vhs_pairing_band_assumption (0.73)"]:::premise
    vhs_tc_velocity_extrema_coincidence["vhs_tc_velocity_extrema_coincidence (0.78)"]:::premise
    phonon_bdg_vhs_tc_hc2_velocity_extrema["phonon_bdg_vhs_tc_hc2_velocity_extrema (0.83)"]:::derived
    strat_3(["deduction"])
    optical_phonons_instantaneous_couplings --> strat_3
    intravalley_coulomb_tuning_parameter --> strat_3
    intervalley_scattering_neglect --> strat_3
    continuum_vhs_pairing_band_assumption --> strat_3
    vhs_tc_velocity_extrema_coincidence --> strat_3
    strat_3 --> phonon_bdg_vhs_tc_hc2_velocity_extrema
    strat_11(["support"]):::weak
    wu_velocity_phonon_form_factor --> strat_11
    strat_11 --> phonon_resistivity_velocity_enhancement
    strat_12(["support"]):::weak
    wu_velocity_phonon_form_factor --> strat_12
    phonon_resistivity_velocity_enhancement --> strat_12
    strat_12 --> phonon_bdg_vhs_tc_hc2_velocity_extrema

    classDef setting fill:#f0f0f0,stroke:#999,color:#333
    classDef premise fill:#ddeeff,stroke:#4488bb,color:#333
    classDef derived fill:#ddffdd,stroke:#44bb44,color:#333
    classDef question fill:#fff3dd,stroke:#cc9944,color:#333
    classDef background fill:#f5f5f5,stroke:#bbb,stroke-dasharray: 5 5,color:#333
    classDef orphan fill:#fff,stroke:#ccc,stroke-dasharray: 5 5,color:#333
    classDef external fill:#fff,stroke:#aaa,stroke-dasharray: 3 3,color:#333
    classDef weak fill:#fff9c4,stroke:#f9a825,stroke-dasharray: 5 5,color:#333
    classDef contra fill:#ffebee,stroke:#c62828,color:#333
```

<a id="optical_phonons_instantaneous_couplings"></a>

#### optical_phonons_instantaneous_couplings

📌 `optical_phonons_instantaneous_couplings`   |   Prior: 0.72   |   Belief: **0.74**

> In MATBG flat-band models where optical phonon energies are about 196 meV for E_2 modes and about 170 meV for A_1/B_1 modes while the electronic flat-band bandwidth is much smaller than 100 meV, Qin, Zou, and MacDonald treat the electron-optical-phonon interaction as effectively instantaneous and parameterize it by static BCS-like couplings g_0 and g_1 [@Qin2021].


<a id="intravalley_coulomb_tuning_parameter"></a>

#### intravalley_coulomb_tuning_parameter

📌 `intravalley_coulomb_tuning_parameter`   |   Prior: 0.68   |   Belief: **0.71**

> In Qin, Zou, and MacDonald's mean-field BdG modeling of MATBG superconductivity, the short-range intravalley Coulomb repulsion parameter u is treated as a phenomenological tuning parameter in meV nm^2 that can be adjusted to reproduce experimental critical temperatures and represents the principal depairing short-range Coulomb effect in the static interaction tensor [@Qin2021].


<a id="intervalley_scattering_neglect"></a>

#### intervalley_scattering_neglect

📌 `intervalley_scattering_neglect`   |   Prior: 0.74   |   Belief: **0.76**

> For Qin, Zou, and MacDonald's MATBG finite-pairing-momentum BdG calculations, intervalley Coulomb scattering matrix elements are neglected relative to intravalley Coulomb repulsion, so the principal depairing Coulomb effect is represented by a single intravalley parameter u in the interaction tensor [@Qin2021].


<a id="continuum_vhs_pairing_band_assumption"></a>

#### continuum_vhs_pairing_band_assumption

📌 `continuum_vhs_pairing_band_assumption`   |   Prior: 0.70   |   Belief: **0.73**

> Qin, Zou, and MacDonald use non-interaction-reconstructed MATBG continuum-model band structures parameterized by twist angle theta and tunneling ratio eta=t_AA/t_AB to represent the flat-band van Hove singularities that determine where phonon-mediated pairing produces maxima of T_c(mu) and minima of extracted average velocity v_F*(mu), while assuming neglected interaction-driven flavor symmetry breaking does not qualitatively change this prediction [@Qin2021].


<a id="vhs_tc_velocity_extrema_coincidence"></a>

#### vhs_tc_velocity_extrema_coincidence

📌 `vhs_tc_velocity_extrema_coincidence`   |   Prior: 0.76   |   Belief: **0.78**

> In Qin, Zou, and MacDonald's MATBG calculations, superconducting critical-temperature maxima and minima of extracted average velocity v_F* occur at chemical potentials corresponding to flat-band van Hove singularities, and this coincidence persists across explored variations of eta, theta, and Coulomb depairing strength u when the interaction remains phonon-dominated and not strongly filling-dependent [@Qin2021].


<a id="phonon_bdg_vhs_tc_hc2_velocity_extrema"></a>

#### phonon_bdg_vhs_tc_hc2_velocity_extrema ★

📌 `phonon_bdg_vhs_tc_hc2_velocity_extrema`   |   Belief: **0.83**

> Qin, Zou, and MacDonald's mean-field finite-pairing-momentum BdG calculations for MATBG continuum-model flat bands with optical-phonon attraction and intravalley Coulomb repulsion find that T_c(mu) has dome-like maxima at flat-band van Hove singularities, H_c2(mu) peaks at the same chemical potentials, and extracted v_F*(mu)=k_B T_c(mu)/(hbar q_c(mu)) has V-shaped minima there, robust across the explored ranges eta about 0.7-0.85, theta about 1.07-1.15 degrees, and u about 20-40 meV nm^2 [@Qin2021].

🔗 **support**([wu_velocity_phonon_form_factor](#wu_velocity_phonon_form_factor), [phonon_resistivity_velocity_enhancement](#phonon_resistivity_velocity_enhancement))

<details><summary>Reasoning</summary>

The accepted extensions keep the path within LKM-backed MATBG continuum calculations where v_F* and electron-phonon inputs are used for transport or pairing. This supports the Qin-Zou-MacDonald phonon-mediated BdG extension only as a model-family continuation.

</details>


## paper_uchida2014 -- Kohn-Sham velocity collapse and flat bands in TBG.

```mermaid
graph TD
    small_angle_corrugation_extrapolation["small_angle_corrugation_extrapolation (0.74)"]:::premise
    kohn_sham_magic_angle_numerical_scope["kohn_sham_magic_angle_numerical_scope (0.70)"]:::premise
    half_filled_flat_band_magnetism_tendency["half_filled_flat_band_magnetism_tendency (0.61)"]:::premise
    kohn_sham_magic_angle_flat_bands["kohn_sham_magic_angle_flat_bands (0.87)"]:::derived
    strat_4(["deduction"])
    small_angle_corrugation_extrapolation --> strat_4
    kohn_sham_magic_angle_numerical_scope --> strat_4
    half_filled_flat_band_magnetism_tendency --> strat_4
    strat_4 --> kohn_sham_magic_angle_flat_bands

    classDef setting fill:#f0f0f0,stroke:#999,color:#333
    classDef premise fill:#ddeeff,stroke:#4488bb,color:#333
    classDef derived fill:#ddffdd,stroke:#44bb44,color:#333
    classDef question fill:#fff3dd,stroke:#cc9944,color:#333
    classDef background fill:#f5f5f5,stroke:#bbb,stroke-dasharray: 5 5,color:#333
    classDef orphan fill:#fff,stroke:#ccc,stroke-dasharray: 5 5,color:#333
    classDef external fill:#fff,stroke:#aaa,stroke-dasharray: 3 3,color:#333
    classDef weak fill:#fff9c4,stroke:#f9a825,stroke-dasharray: 5 5,color:#333
    classDef contra fill:#ffebee,stroke:#c62828,color:#333
```

<a id="small_angle_corrugation_extrapolation"></a>

#### small_angle_corrugation_extrapolation

📌 `small_angle_corrugation_extrapolation`   |   Prior: 0.70   |   Belief: **0.74**

> For commensurate twisted bilayer graphene unit cells labeled by integer pairs (N,N-1), Uchida et al. represent out-of-plane corrugation z(r) by a two-dimensional Fourier series, fit dominant coefficients from optimized larger-angle geometries, extrapolate those coefficients for theta<2 degrees, reconstruct z(r), and use the resulting corrugated geometries as inputs for small-angle band-structure calculations near theta=0.99 degrees [@Uchida2014].


<a id="kohn_sham_magic_angle_numerical_scope"></a>

#### kohn_sham_magic_angle_numerical_scope

📌 `kohn_sham_magic_angle_numerical_scope`   |   Prior: 0.66   |   Belief: **0.70**

> In Uchida et al.'s Kohn-Sham calculations for twisted bilayer graphene, the quoted magic angle theta_M about 1.08 degrees is defined by the vanishing Dirac Fermi velocity and depends on extrapolated small-angle atomic geometries, finite real-space grids, chosen pseudopotentials, and the LDA exchange-correlation approximation with limited vdW-DF checks [@Uchida2014].


<a id="half_filled_flat_band_magnetism_tendency"></a>

#### half_filled_flat_band_magnetism_tendency

📌 `half_filled_flat_band_magnetism_tendency`   |   Prior: 0.55   |   Belief: **0.61**

> Uchida et al. interpret half-filled flat Kohn-Sham bands at charge neutrality in twisted bilayer graphene as indicating a possible tendency toward magnetic ordering upon slight twisting, while acknowledging that explicit spin-polarized total-energy comparisons, Hubbard-model analysis, or many-body calculations would be required to establish spontaneous magnetism [@Uchida2014].


<a id="kohn_sham_magic_angle_flat_bands"></a>

#### kohn_sham_magic_angle_flat_bands ★

📌 `kohn_sham_magic_angle_flat_bands`   |   Belief: **0.87**

> Uchida et al.'s Kohn-Sham band-structure calculations for twisted bilayer graphene find a magic twist angle theta_M about 1.08 degrees where the Dirac Fermi velocity vanishes; near this angle the low-energy Kohn-Sham bands become extremely flat over most of the Brillouin zone, including nearly dispersionless half-filled bands around E_F and about 10 meV splitting between flat bands at Gamma for theta=0.99 degrees [@Uchida2014].

🔗 **deduction**([small_angle_corrugation_extrapolation](#small_angle_corrugation_extrapolation), [kohn_sham_magic_angle_numerical_scope](#kohn_sham_magic_angle_numerical_scope), [half_filled_flat_band_magnetism_tendency](#half_filled_flat_band_magnetism_tendency))

<details><summary>Reasoning</summary>

1. Start from upstream localization and velocity-reduction results in small-angle corrugated twisted bilayer graphene.
2. Define the magic angle as the twist angle where Kohn-Sham Dirac Fermi velocity v_F=(1/hbar) d epsilon / d k vanishes.
3. Report that theta=0.99 degrees has extremely flat bands near E_F and about 10 meV splitting between the flat bands at Gamma.
4. Extract theta_M about 1.08 degrees from the computed velocity-versus-angle curve.
5. Relate AA-region localization to reduced dispersion and half-filled flat bands.
6. Note consistency with earlier continuum and tight-binding predictions while preserving the different numerical method.

</details>


## paper_tritsaris2020 -- claims and deduction for Tritsaris et al. 2020.

```mermaid
graph TD
    kohn_sham_magic_angle_flat_bands["kohn_sham_magic_angle_flat_bands (0.87)"]:::external
    ab_initio_tb_flat_band_workflow["ab_initio_tb_flat_band_workflow (0.84)"]:::premise
    flat_band_detector_interpolation["flat_band_detector_interpolation (0.79)"]:::premise
    ab_initio_magic_angle_flat_band_likelihood["ab_initio_magic_angle_flat_band_likelihood (0.94)"]:::derived
    strat_5(["deduction"])
    ab_initio_tb_flat_band_workflow --> strat_5
    flat_band_detector_interpolation --> strat_5
    strat_5 --> ab_initio_magic_angle_flat_band_likelihood
    strat_14(["support"]):::weak
    kohn_sham_magic_angle_flat_bands --> strat_14
    strat_14 --> ab_initio_magic_angle_flat_band_likelihood

    classDef setting fill:#f0f0f0,stroke:#999,color:#333
    classDef premise fill:#ddeeff,stroke:#4488bb,color:#333
    classDef derived fill:#ddffdd,stroke:#44bb44,color:#333
    classDef question fill:#fff3dd,stroke:#cc9944,color:#333
    classDef background fill:#f5f5f5,stroke:#bbb,stroke-dasharray: 5 5,color:#333
    classDef orphan fill:#fff,stroke:#ccc,stroke-dasharray: 5 5,color:#333
    classDef external fill:#fff,stroke:#aaa,stroke-dasharray: 3 3,color:#333
    classDef weak fill:#fff9c4,stroke:#f9a825,stroke-dasharray: 5 5,color:#333
    classDef contra fill:#ffebee,stroke:#c62828,color:#333
```

<a id="ab_initio_tb_flat_band_workflow"></a>

#### ab_initio_tb_flat_band_workflow

📌 `ab_initio_tb_flat_band_workflow`   |   Prior: 0.78   |   Belief: **0.84**

> For commensurate twisted bilayer graphene in the Tritsaris et al. 2020 high-throughput workflow, the selected LKM chain treats as established a Wannier-derived tight-binding Hamiltonian workflow in which band structures are diagonalized with 60 k-points along Gamma-M-K and automated flat-band detectors inspect a 0.30 eV window around the Fermi level [@Tritsaris2020].


<a id="flat_band_detector_interpolation"></a>

#### flat_band_detector_interpolation

📌 `flat_band_detector_interpolation`   |   Prior: 0.72   |   Belief: **0.79**

> For the same Tritsaris et al. 2020 commensurate twisted-bilayer-graphene workflow, the selected LKM chain treats automated low-dispersion-band detections at the sampled commensurate twist angles as inputs that are converted into a continuous flat-band likelihood p(theta) by an interpolation and blending prescription [@Tritsaris2020].


<a id="ab_initio_magic_angle_flat_band_likelihood"></a>

#### ab_initio_magic_angle_flat_band_likelihood ★

📌 `ab_initio_magic_angle_flat_band_likelihood`   |   Belief: **0.94**

> For 33 unique commensurate twisted bilayer graphene supercells spanning 0.88 degrees <= theta <= 21.79 degrees, Tritsaris et al. 2020 use ab initio Wannier-derived tight-binding calculations and automated flat-band detection to find that the blended flat-band likelihood p(theta) is maximized near theta* approximately 1.1 degrees, where low-dispersion near-flat bands emerge near the Fermi level in the single-particle tight-binding band structures [@Tritsaris2020].

🔗 **support**([kohn_sham_magic_angle_flat_bands](#kohn_sham_magic_angle_flat_bands))

<details><summary>Reasoning</summary>

Both LKM-backed claims are first-principles or ab initio-derived TBG calculations near the first magic angle that report flat or low-dispersion bands. The support is scoped to independent agreement on near-1.1-degree flat-band formation, not equivalence of workflows.

</details>


## paper_liu2020 -- LKM claims and deduction from Liu et al. (2020).

```mermaid
graph TD
    relaxation_broadens_isolates_flat_bands["relaxation_broadens_isolates_flat_bands (0.85)"]:::premise
    heterostrain_flat_band_fine_splitting["heterostrain_flat_band_fine_splitting (0.79)"]:::premise
    relaxation_reproduces_sts_flat_band_trends["relaxation_reproduces_sts_flat_band_trends (0.94)"]:::derived
    full_relaxation_reproduces_flat_band_gaps["full_relaxation_reproduces_flat_band_gaps (0.92)"]:::external
    strat_6(["deduction"])
    relaxation_broadens_isolates_flat_bands --> strat_6
    heterostrain_flat_band_fine_splitting --> strat_6
    strat_6 --> relaxation_reproduces_sts_flat_band_trends
    strat_16(["support"]):::weak
    full_relaxation_reproduces_flat_band_gaps --> strat_16
    strat_16 --> relaxation_reproduces_sts_flat_band_trends

    classDef setting fill:#f0f0f0,stroke:#999,color:#333
    classDef premise fill:#ddeeff,stroke:#4488bb,color:#333
    classDef derived fill:#ddffdd,stroke:#44bb44,color:#333
    classDef question fill:#fff3dd,stroke:#cc9944,color:#333
    classDef background fill:#f5f5f5,stroke:#bbb,stroke-dasharray: 5 5,color:#333
    classDef orphan fill:#fff,stroke:#ccc,stroke-dasharray: 5 5,color:#333
    classDef external fill:#fff,stroke:#aaa,stroke-dasharray: 3 3,color:#333
    classDef weak fill:#fff9c4,stroke:#f9a825,stroke-dasharray: 5 5,color:#333
    classDef contra fill:#ffebee,stroke:#c62828,color:#333
```

<a id="relaxation_broadens_isolates_flat_bands"></a>

#### relaxation_broadens_isolates_flat_bands

📌 `relaxation_broadens_isolates_flat_bands`   |   Prior: 0.80   |   Belief: **0.85**

> For Liu et al.'s continuum-model calculations of magic-angle twisted bilayer graphene, the Bistritzer-MacDonald-type moire Hamiltonian is augmented by atomic-registry-dependent interlayer tunneling and a relaxation-derived displacement field that enlarges AB/BA regions and shrinks AA regions; in that reconstructed geometry, the computed low-energy flat-band manifold has larger bandwidth and greater energetic separation from remote bands than in the unreconstructed rigid geometry, with the qualitative trend robust to moderate model-parameter changes even though explicit spatially non-uniform heterostrain is not included [@Liu2020].


<a id="heterostrain_flat_band_fine_splitting"></a>

#### heterostrain_flat_band_fine_splitting

📌 `heterostrain_flat_band_fine_splitting`   |   Prior: 0.72   |   Belief: **0.79**

> For magic-angle twisted bilayer graphene spectra discussed by Liu et al., spatially non-uniform heterostrain means a slowly varying relative in-plane deformation between graphene layers, parameterized by a local strain tensor field epsilon(r) at the moire scale; such heterostrain can reconstruct the electronic band structure and generate additional flat-band density-of-states fine structure, including three-subpeak splitting seen in some STS spectra, but those heterostrain-induced features are not reproduced by continuum-model calculations that include only atomic-registry-driven lattice relaxation [@Liu2020].


<a id="relaxation_reproduces_sts_flat_band_trends"></a>

#### relaxation_reproduces_sts_flat_band_trends ★

📌 `relaxation_reproduces_sts_flat_band_trends`   |   Belief: **0.94**

> In Liu et al.'s continuum-model electronic-structure calculation for magic-angle twisted bilayer graphene, adding atomic-registry-driven lattice relaxation produces reconstructed geometry with enlarged AB/BA regions and reduced AA regions; compared with the rigid unreconstructed calculation, this reconstructed geometry reproduces the key STS spectroscopic trends of broader low-energy flat bands and greater energetic isolation from remote bands, while the calculation omits explicit spatially non-uniform heterostrain and therefore does not reproduce extra flat-band peak splitting, such as three-subpeak structure, observed in some spectra [@Liu2020].

🔗 **support**([full_relaxation_reproduces_flat_band_gaps](#full_relaxation_reproduces_flat_band_gaps))

<details><summary>Reasoning</summary>

The Cantele DFT relaxation chain and the Liu continuum/STS chain both concern magic-angle TBG relaxation effects on flat-band isolation. This supports the Liu extension as a connected relaxation-specific continuation while keeping DFT and continuum/STS scopes distinct.

</details>


## paper_cantele2020 -- claims and deduction for Cantele et al. 2020.

```mermaid
graph TD
    kohn_sham_magic_angle_flat_bands["kohn_sham_magic_angle_flat_bands (0.87)"]:::external
    ab_initio_magic_angle_flat_band_likelihood["ab_initio_magic_angle_flat_band_likelihood (0.94)"]:::external
    dft_gap_spectroscopy_comparison_assumption["dft_gap_spectroscopy_comparison_assumption (0.70)"]:::premise
    relaxation_component_diagnostic_assumption["relaxation_component_diagnostic_assumption (0.76)"]:::premise
    full_relaxation_reproduces_flat_band_gaps["full_relaxation_reproduces_flat_band_gaps (0.92)"]:::derived
    strat_7(["deduction"])
    dft_gap_spectroscopy_comparison_assumption --> strat_7
    relaxation_component_diagnostic_assumption --> strat_7
    strat_7 --> full_relaxation_reproduces_flat_band_gaps
    strat_14(["support"]):::weak
    kohn_sham_magic_angle_flat_bands --> strat_14
    strat_14 --> ab_initio_magic_angle_flat_band_likelihood
    strat_15(["support"]):::weak
    kohn_sham_magic_angle_flat_bands --> strat_15
    ab_initio_magic_angle_flat_band_likelihood --> strat_15
    strat_15 --> full_relaxation_reproduces_flat_band_gaps

    classDef setting fill:#f0f0f0,stroke:#999,color:#333
    classDef premise fill:#ddeeff,stroke:#4488bb,color:#333
    classDef derived fill:#ddffdd,stroke:#44bb44,color:#333
    classDef question fill:#fff3dd,stroke:#cc9944,color:#333
    classDef background fill:#f5f5f5,stroke:#bbb,stroke-dasharray: 5 5,color:#333
    classDef orphan fill:#fff,stroke:#ccc,stroke-dasharray: 5 5,color:#333
    classDef external fill:#fff,stroke:#aaa,stroke-dasharray: 3 3,color:#333
    classDef weak fill:#fff9c4,stroke:#f9a825,stroke-dasharray: 5 5,color:#333
    classDef contra fill:#ffebee,stroke:#c62828,color:#333
```

<a id="dft_gap_spectroscopy_comparison_assumption"></a>

#### dft_gap_spectroscopy_comparison_assumption

📌 `dft_gap_spectroscopy_comparison_assumption`   |   Prior: 0.62   |   Belief: **0.70**

> For first-magic-angle twisted bilayer graphene, comparing plane-wave DFT Kohn-Sham gaps computed with the vdW-DF2 exchange-correlation functional against spectroscopic gaps assumes that electron-electron correlation and quasiparticle self-energy corrections do not substantially renormalize the relevant gap magnitudes, so DFT gaps of about $26\,\mathrm{meV}$ and $16\,\mathrm{meV}$ can be quantitatively compared to nano-ARPES or tunneling spectroscopy in the same energy window [@Cantele2020].


<a id="relaxation_component_diagnostic_assumption"></a>

#### relaxation_component_diagnostic_assumption

📌 `relaxation_component_diagnostic_assumption`   |   Prior: 0.70   |   Belief: **0.76**

> For twisted bilayer graphene at $\theta=1.08^\circ$, using two constrained optimizations--out-of-plane-only relaxation with fixed in-plane coordinates and in-plane-only relaxation with fixed z coordinates--is treated as a meaningful diagnostic separation of the electronic effects of the two relaxation components, while retaining the caveat that the fully relaxed structure may couple in-plane and out-of-plane degrees of freedom nonlinearly [@Cantele2020].


<a id="full_relaxation_reproduces_flat_band_gaps"></a>

#### full_relaxation_reproduces_flat_band_gaps ★

📌 `full_relaxation_reproduces_flat_band_gaps`   |   Belief: **0.92**

> For twisted bilayer graphene at the first magic twist angle $\theta=1.08^\circ$, plane-wave DFT with vdW-DF2 reproduces the near-Fermi narrow flat-band manifold and the $\Gamma$-point gaps to higher and lower bands only when full atomic relaxation includes both in-plane and out-of-plane displacements. In the fully relaxed geometry, the reported flat-band bandwidth is about $20\,\mathrm{meV}$, with upper and lower separation gaps of about $26\,\mathrm{meV}$ and $16\,\mathrm{meV}$, and tight-binding calculations on the same relaxed coordinates give consistent low-energy bands. Unrelaxed flat geometries lack or strongly underestimate these gaps; in-plane-only relaxation gives zero gaps, while out-of-plane-only relaxation gives underestimated gaps of about $2\,\mathrm{meV}$ and $14\,\mathrm{meV}$ [@Cantele2020].

🔗 **support**([kohn_sham_magic_angle_flat_bands](#kohn_sham_magic_angle_flat_bands), [ab_initio_magic_angle_flat_band_likelihood](#ab_initio_magic_angle_flat_band_likelihood))

<details><summary>Reasoning</summary>

The accepted ab initio/Kohn-Sham flat-band claims provide the connected TBG first-magic-angle context for Cantele et al.'s more specific DFT result that full atomic relaxation is required to reproduce the narrow flat-band manifold and gaps at theta=1.08 degrees.

</details>


## Claims and deduction from Herzog-Arbeitman, Chew, and Bernevig (2022).

```mermaid
graph TD
    bm_magic_angle_velocity_suppression["bm_magic_angle_velocity_suppression (1.00)"]:::external
    magnetic_bloch_cutoff_convergence["magnetic_bloch_cutoff_convergence (0.80)"]:::premise
    reentrant_flat_band_parameter_convergence["reentrant_flat_band_parameter_convergence (0.76)"]:::premise
    magnetic_bloch_reentrant_flat_bands["magnetic_bloch_reentrant_flat_bands (0.93)"]:::derived
    strat_8(["deduction"])
    magnetic_bloch_cutoff_convergence --> strat_8
    reentrant_flat_band_parameter_convergence --> strat_8
    strat_8 --> magnetic_bloch_reentrant_flat_bands
    strat_17(["support"]):::weak
    bm_magic_angle_velocity_suppression --> strat_17
    strat_17 --> magnetic_bloch_reentrant_flat_bands

    classDef setting fill:#f0f0f0,stroke:#999,color:#333
    classDef premise fill:#ddeeff,stroke:#4488bb,color:#333
    classDef derived fill:#ddffdd,stroke:#44bb44,color:#333
    classDef question fill:#fff3dd,stroke:#cc9944,color:#333
    classDef background fill:#f5f5f5,stroke:#bbb,stroke-dasharray: 5 5,color:#333
    classDef orphan fill:#fff,stroke:#ccc,stroke-dasharray: 5 5,color:#333
    classDef external fill:#fff,stroke:#aaa,stroke-dasharray: 3 3,color:#333
    classDef weak fill:#fff9c4,stroke:#f9a825,stroke-dasharray: 5 5,color:#333
    classDef contra fill:#ffebee,stroke:#c62828,color:#333
```

<a id="magnetic_bloch_cutoff_convergence"></a>

#### magnetic_bloch_cutoff_convergence

📌 `magnetic_bloch_cutoff_convergence`   |   Prior: 0.74   |   Belief: **0.80**

> For the Bistritzer-MacDonald magnetic Bloch Hamiltonian
> $H^{\phi=2\pi}(\mathbf{k})$ of twisted bilayer graphene represented in the
> Landau-level basis $|\mathbf{k},n\rangle$, the numerical procedure truncates
> the basis to $n \le n_{\max}$, diagonalizes the resulting finite Hermitian
> matrix at sampled $\mathbf{k}$ points, and assumes that for the magic-angle BM
> parameters and flux $\phi=2\pi$ a numerically accessible cutoff makes the
> low-energy flat-band eigenvalues and topological diagnostics converge within
> quoted tolerances such as energy errors of order 1 meV [@HerzogArbeitman2022].


<a id="reentrant_flat_band_parameter_convergence"></a>

#### reentrant_flat_band_parameter_convergence

📌 `reentrant_flat_band_parameter_convergence`   |   Prior: 0.68   |   Belief: **0.76**

> For the BM magnetic Bloch Hamiltonian
> $H_{BM}^{\phi}(\mathbf{k};w_0,w_1)$ of magic-angle twisted bilayer graphene at
> flux $\phi=2\pi$, truncated in Landau levels and diagonalized across sampled
> interlayer parameters $(w_0,w_1)$, the observed reentrant two flat bands, their
> approximately 40 meV gap to passive bands, and the topology assignments
> separating a crystalline regime from a Landau-level regime are interpreted as
> physical parameter dependence only after convergence in Landau-level cutoff,
> $\mathbf{k}$ mesh, and parameter-grid refinement, subject to the stated BM-model
> approximations [@HerzogArbeitman2022].


<a id="magnetic_bloch_reentrant_flat_bands"></a>

#### magnetic_bloch_reentrant_flat_bands ★

📌 `magnetic_bloch_reentrant_flat_bands`   |   Belief: **0.93**

> The continuum Bistritzer-MacDonald model of magic-angle twisted bilayer
> graphene, after a layer-dependent momentum shift restores moire periodicity,
> can be represented in a magnetic-translation-irrep Landau-level basis at flux
> $\phi=2\pi$ and diagonalized with a finite Landau-level cutoff; for the BM
> interlayer tunneling parameters studied, this calculation produces two
> low-energy reentrant flat bands per valley and spin separated from passive
> bands by a gap of order 40 meV, with topology controlled by $(w_0,w_1)$:
> physical TBG lies in a crystalline regime with vanishing total Chern number for
> the two flat bands, while the first chiral limit $w_0=0$ lies in a
> Landau-level-type regime where each flat band has Chern number -1
> [@HerzogArbeitman2022].

🔗 **support**([bm_magic_angle_velocity_suppression](#bm_magic_angle_velocity_suppression))

<details><summary>Reasoning</summary>

The magnetic-Bloch extension explicitly starts from the BM continuum model at magic-angle parameters. The BM velocity root supplies the connected zero-field magic-angle BM context, while the extension keeps its flux=2pi and topology conditions separate.

</details>


## paper_yamada2020 -- merged-Dirac-point mechanism in twisted bilayer graphene.

```mermaid
graph TD
    bm_magic_angle_velocity_suppression["bm_magic_angle_velocity_suppression (1.00)"]:::external
    kohn_sham_magic_angle_flat_bands["kohn_sham_magic_angle_flat_bands (0.87)"]:::external
    small_angle_dirac_merging_conjecture["small_angle_dirac_merging_conjecture (0.73)"]:::premise
    merged_dirac_magic_angle_flat_band["merged_dirac_magic_angle_flat_band (0.93)"]:::derived
    strat_9(["deduction"])
    small_angle_dirac_merging_conjecture --> strat_9
    strat_9 --> merged_dirac_magic_angle_flat_band
    strat_13(["support"]):::weak
    kohn_sham_magic_angle_flat_bands --> strat_13
    strat_13 --> bm_magic_angle_velocity_suppression
    strat_18(["support"]):::weak
    bm_magic_angle_velocity_suppression --> strat_18
    kohn_sham_magic_angle_flat_bands --> strat_18
    strat_18 --> merged_dirac_magic_angle_flat_band

    classDef setting fill:#f0f0f0,stroke:#999,color:#333
    classDef premise fill:#ddeeff,stroke:#4488bb,color:#333
    classDef derived fill:#ddffdd,stroke:#44bb44,color:#333
    classDef question fill:#fff3dd,stroke:#cc9944,color:#333
    classDef background fill:#f5f5f5,stroke:#bbb,stroke-dasharray: 5 5,color:#333
    classDef orphan fill:#fff,stroke:#ccc,stroke-dasharray: 5 5,color:#333
    classDef external fill:#fff,stroke:#aaa,stroke-dasharray: 3 3,color:#333
    classDef weak fill:#fff9c4,stroke:#f9a825,stroke-dasharray: 5 5,color:#333
    classDef contra fill:#ffebee,stroke:#c62828,color:#333
```

<a id="small_angle_dirac_merging_conjecture"></a>

#### small_angle_dirac_merging_conjecture

📌 `small_angle_dirac_merging_conjecture`   |   Prior: 0.64   |   Belief: **0.73**

> For twisted bilayer graphene in the small-angle continuum limit considered by Yamada and Hasegawa 2020, the K-K' intervalley gap at moire K is treated as negligibly small, the upper two bands near charge neutrality are nearly degenerate, and the four-Dirac-point merging mechanism seen in commensurate tight-binding calculations at moderate twist angles is conjectured to persist continuously to magic-angle conditions, assuming no intervening topological or symmetry reconstruction and no qualitative change from lattice relaxation or electron-electron interactions [@Yamada2020].


<a id="merged_dirac_magic_angle_flat_band"></a>

#### merged_dirac_magic_angle_flat_band ★

📌 `merged_dirac_magic_angle_flat_band`   |   Belief: **0.93**

> In sufficiently small-angle twisted bilayer graphene, where the moire-K gap between the $2n_0$th and $(2n_0+1)$th bands is negligibly small and the upper two bands near charge neutrality are nearly degenerate, Yamada and Hasegawa 2020 propose that three moving Dirac points merge with the fixed K-point Dirac point, producing vanishing Dirac velocity at K; this suppression is conjectured to contribute to extremely narrow nearly flat bands at the magic angles [@Yamada2020].

🔗 **support**([bm_magic_angle_velocity_suppression](#bm_magic_angle_velocity_suppression), [kohn_sham_magic_angle_flat_bands](#kohn_sham_magic_angle_flat_bands))

<details><summary>Reasoning</summary>

The merged-Dirac chain is a conjectural same-system mechanism for vanishing Dirac velocity and near-flat bands at small magic angles. The BM and Kohn-Sham velocity roots support it as a connected mechanistic extension, not as a proved equivalence.

</details>


## Inference Results

**BP converged:** True (2 iterations)

| Label | Type | Prior | Belief | Role |
|-------|------|-------|--------|------|
| [half_filled_flat_band_magnetism_tendency](#half_filled_flat_band_magnetism_tendency) | claim | 0.55 | 0.6084 | independent |
| [dft_gap_spectroscopy_comparison_assumption](#dft_gap_spectroscopy_comparison_assumption) | claim | 0.62 | 0.6994 | independent |
| [kohn_sham_magic_angle_numerical_scope](#kohn_sham_magic_angle_numerical_scope) | claim | 0.66 | 0.7041 | independent |
| [intravalley_coulomb_tuning_parameter](#intravalley_coulomb_tuning_parameter) | claim | 0.68 | 0.7084 | independent |
| [small_angle_dirac_merging_conjecture](#small_angle_dirac_merging_conjecture) | claim | 0.64 | 0.7257 | independent |
| [continuum_vhs_pairing_band_assumption](#continuum_vhs_pairing_band_assumption) | claim | 0.70 | 0.7266 | independent |
| [small_angle_corrugation_extrapolation](#small_angle_corrugation_extrapolation) | claim | 0.70 | 0.7389 | independent |
| [optical_phonons_instantaneous_couplings](#optical_phonons_instantaneous_couplings) | claim | 0.72 | 0.7449 | independent |
| [reentrant_flat_band_parameter_convergence](#reentrant_flat_band_parameter_convergence) | claim | 0.68 | 0.7560 | independent |
| [relaxation_component_diagnostic_assumption](#relaxation_component_diagnostic_assumption) | claim | 0.70 | 0.7627 | independent |
| [intervalley_scattering_neglect](#intervalley_scattering_neglect) | claim | 0.74 | 0.7631 | independent |
| [vhs_tc_velocity_extrema_coincidence](#vhs_tc_velocity_extrema_coincidence) | claim | 0.76 | 0.7813 | independent |
| [heterostrain_flat_band_fine_splitting](#heterostrain_flat_band_fine_splitting) | claim | 0.72 | 0.7908 | independent |
| [flat_band_detector_interpolation](#flat_band_detector_interpolation) | claim | 0.72 | 0.7911 | independent |
| [magnetic_bloch_cutoff_convergence](#magnetic_bloch_cutoff_convergence) | claim | 0.74 | 0.8017 | independent |
| [moire_spinor_phonon_form_factor](#moire_spinor_phonon_form_factor) | claim | 0.76 | 0.8135 | independent |
| [phonon_bdg_vhs_tc_hc2_velocity_extrema](#phonon_bdg_vhs_tc_hc2_velocity_extrema) | claim | — | 0.8268 | derived |
| [relaxed_tunneling_magic_angle_velocity](#relaxed_tunneling_magic_angle_velocity) | claim | 0.78 | 0.8290 | independent |
| [ab_initio_tb_flat_band_workflow](#ab_initio_tb_flat_band_workflow) | claim | 0.78 | 0.8358 | independent |
| [relaxation_broadens_isolates_flat_bands](#relaxation_broadens_isolates_flat_bands) | claim | 0.80 | 0.8506 | independent |
| [bm_velocity_suppression_caveated](#bm_velocity_suppression_caveated) | claim | 0.80 | 0.8690 | independent |
| [kohn_sham_magic_angle_flat_bands](#kohn_sham_magic_angle_flat_bands) | claim | — | 0.8749 | derived |
| [bm_velocity_linear_fit](#bm_velocity_linear_fit) | claim | 0.82 | 0.8889 | independent |
| [bm_velocity_bare_input](#bm_velocity_bare_input) | claim | 0.84 | 0.9013 | independent |
| [wu_velocity_phonon_form_factor](#wu_velocity_phonon_form_factor) | claim | — | 0.9169 | derived |
| [full_relaxation_reproduces_flat_band_gaps](#full_relaxation_reproduces_flat_band_gaps) | claim | — | 0.9172 | derived |
| [merged_dirac_magic_angle_flat_band](#merged_dirac_magic_angle_flat_band) | claim | — | 0.9273 | derived |
| [magnetic_bloch_reentrant_flat_bands](#magnetic_bloch_reentrant_flat_bands) | claim | — | 0.9311 | derived |
| [relaxation_reproduces_sts_flat_band_trends](#relaxation_reproduces_sts_flat_band_trends) | claim | — | 0.9358 | derived |
| [ab_initio_magic_angle_flat_band_likelihood](#ab_initio_magic_angle_flat_band_likelihood) | claim | — | 0.9373 | derived |
| [phonon_resistivity_velocity_enhancement](#phonon_resistivity_velocity_enhancement) | claim | — | 0.9758 | derived |
| [bm_magic_angle_velocity_suppression](#bm_magic_angle_velocity_suppression) | claim | — | 0.9950 | derived |
