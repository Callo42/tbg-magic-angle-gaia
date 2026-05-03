"""paper_liu2020 -- LKM claims and deduction from Liu et al. (2020).

Source: Tunable lattice reconstruction and bandwidth of flat bands in magic-angle twisted bilayer graphene
DOI: 10.48550/arXiv.2007.01993
Authors: Yi-Wen Liu | Ying Su | Xiao-Feng Zhou | Long-Jing Yin | Chao Yan |
    Si-Yu Li | Wei Yan | Sheng Han | Zhong-Qiu Fu | Yu Zhang | Qian Yang |
    Ya-Ning Ren | Lin He
Reference key (CSL): Liu2020
"""
from gaia.lang import claim, deduction


gcn_8cd2984a6296435c = claim(
    "For Liu et al.'s continuum-model calculations of magic-angle twisted bilayer graphene, the Bistritzer-MacDonald-type moire Hamiltonian is augmented by atomic-registry-dependent interlayer tunneling and a relaxation-derived displacement field that enlarges AB/BA regions and shrinks AA regions; in that reconstructed geometry, the computed low-energy flat-band manifold has larger bandwidth and greater energetic separation from remote bands than in the unreconstructed rigid geometry, with the qualitative trend robust to moderate model-parameter changes even though explicit spatially non-uniform heterostrain is not included [@Liu2020].",
    lkm_id="gcn_8cd2984a6296435c",
    source_paper="paper:867745366357836075",
    provenance_source="lkm",
    lkm_original="For continuum-model electronic-structure calculations of magic-angle twisted bilayer graphene that explicitly incorporate lattice relaxation via atomic-registry-dependent interlayer coupling leading to enlarged AB/BA regions and shrunken AA regions, the computed low-energy flat-band manifold exhibits qualitatively increased bandwidth (broader flat bands) and increased energetic separation from remote bands in the reconstructed geometry relative to the unreconstructed rigid geometry, and this qualitative trend is robust to moderate variations of model parameters even when spatially non-uniform heterostrain is not included in the calculation; here \"continuum model\" refers to the Bistritzer\u2013MacDonald-type moir\u00e9 Hamiltonian augmented by a registry-dependent interlayer tunneling parameterization and a relaxation-derived displacement field.\n      [18-21]",
)

gcn_ed8fa9253ea24982 = claim(
    "For magic-angle twisted bilayer graphene spectra discussed by Liu et al., spatially non-uniform heterostrain means a slowly varying relative in-plane deformation between graphene layers, parameterized by a local strain tensor field epsilon(r) at the moire scale; such heterostrain can reconstruct the electronic band structure and generate additional flat-band density-of-states fine structure, including three-subpeak splitting seen in some STS spectra, but those heterostrain-induced features are not reproduced by continuum-model calculations that include only atomic-registry-driven lattice relaxation [@Liu2020].",
    lkm_id="gcn_ed8fa9253ea24982",
    source_paper="paper:867745366357836075",
    provenance_source="lkm",
    lkm_original="Spatially non-uniform heterostrain (a slowly-varying relative in-plane deformation between top and bottom graphene layers parameterized by a local strain tensor field $\\epsilon(\\mathbf{r})$ that varies at the moir\u00e9 scale) can reconstruct the electronic band structure of magic-angle twisted bilayer graphene and produce additional fine structure in the flat-band density of states, such as three-subpeak splitting of the flat-band manifold observed in some STS spectra, and such heterostrain-induced features are not reproduced by continuum-model calculations that include only atomic-registry-driven lattice relaxation but omit explicit heterostrain fields.\n      [54-55]",
)

gcn_c220df1acc8b476a = claim(
    "In Liu et al.'s continuum-model electronic-structure calculation for magic-angle twisted bilayer graphene, adding atomic-registry-driven lattice relaxation produces reconstructed geometry with enlarged AB/BA regions and reduced AA regions; compared with the rigid unreconstructed calculation, this reconstructed geometry reproduces the key STS spectroscopic trends of broader low-energy flat bands and greater energetic isolation from remote bands, while the calculation omits explicit spatially non-uniform heterostrain and therefore does not reproduce extra flat-band peak splitting, such as three-subpeak structure, observed in some spectra [@Liu2020].",
    lkm_id="gcn_c220df1acc8b476a",
    source_paper="paper:867745366357836075",
    provenance_source="lkm",
    lkm_original="Continuum-model electronic-structure calculations of magic-angle twisted bilayer graphene that include lattice relaxation driven by atomic-registry-dependent interlayer coupling reproduce the key experimental spectroscopic trends: the reconstructed geometry obtained from relaxation (enlarged AB/BA regions and reduced AA regions) yields broadened low-energy flat bands and increased energetic isolation of the flat-band manifold from remote bands relative to the unreconstructed rigid-geometry calculation. The implemented calculations omit explicit spatially non-uniform heterostrain and therefore do not reproduce additional fine splitting of the flat-band peaks (for example, three-subpeak structure) seen in some experimental spectra, which can be induced by heterostrain effects.",
)

gfac_e5303e2e42664d99 = deduction(
    [gcn_8cd2984a6296435c, gcn_ed8fa9253ea24982],
    gcn_c220df1acc8b476a,
    reason=(
        "1. Define the computational framework: perform continuum-model band-structure and density-of-states (DOS) calculations for magic-angle TBG in two geometries -- the unreconstructed (rigid) geometry and a reconstructed geometry that includes lattice relaxation in the form of atomic registry rearrangement corresponding to enlarged AB/BA regions and shrunken AA regions.\n"
        "Fig. 4\nFig. S10\n"
        "2. Explain what is meant by lattice relaxation in the calculation: incorporate atomic registry rearrangement (i.e., allowing the local stacking registries to shift so that AB/BA regions are enlarged and AA regions are reduced and corrugated) when computing the continuum-model moire Hamiltonian and deriving band structures and density of states.\n"
        "[18-21]\n"
        "3. Report the computational outcome qualitatively: the calculations that include lattice relaxation produce low-energy flat bands that are broader (increased bandwidth) and more energetically isolated from the remote bands (i.e., larger gaps or separation between flat-band manifold and higher-energy conduction bands) than the calculations performed on the unreconstructed, rigid geometry.\n"
        "Fig. S10\n"
        "4. Compare computation to experiment: state that these theoretical results reproduce the essential experimental spectroscopic trends observed in STM/STS measurements on magic-angle TBG, namely that the reconstructed geometry yields broadened low-energy flat bands and increased energetic isolation from remote bands relative to the unreconstructed geometry.\n"
        "Fig. 4d\nFig. 4e\n"
        "5. State calculation limitations: explicitly record that the present implementation of the continuum-model calculations does not include heterostrain (spatially varying lattice deformation between layers) and therefore does not capture additional subpeak splitting (three subpeaks) observed in some experimental spectra; the authors attribute such extra splittings to strain effects discussed in prior literature.\n"
        "[54-55]\nFig. S10"
    ),
    prior=0.95,
)
