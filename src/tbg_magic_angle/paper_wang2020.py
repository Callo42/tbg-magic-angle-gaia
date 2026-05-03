"""paper_wang2020 -- claims and deductions from Wang, Bultinck, and Zaletel 2020.

Source: Flat-band topology of magic angle graphene on a transition metal dichalcogenide
DOI: 10.1103/physrevb.102.235146
Authors: Tianle Wang | Nick Bultinck | Michael P. Zaletel
Reference key (CSL): Wang2020
"""

from gaia.lang import claim, deduction, support


_PREMISE_ORIGINAL = (
    "The two-valley continuum model of twisted bilayer graphene (TBG), which "
    "treats valley indices $\\tau=\\pm$ as effectively decoupled and describes "
    "low-energy moire physics via the Bistritzer-MacDonald continuum Hamiltonian "
    "parametrized by the twist angle $\\theta$, accurately captures the "
    "single-particle flat-band physics when the twist angle $\\theta$ is "
    "sufficiently small so that intervalley scattering is negligible and is "
    "sufficiently close to the first magic angle $\\theta^{*}\\approx1.08^\\circ$ "
    "so that (i) the eight active flat bands are narrowly separated from remote "
    "bands by appreciable gaps and (ii) the active-band bandwidths are comparable "
    "to or smaller than proximate energy scales (Rashba, Ising, sublattice $u$); "
    "outside this regime processes such as valley-mixing, remote-band hybridization, "
    "or large kinetic bandwidth invalidate the isolated-band projection and the "
    "subsequent conclusions."
)

_ROOT_ORIGINAL = (
    "The reconstructed-band phenomena described above--Rashba-induced isolated "
    "extremely flat band pairs near K^{\\pm}, the sixteen-Dirac-point structure "
    "in the single-valley four-band spectrum, and the computed Chern-number phase "
    "diagrams for isolated active bands--are valid in the continuum "
    "two-decoupled-valley description of twisted bilayer graphene that applies "
    "at sufficiently small twist angles and require being near the first magic "
    "angle so that (i) the eight active flat bands are well separated from remote "
    "bands by appreciable gaps and (ii) the active-band bandwidth is comparable "
    "to or smaller than typical proximate energy scales (Rashba \\sim 16 meV, "
    "Ising \\sim 1 meV, sublattice u \\sim 1\\text{--}2 meV); if the twist angle "
    "is too far from the magic angle so that the active-band bandwidth is much "
    "larger than these proximate couplings, then the Rashba coupling will not "
    "reconstruct the active bands and the reported band topology and extreme "
    "flatness need not occur."
)


gcn_fb78cfd7_magic_angle_continuum_regime = claim(
    r"""In Wang, Bultinck, and Zaletel's TBG-on-transition-metal-dichalcogenide continuum analysis, the two-valley Bistritzer-MacDonald continuum model with effectively decoupled valley indices tau = +/- is an appropriate description of single-particle flat-band physics only for sufficiently small twist angles near the first magic angle theta* ~= 1.08 degrees, where intervalley scattering is negligible, the eight active flat bands are isolated from remote bands by appreciable gaps, and their bandwidths are comparable to or smaller than the proximate Rashba, Ising, and sublattice energy scales [@Wang2020].""",
    lkm_id="gcn_fb78cfd75da34fb5",
    source_paper="paper:812527076643962881",
    provenance_source="lkm",
    lkm_original=_PREMISE_ORIGINAL,
)


gcn_9f7dbaf8_substrate_flat_band_topology_regime = claim(
    r"""In Wang, Bultinck, and Zaletel's continuum two-decoupled-valley description of magic-angle TBG on a transition metal dichalcogenide, the reported reconstructed-band phenomena--Rashba-induced isolated extremely flat band pairs near K^{+/-}, the sixteen-Dirac-point single-valley four-band structure, and Chern-number phase diagrams for isolated active bands--are scoped to sufficiently small twist angles near the first magic angle, where the active eight bands are isolated and have bandwidth comparable to or smaller than proximate scales such as Rashba ~16 meV, Ising ~1 meV, and sublattice u ~1-2 meV; away from that regime, large active-band bandwidth can prevent Rashba reconstruction and the reported topology and extreme flatness need not occur [@Wang2020].""",
    lkm_id="gcn_9f7dbaf8f0014316",
    source_paper="paper:812527076643962881",
    provenance_source="lkm",
    lkm_original=_ROOT_ORIGINAL,
)


helper_rashba_isolated_flat_pairs = claim(
    r"""Within Wang et al.'s near-first-magic-angle TBG-on-TMD continuum regime, Rashba proximity coupling can reconstruct the active bands into isolated, extremely flat band pairs near K^{+/-} [@Wang2020].""",
    lkm_id="gcn_9f7dbaf8f0014316",
    source_paper="paper:812527076643962881",
    provenance_source="lkm_decomposition",
    decomposition_of="gcn_9f7dbaf8f0014316",
    lkm_original=_ROOT_ORIGINAL,
)


helper_single_valley_sixteen_dirac_structure = claim(
    r"""Within Wang et al.'s near-first-magic-angle, single-valley four-band continuum spectrum for TBG on a transition metal dichalcogenide, the reconstructed active bands exhibit a sixteen-Dirac-point structure [@Wang2020].""",
    lkm_id="gcn_9f7dbaf8f0014316",
    source_paper="paper:812527076643962881",
    provenance_source="lkm_decomposition",
    decomposition_of="gcn_9f7dbaf8f0014316",
    lkm_original=_ROOT_ORIGINAL,
)


helper_chern_phase_diagram_scope = claim(
    r"""Wang et al.'s Chern-number phase diagrams for TBG-on-TMD isolated active bands are scoped to the continuum two-decoupled-valley model near the first magic angle, where the active flat bands are isolated from remote bands and narrow enough for proximate terms to reconstruct them [@Wang2020].""",
    lkm_id="gcn_9f7dbaf8f0014316",
    source_paper="paper:812527076643962881",
    provenance_source="lkm_decomposition",
    decomposition_of="gcn_9f7dbaf8f0014316",
    lkm_original=_ROOT_ORIGINAL,
)


helper_away_from_magic_angle_no_reconstruction = claim(
    r"""In Wang et al.'s TBG-on-TMD continuum setting, if the twist angle is too far from the first magic angle and the active-band bandwidth is much larger than the proximate Rashba, Ising, and sublattice couplings, Rashba coupling is not expected to reconstruct the active bands, so the reported band topology and extreme flatness need not occur [@Wang2020].""",
    lkm_id="gcn_9f7dbaf8f0014316",
    source_paper="paper:812527076643962881",
    provenance_source="lkm_decomposition",
    decomposition_of="gcn_9f7dbaf8f0014316",
    lkm_original=_ROOT_ORIGINAL,
)


gfac_c68ea7fe_magic_angle_regime_to_reconstruction_scope = deduction(
    [gcn_fb78cfd7_magic_angle_continuum_regime],
    gcn_9f7dbaf8_substrate_flat_band_topology_regime,
    reason=(
        "1. State the applicability domain of the continuum two-decoupled-valley model: require that the TBG twist angle be small enough so that valley-mixing terms are negligible and the two-valley continuum approximation is valid (i.e., the low-energy physics can be described by separate $\\tau=\\pm$ valley moire Hamiltonians).\n"
        "2. Specify the additional constraint that the twist angle must be sufficiently close to the first magic angle (approximately $\\theta^{*}\\sim 1.08^{\\circ}$) so that (i) the eight active flat bands near charge neutrality are well separated from remote bands by an appreciable gap, and (ii) the bandwidth of the active eight bands is comparable to or smaller than the realistic proximity-induced energy scales (Rashba $\\sim 16\\ \\text{meV}$, Ising $\\sim 1\\ \\text{meV}$, sublattice splitting $u\\sim 1$-$2\\ \\text{meV}$); these two conditions ensure that the proximity terms can reconstruct the active bands and induce the topological phenomena described.\n"
        "3. Explain the failure mode when away from this regime: if the twist angle is too far from the first magic angle so that the active-band bandwidth becomes large compared to the SOC strengths, the Rashba and other proximity couplings will be too weak relative to the kinetic bandwidth to significantly reconstruct the active bands; consequently the Rashba-induced splitting that produces extremely-flat pairs near $K^{\\pm}$, the 16 Dirac-point structure, and the Chern-number phase diagrams derived for the reconstructed bands will not occur.\n"
        "4. Conclude that the reconstructed-band phenomena reported in this work (isolated flat pairs at $K^{\\pm}$, the sixteen-Dirac pattern, and the computed valley-Chern and time-reversal TI phase diagrams) apply within the continuum, two-decoupled-valley description appropriate for small twist angles and require being sufficiently close to the first magic angle so that the active eight bands are narrow and separated from remote bands; outside this regime the reported topology and extreme flatness are not expected to be realized."
    ),
    prior=0.95,
)


strat_decompose_rashba_isolated_flat_pairs = support(
    [gcn_9f7dbaf8_substrate_flat_band_topology_regime],
    helper_rashba_isolated_flat_pairs,
    reason=(
        "The selected LKM root explicitly names Rashba-induced isolated extremely "
        "flat band pairs near K^{+/-}, and factor steps 2-4 scope this statement "
        "to the near-first-magic-angle active-band regime."
    ),
    prior=0.90,
)


strat_decompose_sixteen_dirac_structure = support(
    [gcn_9f7dbaf8_substrate_flat_band_topology_regime],
    helper_single_valley_sixteen_dirac_structure,
    reason=(
        "The selected LKM root explicitly names the sixteen-Dirac-point structure "
        "in the single-valley four-band spectrum as one of the reconstructed-band "
        "phenomena covered by the scoped conclusion."
    ),
    prior=0.90,
)


strat_decompose_chern_phase_diagram_scope = support(
    [
        gcn_fb78cfd7_magic_angle_continuum_regime,
        gcn_9f7dbaf8_substrate_flat_band_topology_regime,
    ],
    helper_chern_phase_diagram_scope,
    reason=(
        "The LKM premise provides the model and near-magic-angle isolation "
        "conditions, while the selected root names the computed Chern-number "
        "phase diagrams for isolated active bands within that regime."
    ),
    prior=0.90,
)


strat_decompose_away_from_magic_angle_failure = support(
    [gcn_9f7dbaf8_substrate_flat_band_topology_regime],
    helper_away_from_magic_angle_no_reconstruction,
    reason=(
        "The selected LKM root and factor step 3 explicitly state the failure "
        "mode: away from the first magic angle, large active-band bandwidth makes "
        "proximate couplings too weak to reconstruct the active bands."
    ),
    prior=0.90,
)
