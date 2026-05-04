"""paper_dassarma2022 -- BM velocity suppression and phonon-limited resistivity.

Source: Strange metallicity of moire twisted bilayer graphene
DOI: 10.48550/arXiv.2201.10270
Reference key: DasSarma2022
"""

from gaia.lang import claim, deduction


gcn_1cb7675d5185405d = claim(
    "For twisted bilayer graphene, the Bistritzer-MacDonald continuum moire-band model predicts a moire-band Fermi velocity v_F*(theta) at the moire Dirac points; with standard BM parameters it strongly suppresses v_F* toward zero near a magic twist angle around 1 degree and gives v_F*/v_F about 1/4 at theta=1.5 degrees within the noninteracting continuum approximation without lattice relaxation or many-body self-energy corrections [@DasSarma2022].",
    lkm_id="gcn_1cb7675d5185405d",
    source_paper="paper:867747792313909990",
    provenance_source="lkm",
    provenance_file="artifacts/lkm-discovery/input/may4_evidence_gcn_feace4c9a0154885.json",
    lkm_original="The Bistritzer-MacDonald (BM) continuum moire-band model is defined as the continuum two-layer Dirac Hamiltonian with interlayer tunneling parameters w_0,w_1 and monolayer Dirac velocity v_F and predicts a moire-band Fermi velocity v_F*(theta) at the moire Dirac points as a function of twist angle theta.",
)

gcn_feace4c9a0154885 = claim(
    "In Das Sarma and Wu's strange-metallicity model for twisted bilayer graphene, the BM continuum calculation predicts strong v_F* suppression near the magic angle and v_F*/v_F about 1/4 at theta=1.5 degrees; because the phonon-limited resistivity and its temperature coefficient scale as 1/v_F*^2, this velocity reduction implies up to about a 16-fold enhancement of phonon-limited resistivity relative to untwisted monolayer graphene in the small-v_F* regime [@DasSarma2022].",
    lkm_id="gcn_feace4c9a0154885",
    source_paper="paper:867747792313909990",
    provenance_source="lkm",
    provenance_file="artifacts/lkm-discovery/input/may4_evidence_gcn_feace4c9a0154885.json",
    lkm_original="The Bistritzer-MacDonald (BM) continuum moire-band calculation predicts a strong suppression of the moire-band Fermi velocity v_F* as theta approaches the magic angle near 1 degree, with v_F*/v_F approximately 1/4 at theta=1.5 degrees; since phonon-limited resistivity and its temperature coefficient scale as 1/v_F*^2, this suppression implies up to about 16-fold enhancement.",
)

gfac_80bf41b7112e4d20 = deduction(
    [gcn_1cb7675d5185405d],
    gcn_feace4c9a0154885,
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
