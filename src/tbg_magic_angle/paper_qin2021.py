"""paper_qin2021 -- critical fields and phonon-mediated pairing in MATBG.

Source: Critical magnetic fields and electron-pairing in magic-angle twisted
bilayer graphene
DOI: 10.48550/arXiv.2102.10504
Reference key: Qin2021
"""

from gaia.lang import claim, deduction


optical_phonons_instantaneous_couplings = claim(
    "In MATBG flat-band models where optical phonon energies are about 196 meV for E_2 modes and about 170 meV for A_1/B_1 modes while the electronic flat-band bandwidth is much smaller than 100 meV, Qin, Zou, and MacDonald treat the electron-optical-phonon interaction as effectively instantaneous and parameterize it by static BCS-like couplings g_0 and g_1 [@Qin2021].",
    lkm_id="gcn_1b0c5250d2574e24",
    source_paper="paper:867761816883691597",
    provenance_source="lkm",
    provenance_file="artifacts/lkm-discovery/input/may4_evidence_gcn_a0ab3201de0e41ad.json",
    lkm_original=r"""In twisted bilayer graphene flat-band models where the relevant in-plane optical phonon mode energies are \hbar\omega_{E_2}\approx196\ \text{meV} and \hbar\omega_{A_1,B_1}\approx170\ \text{meV} while the electronic flat-band bandwidth \mathcal{W} is much smaller than 100\ \text{meV} (typical flat-band widths in the continuum models are a few to a few tens of meV), the electron–optical-phonon-mediated interaction can be treated as effectively instantaneous for mean-field pairing calculations; accordingly retardation effects are neglected and the phonon-induced attraction is represented by static BCS-like interaction parameters g_0 and g_1 that enter the gap equation and parameterize the contributions of the E_2 and A_1/B_1 phonon modes to the effective instantaneous attraction.""",
)

intravalley_coulomb_tuning_parameter = claim(
    "In Qin, Zou, and MacDonald's mean-field BdG modeling of MATBG superconductivity, the short-range intravalley Coulomb repulsion parameter u is treated as a phenomenological tuning parameter in meV nm^2 that can be adjusted to reproduce experimental critical temperatures and represents the principal depairing short-range Coulomb effect in the static interaction tensor [@Qin2021].",
    lkm_id="gcn_4eda4fedb8364912",
    source_paper="paper:867761816883691597",
    provenance_source="lkm",
    provenance_file="artifacts/lkm-discovery/input/may4_evidence_gcn_a0ab3201de0e41ad.json",
    lkm_original=r"""In mean-field Bogoliubov–de Gennes modeling of MATBG superconductivity with optical-phonon-mediated attraction and repulsive Coulomb interactions, the short-range intra-valley Coulomb repulsion strength parameter u (with units of meV·nm^2 in the continuum-model interaction tensor) can be treated as a phenomenological tuning parameter and adjusted to reproduce experimentally observed critical temperatures T_c, even when the tuned value differs from crude microscopic estimates of the screened Coulomb interaction; in this modeling u parametrizes the principal depairing short-range Coulomb effect entering the static interaction tensor V used in the self-consistent gap equation.""",
)

intervalley_scattering_neglect = claim(
    "For Qin, Zou, and MacDonald's MATBG finite-pairing-momentum BdG calculations, intervalley Coulomb scattering matrix elements are neglected relative to intravalley Coulomb repulsion, so the principal depairing Coulomb effect is represented by a single intravalley parameter u in the interaction tensor [@Qin2021].",
    lkm_id="gcn_993c306ad37c4dfb",
    source_paper="paper:867761816883691597",
    provenance_source="lkm",
    provenance_file="artifacts/lkm-discovery/input/may4_evidence_gcn_a0ab3201de0e41ad.json",
    lkm_original=r"""For the purposes of the mean-field finite-pairing-momentum BdG calculations reported for MATBG, Coulomb-scattering processes that change electron valley index (intervalley Coulomb scattering matrix elements) are neglected (taken to be parametrically small compared to intravalley Coulomb repulsion), so that the principal depairing Coulomb effect in the interaction tensor is described by a single intra-valley parameter u; here 'valley' denotes the inequivalent graphene Dirac points and 'intervalley scattering' denotes two-body Coulomb matrix elements that connect states in different valley sectors.""",
)

continuum_vhs_pairing_band_assumption = claim(
    "Qin, Zou, and MacDonald use non-interaction-reconstructed MATBG continuum-model band structures parameterized by twist angle theta and tunneling ratio eta=t_AA/t_AB to represent the flat-band van Hove singularities that determine where phonon-mediated pairing produces maxima of T_c(mu) and minima of extracted average velocity v_F*(mu), while assuming neglected interaction-driven flavor symmetry breaking does not qualitatively change this prediction [@Qin2021].",
    lkm_id="gcn_2bc94d32817142f7",
    source_paper="paper:867761816883691597",
    provenance_source="lkm",
    provenance_file="artifacts/lkm-discovery/input/may4_evidence_gcn_a0ab3201de0e41ad.json",
    lkm_original=r"""The non-interaction-reconstructed continuum-model band structures of MATBG used in the finite-pairing-momentum mean-field calculations, parameterized by twist angle \theta and intersublattice-to-intrasublattice tunneling ratio \eta=t_{\mathrm{AA}}/t_{\mathrm{AB}}, are taken to represent the salient features of the electronic structure relevant for predicting where flat-band van Hove singularities (VHSs) occur in band filling, with the modeling assumption that neglecting possible interaction-driven flavor (spin/valley) symmetry breaking and the associated Fermi-surface reconstructions does not qualitatively change the prediction that phonon-mediated pairing produces maxima of T_c(\mu) and minima of the extracted average velocity v_F^*(\mu) at the VHSs determined from the non-reconstructed continuum-model band structure.""",
)

vhs_tc_velocity_extrema_coincidence = claim(
    "In Qin, Zou, and MacDonald's MATBG calculations, superconducting critical-temperature maxima and minima of extracted average velocity v_F* occur at chemical potentials corresponding to flat-band van Hove singularities, and this coincidence persists across explored variations of eta, theta, and Coulomb depairing strength u when the interaction remains phonon-dominated and not strongly filling-dependent [@Qin2021].",
    lkm_id="gcn_324b385e04254463",
    source_paper="paper:867761816883691597",
    provenance_source="lkm",
    provenance_file="artifacts/lkm-discovery/input/may4_evidence_gcn_a0ab3201de0e41ad.json",
    lkm_original=r"""The coincidence that superconducting critical temperature maxima and minima of the extracted average velocity v_F^* occur at chemical potentials corresponding to flat-band van Hove singularities is a generic feature of phonon-mediated pairing in two-dimensional flat-band continuum-model representations of magic-angle twisted bilayer graphene and persists across the continuum-model parameter variations explored here (variations of \eta, \theta, and Coulomb depairing strength u), provided that the interaction remains phonon-dominated and is not itself strongly dependent on band filling.""",
)

phonon_bdg_vhs_tc_hc2_velocity_extrema = claim(
    "Qin, Zou, and MacDonald's mean-field finite-pairing-momentum BdG calculations for MATBG continuum-model flat bands with optical-phonon attraction and intravalley Coulomb repulsion find that T_c(mu) has dome-like maxima at flat-band van Hove singularities, H_c2(mu) peaks at the same chemical potentials, and extracted v_F*(mu)=k_B T_c(mu)/(hbar q_c(mu)) has V-shaped minima there, robust across the explored ranges eta about 0.7-0.85, theta about 1.07-1.15 degrees, and u about 20-40 meV nm^2 [@Qin2021].",
    lkm_id="gcn_a0ab3201de0e41ad",
    source_paper="paper:867761816883691597",
    provenance_source="lkm",
    provenance_file="artifacts/lkm-discovery/input/may4_evidence_gcn_a0ab3201de0e41ad.json",
    lkm_original=r"""Mean-field finite-pairing-momentum Bogoliubov–de Gennes calculations for magic-angle twisted bilayer graphene continuum-model band structures in which in-plane optical phonons provide an effectively instantaneous electron–electron attraction (parameterized by static coupling strengths g_0 and g_1) that competes with a repulsive intra-valley Coulomb interaction of strength u show the following band-filling dependent relationships: (i) the zero-pairing-momentum critical temperature T_c(\mu) exhibits dome-like maxima that are centered at chemical potentials \mu where the flat-band density-of-states (DOS) has van Hove singularities (VHSs); (ii) the perpendicular upper critical field H_{c2}(\mu), obtained from the microscopic critical pairing wavevector q_c(\mu) via H_{c2}(\mu)=\Phi_s q_c(\mu)^2/(2\pi) with \Phi_s=\pi\hbar c/e, exhibits sharp peaks at the same VHS chemical potentials; and (iii) the extracted average velocity v_F^*(\mu)=k_B T_c(\mu)/[\hbar q_c(\mu)] exhibits V-shaped minima located at those VHS chemical potentials, so that v_F^* minima are coincident with T_c maxima. These relationships are robust across the continuum-model parameter variations explored in the calculations reported here, specifically for intra-valley Coulomb strengths u of order tens of meV·nm^2 (examples shown for u\approx20–40 meV·nm^2), intersublattice-to-intrasublattice tunneling ratios \eta=t_{\mathrm{AA}}/t_{\mathrm{AB}} in the range \sim0.7–0.85, and twist angles \theta near the magic-angle values employed in the numerical studies (\sim1.07^\circ–1.15^\circ).""",
)

derive_phonon_bdg_vhs_tc_hc2_velocity_extrema = deduction(
    [
        optical_phonons_instantaneous_couplings,
        intravalley_coulomb_tuning_parameter,
        intervalley_scattering_neglect,
        continuum_vhs_pairing_band_assumption,
        vhs_tc_velocity_extrema_coincidence,
    ],
    phonon_bdg_vhs_tc_hc2_velocity_extrema,
    reason=(
        "1. Treat the microscopic finite-momentum BdG protocol and GL-form fit "
        "as available for extracting q_c, H_c2, and v_F*.\n"
        "2. Specify optical-phonon-mediated instantaneous attraction g_0,g_1 "
        "competing with intravalley Coulomb repulsion u in the interaction tensor.\n"
        "3. Define T_c(mu) from the q=0 mean-field solution.\n"
        "4. Observe T_c(mu) dome maxima at flat-band VHS chemical potentials.\n"
        "5. Compute H_c2(mu)=Phi_s q_c(mu)^2/(2 pi) and observe peaks at the same VHSs.\n"
        "6. Compute v_F*(mu)=k_B T_c(mu)/(hbar q_c(mu)) and observe V-shaped minima at the VHSs.\n"
        "7. Vary u, eta, and theta and retain the coincidence of T_c maxima, H_c2 peaks, and v_F* minima.\n"
        "8. Conclude that the stated relationships hold within the reported MATBG mean-field model."
    ),
    prior=0.95,
)
