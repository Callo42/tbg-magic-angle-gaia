"""paper_cantele2020 -- claims and deduction for Cantele et al. 2020.

Source: Structural relaxation and low-energy properties of twisted bilayer graphene
DOI: 10.1103/physrevresearch.2.043127
Authors: Giovanni Cantele | Dario Alfe | Felice Conte | Vittorio Cataudella | Domenico Ninno | Procolo Lucignano
Reference key (CSL): Cantele2020
"""

from gaia.lang import claim, deduction


dft_gap_spectroscopy_comparison_assumption = claim(
    "For first-magic-angle twisted bilayer graphene, comparing plane-wave DFT "
    "Kohn-Sham gaps computed with the vdW-DF2 exchange-correlation functional "
    "against spectroscopic gaps assumes that electron-electron correlation and "
    "quasiparticle self-energy corrections do not substantially renormalize "
    "the relevant gap magnitudes, so DFT gaps of about $26\\,\\mathrm{meV}$ "
    "and $16\\,\\mathrm{meV}$ can be quantitatively compared to nano-ARPES or "
    "tunneling spectroscopy in the same energy window [@Cantele2020].",
    lkm_id="gcn_6463be97083b44fd",
    source_paper="paper:812551532191940608",
    provenance_source="lkm",
    lkm_original=(
        "For twisted bilayer graphene at the first magic angle, interpreting "
        "agreement between experimentally measured spectroscopic gap magnitudes "
        "and single-particle Kohn–Sham eigenvalue gaps computed in plane-wave "
        "density-functional theory using the vdW-DF2 exchange-correlation "
        "functional assumes that electron-electron correlation effects and "
        "quasiparticle self-energy corrections do not substantially renormalize "
        "the relevant band-gap magnitudes, so that computed gaps of order "
        "$\\sim 26\\,\\text{meV}$ and $\\sim 16\\,\\text{meV}$ can be "
        "quantitatively compared to spectroscopic gaps (e.g., from nano-ARPES "
        "or tunneling spectroscopy) in the same energy window."
    ),
)

relaxation_component_diagnostic_assumption = claim(
    "For twisted bilayer graphene at $\\theta=1.08^\\circ$, using two "
    "constrained optimizations--out-of-plane-only relaxation with fixed "
    "in-plane coordinates and in-plane-only relaxation with fixed z "
    "coordinates--is treated as a meaningful diagnostic separation of the "
    "electronic effects of the two relaxation components, while retaining the "
    "caveat that the fully relaxed structure may couple in-plane and "
    "out-of-plane degrees of freedom nonlinearly [@Cantele2020].",
    lkm_id="gcn_abaf80790d664630",
    source_paper="paper:812551532191940608",
    provenance_source="lkm",
    lkm_original=(
        "For twisted bilayer graphene at twist angle $\\theta=1.08^\\circ$, "
        "performing two constrained structural optimizations—one allowing only "
        "out-of-plane ($z$) displacements while keeping all in-plane coordinates "
        "fixed, and one allowing only in-plane ($x$-$y$) displacements while "
        "keeping all $z$ coordinates fixed—and then computing band structures "
        "on these partially relaxed geometries is assumed to provide a "
        "meaningful diagnostic separation of the electronic consequences of "
        "out-of-plane versus in-plane relaxation components, despite the "
        "possibility of nonlinear coupling between in-plane and out-of-plane "
        "degrees of freedom in an unconstrained full relaxation."
    ),
)

full_relaxation_reproduces_flat_band_gaps = claim(
    "For twisted bilayer graphene at the first magic twist angle "
    "$\\theta=1.08^\\circ$, plane-wave DFT with vdW-DF2 reproduces the "
    "near-Fermi narrow flat-band manifold and the $\\Gamma$-point gaps to "
    "higher and lower bands only when full atomic relaxation includes both "
    "in-plane and out-of-plane displacements. In the fully relaxed geometry, "
    "the reported flat-band bandwidth is about $20\\,\\mathrm{meV}$, with "
    "upper and lower separation gaps of about $26\\,\\mathrm{meV}$ and "
    "$16\\,\\mathrm{meV}$, and tight-binding calculations on the same relaxed "
    "coordinates give consistent low-energy bands. Unrelaxed flat geometries "
    "lack or strongly underestimate these gaps; in-plane-only relaxation gives "
    "zero gaps, while out-of-plane-only relaxation gives underestimated gaps "
    "of about $2\\,\\mathrm{meV}$ and $14\\,\\mathrm{meV}$ [@Cantele2020].",
    lkm_id="gcn_de1d329f326f4e75",
    source_paper="paper:812551532191940608",
    provenance_source="lkm",
    lkm_original=(
        "For twisted bilayer graphene at the first magic twist angle "
        "$\\theta=1.08^\\circ$, the single-particle electronic structure "
        "computed by density functional theory (DFT) shows that the narrow "
        "flat-band manifold near the Fermi energy and the energy gaps at the "
        "$\\Gamma$ point separating that manifold from higher- and lower-energy "
        "bands are reproduced only when full atomic relaxation is included, "
        "where full relaxation includes both in-plane ($x$-$y$) and "
        "out-of-plane ($z$) atomic displacements relative to the initial "
        "twisted but flat bilayer geometry. For the fully relaxed geometry at "
        "$\\theta=1.08^\\circ$, the reported flat-band bandwidth is "
        "$\\sim 20\\,\\text{meV}$, the gap separating the flat-band manifold "
        "from the higher-energy bands is $\\approx 26\\,\\text{meV}$, and the "
        "gap separating the flat-band manifold from the lower-energy bands is "
        "$\\approx 16\\,\\text{meV}$, and tight-binding calculations evaluated "
        "on the same relaxed atomic coordinates yield consistent low-energy "
        "bands. For the unrelaxed flat bilayer geometry these $\\Gamma$-point "
        "gaps are absent or strongly underestimated, and for constrained "
        "relaxations at $\\theta=1.08^\\circ$ the in-plane-only relaxed "
        "geometry (fixed $z$ coordinates) yields zero gaps while the "
        "out-of-plane-only relaxed geometry (fixed $x$-$y$ coordinates) yields "
        "underestimated gaps of order $\\sim 2\\,\\text{meV}$ (upper side) and "
        "$\\sim 14\\,\\text{meV}$ (lower side)."
    ),
)

derive_full_relaxation_reproduces_flat_band_gaps = deduction(
    [
        dft_gap_spectroscopy_comparison_assumption,
        relaxation_component_diagnostic_assumption,
    ],
    full_relaxation_reproduces_flat_band_gaps,
    reason=(
        "1. State upstream result being used as known: the atomistic relaxation "
        "patterns induced by interlayer vdW interactions and their quantitative "
        "aspects (out-of-plane buckling, in-plane vortexlike displacements, "
        "shrinking of AA regions, and numerical displacement magnitudes) are "
        "taken as established from the previously reconstructed structural "
        "analysis (conclusion 1). These relaxed atomic geometries are the "
        "starting point for the following electronic-structure deductions.\n"
        "2. Summarize the computational approach used to obtain electronic band "
        "structures from relaxed and unrelaxed geometries: single-particle "
        "electronic structures were computed using DFT within the same "
        "VASP/vdW-DF2 framework (self-consistent-field runs sampled at the "
        "$\\Gamma$ point for the large supercells), and complementary "
        "tight-binding calculations were performed using a Slater-Koster "
        "parametrization for $p_z$ orbitals with atom positions taken from the "
        "relaxed geometries. Non-self-consistent calculations at other $k$ "
        "points used the SCF reference; for the smallest cell only one $k$ "
        "point could be computed at a time and energies are referred to the SCF "
        "Fermi energy. These computational procedures produce band structures "
        "for relaxed and unrelaxed atomic configurations that are directly "
        "compared. [51]\n"
        "3. Compare relaxed versus unrelaxed band structures at the first magic "
        "angle $\\theta=1.08^\\circ$: the band-structure plots along the "
        "$K-\\Gamma-M-K'$ path show that including full atomic relaxation is "
        "necessary to reproduce the experimentally observed narrow flat-band "
        "manifold and the energy gaps that separate that manifold from both "
        "higher and lower energy bands. The fully relaxed DFT band structure "
        "shows a bandwidth of approximately $20\\,\\mathrm{meV}$ and gaps of "
        "about $26\\,\\mathrm{meV}$ on the electron side and about "
        "$16\\,\\mathrm{meV}$ on the hole side. Fig. 5\n"
        "4. State the failure of unrelaxed geometries to reproduce the "
        "experimental gaps: band structures computed for unrelaxed flat bilayer "
        "geometries lack the energy gaps isolating the flat-band manifold at "
        "$\\theta=1.08^\\circ$, or greatly underestimate them, while relaxed "
        "panels show the gaps. Fig. 5\n"
        "5. Report partial-relaxation tests and their electronic consequences: "
        "in-plane-only relaxation produces essentially zero energy gaps, "
        "whereas out-of-plane-only relaxation produces nonzero but "
        "underestimated gaps of approximately $2\\,\\mathrm{meV}$ and "
        "$14\\,\\mathrm{meV}$ on the two sides. Fig. 6\n"
        "6. Note the agreement between DFT and tight-binding when using the "
        "relaxed geometry: tight-binding calculations using the Slater-Koster "
        "$p_z$ parametrization on the DFT-relaxed atomic positions reproduce "
        "the DFT bands closely near the Fermi energy, indicating that the "
        "relaxed geometry is the essential ingredient for the observed flat "
        "bands and gaps. Fig. 5"
    ),
    prior=0.95,
)
