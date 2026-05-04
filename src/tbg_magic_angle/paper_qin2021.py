"""paper_qin2021 -- critical fields and phonon-mediated pairing in MATBG.

Source: Critical magnetic fields and electron-pairing in magic-angle twisted
bilayer graphene
DOI: 10.48550/arXiv.2102.10504
Reference key: Qin2021
"""

from gaia.lang import claim, deduction


gcn_1b0c5250d2574e24 = claim(
    "In MATBG flat-band models where optical phonon energies are about 196 meV for E_2 modes and about 170 meV for A_1/B_1 modes while the electronic flat-band bandwidth is much smaller than 100 meV, Qin, Zou, and MacDonald treat the electron-optical-phonon interaction as effectively instantaneous and parameterize it by static BCS-like couplings g_0 and g_1 [@Qin2021].",
    lkm_id="gcn_1b0c5250d2574e24",
    source_paper="paper:867761816883691597",
    provenance_source="lkm",
    provenance_file="artifacts/lkm-discovery/input/may4_evidence_gcn_a0ab3201de0e41ad.json",
    lkm_original="In twisted bilayer graphene flat-band models where the relevant in-plane optical phonon mode energies are about 196 meV and 170 meV while the electronic flat-band bandwidth is much smaller than 100 meV, the electron-optical-phonon-mediated interaction can be treated as effectively instantaneous for mean-field pairing calculations.",
)

gcn_4eda4fedb8364912 = claim(
    "In Qin, Zou, and MacDonald's mean-field BdG modeling of MATBG superconductivity, the short-range intravalley Coulomb repulsion parameter u is treated as a phenomenological tuning parameter in meV nm^2 that can be adjusted to reproduce experimental critical temperatures and represents the principal depairing short-range Coulomb effect in the static interaction tensor [@Qin2021].",
    lkm_id="gcn_4eda4fedb8364912",
    source_paper="paper:867761816883691597",
    provenance_source="lkm",
    provenance_file="artifacts/lkm-discovery/input/may4_evidence_gcn_a0ab3201de0e41ad.json",
    lkm_original="In mean-field Bogoliubov-de Gennes modeling of MATBG superconductivity with optical-phonon-mediated attraction and repulsive Coulomb interactions, the short-range intra-valley Coulomb repulsion strength parameter u can be treated as a phenomenological tuning parameter.",
)

gcn_993c306ad37c4dfb = claim(
    "For Qin, Zou, and MacDonald's MATBG finite-pairing-momentum BdG calculations, intervalley Coulomb scattering matrix elements are neglected relative to intravalley Coulomb repulsion, so the principal depairing Coulomb effect is represented by a single intravalley parameter u in the interaction tensor [@Qin2021].",
    lkm_id="gcn_993c306ad37c4dfb",
    source_paper="paper:867761816883691597",
    provenance_source="lkm",
    provenance_file="artifacts/lkm-discovery/input/may4_evidence_gcn_a0ab3201de0e41ad.json",
    lkm_original="For the purposes of the mean-field finite-pairing-momentum BdG calculations reported for MATBG, Coulomb-scattering processes that change electron valley index are neglected, so the principal depairing Coulomb effect is described by a single intra-valley parameter u.",
)

gcn_2bc94d32817142f7 = claim(
    "Qin, Zou, and MacDonald use non-interaction-reconstructed MATBG continuum-model band structures parameterized by twist angle theta and tunneling ratio eta=t_AA/t_AB to represent the flat-band van Hove singularities that determine where phonon-mediated pairing produces maxima of T_c(mu) and minima of extracted average velocity v_F*(mu), while assuming neglected interaction-driven flavor symmetry breaking does not qualitatively change this prediction [@Qin2021].",
    lkm_id="gcn_2bc94d32817142f7",
    source_paper="paper:867761816883691597",
    provenance_source="lkm",
    provenance_file="artifacts/lkm-discovery/input/may4_evidence_gcn_a0ab3201de0e41ad.json",
    lkm_original="The non-interaction-reconstructed continuum-model band structures of MATBG used in the finite-pairing-momentum mean-field calculations are taken to represent the salient features relevant for predicting where flat-band van Hove singularities occur in band filling.",
)

gcn_324b385e04254463 = claim(
    "In Qin, Zou, and MacDonald's MATBG calculations, superconducting critical-temperature maxima and minima of extracted average velocity v_F* occur at chemical potentials corresponding to flat-band van Hove singularities, and this coincidence persists across explored variations of eta, theta, and Coulomb depairing strength u when the interaction remains phonon-dominated and not strongly filling-dependent [@Qin2021].",
    lkm_id="gcn_324b385e04254463",
    source_paper="paper:867761816883691597",
    provenance_source="lkm",
    provenance_file="artifacts/lkm-discovery/input/may4_evidence_gcn_a0ab3201de0e41ad.json",
    lkm_original="The coincidence that superconducting critical temperature maxima and minima of the extracted average velocity v_F* occur at chemical potentials corresponding to flat-band van Hove singularities is a generic feature of phonon-mediated pairing in two-dimensional flat-band continuum-model representations of magic-angle twisted bilayer graphene.",
)

gcn_a0ab3201de0e41ad = claim(
    "Qin, Zou, and MacDonald's mean-field finite-pairing-momentum BdG calculations for MATBG continuum-model flat bands with optical-phonon attraction and intravalley Coulomb repulsion find that T_c(mu) has dome-like maxima at flat-band van Hove singularities, H_c2(mu) peaks at the same chemical potentials, and extracted v_F*(mu)=k_B T_c(mu)/(hbar q_c(mu)) has V-shaped minima there, robust across the explored ranges eta about 0.7-0.85, theta about 1.07-1.15 degrees, and u about 20-40 meV nm^2 [@Qin2021].",
    lkm_id="gcn_a0ab3201de0e41ad",
    source_paper="paper:867761816883691597",
    provenance_source="lkm",
    provenance_file="artifacts/lkm-discovery/input/may4_evidence_gcn_a0ab3201de0e41ad.json",
    lkm_original="Mean-field finite-pairing-momentum Bogoliubov-de Gennes calculations for magic-angle twisted bilayer graphene continuum-model band structures show T_c dome maxima, H_c2 peaks, and v_F* minima at flat-band van Hove singularities across the explored parameter ranges.",
)

gfac_8e790c60b9c94313 = deduction(
    [
        gcn_1b0c5250d2574e24,
        gcn_4eda4fedb8364912,
        gcn_993c306ad37c4dfb,
        gcn_2bc94d32817142f7,
        gcn_324b385e04254463,
    ],
    gcn_a0ab3201de0e41ad,
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
