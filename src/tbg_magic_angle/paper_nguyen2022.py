"""paper_nguyen2022 -- claims and deductions from Nguyen et al. 2022.

Source: Electronic properties of twisted multilayer graphene
DOI: 10.48550/arXiv.2203.09188
Authors: V. Hung Nguyen | Trinh X. Hoang | J.-C. Charlier
Reference key (CSL): Nguyen2022
"""

from gaia.lang import claim, deduction, support


_PREMISE_ORIGINAL = "Define the SM-(AB)$_2$ system as a graphene monolayer twisted by angle $\\\\theta$ placed atop an AB-stacked bilayer substrate. Define the layer-decomposed density of states $\\\\rho_{\\\\ell}(E)=\\\\sum_{i\\\\in\\\\ell}\\\\langle i|\\\\delta(E-H)|i\\\\rangle$, where the sum runs over atomic orbitals on layer $\\\\ell$ and $H$ is the single-particle tight-binding Hamiltonian. The computed result at the magic-angle moiré geometry is that the low-energy flat-band eigenstates produce a strong peak in $\\\\rho_{\\\\mathrm{top}}(E\\\\approx0)$ (indicating spatial localization on the twisted monolayer top layer) while $\\\\rho_{\\\\mathrm{bottom\\\\ bilayer}}(E\\\\approx0)$ is comparatively broadened (indicating delocalization across the bilayer); i.e., the flat-band spectral weight in SM-(AB)$_2$ is layer-polarized and shows coexisting localized and delocalized character across layers.\n      [73][74]"

_ROOT_ORIGINAL = "For the twisted monolayer–bilayer geometry defined as a graphene monolayer rotated by angle $\\\\theta$ and placed on top of an AB-stacked graphene bilayer (denoted SM-(AB)$_2$), the moiré system at its magic-angle moiré geometry (near $\\\\theta\\\\simeq1.1^{\\\\circ}$) exhibits isolated low-energy flat bands, but these flat bands are quantitatively less flat than those of relaxed twisted bilayer graphene: the SM-(AB)$_2$ flat-band manifold has larger bandwidth and a smaller zero-energy DOS peak than magic-angle TBLG. Layer-resolved density of states $\\\\rho_{\\\\ell}(E)$ shows that the flat-band spectral weight is strongly localized on the twisted monolayer (top layer) while it is comparatively broadened and delocalized across the AB bilayer (the two bottom layers), producing a spatially separated localized–delocalized electronic character across layers."


gcn_42c7afbd_smab2_layer_resolved_dos = claim(
    r"""In Nguyen et al.'s relaxed-geometry Slater-Koster p_z tight-binding calculation for SM-(AB)_2, defined as a graphene monolayer twisted by angle theta on an AB-stacked bilayer, the layer-decomposed density of states rho_l(E) at the magic-angle moire geometry shows a strong near-zero-energy flat-band peak on the twisted top monolayer and comparatively broadened near-zero-energy spectral weight across the two bottom bilayer layers; this indicates layer-polarized flat-band spectral weight with coexisting localized and delocalized character across layers [@Nguyen2022].""",
    lkm_id="gcn_42c7afbd21b5483d",
    source_paper="paper:867761060289970778",
    provenance_source="lkm",
    lkm_original=_PREMISE_ORIGINAL,
)


gcn_14a55aff_smab2_flat_band_localization = claim(
    r"""For Nguyen et al.'s SM-(AB)_2 twisted monolayer-bilayer graphene geometry near theta ~= 1.1 deg, relaxed-geometry tight-binding calculations find isolated low-energy flat bands, but the flat-band manifold is less flat than relaxed magic-angle twisted bilayer graphene because it has a larger bandwidth and smaller zero-energy density-of-states peak; layer-resolved density of states further shows flat-band spectral weight localized mainly on the twisted monolayer top layer and broadened or delocalized across the AB-bilayer bottom layers [@Nguyen2022].""",
    lkm_id="gcn_14a55aff3de24a3a",
    source_paper="paper:867761060289970778",
    provenance_source="lkm",
    lkm_original=_ROOT_ORIGINAL,
)


helper_smab2_isolated_low_energy_flat_bands = claim(
    r"""In Nguyen et al.'s relaxed SM-(AB)_2 calculation at the magic-angle moire geometry, the band structure contains isolated low-energy flat bands near the Fermi level and a corresponding zero-energy density-of-states peak [@Nguyen2022].""",
    lkm_id="gcn_14a55aff3de24a3a",
    source_paper="paper:867761060289970778",
    provenance_source="lkm_decomposition",
    decomposition_of="gcn_14a55aff3de24a3a",
    lkm_original=_ROOT_ORIGINAL,
)


helper_smab2_less_flat_than_relaxed_tbg = claim(
    r"""In Nguyen et al.'s relaxed-geometry comparison, the SM-(AB)_2 low-energy flat-band manifold near theta ~= 1.1 deg is quantitatively less flat than relaxed magic-angle twisted bilayer graphene, with larger flat-band bandwidth and a smaller zero-energy density-of-states peak [@Nguyen2022].""",
    lkm_id="gcn_14a55aff3de24a3a",
    source_paper="paper:867761060289970778",
    provenance_source="lkm_decomposition",
    decomposition_of="gcn_14a55aff3de24a3a",
    lkm_original=_ROOT_ORIGINAL,
)


helper_smab2_layer_separated_character = claim(
    r"""Nguyen et al.'s layer-resolved density-of-states analysis for SM-(AB)_2 indicates spatially separated electronic character: near-zero-energy flat-band states are localized mainly on the twisted top monolayer, while the corresponding spectral weight is comparatively broadened and delocalized across the AB-bilayer bottom layers [@Nguyen2022].""",
    lkm_id="gcn_42c7afbd21b5483d",
    source_paper="paper:867761060289970778",
    provenance_source="lkm_decomposition",
    decomposition_of="gcn_42c7afbd21b5483d",
    lkm_original=_PREMISE_ORIGINAL,
)


gfac_f1d4418d_smab2_flat_band_localization = deduction(
    [gcn_42c7afbd_smab2_layer_resolved_dos],
    gcn_14a55aff_smab2_flat_band_localization,
    reason=(
        "1. Begin from upstream conclusions taken as known: conclusion 1 (the magic-angle $\\theta\\simeq1.1^{\\circ}$ coincides with maximized AA-region localization and yields flat bands in relaxed structures) and conclusion 10 (the atomistic relaxation and Slater-Koster $p_{z}$ TB protocol used to compute electronic structure) are treated as established starting points for analyzing SM-(AB)$_2$.\n"
        "2. Describe the system considered and the computational setup: SM-(AB)$_2$ denotes a twisted monolayer placed atop an AB-stacked bilayer (define SM-(AB)$_2$ accordingly); calculations are performed at the system's magic-angle moire using the relaxed geometries and the TB Hamiltonian from the established protocol.\nFig. 5\n"
        "3. Report the computed bandstructure observation for SM-(AB)$_2$: the TB bandstructure computed on relaxed geometry shows isolated low-energy flat bands near the Fermi level (i.e., similar in topology to magic-angle TBLG), and the DOS shows a zero-energy peak corresponding to these bands; these features are evident in the plotted bandstructure and DOS for SM-(AB)$_2$.\nFig. 5\n"
        "4. Quantitatively compare the flatness to magic-angle TBLG: although SM-(AB)$_2$ has isolated low-energy flat bands, the computed bandwidth of these flat bands is larger (i.e., the bands are less flat) and the zero-energy DOS peak is smaller than that obtained for magic-angle TBLG in the relaxed-geometry calculations presented; the paper explicitly states that the bands are \"less flat (lower)\" and the zero-energy DOS peak is reduced compared to TBLG in their magic-angle comparisons.\nFig. 5\n"
        "5. Explain the structural-electronic rationale provided: define AAB stacking as the local registry of the moire AA-like regions in SM-(AB)$_2$ (i.e., a mixture of AA and AB stacking); because AA regions are favorable for strong electronic localization while AB is unfavorable, the AAB-type regions reduce net AA-like localization compared to pure AA in TBLG, which diminishes the strength of real-space localization and thereby produces a larger flat-band bandwidth and smaller zero-energy DOS peak in SM-(AB)$_2$.\nFig. 6\n"
        "6. Report the layer-resolved LDOS result that demonstrates spatially separated localized and delocalized character: layer-decomposed LDOS (define LD-DOS as layer-decomposed density of states) for SM-(AB)$_2$ shows that the flat-band states are spatially localized on the twisted monolayer side (top layer) while the same low-energy states are comparatively delocalized on the bilayer (bottom two layers), i.e., a coexistence of localized and delocalized behavior across different layers of the junction.\nFig. 6\n"
        "7. Cite supportive comparisons and prior observations: the reported layer-separated localized-delocalized electronic character in SM-(AB)$_2$ is consistent with recent experimental observations referenced by the authors and with related theoretical findings on delocalized correlated states in double-bilayer contexts.\n[73]\n[74]"
    ),
    prior=0.95,
)


strat_decompose_smab2_isolated_flat_bands = support(
    [gcn_14a55aff_smab2_flat_band_localization],
    helper_smab2_isolated_low_energy_flat_bands,
    reason=(
        "The selected LKM root and factor step 3 explicitly state that relaxed "
        "SM-(AB)_2 has isolated low-energy flat bands near the Fermi level and "
        "a zero-energy density-of-states peak at the magic-angle moire geometry."
    ),
    prior=0.90,
)


strat_decompose_smab2_reduced_flatness = support(
    [gcn_14a55aff_smab2_flat_band_localization],
    helper_smab2_less_flat_than_relaxed_tbg,
    reason=(
        "The selected LKM root and factor steps 4 and 5 explicitly compare "
        "SM-(AB)_2 with relaxed magic-angle TBLG and report larger bandwidth "
        "and a smaller zero-energy DOS peak for SM-(AB)_2."
    ),
    prior=0.90,
)


strat_decompose_smab2_layer_separation = support(
    [gcn_42c7afbd_smab2_layer_resolved_dos],
    helper_smab2_layer_separated_character,
    reason=(
        "The selected LKM premise and factor step 6 define the layer-decomposed "
        "density of states and state the top-layer localization plus bottom-bilayer "
        "broadening/delocalization pattern."
    ),
    prior=0.90,
)
