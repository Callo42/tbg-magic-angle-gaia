"""paper_uchida2014 -- Kohn-Sham velocity collapse and flat bands in TBG.

Source: Atomic corrugation and electron localization due to Moire patterns in
twisted bilayer graphenes
DOI: 10.1103/physrevb.90.155451
Reference key: Uchida2014
"""

from gaia.lang import claim, deduction


gcn_159120a419184e9e = claim(
    "For commensurate twisted bilayer graphene unit cells labeled by integer pairs (N,N-1), Uchida et al. represent out-of-plane corrugation z(r) by a two-dimensional Fourier series, fit dominant coefficients from optimized larger-angle geometries, extrapolate those coefficients for theta<2 degrees, reconstruct z(r), and use the resulting corrugated geometries as inputs for small-angle band-structure calculations near theta=0.99 degrees [@Uchida2014].",
    lkm_id="gcn_159120a419184e9e",
    source_paper="paper:814686513320165384",
    provenance_source="lkm",
    provenance_file="artifacts/lkm-discovery/input/may4_evidence_gcn_848085b12d384915.json",
    lkm_original="For commensurate twisted bilayer graphene unit cells labeled by integer indices (N,N-1), the atomic corrugation z(r) is represented by a two-dimensional Fourier series; fitted dominant coefficients are extrapolated for small twist angles theta<2 degrees and used as geometry input for band-structure calculations.",
)

gcn_75a1c2477ca448b0 = claim(
    "In Uchida et al.'s Kohn-Sham calculations for twisted bilayer graphene, the quoted magic angle theta_M about 1.08 degrees is defined by the vanishing Dirac Fermi velocity and depends on extrapolated small-angle atomic geometries, finite real-space grids, chosen pseudopotentials, and the LDA exchange-correlation approximation with limited vdW-DF checks [@Uchida2014].",
    lkm_id="gcn_75a1c2477ca448b0",
    source_paper="paper:814686513320165384",
    provenance_source="lkm",
    provenance_file="artifacts/lkm-discovery/input/may4_evidence_gcn_848085b12d384915.json",
    lkm_original="Let the Dirac Fermi velocity be v_F=(1/hbar) partial epsilon / partial k at the Dirac point; the reported magic twist angle theta_M about 1.08 degrees is obtained from band-structure computations that depend on extrapolated small-angle geometries and numerical approximations.",
)

gcn_390a496067b94209 = claim(
    "Uchida et al. interpret half-filled flat Kohn-Sham bands at charge neutrality in twisted bilayer graphene as indicating a possible tendency toward magnetic ordering upon slight twisting, while acknowledging that explicit spin-polarized total-energy comparisons, Hubbard-model analysis, or many-body calculations would be required to establish spontaneous magnetism [@Uchida2014].",
    lkm_id="gcn_390a496067b94209",
    source_paper="paper:814686513320165384",
    provenance_source="lkm",
    provenance_file="artifacts/lkm-discovery/input/may4_evidence_gcn_848085b12d384915.json",
    lkm_original="When the computed single-particle Kohn-Sham band structure at charge neutrality shows two nearly dispersionless half-filled bands, the presence of half-filled flat Kohn-Sham bands is interpreted as indicating a tendency toward magnetic ordering, despite the absence of explicit spin-polarized or many-body calculations.",
)

gcn_848085b12d384915 = claim(
    "Uchida et al.'s Kohn-Sham band-structure calculations for twisted bilayer graphene find a magic twist angle theta_M about 1.08 degrees where the Dirac Fermi velocity vanishes; near this angle the low-energy Kohn-Sham bands become extremely flat over most of the Brillouin zone, including nearly dispersionless half-filled bands around E_F and about 10 meV splitting between flat bands at Gamma for theta=0.99 degrees [@Uchida2014].",
    lkm_id="gcn_848085b12d384915",
    source_paper="paper:814686513320165384",
    provenance_source="lkm",
    provenance_file="artifacts/lkm-discovery/input/may4_evidence_gcn_848085b12d384915.json",
    lkm_original="The computed dependence of the Kohn-Sham Dirac Fermi velocity on twist angle for twisted bilayer graphene exhibits a magic twist angle theta_M approximately 1.08 degrees at which the Kohn-Sham Fermi velocity vanishes; nearby, low-energy Kohn-Sham bands become extremely flat across most of the Brillouin zone.",
)

gfac_e7f366dda20d45cf = deduction(
    [gcn_159120a419184e9e, gcn_75a1c2477ca448b0, gcn_390a496067b94209],
    gcn_848085b12d384915,
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
