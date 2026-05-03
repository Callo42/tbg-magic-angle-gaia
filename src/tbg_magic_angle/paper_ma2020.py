"""paper_ma2020 -- LKM claims and deduction from Ma et al. (2020).

Source: Moire Flat Bands of Twisted Few-layer Graphite
DOI: 10.48550/arXiv.2001.07995
Authors: Zhen Ma | Shuai Li | Meng-Meng Xiao | Ya-Wen Zheng | Ming Lu |
    HaiWen Liu | Jin-Hua Gao | X. C. Xie
Reference key (CSL): Ma2020
"""
from gaia.lang import claim, deduction


gcn_2fcfd55afc454c94 = claim(
    "In Ma et al.'s continuum calculations for twisted few-layer graphite, the two few-layer-graphite slabs are treated as rigid, uniformly twisted atomic layers; the calculation does not include in-plane lattice relaxation, out-of-plane corrugation, or spatial twist-angle inhomogeneity across the moire supercell [@Ma2020].",
    lkm_id="gcn_2fcfd55afc454c94",
    source_paper="paper:867748811072602427",
    provenance_source="lkm",
    lkm_original="The continuum calculations used to determine the magic twist angle of about $1.05^\\circ$ treat the two few-layer-graphite slabs as rigid, uniformly twisted atomic layers and do not include in-plane lattice relaxation, out-of-plane corrugation, or spatial twist-angle inhomogeneity across the moir\u00e9 supercell.",
)

gcn_2ceab67f16f34d1e = claim(
    "For N=3 twisted few-layer graphite systems in Ma et al.'s minimal continuum-model twist-angle scan, with parameters omega_1/omega_2/gamma_0/gamma_1/gamma_3/gamma_4 = 78/98/2610/360/0/0 meV and xi = -1, the principal magic-angle estimate near 1.05 degrees is obtained while omitting remote hoppings gamma_3 and gamma_4; separate full-parameter calculations with gamma_3 = 283 meV and gamma_4 = 138 meV make the flat bands dispersive, separate them in energy, and open twist-angle-dependent gaps at the Dirac points of linear bands, so the precise magic-angle value depends on the chosen continuum parameters and on the minimal-model scan [@Ma2020].",
    lkm_id="gcn_2ceab67f16f34d1e",
    source_paper="paper:867748811072602427",
    provenance_source="lkm",
    lkm_original="The principal magic-angle estimate of about $1.05^\\circ$ is identified from the minimal continuum model used to scan twist angle in the $N=3$ systems, with parameters $\\omega_1/\\omega_2/\\gamma_0/\\gamma_1/\\gamma_3/\\gamma_4=78/98/2610/360/0/0\\,\\mathrm{meV}$ and $\\xi=-1$, so the central numerical identification omits remote hoppings $\\gamma_3$ and $\\gamma_4$. Full-parameter calculations presented separately show that including $\\gamma_3=283\\,\\mathrm{meV}$ and $\\gamma_4=138\\,\\mathrm{meV}$ makes the flat bands dispersive, separates them in energy, and opens twist-angle-dependent gaps at the Dirac points of linear bands, so the precise magic-angle value depends on the chosen continuum parameters and on use of the minimal-model scan.Fig. 2 (minimal-model \u03b8 scans) and Supplementary Fig. S4 (full-parameter comparisons)",
)

gcn_f23eff9c755840f2 = claim(
    "In Ma et al.'s continuum description of twisted few-layer graphite, the numerical twist angle at which the two primary moire bands become nearly flat is about 1.05 degrees; this equals the principal magic-angle value obtained for twisted bilayer graphene within the same continuum-model formalism, while the claim is scoped to the primary two-band pair rather than all moire bands [@Ma2020].",
    lkm_id="gcn_f23eff9c755840f2",
    source_paper="paper:867748811072602427",
    provenance_source="lkm",
    lkm_original="The numerically identified twist angle at which the two primary moir\u00e9 bands become nearly flat in twisted few-layer graphite is about $1.05^\\circ$, the same numerical value as the principal magic angle obtained for twisted bilayer graphene within the same continuum description.",
)

gfac_6988d3b9bea84c0f = deduction(
    [gcn_2fcfd55afc454c94, gcn_2ceab67f16f34d1e],
    gcn_f23eff9c755840f2,
    reason=(
        "1. Use the previously established numerical continuum-model framework and the minimal-model calculations to identify the twist angle at which the primary pair of moire bands becomes nearly flat in tFL-graphite; denote the twist angle by $\\theta$ measured in degrees.\n"
        "2. Report the numerical observation from the band plots: the calculations presented for multiple tFL-graphite configurations show that the two primary moire bands become nearly flat at $\\theta\\approx 1.05^\\circ$; this numerical value coincides with the principal magic angle previously reported for twisted bilayer graphene within the same employed continuum-model formalism.\nFig. 2\n[9-14]\n"
        "3. Record the authors' qualification that only two of the multiple moire bands flatten at the magic angle while the remaining bands remain dispersive (albeit narrowed), i.e., the magic-angle flatness pertains to the principal two-band pair in tFL-graphite as in TBG, even though the overall moire spectrum is richer.\nFig. 2"
    ),
    prior=0.95,
)
