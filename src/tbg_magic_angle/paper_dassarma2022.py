"""paper_dassarma2022 -- BM velocity suppression and phonon-limited resistivity.

Source: Strange metallicity of moire twisted bilayer graphene
DOI: 10.48550/arXiv.2201.10270
Reference key: DasSarma2022
"""

from gaia.lang import claim, deduction


bm_velocity_suppression_caveated = claim(
    "For twisted bilayer graphene, the Bistritzer-MacDonald continuum moire-band model predicts a moire-band Fermi velocity v_F*(theta) at the moire Dirac points; with standard BM parameters it strongly suppresses v_F* toward zero near a magic twist angle around 1 degree and gives v_F*/v_F about 1/4 at theta=1.5 degrees within the noninteracting continuum approximation without lattice relaxation or many-body self-energy corrections [@DasSarma2022].",
    lkm_id="gcn_1cb7675d5185405d",
    source_paper="paper:867747792313909990",
    provenance_source="lkm",
    provenance_file="artifacts/lkm-discovery/input/may4_evidence_gcn_feace4c9a0154885.json",
    lkm_original=r"""The Bistritzer–MacDonald (BM) continuum moiré-band model is defined as the continuum two-layer Dirac Hamiltonian with interlayer tunneling parameters $w_{0},w_{1}$ and monolayer Dirac velocity $v_{F}$ and predicts a moiré-band Fermi velocity $v_{F}^{*}(\theta)$ at the moiré Dirac points as a function of twist angle $\theta$; with standard BM parameter choices the model yields a strong suppression of $v_{F}^{*}$ approaching zero at a 'magic' twist angle near $1^\circ$ and gives $v_{F}^{*}/v_{F}\approx 1/4$ at $\theta=1.5^\circ$ within the noninteracting continuum approximation, this prediction referring to the single-particle moiré band velocity in the absence of lattice relaxation or many-body self-energy corrections.
      R. Bistritzer and A. H. MacDonald, Proc. Natl. Acad. Sci. U.S.A. 108, 12233 (2011)""",
)

phonon_resistivity_velocity_enhancement = claim(
    "In Das Sarma and Wu's strange-metallicity model for twisted bilayer graphene, the BM continuum calculation predicts strong v_F* suppression near the magic angle and v_F*/v_F about 1/4 at theta=1.5 degrees; because the phonon-limited resistivity and its temperature coefficient scale as 1/v_F*^2, this velocity reduction implies up to about a 16-fold enhancement of phonon-limited resistivity relative to untwisted monolayer graphene in the small-v_F* regime [@DasSarma2022].",
    lkm_id="gcn_feace4c9a0154885",
    source_paper="paper:867747792313909990",
    provenance_source="lkm",
    provenance_file="artifacts/lkm-discovery/input/may4_evidence_gcn_feace4c9a0154885.json",
    lkm_original=r"""The Bistritzer–MacDonald (BM) continuum moiré-band calculation, implemented as the two-layer continuum Dirac Hamiltonian with standard interlayer tunneling parameters and monolayer Dirac velocity $v_{F}$, predicts a strong suppression of the moiré-band Fermi velocity $v_{F}^{*}$ as the twist angle $\theta$ approaches the magic angle near $1^\circ$, with $v_{F}^{*}/v_{F}\to0$ at the magic angle and with a numerical value $v_{F}^{*}/v_{F}\approx 1/4$ at $\theta=1.5^\circ$ within the noninteracting BM model without lattice relaxation; since phonon-limited resistivity and its temperature coefficient scale as $1/v_{F}^{*2}$, this suppression implies up to $\sim 16$-fold enhancement of phonon-limited resistivity relative to untwisted monolayer graphene when $v_{F}^{*}$ is reduced into the small-$v_{F}^{*}$ regime.""",
)

derive_phonon_resistivity_velocity_enhancement = deduction(
    [bm_velocity_suppression_caveated],
    phonon_resistivity_velocity_enhancement,
    reason=(
        "1. Adopt the Bistritzer-MacDonald moire-band model for TBG and define "
        "v_F as the monolayer Dirac velocity and v_F* as the moire-band Dirac "
        "velocity.\n"
        "2. Compute v_F* as a function of twist angle and observe strong "
        "suppression as theta approaches the magic angle near 1 degree, with "
        "v_F*/v_F tending to zero at the BM magic angle.\n"
        "3. Extract the numerical BM-model statement v_F*/v_F approximately "
        "1/4 at theta=1.5 degrees.\n"
        "4. Use the 1/v_F*^2 dependence in the phonon-resistivity formula to "
        "infer up to roughly 16-fold enhancement of phonon-limited resistivity "
        "and its temperature coefficient when v_F* is reduced to this value."
    ),
    prior=0.95,
)
