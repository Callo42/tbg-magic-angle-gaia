"""paper_park2021 -- LKM claims and deduction from Park et al. (2021).

Source: Tunable strongly coupled superconductivity in magic-angle twisted trilayer graphene
DOI: 10.1038/s41586-021-03192-0
Authors: Jeong Min Park | Yuan Cao | Kenji Watanabe | Takashi Taniguchi |
    Pablo Jarillo-Herrero
Reference key (CSL): Park2021
"""

from gaia.lang import claim, deduction, support


_ROOT_ORIGINAL = r"""Continuum-model calculations for mirror-symmetric A-tw-A magic-angle twisted trilayer graphene (MATTG), consisting of three graphene monolayers sequentially twisted by $+\theta$ and $-\theta$ with $\theta\approx1.57^\circ$, yield (a) mirror-symmetry-protected flat bands derived from mirror-symmetric combinations of outer-layer hopping and (b) coexisting gapless Dirac bands with opposite mirror character, such that hybridization between the flat and Dirac bands is forbidden when mirror symmetry is present. The flat bands can be mathematically reduced to magic-angle twisted bilayer graphene (MATBG)-like bands with an effective twist angle $\theta/\sqrt{2}$, implying a larger magic angle for MATTG of $\theta_{\mathrm{MATTG}}\approx1.6^\circ$. A perpendicular electric displacement field $D$ breaks the mirror symmetry and hybridizes the flat and Dirac bands, enabling in situ electrical control of the flat-band bandwidth and topology. These calculations neglect direct coupling between the topmost and bottommost graphene layers and use interlayer hopping parameters $w=0.1\ \mathrm{eV}$ and $w'=0.08\ \mathrm{eV}$, and they model the displacement field through an imposed interlayer potential difference $\Delta V=dD/\varepsilon_0$ with interlayer spacing $d\approx0.3\ \mathrm{nm}$ and vacuum permittivity $\varepsilon_0$."""

_CONTINUUM_APPROX_ORIGINAL = r"""In continuum-model calculations of mirror-symmetric A-tw-A magic-angle twisted trilayer graphene, consisting of three graphene monolayers with sequential twist angles $+\theta$ and $-\theta$, qualitative band-structure features (mirror-protected flat bands, coexisting gapless Dirac bands, and displacement-field-driven hybridization) are assumed to be captured while making the approximations of (i) neglecting direct coupling matrix elements between the topmost and bottommost graphene layers, (ii) using fixed interlayer hopping parameters $w=0.1\,\mathrm{eV}$ and $w'=0.08\,\mathrm{eV}$ (with $w'$ included empirically to mimic lattice relaxation), and (iii) representing a perpendicular displacement field $D$ by a non-self-consistent imposed interlayer potential difference $\Delta V=dD/\varepsilon_0$ with interlayer spacing $d\approx0.3\,\mathrm{nm}$ and vacuum permittivity $\varepsilon_0$. These approximations are expected to affect quantitative details such as bandwidths, particle–hole asymmetry, Van Hove singularity energies, and hybridization strengths without being assumed to eliminate the coexistence of flat and Dirac bands or the symmetry-based hybridization control by $D$."""

_THETA_MAPPING_ORIGINAL = r"""The reduction of mirror-symmetric flat bands in A-tw-A stacked twisted trilayer graphene to an effective two-layer (twisted-bilayer-like) bandstructure with an effective twist angle $\theta/\sqrt{2}$, where $\theta$ is the actual sequential twist angle between adjacent layers, is an approximate mapping that neglects higher-order coupling terms, layer-dependent relaxation effects, and deviations from ideal mirror symmetry; consequently, the numerical factor and the resulting magic-angle estimate $\theta_{\mathrm{MATTG}}\approx1.6^\circ$ depend on the neglected terms even if the mapping captures the qualitative trend that the trilayer magic angle exceeds the bilayer magic angle."""

_DISPLACEMENT_MODEL_ORIGINAL = r"""Modeling an externally applied perpendicular electric displacement field $D$ in twisted trilayer graphene by an interlayer electrostatic potential difference $\Delta V=dD/\varepsilon_0$, with interlayer spacing $d\approx0.3\,\mathrm{nm}$ and vacuum permittivity $\varepsilon_0$, assumes that neglecting self-consistent electronic screening and non-local screening corrections still qualitatively captures mirror-symmetry breaking and hybridization between flat and Dirac bands, even though the approximation can quantitatively misestimate hybridization strengths and the displacement-field values at which bandstructure features such as Van Hove singularities occur."""


gcn_c680c239_mattg_continuum_approximations = claim(
    r"""For Park et al.'s continuum-model calculation of mirror-symmetric A-tw-A magic-angle twisted trilayer graphene, with three graphene monolayers sequentially twisted by +theta and -theta, the selected LKM chain treats the calculation as qualitatively capturing mirror-protected flat bands, coexisting gapless Dirac bands, and displacement-field-driven hybridization while using three approximations: neglecting direct top-bottom layer coupling, fixing interlayer hoppings w=0.1 eV and w'=0.08 eV with w' mimicking lattice relaxation, and representing perpendicular displacement field D by a non-self-consistent interlayer potential difference Delta V=dD/epsilon_0 with d about 0.3 nm [@Park2021].""",
    lkm_id="gcn_c680c2399704407b",
    source_paper="paper:812508547391684608",
    provenance_source="lkm",
    lkm_original=_CONTINUUM_APPROX_ORIGINAL,
)

gcn_3618ccee_mattg_theta_over_sqrt2_mapping = claim(
    r"""In the selected Park et al. LKM chain, the mirror-symmetric flat bands of A-tw-A twisted trilayer graphene are approximately reduced to a twisted-bilayer-like band structure with effective twist angle theta/sqrt(2), implying a MATTG magic-angle estimate near theta_MATTG about 1.6 degrees, while the mapping is explicitly scoped by neglected higher-order coupling terms, layer-dependent relaxation effects, and deviations from ideal mirror symmetry [@Park2021].""",
    lkm_id="gcn_3618ccee24d94ab2",
    source_paper="paper:812508547391684608",
    provenance_source="lkm",
    lkm_original=_THETA_MAPPING_ORIGINAL,
)

gcn_71314760_mattg_displacement_field_modeling = claim(
    r"""In Park et al.'s MATTG continuum-model treatment, an externally applied perpendicular electric displacement field D is modeled as an imposed interlayer electrostatic potential difference Delta V=dD/epsilon_0 with interlayer spacing d about 0.3 nm; the selected LKM chain treats this non-self-consistent approximation as qualitatively capturing mirror-symmetry breaking and flat-band/Dirac-band hybridization, while warning that screening and non-local corrections can shift quantitative hybridization strengths and Van Hove singularity positions [@Park2021].""",
    lkm_id="gcn_713147608cae4a93",
    source_paper="paper:812508547391684608",
    provenance_source="lkm",
    lkm_original=_DISPLACEMENT_MODEL_ORIGINAL,
)

gcn_b4e3bdff_mattg_mirror_flat_dirac_control = claim(
    r"""For Park et al.'s mirror-symmetric A-tw-A magic-angle twisted trilayer graphene with sequential twist angles +theta and -theta and theta about 1.57 degrees, continuum-model calculations yield mirror-symmetry-protected flat bands derived from mirror-symmetric outer-layer hopping combinations and coexisting gapless Dirac bands of opposite mirror character, so flat-band/Dirac-band hybridization is forbidden when mirror symmetry is present; the flat bands map approximately to MATBG-like bands with effective twist angle theta/sqrt(2), giving a larger MATTG magic angle near 1.6 degrees, and a perpendicular displacement field D breaks mirror symmetry and hybridizes the flat and Dirac bands, enabling electrical control of flat-band bandwidth and topology under the stated continuum-model approximations [@Park2021].""",
    lkm_id="gcn_b4e3bdff3c0c439a",
    source_paper="paper:812508547391684608",
    provenance_source="lkm",
    lkm_original=_ROOT_ORIGINAL,
)

helper_mattg_zero_d_mirror_protected_flat_dirac = claim(
    r"""For Park et al.'s zero-displacement-field continuum calculation of mirror-symmetric A-tw-A MATTG near theta about 1.57 degrees, the flat bands are mirror symmetric, the coexisting gapless Dirac bands are mirror antisymmetric, and symmetry forbids their hybridization at D=0 [@Park2021].""",
    lkm_id="gcn_b4e3bdff3c0c439a",
    source_paper="paper:812508547391684608",
    provenance_source="lkm_decomposition",
    decomposition_of="gcn_b4e3bdff3c0c439a",
    lkm_original=_ROOT_ORIGINAL,
)

helper_mattg_magic_angle_larger_than_matbg = claim(
    r"""For Park et al.'s mirror-symmetric A-tw-A MATTG model, the selected LKM chain states that the flat bands reduce mathematically to MATBG-like bands with effective twist angle theta/sqrt(2), so a physical twist theta about 1.57 degrees corresponds to a larger trilayer magic-angle estimate near 1.6 degrees [@Park2021].""",
    lkm_id="gcn_b4e3bdff3c0c439a",
    source_paper="paper:812508547391684608",
    provenance_source="lkm_decomposition",
    decomposition_of="gcn_b4e3bdff3c0c439a",
    lkm_original=_ROOT_ORIGINAL,
)

helper_mattg_displacement_field_hybridizes_bands = claim(
    r"""For Park et al.'s MATTG continuum model, applying a finite perpendicular displacement field D through Delta V=dD/epsilon_0 breaks the mirror symmetry, mixes mirror characters, and allows hybridization between formerly mirror-protected flat bands and Dirac bands, producing tunable changes in flat-band bandwidth and topology [@Park2021].""",
    lkm_id="gcn_b4e3bdff3c0c439a",
    source_paper="paper:812508547391684608",
    provenance_source="lkm_decomposition",
    decomposition_of="gcn_b4e3bdff3c0c439a",
    lkm_original=_ROOT_ORIGINAL,
)


gfac_170b7417_mattg_bandstructure_deduction = deduction(
    [
        gcn_c680c239_mattg_continuum_approximations,
        gcn_3618ccee_mattg_theta_over_sqrt2_mapping,
        gcn_71314760_mattg_displacement_field_modeling,
    ],
    gcn_b4e3bdff_mattg_mirror_flat_dirac_control,
    reason=r"""1. Define the system and calculation framework: MATTG consists of three graphene monolayers with sequential twist angles $\theta$ and $-\theta$ between layers; the continuum-model calculation used is the twisted-bilayer continuum model extended to a third layer with the same relative twist as the bottom layer. The calculation neglects direct coupling between the topmost and bottommost layers and uses interlayer hopping parameters off-diagonal $w=0.1\ \mathrm{eV}$ and diagonal $w'=0.08\ \mathrm{eV}$ (the latter empirically accounting for lattice relaxation). Fig. 1b, Fig. 1c [2,18,25,26]
2. Present the calculated bandstructure at zero perpendicular electric displacement field $D$: the calculated bands for valley K show a set of nearly flat bands near charge neutrality and coexisting gapless Dirac bands, with the mirror-symmetry character of each eigenstate indicated by a colour scale (mirror-symmetric eigenstates evaluate to $+1$ under the top-bottom layer inner-product projection, mirror-antisymmetric to $-1$, and intermediate values for nonsymmetric states). In these zero-$D$ calculations, the flat bands are mirror symmetric and the Dirac bands are mirror antisymmetric, hence hybridization between them is symmetry-forbidden at $D=0$. Fig. 1b
3. Explain the origin of the flat bands in this mirror-symmetric stacking: the flat bands arise from mirror-symmetric hopping from the two outer layers onto the central layer; mathematically, these flat bands reduce to an effective twisted-bilayer-like bandstructure with an effective twist angle $\theta/\sqrt{2}$ (that is, effective twist $=\theta/\sqrt{2}$), implying a larger MATTG magic angle than MATBG. Using $\theta\approx1.57^\circ$, this reduction yields an estimated MATTG magic-angle value $\theta_{\mathrm{MATTG}}\approx1.6^\circ$. Fig. 1b [18]
4. Describe the effect of a perpendicular displacement field $D$ in the calculation: applying a finite $D$ breaks the mirror symmetry by imposing an interlayer potential difference $\Delta V = d D/\varepsilon_{0}$ (where $d\approx0.3\ \mathrm{nm}$ is the interlayer spacing and $\varepsilon_{0}$ is the vacuum permittivity), which mixes mirror-symmetry characters and allows hybridization between the formerly mirror-protected flat bands and the Dirac bands. The calculated bandstructure at finite $D$ shows this hybridization and the resulting controllable changes in band bandwidth and topology. Fig. 1c
5. State the approximations and limitations used in the calculations as presented: neglect of direct coupling between the topmost and bottommost layers is explicitly adopted; the chosen interlayer hopping parameters are $w=0.1\ \mathrm{eV}$ and $w'=0.08\ \mathrm{eV}$; the calculation does not include a self-consistent screening treatment of the applied $D$ (authors remark that screening by outer layers reduces the actual interlayer field relative to externally applied $D$), nor high-order and non-local interlayer coupling terms that can introduce particle-hole asymmetry. Extended Data Fig. 1""",
    prior=0.95,
)

strat_decompose_mattg_zero_d_mirror_protection = support(
    [gcn_b4e3bdff_mattg_mirror_flat_dirac_control],
    helper_mattg_zero_d_mirror_protected_flat_dirac,
    reason=(
        "The selected root and LKM factor step 2 explicitly state that at zero "
        "displacement field the flat bands and Dirac bands have opposite mirror "
        "characters, making their hybridization symmetry-forbidden."
    ),
    prior=0.90,
)

strat_decompose_mattg_larger_magic_angle = support(
    [gcn_b4e3bdff_mattg_mirror_flat_dirac_control],
    helper_mattg_magic_angle_larger_than_matbg,
    reason=(
        "The selected root and LKM factor step 3 explicitly state the "
        "theta/sqrt(2) reduction and the resulting larger MATTG magic-angle "
        "estimate near 1.6 degrees."
    ),
    prior=0.90,
)

strat_decompose_mattg_displacement_hybridization = support(
    [gcn_b4e3bdff_mattg_mirror_flat_dirac_control],
    helper_mattg_displacement_field_hybridizes_bands,
    reason=(
        "The selected root and LKM factor step 4 explicitly state that finite D "
        "breaks mirror symmetry, mixes mirror character, and permits flat/Dirac "
        "band hybridization with tunable bandwidth and topology."
    ),
    prior=0.90,
)
