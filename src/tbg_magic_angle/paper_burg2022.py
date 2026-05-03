"""paper_burg2022 -- claims and deductions from Burg et al. 2022.

Source: Emergence of Correlations in Alternating Twist Quadrilayer Graphene
DOI: 10.48550/arXiv.2201.01637
Authors: G. William Burg | Eslam Khalaf | Yimeng Wang | Kenji Watanabe | Takashi Taniguchi | Emanuel Tutuc
Reference key (CSL): Burg2022
"""

from gaia.lang import claim, deduction, support


_MAPPING_ORIGINAL = "Mapping an alternating-twist multilayer-graphene (ATMG) twist angle $\\theta_{\\mathrm{ATQG}}$ to an \"equivalent\" twisted-bilayer-graphene (TBG) twist angle $\\theta_{\\mathrm{TBG}}$ by the heuristic relation $\\theta_{\\mathrm{TBG}} = \\theta_{\\mathrm{ATQG}}/\\varphi$, where $\\varphi \\approx 1.6180339887$ is the golden ratio, provides an approximate effective twist-angle scaling between ATQG subsystems and TBG subsystems according to theoretical decomposition statements for ATMG into TBG-like subsystems; this mapping is explicitly heuristic and meant as a comparative tool to place ATQG data in a TBG context, but it does not guarantee quantitative equivalence of bandwidths, interaction strengths, or exact magic-angle conditions between the two systems."

_ROOT_ORIGINAL = "Comparing the two measured ATQG devices with twist angles $\\theta = 1.96^\\circ$ (above the magic angle $1.68^\\circ$) and $\\theta = 1.52^\\circ$ (below the magic angle $1.68^\\circ$) reveals an asymmetric twist-angle dependence of correlated phases: the $\\theta = 1.96^\\circ$ device exhibits dominant correlated-insulator resistance maxima on the hole-doped side and no observed superconductivity down to $160\\,$mK, whereas the $\\theta = 1.52^\\circ$ device shows evidence of superconducting-like transport signatures near half filling while correlated-insulator signatures in that device are weaker; this device-to-device comparison indicates that, in these ATQG samples, superconductivity favors angles smaller than the magic angle while correlated insulators favor angles larger than the magic angle, implying a decoupling of superconductivity and correlated insulating order as a function of twist angle in ATQG that differs from some reported trends in twisted bilayer graphene (TBG)."


gcn_51a6d18a_atqg_tbg_angle_mapping = claim(
    r"""For alternating-twist quadrilayer graphene (ATQG), the selected LKM chain uses the heuristic relation theta_TBG = theta_ATQG / phi, with phi approximately 1.618, to compare ATQG twist angles with TBG-like subsystem angles; this mapping is only a comparative tool and does not guarantee quantitative equivalence of bandwidths, interaction strengths, or exact magic-angle conditions between ATQG and TBG [@Burg2022].""",
    lkm_id="gcn_51a6d18a02c4407d",
    source_paper="paper:867774235207008693",
    provenance_source="lkm",
    lkm_original=_MAPPING_ORIGINAL,
)


gcn_225da7b3_atqg_angle_phase_decoupling = claim(
    r"""In the two Burg et al. ATQG devices, theta=1.96 deg lies above the stated ATQG magic angle of 1.68 deg and shows dominant hole-side correlated-insulator resistance maxima with no observed superconductivity down to 160 mK, while theta=1.52 deg lies below 1.68 deg and shows superconducting-like transport signatures near half filling with weaker correlated-insulator signatures; comparing these devices indicates that superconductivity favors smaller-than-magic angles and correlated insulators favor larger-than-magic angles in these ATQG samples, so superconductivity and correlated insulating order are decoupled as functions of twist angle in a way that differs from some reported TBG trends [@Burg2022].""",
    lkm_id="gcn_225da7b340cb47b8",
    source_paper="paper:867774235207008693",
    provenance_source="lkm",
    lkm_original=_ROOT_ORIGINAL,
)


helper_atqg_196_correlated_insulator_no_sc = claim(
    r"""For the Burg et al. ATQG device with theta=1.96 deg, which is above the stated ATQG magic angle 1.68 deg, the selected LKM evidence reports dominant correlated-insulator resistance maxima on the hole-doped side at n=-n_s/2 and -n_s and no observed superconducting signatures down to 160 mK [@Burg2022].""",
    lkm_id="gcn_225da7b340cb47b8",
    source_paper="paper:867774235207008693",
    provenance_source="lkm_decomposition",
    decomposition_of="gcn_225da7b340cb47b8",
    lkm_original=_ROOT_ORIGINAL,
)


helper_atqg_152_superconducting_like_transport = claim(
    r"""For the Burg et al. ATQG device with theta=1.52 deg, which is below the stated ATQG magic angle 1.68 deg, the selected LKM evidence reports superconducting-like transport signatures near half filling, including sharp dV/dI peaks, a low-resistance dome, T_c approximately 1.34 K, and T_BKT approximately 1.29 K, while correlated-insulator signatures are weaker than in the larger-angle device [@Burg2022].""",
    lkm_id="gcn_225da7b340cb47b8",
    source_paper="paper:867774235207008693",
    provenance_source="lkm_decomposition",
    decomposition_of="gcn_225da7b340cb47b8",
    lkm_original=_ROOT_ORIGINAL,
)


helper_atqg_asymmetric_angle_dependence = claim(
    r"""Within the two Burg et al. ATQG samples, the direct device comparison supports an asymmetric twist-angle dependence: superconducting-like transport is more prominent at theta=1.52 deg below the stated 1.68 deg magic angle, whereas correlated-insulator signatures are more prominent at theta=1.96 deg above that angle [@Burg2022].""",
    lkm_id="gcn_225da7b340cb47b8",
    source_paper="paper:867774235207008693",
    provenance_source="lkm_decomposition",
    decomposition_of="gcn_225da7b340cb47b8",
    lkm_original=_ROOT_ORIGINAL,
)


helper_atqg_tbg_equivalent_angle_context = claim(
    r"""Using the Burg et al. heuristic theta_TBG = theta_ATQG / phi, the selected LKM evidence places the theta=1.96 deg and theta=1.52 deg ATQG samples at TBG-like angles of approximately 1.21 deg and 0.94 deg, respectively, while preserving the caution that the mapping is comparative rather than quantitatively exact [@Burg2022].""",
    lkm_id="gcn_51a6d18a02c4407d",
    source_paper="paper:867774235207008693",
    provenance_source="lkm_decomposition",
    decomposition_of="gcn_51a6d18a02c4407d",
    lkm_original=_MAPPING_ORIGINAL,
)


strat_gfac_b160d54c_atqg_angle_phase_decoupling = deduction(
    [gcn_51a6d18a_atqg_tbg_angle_mapping],
    gcn_225da7b3_atqg_angle_phase_decoupling,
    reason="1. From the $\\theta = 1.96^\\circ$ device measurements, the authors establish that correlated insulators on the hole side (at $n = -n_{\\text{s}}/2$ and $-n_{\\text{s}}$) are the dominant correlated phenomena and that no superconducting signatures are observed in the measured ranges for that device; these observations were presented earlier and are taken as experimental facts for the comparison.\nFig. 1e\n2. From the $\\theta = 1.52^\\circ$ device measurements, the authors establish that superconducting-like signatures\u2014sharp $\\mathrm{d}V/\\mathrm{d}I$ peaks, a low-resistance dome, a measured $T_{\\mathrm{c}} \\approx 1.34\\,$K, and $T_{\\mathrm{BKT}} \\approx 1.29\\,$K\u2014occur near half filling while correlated-insulator signatures in that device appear weaker than in the larger-angle device; these observations are likewise taken from the experimental data described for the smaller-angle device.\nFig. 3g\n3. Comparing these two device-specific outcomes as a function of twist angle, the authors note an asymmetric dependence: superconductivity appears and is more prominent at the smaller twist angle ($\\theta = 1.52^\\circ$) while correlated insulators are more prominent at the larger twist angle ($\\theta = 1.96^\\circ$), indicating that superconductivity and correlated insulating order are not tightly coupled across $\\theta$ in the same way they sometimes appear coupled in twisted bilayer graphene (TBG).\nFig. 1e\n4. The authors place this experimental twist-angle dependence in context by mapping the ATQG twist angles to an equivalent TBG twist angle by dividing the ATQG twist angle by the golden ratio ($\\approx 1.62$), thereby noting that the $\\theta = 1.96^\\circ$ and $\\theta = 1.52^\\circ$ samples map to TBG-like angles of $1.21^\\circ$ and $0.94^\\circ$ respectively; they then compare the observed asymmetry to reports in TBG and conclude that the observed decoupling\u2014superconductivity favoring angles smaller than the magic angle while correlated insulators favor larger-than-magic angles\u2014is a trend that departs from some reported TBG behaviors and suggests a distinct role for dispersive bands in ATQG.\n5. Based on the direct experimental comparison between the two samples and the discussion of differences relative to TBG literature, the authors conclude that superconductivity and correlated insulating order in ATQG are decoupled as a function of twist angle in the presented devices: superconductivity is favored at angles smaller than the magic angle in these devices while correlated insulators favor larger-than-magic angles, evidencing an asymmetric twist-angle dependence of correlated phases in ATQG.\n(Discussion text and comparisons in main text)",
    prior=0.95,
)


strat_decompose_atqg_196_device = support(
    [gcn_225da7b3_atqg_angle_phase_decoupling],
    helper_atqg_196_correlated_insulator_no_sc,
    reason=(
        "The selected LKM root and factor step 1 explicitly identify the "
        "theta=1.96 deg ATQG device as the larger-angle sample with hole-side "
        "correlated-insulator maxima and no observed superconductivity down to 160 mK."
    ),
    prior=0.90,
)


strat_decompose_atqg_152_device = support(
    [gcn_225da7b3_atqg_angle_phase_decoupling],
    helper_atqg_152_superconducting_like_transport,
    reason=(
        "The selected LKM root and factor step 2 explicitly identify the "
        "theta=1.52 deg ATQG device as the smaller-angle sample with "
        "superconducting-like transport near half filling and weaker correlated-insulator signatures."
    ),
    prior=0.90,
)


strat_decompose_atqg_angle_asymmetry = support(
    [gcn_225da7b3_atqg_angle_phase_decoupling],
    helper_atqg_asymmetric_angle_dependence,
    reason=(
        "The selected LKM root and factor steps 3 and 5 state the comparative "
        "twist-angle trend: superconductivity is favored below the stated magic "
        "angle, while correlated insulators are favored above it in the measured ATQG devices."
    ),
    prior=0.90,
)


strat_decompose_atqg_tbg_mapping_context = support(
    [gcn_51a6d18a_atqg_tbg_angle_mapping],
    helper_atqg_tbg_equivalent_angle_context,
    reason=(
        "The selected LKM premise gives the theta_TBG = theta_ATQG / phi heuristic, "
        "and factor step 4 applies it to the two ATQG devices as approximately "
        "1.21 deg and 0.94 deg TBG-like angles."
    ),
    prior=0.90,
)
