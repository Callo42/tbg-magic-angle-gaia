"""paper_cao2018 -- claims and deductions from Cao et al. 2018.

Source: Unconventional superconductivity in magic-angle graphene superlattices
DOI: 10.1038/nature26160
Authors: Yuan Cao | Valla Fatemi | Shiang Fang | Kenji Watanabe |
Takashi Taniguchi | Efthimios Kaxiras | Pablo Jarillo-Herrero
Reference key (CSL): Cao2018
"""

from gaia.lang import claim, deduction, support


_CORRELATED_INSULATOR_ORIGINAL = r"""When transport measured versus temperature at gate-induced carrier density equal to nominal half-filling of the moiré flat band ($n=\pm n_s/2$) displays insulating temperature dependence (resistance that increases upon cooling) over an intermediate temperature range (here roughly 1–4 K), this phenomenology is consistent with the presence of a correlated insulating state driven by electron–electron interactions (a Mott-like insulator) under the assumption that single-particle band gaps or disorder-dominated localization do not fully account for the observed gap magnitude and temperature dependence; this interpretation is plausible in light of the very narrow flat-band bandwidth (of order 5–10 meV) and the enhanced Coulomb interaction energy in magic-angle twisted bilayer graphene, but does not constitute a rigorous microscopic proof of a Mott mechanism."""

_ROOT_ORIGINAL = r"""The temperature versus gate-induced carrier-density phase diagram of magic-angle twisted bilayer graphene (MA-TBG, i.e., twisted bilayer graphene with $\theta$ near the first magic angle) exhibits superconducting dome-shaped regions on both sides of a correlated insulating state centered at nominal half-filling $n=\pm n_{s}/2$ of the flat moiré bands, where $n_{s}=4/A$ is the superlattice density and $A\approx\sqrt{3}a^2/(2\theta^2)$ is the moiré unit cell area with graphene lattice constant $a=0.246\ \text{nm}$. In the two devices examined (device M1, $\theta=1.16^\circ$, and device M2, $\theta=1.05^\circ$), cooling at carrier densities just adjacent to the half-filling insulating density produces two pronounced superconducting regions (domes) whose four-probe resistance is fully suppressed below the measurement floor at the lowest temperature (70 mK). The correlated insulating region at nominal half-filling shows insulating temperature dependence (increasing resistance upon cooling) over an intermediate temperature window of roughly 1–4 K, and the superconducting domes appear when the device is electrostatically doped away from this correlated insulator."""


gcn_ffd6d31f_correlated_insulator_phenomenology = claim(
    r"""For magic-angle twisted bilayer graphene near the first magic angle, the selected LKM chain treats transport at nominal half-filling of the flat moire band, n=+-n_s/2, that shows resistance increasing on cooling over roughly 1-4 K as phenomenology consistent with a correlated, Mott-like insulating state driven by electron-electron interactions, while noting that this does not by itself prove a microscopic Mott mechanism [@Cao2018].""",
    lkm_id="gcn_ffd6d31f7b2642e6",
    source_paper="paper:813052701314121729",
    provenance_source="lkm",
    lkm_original=_CORRELATED_INSULATOR_ORIGINAL,
)

gcn_006f88d8_ma_tbg_superconducting_domes = claim(
    r"""For Cao et al. 2018 magic-angle twisted bilayer graphene devices M1 (theta=1.16 deg) and M2 (theta=1.05 deg), the temperature versus gate-induced carrier-density phase diagram shows superconducting dome-shaped regions adjacent to a correlated insulating state centered at nominal half-filling n=+-n_s/2 of the flat moire bands, with n_s=4/A and A~=sqrt(3)a^2/(2 theta^2) for graphene lattice constant a=0.246 nm; near the adjacent carrier densities the four-probe resistance is suppressed below the measurement floor at 70 mK, while the half-filling region has insulating temperature dependence over roughly 1-4 K [@Cao2018].""",
    lkm_id="gcn_006f88d8df3548fa",
    source_paper="paper:813052701314121729",
    provenance_source="lkm",
    lkm_original=_ROOT_ORIGINAL,
)

helper_ma_tbg_domes_adjacent_to_correlated_insulator = claim(
    r"""For the Cao et al. 2018 MA-TBG devices, the selected LKM root states that superconducting dome-shaped regions occur at carrier densities just adjacent to the half-filling correlated insulating density, on both sides of that correlated insulator in the mapped temperature-density phase diagram [@Cao2018].""",
    lkm_id="gcn_006f88d8df3548fa",
    source_paper="paper:813052701314121729",
    provenance_source="lkm_decomposition",
    decomposition_of="gcn_006f88d8df3548fa",
    lkm_original=_ROOT_ORIGINAL,
)

helper_ma_tbg_resistance_suppressed_at_70_mk = claim(
    r"""For Cao et al. 2018 MA-TBG devices M1 and M2, cooling at carrier densities adjacent to the half-filling insulating state produces superconducting regions in which four-probe resistance is suppressed below the measurement floor at the 70 mK base temperature [@Cao2018].""",
    lkm_id="gcn_006f88d8df3548fa",
    source_paper="paper:813052701314121729",
    provenance_source="lkm_decomposition",
    decomposition_of="gcn_006f88d8df3548fa",
    lkm_original=_ROOT_ORIGINAL,
)

helper_ma_tbg_half_filling_insulating_window = claim(
    r"""For the Cao et al. 2018 MA-TBG phase diagram, the correlated insulating region centered at nominal half-filling n=+-n_s/2 shows insulating temperature dependence, i.e. resistance increasing upon cooling, over an intermediate temperature window of roughly 1-4 K [@Cao2018].""",
    lkm_id="gcn_006f88d8df3548fa",
    source_paper="paper:813052701314121729",
    provenance_source="lkm_decomposition",
    decomposition_of="gcn_006f88d8df3548fa",
    lkm_original=_ROOT_ORIGINAL,
)


strat_gfac_1433dc8665164d11_phase_diagram = deduction(
    [gcn_ffd6d31f_correlated_insulator_phenomenology],
    gcn_006f88d8_ma_tbg_superconducting_domes,
    reason=r"""1. Treat conclusion 1 (observation of intrinsic, gate-tunable superconductivity in MA-TBG) as established and use it as the starting point: superconductivity appears in MA-TBG devices near the magic angle upon electrostatic doping away from correlated insulating states at half-filling.
2. Describe the $T$ versus $n$ measurements that map the phase diagram: four-probe resistance $R_{xx}$ measured as a function of carrier density $n$ and temperature $T$ for devices M1 and M2 reveals regions of vanishing resistance (superconducting domes) adjacent to an insulating region centered at half-filling $n=\pm n_{s}/2$ of the flat bands.
Fig. 2b
Fig. 2c
3. Characterize the superconducting domes in density-temperature space: in both devices, cooling at densities just adjacent to the half-filling correlated insulating state produces pronounced superconducting regions (domes) where the resistance is fully suppressed below the measurement floor at base temperature; the domes appear on both sides of the correlated insulator (i.e. on densities slightly less and slightly greater than $-n_{s}/2$ in the hole-doped side for these measurements).
Fig. 2b
4. Describe the correlated insulating region's temperature dependence: when cooling through the density corresponding to half-filling, the system exhibits insulating temperature dependence over an intermediate temperature range (roughly 1--4 K) before superconductivity appears at lower temperatures in adjacent densities, indicating a Mott-like correlated insulating phase centered at $n=\pm n_{s}/2$ that gives way to superconductivity upon doping.
Fig. 4a
5. State the authors' interpretation and analogy to cuprates: the presence of superconducting domes adjacent to a correlated insulating (Mott-like) state in the $T$-$n$ phase diagram is highlighted by the authors as phenomenologically similar to cuprate phase diagrams, supporting the description of the insulating phase as a correlated (Mott-like) state and the superconductivity as emerging upon electrostatic doping away from this parent insulator.""",
    prior=0.95,
)

strat_decompose_ma_tbg_dome_adjacency = support(
    [gcn_006f88d8_ma_tbg_superconducting_domes],
    helper_ma_tbg_domes_adjacent_to_correlated_insulator,
    reason=(
        "The selected LKM root and factor steps 2-3 explicitly state that the "
        "temperature-density phase diagram contains superconducting domes "
        "adjacent to the half-filling correlated insulator."
    ),
    prior=0.90,
)

strat_decompose_ma_tbg_zero_resistance = support(
    [gcn_006f88d8_ma_tbg_superconducting_domes],
    helper_ma_tbg_resistance_suppressed_at_70_mk,
    reason=(
        "The selected LKM root and factor step 3 explicitly report full "
        "suppression of four-probe resistance below the measurement floor at "
        "the 70 mK base temperature in the superconducting regions."
    ),
    prior=0.90,
)

strat_decompose_ma_tbg_half_filling_insulator = support(
    [gcn_006f88d8_ma_tbg_superconducting_domes],
    helper_ma_tbg_half_filling_insulating_window,
    reason=(
        "The selected LKM root and factor step 4 explicitly state that the "
        "half-filling region shows insulating temperature dependence over "
        "roughly 1-4 K."
    ),
    prior=0.90,
)
