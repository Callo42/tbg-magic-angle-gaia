"""paper_ge2021 -- claims and deduction for Ge et al. 2021.

Source: Emerging flat bands in large-angle twisted bi-layer graphene under pressure
DOI: 10.1039/d1nr00220a
Authors: Liangbing Ge | Kun Ni | Xiaojun Wu | Zhengping Fu | Yalin Lu | Yanwu Zhu
Reference key (CSL): Ge2021
"""

from gaia.lang import claim, deduction


gcn_e83deb9969844b33 = claim(
    "For commensurate large-angle twisted bilayer graphene studied by Ge et al. "
    "from about 9 degrees to about 27.8 degrees, the pressure-induced narrow "
    "bands and van Hove singularities reported for the 9.4 degree structure at "
    "interlayer spacing $2.44\\,\\mathrm{\\AA}$ are treated as representative of "
    "a broader compression route to engineer flat bands without magic-angle "
    "fine tuning [@Ge2021].",
    lkm_id="gcn_e83deb9969844b33",
    source_paper="paper:812469412236886018",
    provenance_source="lkm",
    lkm_original=(
        "The emergence of pressure-induced narrow bands and van Hove "
        "singularities observed for commensurate 9.4$^\\circ$ twisted bilayer "
        "graphene at an interlayer spacing of $2.44\\,\\mathrm{\\AA}$ is assumed "
        "to be representative of behavior across commensurate large twist angles "
        "studied from approximately 9$^\\circ$ up to approximately 27.8$^\\circ$, "
        "such that compression can be used as a broadly applicable route to "
        "engineer flat bands in large-angle twisted bilayer graphene unit cells "
        "without requiring fine-tuning of the twist angle to a magic value."
    ),
)

gcn_ba97172fd9264409 = claim(
    "In compressed twisted bilayer graphene with the same pressure and geometry "
    "considered by Ge et al., enhanced Kohn-Sham density of states at the Fermi "
    "level and near-Fermi van Hove singularities are used as suggestive single-"
    "particle indicators for possible correlation-driven phases, even though no "
    "explicit many-body calculation or experimental verification is supplied "
    "for superconductivity or correlated insulation [@Ge2021].",
    lkm_id="gcn_ba97172fd9264409",
    source_paper="paper:812469412236886018",
    provenance_source="lkm",
    lkm_original=(
        "An enhanced single-particle density of states at the Fermi level "
        "computed from Kohn-Sham density functional theory band structures and "
        "the presence of near-Fermi van Hove singularities are taken to be "
        "sufficient indicators to infer that electron correlations will "
        "necessarily produce many-body phases such as superconductivity or "
        "correlated insulating behavior in twisted bilayer graphene under the "
        "same pressure and geometry, without performing explicit many-body "
        "calculations or experimental verification."
    ),
)

gcn_105d2fc961f949b6 = claim(
    "Applying external compression to commensurate twisted bilayer graphene with "
    "twist angles from about 9.4 degrees to about 27.8 degrees can produce "
    "narrow flat electronic bands and near-Fermi van Hove singularities in "
    "large-angle regimes that are single-layer-graphene-like at ambient "
    "pressure; pressure is therefore a feasible control parameter for flat-band "
    "engineering in easier-to-fabricate larger-angle devices and motivates, but "
    "does not demonstrate, possible correlated phases [@Ge2021].",
    lkm_id="gcn_105d2fc961f949b6",
    source_paper="paper:812469412236886018",
    provenance_source="lkm",
    lkm_original=(
        "Applying external compression to twisted bilayer graphene with "
        "commensurate twist angles in the range from approximately 9.4$^\\circ$ "
        "up to approximately 27.8$^\\circ$ provides a route to generate narrow, "
        "flat electronic bands and associated van Hove singularities near the "
        "Fermi level in twist-angle regimes that exhibit single-layer-graphene-"
        "like linear dispersion at ambient pressure; pressure therefore provides "
        "a feasible control parameter for flat-band engineering in larger-angle "
        "twisted bilayer graphene, which could in principle enable electron-"
        "correlation phenomena (for example, superconductivity or correlated "
        "insulating behavior) in structures that are easier to fabricate than "
        "magic-angle devices."
    ),
)

strat_gfac_b4366b0e9b4a4f0f = deduction(
    [gcn_e83deb9969844b33, gcn_ba97172fd9264409],
    gcn_105d2fc961f949b6,
    reason=(
        "1. The established results provide three ingredients: at ambient "
        "pressure, large-angle TBG from about 9 degrees up to nearly 30 degrees "
        "has SLG-like dispersion near K; pressure monotonically reduces Fermi "
        "velocity for large twist angles; and for the 9.4 degree structure, "
        "compression to 75.52 GPa removes the linear Dirac-like dispersion, "
        "creates flat bands near the Fermi level, and produces near-Fermi van "
        "Hove singularities associated with saddle points in the VBM and CBM "
        "(Fig. 1, Fig. 3).\n"
        "2. The results summary states that for twist angles above 9 degrees up "
        "to nearly 30 degrees, dispersion is SLG-like at K under ambient "
        "conditions but changes drastically under external pressure, and the "
        "eigenvalue spectra display a flat band around the Fermi level.\n"
        "3. Because the control parameter is external pressure rather than "
        "precise tuning to the magic angle, the paper interprets compression as "
        "an alternative route to generating flat bands in TBG, motivated by the "
        "difficulty of preparing precisely controlled small-angle bilayers and "
        "by prior focus on twist angles below 2 degrees.\n"
        "4. The near-Fermi flat bands and associated VHSs enhance the density "
        "of states close to the Fermi level, and the paper links such electronic "
        "structures to properties previously found in small-angle TBG, including "
        "superconductivity and correlated insulation, without claiming direct "
        "demonstration of those many-body phases.\n"
        "5. The forward-looking inference is that, if pressure can generate in "
        "larger-angle TBG the same electronic ingredients associated with "
        "correlated phenomena in magic-angle systems, then pressure provides "
        "opportunities for flat-band engineering and further exploration of "
        "pressure-tuned correlated behavior.\n"
        "6. The argument is suggestive rather than demonstrative for many-body "
        "phases: the paper says flat bands may induce superconductivity and "
        "that electron correlations take place, but provides no separate many-"
        "body derivation or experimental proof of superconductivity or "
        "correlated insulating order in compressed large-angle systems.\n"
        "7. Therefore, the conclusion is that external compression is a "
        "practical engineering knob for producing narrow flat bands and "
        "associated VHSs in larger-angle TBG, offering an alternative to strict "
        "magic-angle fabrication and motivating experimental and theoretical "
        "exploration of possible correlation-driven phases."
    ),
    prior=0.95,
)
