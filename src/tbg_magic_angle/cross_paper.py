"""cross_paper -- grounded synthesis across validated TBG root subgraphs.

The parent package keeps subgraph directories unchanged and wires only scoped
support claims. No equivalence() or contradiction() is emitted because the
selected roots differ by system, twist-angle regime, pressure/substrate
condition, layer count, or model/experimental observable.
"""

from gaia.lang import claim, support

from .paper_cao2018 import gcn_006f88d8_ma_tbg_superconducting_domes
from .paper_dassarma2020 import gcn_7bca73ad98eb4ed4
from .paper_herzogarbeitman2022 import gcn_afdfbd0c013048d8
from .paper_ge2021 import gcn_105d2fc961f949b6
from .paper_yamada2020 import gcn_8159f32d_merged_dirac_magic_angle_flat_band
from .paper_ma2020 import gcn_f23eff9c755840f2
from .paper_ma2019 import gcn_2cf09f115b814154
from .paper_burg2022 import gcn_225da7b3_atqg_angle_phase_decoupling
from .paper_nguyen2022 import gcn_14a55aff_smab2_flat_band_localization
from .paper_tritsaris2020 import gcn_5f58746b_magic_angle_flat_band_likelihood
from .paper_liu2020 import gcn_c220df1acc8b476a
from .paper_cantele2020 import gcn_de1d329f326f4e75
from .paper_zhang2019 import gcn_584669e24c6145a7
from .paper_wang2020 import gcn_9f7dbaf8_substrate_flat_band_topology_regime
from .paper_park2021 import gcn_b4e3bdff_mattg_mirror_flat_dirac_control


parent_tbg_flat_band_to_correlated_phenomenology = claim(
    "The selected TBG roots connect a magic-angle flat-band mechanism to correlated phase phenomenology: BM-continuum velocity suppression near the first magic angle and ab initio flat-band detection near theta about 1.1 degrees provide single-particle flat-band context, while Cao et al. observe superconducting domes adjacent to correlated insulating behavior in MA-TBG devices [@DasSarma2020; @Tritsaris2020; @Cao2018].",
    provenance_source="parent_synthesis",
    source_roots=[
        "gcn_7bca73ad98eb4ed4",
        "gcn_5f58746bcc0b4098",
        "gcn_006f88d8df3548fa",
    ],
    synthesis_scope="connects mechanism context to phenomenology without claiming BM alone proves superconductivity",
)

parent_scoped_flat_band_variants = claim(
    "The pressure-tuned, merged-Dirac, magnetic-Bloch, few-layer-graphite, and ab initio roots are scoped variants of flat-band formation or detection around moire graphene: they share flat or velocity-suppressed bands as the theme, but differ by pressure, flux, commensuration, continuum/tight-binding method, or multilayer geometry [@Ge2021; @Yamada2020; @HerzogArbeitman2022; @Ma2020; @Tritsaris2020].",
    provenance_source="parent_synthesis",
    source_roots=[
        "gcn_105d2fc961f949b6",
        "gcn_8159f32dda354258",
        "gcn_afdfbd0c013048d8",
        "gcn_f23eff9c755840f2",
        "gcn_5f58746bcc0b4098",
    ],
    synthesis_scope="support/scope bridge only; not a claim of identical mechanisms or systems",
)

parent_multilayer_extensions_not_equivalent_to_tbg = claim(
    "The twisted trilayer, alternating-twist quadrilayer, and twisted monolayer-bilayer roots are nearby moire graphene extensions rather than equivalents of magic-angle TBG: each uses a different stacking or layer count and the selected LKM claims explicitly scope their flat-band or correlated-phase behavior to those geometries [@Ma2019; @Burg2022; @Nguyen2022].",
    provenance_source="parent_synthesis",
    source_roots=[
        "gcn_2cf09f115b814154",
        "gcn_225da7b340cb47b8",
        "gcn_14a55aff3de24a3a",
    ],
    synthesis_scope="nearby moire-graphene extension; keep distinct from TBG equivalence",
)

parent_no_same_scope_contradiction_found = claim(
    "Across the selected TBG, substrate-perturbed TBG, and nearby multilayer moire roots, the parent synthesis treats apparent differences in angles, relaxation protocols, substrate perturbations, pressure response, multilayer behavior, and correlated-phase trends as scope distinctions because the source claims do not assert incompatible values for the same system under the same conditions.",
    provenance_source="parent_synthesis_audit",
    source_roots=[
        "gcn_006f88d8df3548fa",
        "gcn_7bca73ad98eb4ed4",
        "gcn_afdfbd0c013048d8",
        "gcn_105d2fc961f949b6",
        "gcn_8159f32dda354258",
        "gcn_f23eff9c755840f2",
        "gcn_2cf09f115b814154",
        "gcn_225da7b340cb47b8",
        "gcn_14a55aff3de24a3a",
        "gcn_5f58746bcc0b4098",
        "gcn_c220df1acc8b476a",
        "gcn_de1d329f326f4e75",
        "gcn_584669e24c6145a7",
        "gcn_9f7dbaf8f0014316",
        "gcn_b4e3bdff3c0c439a",
    ],
    synthesis_scope="audit conclusion; no contradiction() emitted",
)

parent_relaxation_dft_realistic_flat_band_modeling = claim(
    "The lattice-reconstruction, DFT-relaxation, and ab initio roots support a more realistic modeling scope for magic-angle TBG flat bands: relaxation-aware continuum modeling explains broader and better isolated flat bands, full in-plane and out-of-plane DFT relaxation is needed for first-magic-angle gaps and narrow bands, and Wannier-based ab initio workflows provide an independent flat-band detection context [@Liu2020; @Cantele2020; @Tritsaris2020].",
    provenance_source="parent_synthesis",
    source_roots=[
        "gcn_c220df1acc8b476a",
        "gcn_de1d329f326f4e75",
        "gcn_5f58746bcc0b4098",
    ],
    synthesis_scope="support bridge for relaxation-aware and first-principles flat-band modeling; not an equivalence between continuum, DFT, and Wannier workflows",
)

parent_substrate_topological_perturbation_scope = claim(
    "The h-BN-aligned and transition-metal-dichalcogenide substrate roots support a substrate/topological perturbation scope for magic-angle TBG: h-BN alignment introduces a staggered-mass continuum term with valley Chern active bands, while TBG on a TMD is scoped to near-first-magic-angle active bands where proximate Rashba, Ising, and sublattice terms can reconstruct flat bands and Chern-number phase diagrams [@Zhang2019; @Wang2020].",
    provenance_source="parent_synthesis",
    source_roots=[
        "gcn_584669e24c6145a7",
        "gcn_9f7dbaf8f0014316",
    ],
    synthesis_scope="support bridge for substrate-induced topology; not an equivalence between h-BN and TMD perturbations",
)

parent_mattg_superconducting_moire_extension_not_equivalent = claim(
    "The Park et al. MATTG root extends the superconducting magic-angle moire graphene family beyond bilayer TBG, but it is not equivalent to MA-TBG: MATTG uses mirror-symmetric A-tw-A trilayer geometry with a larger magic angle near 1.6 degrees and displacement-field-tunable flat/Dirac-band hybridization, whereas the Cao et al. root concerns bilayer MA-TBG superconducting domes adjacent to correlated insulating states [@Park2021; @Cao2018].",
    provenance_source="parent_synthesis",
    source_roots=[
        "gcn_b4e3bdff3c0c439a",
        "gcn_006f88d8df3548fa",
    ],
    synthesis_scope="nearby superconducting magic-angle moire-family extension; explicitly not TBG equivalence",
)

strat_parent_flat_band_to_correlated_phenomenology = support(
    [
        gcn_7bca73ad98eb4ed4,
        gcn_5f58746b_magic_angle_flat_band_likelihood,
        gcn_006f88d8_ma_tbg_superconducting_domes,
    ],
    parent_tbg_flat_band_to_correlated_phenomenology,
    reason=(
        "BM velocity suppression and ab initio flat-band likelihood ground the "
        "single-particle magic-angle flat-band context, while the Cao root "
        "grounds the correlated-insulator and superconducting-dome phenomenology. "
        "This is a scoped synthesis bridge, not an equivalence or causal proof."
    ),
    prior=0.82,
)

strat_parent_scoped_flat_band_variants = support(
    [
        gcn_105d2fc961f949b6,
        gcn_8159f32d_merged_dirac_magic_angle_flat_band,
        gcn_afdfbd0c013048d8,
        gcn_f23eff9c755840f2,
        gcn_5f58746b_magic_angle_flat_band_likelihood,
    ],
    parent_scoped_flat_band_variants,
    reason=(
        "Each premise is a validated selected root about flat-band formation, "
        "velocity suppression, or flat-band detection in a scoped moire graphene "
        "setting. Their shared theme supports a parent variant claim while their "
        "different regimes prevent equivalence."
    ),
    prior=0.78,
)

strat_parent_multilayer_extensions_not_equivalent = support(
    [
        gcn_2cf09f115b814154,
        gcn_225da7b3_atqg_angle_phase_decoupling,
        gcn_14a55aff_smab2_flat_band_localization,
    ],
    parent_multilayer_extensions_not_equivalent_to_tbg,
    reason=(
        "The trilayer, quadrilayer, and monolayer-bilayer roots all preserve "
        "their own layer geometry and reported behavior. They support a nearby-"
        "extension synthesis claim and explicitly do not justify equivalence to TBG."
    ),
    prior=0.80,
)

strat_parent_no_same_scope_contradiction = support(
    [
        gcn_006f88d8_ma_tbg_superconducting_domes,
        gcn_7bca73ad98eb4ed4,
        gcn_afdfbd0c013048d8,
        gcn_105d2fc961f949b6,
        gcn_8159f32d_merged_dirac_magic_angle_flat_band,
        gcn_f23eff9c755840f2,
        gcn_2cf09f115b814154,
        gcn_225da7b3_atqg_angle_phase_decoupling,
        gcn_14a55aff_smab2_flat_band_localization,
        gcn_5f58746b_magic_angle_flat_band_likelihood,
        gcn_c220df1acc8b476a,
        gcn_de1d329f326f4e75,
        gcn_584669e24c6145a7,
        gcn_9f7dbaf8_substrate_flat_band_topology_regime,
        gcn_b4e3bdff_mattg_mirror_flat_dirac_control,
    ],
    parent_no_same_scope_contradiction_found,
    reason=(
        "The parent candidates, contradiction flags, and validated subgraph roots "
        "show different systems, methods, twist-angle regimes, relaxation or "
        "substrate perturbations, pressure/flux conditions, and layer counts. "
        "Those differences are logged as scope distinctions rather than "
        "contradiction edges."
    ),
    prior=0.75,
)

strat_parent_relaxation_dft_realistic_modeling = support(
    [
        gcn_c220df1acc8b476a,
        gcn_de1d329f326f4e75,
        gcn_5f58746b_magic_angle_flat_band_likelihood,
    ],
    parent_relaxation_dft_realistic_flat_band_modeling,
    reason=(
        "The Liu root grounds lattice-relaxed continuum spectroscopy trends, "
        "the Cantele root grounds full atomic relaxation in first-magic-angle "
        "DFT and tight-binding bands, and the Tritsaris root adds an ab initio "
        "flat-band likelihood workflow. Together they support realistic "
        "flat-band modeling scope without treating the methods as equivalent."
    ),
    prior=0.82,
)

strat_parent_substrate_topological_scope = support(
    [
        gcn_584669e24c6145a7,
        gcn_9f7dbaf8_substrate_flat_band_topology_regime,
    ],
    parent_substrate_topological_perturbation_scope,
    reason=(
        "The Zhang root grounds h-BN-induced staggered-mass topology in "
        "MA-TBG, while the Wang root grounds a TMD-proximity regime where "
        "substrate terms reconstruct active bands and define Chern-number "
        "phase diagrams. This is a substrate/topology scope bridge only."
    ),
    prior=0.80,
)

strat_parent_mattg_family_extension = support(
    [
        gcn_b4e3bdff_mattg_mirror_flat_dirac_control,
        gcn_006f88d8_ma_tbg_superconducting_domes,
    ],
    parent_mattg_superconducting_moire_extension_not_equivalent,
    reason=(
        "The Park root places mirror-symmetric magic-angle twisted trilayer "
        "graphene in the same broader superconducting moire graphene family, "
        "while the Cao root preserves the bilayer MA-TBG phenomenology. The "
        "different layer count and mirror-symmetry control prevent equivalence."
    ),
    prior=0.78,
)
