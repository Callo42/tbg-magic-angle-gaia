"""paper_uchida2014 -- Kohn-Sham velocity collapse and flat bands in TBG.

Source: Atomic corrugation and electron localization due to Moire patterns in
twisted bilayer graphenes
DOI: 10.1103/physrevb.90.155451
Reference key: Uchida2014
"""

from gaia.lang import claim, deduction


small_angle_corrugation_extrapolation = claim(
    "For commensurate twisted bilayer graphene unit cells labeled by integer pairs (N,N-1), Uchida et al. represent out-of-plane corrugation z(r) by a two-dimensional Fourier series, fit dominant coefficients from optimized larger-angle geometries, extrapolate those coefficients for theta<2 degrees, reconstruct z(r), and use the resulting corrugated geometries as inputs for small-angle band-structure calculations near theta=0.99 degrees [@Uchida2014].",
    lkm_id="gcn_159120a419184e9e",
    source_paper="paper:814686513320165384",
    provenance_source="lkm",
    provenance_file="artifacts/lkm-discovery/input/may4_evidence_gcn_848085b12d384915.json",
    lkm_original=r"""For commensurate twisted bilayer graphene (tBLG) unit cells labeled by integer indices $(N,N-1)$, let the lateral coordinates be $\\mathbf{r}=(x,y)$ in the plane of the layers and let $z(\\mathbf{r})$ denote the out-of-plane atomic coordinate (height) of atoms relative to a reference plane; the atomic corrugation $z(\\mathbf{r})$ is represented by the two-dimensional Fourier series
      $$
      z(\\mathbf{r})=\\sum_{j=0}^{\\infty}\\{\\alpha_j\\cos(\\mathbf{G}_j\\cdot\\mathbf{r})+\\beta_j\\sin(\\mathbf{G}_j\\cdot\\mathbf{r})\\},
      $$
      where $\\{\\mathbf{G}_j\\}$ are the reciprocal-lattice vectors of the lateral supercell and $\\{\\alpha_j,\\beta_j\\}$ are the corresponding Fourier coefficients; the procedure used to obtain atomic geometries for small twist angles $\\theta<2^{\\circ}$ in these $(N,N-1)$ commensurate cells is: compute Fourier coefficients $\\{\\alpha_j,\\beta_j\\}$ for fully optimized geometries at larger $\\theta$, fit the dominant coefficient $\\alpha_1$ (the cosine coefficient associated with the shortest nonzero reciprocal vector $\\mathbf{G}_1$) as a smooth Gaussian function of $\\theta$, extrapolate the small-$\\theta$ values of the dominant coefficients (the first seven shortest reciprocal vectors are assumed to dominate the corrugation) using these Gaussian fits, reconstruct $z(\\mathbf{r})$ from the extrapolated dominant coefficients, and use the resulting extrapolated corrugated geometry as input for band-structure calculations at $\\theta\\approx0.99^{\\circ}$ and similar small angles.
      Uchida et al., PHYS. REV. B 90, 155451 (2014), Appendix D""",
)

kohn_sham_magic_angle_numerical_scope = claim(
    "In Uchida et al.'s Kohn-Sham calculations for twisted bilayer graphene, the quoted magic angle theta_M about 1.08 degrees is defined by the vanishing Dirac Fermi velocity and depends on extrapolated small-angle atomic geometries, finite real-space grids, chosen pseudopotentials, and the LDA exchange-correlation approximation with limited vdW-DF checks [@Uchida2014].",
    lkm_id="gcn_75a1c2477ca448b0",
    source_paper="paper:814686513320165384",
    provenance_source="lkm",
    provenance_file="artifacts/lkm-discovery/input/may4_evidence_gcn_848085b12d384915.json",
    lkm_original=r"""Let the Dirac Fermi velocity be $v_{\\mathrm{F}}\\equiv(1/\\hbar)\\partial\\varepsilon/\\partial k$ evaluated at the Dirac point in the Kohn-Sham band structure; the proposition is that the reported numerical value of the magic twist angle $\\theta_{\\mathrm{M}}\\approx 1.08^{\\circ}$, defined by the vanishing Kohn-Sham $v_{\\mathrm{F}}$, is obtained from band-structure computations that depend on (i) atomic geometries for $\\theta<2^{\\circ}$ constructed by extrapolating Fourier coefficients fitted from larger-$\\theta$ geometry optimizations, (ii) finite numerical real-space grids and the chosen pseudopotentials, and (iii) the chosen exchange-correlation approximation (LDA with limited vdW-DF checks); therefore the numeric value $1.08^{\\circ}$ is tied to these computational approximations and the stated precision assumes these approximations place the Kohn-Sham zero-crossing within the quoted uncertainty.""",
)

half_filled_flat_band_magnetism_tendency = claim(
    "Uchida et al. interpret half-filled flat Kohn-Sham bands at charge neutrality in twisted bilayer graphene as indicating a possible tendency toward magnetic ordering upon slight twisting, while acknowledging that explicit spin-polarized total-energy comparisons, Hubbard-model analysis, or many-body calculations would be required to establish spontaneous magnetism [@Uchida2014].",
    lkm_id="gcn_390a496067b94209",
    source_paper="paper:814686513320165384",
    provenance_source="lkm",
    provenance_file="artifacts/lkm-discovery/input/may4_evidence_gcn_848085b12d384915.json",
    lkm_original=r"""When the computed single-particle Kohn-Sham band structure at charge neutrality for twisted bilayer graphene shows two nearly dispersionless bands crossing the Kohn-Sham Fermi level $E_{\\mathrm{F}}$ that are half filled under the single-particle occupation, the proposition asserted is that the presence of half-filled flat Kohn-Sham bands is interpreted as indicating a tendency toward magnetic ordering (spontaneous spin polarization) upon slight twisting, despite the absence of explicit spin-polarized total-energy comparisons, Hubbard-model analyses, or many-body calculations that would be required to establish spontaneous magnetism and to determine its character.""",
)

kohn_sham_magic_angle_flat_bands = claim(
    "Uchida et al.'s Kohn-Sham band-structure calculations for twisted bilayer graphene find a magic twist angle theta_M about 1.08 degrees where the Dirac Fermi velocity vanishes; near this angle the low-energy Kohn-Sham bands become extremely flat over most of the Brillouin zone, including nearly dispersionless half-filled bands around E_F and about 10 meV splitting between flat bands at Gamma for theta=0.99 degrees [@Uchida2014].",
    lkm_id="gcn_848085b12d384915",
    source_paper="paper:814686513320165384",
    provenance_source="lkm",
    provenance_file="artifacts/lkm-discovery/input/may4_evidence_gcn_848085b12d384915.json",
    lkm_original=r"""The computed dependence of the Kohn-Sham Dirac Fermi velocity on twist angle for twisted bilayer graphene (tBLG) exhibits a magic twist angle $\\theta_{\\mathrm{M}}\\approx 1.08^{\\circ}$ at which the Kohn-Sham Fermi velocity $v_{\\mathrm{F}}$ vanishes ($v_{\\mathrm{F}}=0$); in the vicinity of this angle the low-energy Kohn-Sham bands become extremely flat across most of the Brillouin zone, producing two nearly dispersionless bands that are half filled at the single-particle Kohn-Sham Fermi level $E_{\\mathrm{F}}$ (for example, at $\\theta=0.99^{\\circ}$ the calculated Kohn-Sham band structure shows nearly dispersionless bands around $E_{\\mathrm{F}}$ and an energy splitting of about $10\\ \\mathrm{meV}$ between these flat bands at the $\\Gamma$ point), and the computed function $v_{\\mathrm{F}}(\\theta)$ is nonmonotonic at small $\\theta$, vanishing at $\\theta_{\\mathrm{M}}$ and increasing slightly for still smaller $\\theta$.""",
)

derive_kohn_sham_magic_angle_flat_bands = deduction(
    [
        small_angle_corrugation_extrapolation,
        kohn_sham_magic_angle_numerical_scope,
        half_filled_flat_band_magnetism_tendency,
    ],
    kohn_sham_magic_angle_flat_bands,
    reason=(
        "1. Start from upstream localization and velocity-reduction results in "
        "small-angle corrugated twisted bilayer graphene.\n"
        "2. Define the magic angle as the twist angle where Kohn-Sham Dirac "
        "Fermi velocity v_F=(1/hbar) d epsilon / d k vanishes.\n"
        "3. Report that theta=0.99 degrees has extremely flat bands near E_F "
        "and about 10 meV splitting between the flat bands at Gamma.\n"
        "4. Extract theta_M about 1.08 degrees from the computed velocity-versus-angle curve.\n"
        "5. Relate AA-region localization to reduced dispersion and half-filled flat bands.\n"
        "6. Note consistency with earlier continuum and tight-binding predictions while preserving the different numerical method."
    ),
    prior=0.95,
)
