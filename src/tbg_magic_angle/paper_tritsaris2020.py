"""paper_tritsaris2020 -- claims and deduction for Tritsaris et al. 2020.

Source: Electronic structure calculations of twisted multi-layer graphene superlattices
DOI: 10.1088/2053-1583/ab8f62
Authors: Georgios A Tritsaris | Stephen Carr | Ziyan Zhu | Yiqi Xie | Steven B Torrisi | Jing Tang | Marios Mattheakis | Daniel T Larson | Efthimios Kaxiras
Reference key: Tritsaris2020
"""

from gaia.lang import claim, deduction


_ROOT_ORIGINAL = (
    "For commensurate twisted bilayer graphene supercells computed at 33 unique "
    "commensurate twist angles spanning 0.88° ≤ θ ≤ 21.79°, the ab initio "
    "Wannier-derived tight-binding calculations and automated flat-band "
    "detection identify a maximized flat-band likelihood p(θ) at a magic angle "
    "θ* ≈ 1.1°, with the emergence of low-dispersion (near-flat) bands near the "
    "Fermi level in the single-particle TB band structures at that angle."
)


gcn_af432bff_ab_initio_tb_workflow = claim(
    "For commensurate twisted bilayer graphene in the Tritsaris et al. 2020 "
    "high-throughput workflow, the selected LKM chain treats as established "
    "a Wannier-derived tight-binding Hamiltonian workflow in which band "
    "structures are diagonalized with 60 k-points along Gamma-M-K and "
    "automated flat-band detectors inspect a 0.30 eV window around the Fermi "
    "level [@Tritsaris2020].",
    lkm_id="gcn_af432bff1d3e4cf0",
    source_paper="paper:812643486368006145",
    provenance_source="lkm",
    lkm_original="",
    todo="LKM premise content was empty; statement is reconstructed only from factor steps 1 and 3.",
)


gcn_be5d1975_detector_interpolation = claim(
    "For the same Tritsaris et al. 2020 commensurate twisted-bilayer-graphene "
    "workflow, the selected LKM chain treats automated low-dispersion-band "
    "detections at the sampled commensurate twist angles as inputs that are "
    "converted into a continuous flat-band likelihood p(theta) by an "
    "interpolation and blending prescription [@Tritsaris2020].",
    lkm_id="gcn_be5d1975ecac4211",
    source_paper="paper:812643486368006145",
    provenance_source="lkm",
    lkm_original="",
    todo="LKM premise content was empty; statement is reconstructed only from factor step 3.",
)


gcn_5f58746b_magic_angle_flat_band_likelihood = claim(
    "For 33 unique commensurate twisted bilayer graphene supercells spanning "
    "0.88 degrees <= theta <= 21.79 degrees, Tritsaris et al. 2020 use ab "
    "initio Wannier-derived tight-binding calculations and automated flat-band "
    "detection to find that the blended flat-band likelihood p(theta) is "
    "maximized near theta* approximately 1.1 degrees, where low-dispersion "
    "near-flat bands emerge near the Fermi level in the single-particle "
    "tight-binding band structures [@Tritsaris2020].",
    lkm_id="gcn_5f58746bcc0b4098",
    source_paper="paper:812643486368006145",
    provenance_source="lkm",
    lkm_original=_ROOT_ORIGINAL,
)


strat_gfac_c4fed52224164214 = deduction(
    [
        gcn_af432bff_ab_initio_tb_workflow,
        gcn_be5d1975_detector_interpolation,
    ],
    gcn_5f58746b_magic_angle_flat_band_likelihood,
    reason=(
        "1. Treat the high-throughput ab initio TB workflow (conclusion 3) "
        "as established and use it to compute commensurate twisted bilayer "
        "graphene band structures for a dense set of commensurate angles in "
        "the interval $0.88^{\\circ} \\leq \\theta \\leq 21.79^{\\circ}$; "
        "the workflow uses the Wannier-derived TB Hamiltonian, diagonalization "
        "with 60 k-points along $\\Gamma$-M-K, and automated flat-band detectors "
        "within a 0.30 eV window around the Fermi level.\n"
        "2. Identify commensurate twist angles using the integer-pair "
        "parametrization: associate each commensurate twist angle $\\theta$ "
        "with a pair of integers $(M,N)$ defining the periodic supercell via "
        "$\\cos(\\theta) = (N^2 + 4NM + M^2)/(2(N^2 + NM + M^2))$, so "
        "that specific small angles correspond to large $(M,N)$ pairs (for "
        "example, $(32,31) \\to 1.05^{\\circ}$, $(27,26) \\to "
        "1.25^{\\circ}$, $(23,22) \\to 1.47^{\\circ}$), enabling "
        "enumeration of 33 unique commensurate bilayers in the stated range. "
        "[38]\n"
        "3. Compute TB band structures for the 33 unique commensurate bilayers "
        "and apply the automated flat-band detectors to obtain model-based "
        "detections of low-dispersion bands at the sampled commensurate "
        "$\\theta$ values, producing detection outputs that are converted "
        "into continuous predictions $p(\\theta)$ via the interpolation/blending "
        "prescription (conclusion 2). Fig. 4\n"
        "4. Observe the evolution of low-energy bands with decreasing $\\theta$: "
        "for large $\\theta$ the low-energy band structure resembles that of "
        "an isolated graphene monolayer, while as $\\theta$ decreases into "
        "the small-angle regime the number of bands increases and the bands "
        "near the Fermi level become progressively flatter due to interlayer "
        "hybridization as seen in the calculated TB band structures.\n"
        "5. Report the primary quantitative result for bilayer graphene: the "
        "computed, blended prediction $p(\\theta)$ is maximized near the "
        "well-known magic angle, with the ab initio TB calculations identifying "
        "$\\theta^{*} \\approx 1.1^{\\circ}$ (the workflow shows G/G@1.08 "
        "as an example close to this maximum), and the formation of "
        "low-dispersion bands near the Fermi level is observed in the "
        "single-particle TB band structures at this angle. Fig. 4\n"
        "6. Record the caveat about structural relaxation: note that for twist "
        "angles below about $1.0^{\\circ}$ atomic relaxation effects "
        "(structural reconstruction) can significantly modify band structures "
        "(e.g., widening single-particle gaps), and that such relaxation effects "
        "are not included in the present high-throughput TB workflow, an "
        "explicit limitation acknowledged by the authors. [31]"
    ),
    prior=0.95,
)
