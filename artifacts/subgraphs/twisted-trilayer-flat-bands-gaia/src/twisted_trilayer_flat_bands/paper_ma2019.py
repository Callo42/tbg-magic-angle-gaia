"""paper_ma2019 -- LKM claims and deduction from Ma et al. (2019).

Source: Topological flat bands in twisted trilayer graphene
DOI: 10.48550/arXiv.1905.00622
Authors: Zhen Ma | Shuai Li | Ya-Wen Zheng | Meng-Meng Xiao | Hua Jiang |
    Jin-Hua Gao | X. C. Xie
Reference key (CSL): Ma2019
"""
from gaia.lang import claim, deduction


gcn_768268d063184cb8 = claim(
    """In Ma et al.'s continuum-model description of twisted trilayer graphene, a graphene monolayer on an AB-stacked bilayer is modeled with a single-valley 6x6 Bloch Hamiltonian in the (A1,B1,A2,B2,A3,B3) sublattice basis; setting the AB-bilayer remote hopping parameters gamma_3 = 0, gamma_4 = 0, and the dimer-site energy Delta' = 0 defines a minimal model intended to isolate the primary moire interlayer-coupling mechanisms that produce the largest magic-angle nearly flat central bands [@Ma2019].""",
    lkm_id="gcn_768268d063184cb8",
    source_paper="paper:867757254252691813",
    provenance_source="lkm",
    lkm_original="""Consider twisted trilayer graphene defined as a graphene monolayer (top layer, index 3) placed on an AB-stacked graphene bilayer (layers 1 and 2) with a small relative twist angle θ between the monolayer and the bilayer, and consider the single-valley 6×6 continuum-model Bloch Hamiltonian H_TLG(θ) written in the sublattice basis (A1,B1,A2,B2,A3,B3) with an AB bilayer block h_b(k) parametrized by Slonczewski–Weiss–McClure tight-binding parameters: nearest-neighbor intralayer hopping γ0, dominant interlayer vertical hopping γ1, trigonal-warping γ3, electron–hole asymmetry γ4, and dimer-site on-site energy Δ'. The proposition is that imposing the minimal-model approximation γ3 = 0, γ4 = 0, and Δ' = 0 isolates the primary moiré-interlayer-coupling mechanisms and, without introducing qualitatively different single-particle mechanisms in the continuum Hamiltonian, captures the formation of the magic-angle nearly flat central moiré bands (including the existence of a largest magic angle) in the continuum-model twisted trilayer graphene.""",
)

gcn_ba18ade2bb8145ee = claim(
    """For Ma et al.'s minimal continuum-model Hamiltonian for twisted trilayer graphene, the tight-binding parameter choices gamma_0 = 2464 meV and gamma_1 = 400 meV, together with gamma_3 = gamma_4 = Delta' = 0, determine the numerically reported largest magic angle near theta = 1.12 degrees, so the precise value is sensitive to the adopted gamma_0 and gamma_1 parameters [@Ma2019].""",
    lkm_id="gcn_ba18ade2bb8145ee",
    source_paper="paper:867757254252691813",
    provenance_source="lkm",
    lkm_original="""Using the continuum-model minimal Hamiltonian H_TLG(θ) with γ3 = γ4 = Δ' = 0, the numerical choices γ0 = 2464 meV (nearest-neighbor intralayer hopping) and γ1 = 400 meV (vertical interlayer hopping) determine the numerical value of the largest magic twist angle obtained from band-structure calculations in this parametrization; with these numerical values the largest magic angle produced by the continuum-model bands is near θ ≈ 1.12°, illustrating that the precise numerical value of the largest magic angle is sensitive to the adopted tight-binding parameters γ0 and γ1.""",
)

gcn_2a4995cfc44a4638 = claim(
    """In Ma et al.'s numerical continuum-model calculation for twisted trilayer graphene, the finite plane-wave basis of moire reciprocal lattice vectors and the finite k-point sampling are assumed to be sufficiently converged that the observed narrowing of the two central bands and the identification of a nearly flat pair are not artifacts of basis truncation or coarse k-point sampling [@Ma2019].""",
    lkm_id="gcn_2a4995cfc44a4638",
    source_paper="paper:867757254252691813",
    provenance_source="lkm",
    lkm_original="""In numerical continuum-model computations of the moiré band structure for twisted trilayer graphene the Bloch Hamiltonian H_TLG(θ) is represented in a finite plane-wave basis formed from a truncated set of moiré reciprocal lattice vectors {G} and the moiré Brillouin zone integrals are approximated by sampling on a finite k-point mesh; the proposition is that the chosen basis truncation (finite number of retained G vectors) and finite k-point sampling used in the presented calculations converge sufficiently (i.e., change the reported band energies by only a small fraction of the quoted energy scales) so that the observed progressive narrowing of the two central bands upon decreasing θ and the identification of a nearly flat pair of bands at a particular angle are not numerical artifacts of insufficient basis size or coarse k-point sampling but reflect the true behavior of the continuum Hamiltonian within the stated numerical tolerances.""",
)

gcn_4249f998947d4ee0 = claim(
    """In Ma et al.'s search for the largest magic angle of twisted trilayer graphene, evaluating the continuum-model band structures on a discrete set of twist angles, including theta = 5.0 degrees, 1.53 degrees, and 1.12 degrees, is assumed to locate the largest nearly flat two-central-band angle within the angular resolution used, rather than missing a narrow higher-angle interval [@Ma2019].""",
    lkm_id="gcn_4249f998947d4ee0",
    source_paper="paper:867757254252691813",
    provenance_source="lkm",
    lkm_original="""In the numerical search for the largest magic angle the continuum-model band structures are evaluated at a discrete set of twist-angle values (for example a sampling that includes θ = 5.0°, 1.53°, 1.12°), and the proposition is that scanning such a finite discrete set of θ values with the stated numerical resolution is sufficient to locate, within the sampling resolution, the largest angle at which the two central moiré bands become nearly flat, i.e., the true maximal magic angle does not lie in a narrow interval missed by the chosen discrete sampling grid given the numerical resolution employed.""",
)

gcn_2cf09f115b814154 = claim(
    """In Ma et al.'s minimal continuum model for twisted trilayer graphene, formed by placing a graphene monolayer on an AB-stacked graphene bilayer, the parameter set gamma_3 = gamma_4 = Delta' = 0, gamma_0 = 2464 meV, and gamma_1 = 400 meV gives a largest magic twist angle near theta = 1.12 degrees, where two low-energy moire bands near charge neutrality become nearly flat around the Fermi level [@Ma2019].""",
    lkm_id="gcn_2cf09f115b814154",
    source_paper="paper:867757254252691813",
    provenance_source="lkm",
    lkm_original="""Consider the continuum-model description of twisted trilayer graphene formed by placing a graphene monolayer (top layer, layer index 3) on an AB-stacked graphene bilayer (layers 1 and 2) with a small relative twist angle θ between the monolayer and the bilayer; in this model the low-energy electronic spectrum forms moiré Bloch bands. In the minimal-model limit in which the AB bilayer remote-hopping parameters are set to zero (trigonal-warping γ3 = 0, electron–hole–asymmetry γ4 = 0, and dimer-site on-site energy Δ' = 0) and with nearest-neighbor intralayer hopping γ0 = 2464 meV and dominant interlayer vertical hopping γ1 = 400 meV, there exists a largest "magic" twist angle at which the two low-energy moiré bands near charge neutrality become nearly flat, and the largest such magic angle in this minimal-model parameterization is approximately θ ≈ 1.12°; at θ ≈ 1.12° the continuum-model spectrum contains two nearly flat moiré bands around the Fermi level under the stated minimal-model assumptions and parameter values.""",
)

gfac_0046298fbcb144c4 = deduction(
    [
        gcn_768268d063184cb8,
        gcn_ba18ade2bb8145ee,
        gcn_2a4995cfc44a4638,
        gcn_4249f998947d4ee0,
    ],
    gcn_2cf09f115b814154,
    reason=(
        "1. Define the physical system: \"twisted trilayer graphene\" (twisted TLG) is a stack where a single graphene monolayer (layer index $3$) is placed on top of an AB-stacked bilayer graphene (layers indices $1,2$) with a relative twist angle $\\theta$ between the single layer and the bilayer; the moire superlattice vectors are $\\boldsymbol{t}_{1},\\boldsymbol{t}_{2}$ and the corresponding moire reciprocal vectors are $\\mathbf{G}_{1},\\mathbf{G}_{2}$ as constructed from the underlying graphene lattice vectors $\\boldsymbol{a}_{1},\\boldsymbol{a}_{2}$ and their reciprocal vectors $\\boldsymbol{b}_{1},\\boldsymbol{b}_{2}$.\n"
        "2. State the computational framework used to obtain bands: employ a continuum-model Hamiltonian for one valley, written as a $6\\times 6$ matrix in the Bloch basis $(A_{1},B_{1},A_{2},B_{2},A_{3},B_{3})$, with the block structure $H_{\\mathrm{TLG}}(\\theta)=\\begin{pmatrix} h_{b}(k_{1}) & T(\\boldsymbol{r}) \\\\ T^{\\dagger}(\\boldsymbol{r}) & h_{0}(k_{2}) \\end{pmatrix} + U$, where $k_{1}=R(-\\theta/2)(k-K_{\\xi}^{b})$, $k_{2}=R(\\theta/2)(k-K_{\\xi}^{t})$, $h_{0}(\\boldsymbol{k})=-\\hbar v_{F}\\boldsymbol{k}\\cdot\\boldsymbol{\\sigma}$ is the monolayer graphene Hamiltonian with Fermi velocity $v_{F}$ and Pauli matrices $\\boldsymbol{\\sigma}$, $h_{b}(k)$ is the AB-stacked bilayer Hamiltonian, $T(\\boldsymbol{r})$ is the moire interlayer tunneling between the twisted monolayer and the bilayer, and $U=\\mathrm{diag}(-V,-V,0,0,V,V)$ is the perpendicular electric-field induced interlayer potential difference with parameter $V$.\n"
        "3. Define the minimal-model approximation used to identify the magic-angle physics: set the bilayer remote-hopping parameters to zero, i.e., $\\gamma_{3}=0$, $\\gamma_{4}=0$, and the on-site dimer potential $\\Delta' = 0$, so that the AB-stacked bilayer Hamiltonian $h_{b}$ contains only the leading intralayer nearest-neighbor hopping parameter $\\gamma_{0}$ and the dominant interlayer vertical hopping $\\gamma_{1}$. The authors state that this minimal model isolates the primary moire and interlayer-coupling physics relevant to flat-band formation.\n"
        "4. Record the numerical minimal-model tight-binding parameters used to locate the largest magic angle: the nearest-neighbor intralayer hopping is $\\gamma_{0}=2464\\ \\mathrm{meV}$ and the dominant interlayer vertical hopping is $\\gamma_{1}=400\\ \\mathrm{meV}$; set $\\gamma_{3}=\\gamma_{4}=\\Delta'=0$ in the minimal model.\n"
        "5. Describe the numerical procedure and evidence showing band flattening: use the continuum-model Hamiltonian with the minimal-model parameters and compute moire superlattice band structures for multiple twist angles $\\theta$; the computed band structures show that as $\\theta$ is decreased from larger values such as $\\theta=5^{\\circ}$ toward smaller values, the two low-energy moire bands nearest the Fermi level narrow progressively, consistent with moire-band flattening. Fig. 1(c-h).\n"
        "6. Identify the largest magic angle from the numerical band series: inspect the calculated sequence of band structures shown for decreasing $\\theta$ and find the largest twist angle at which the two central bands become nearly dispersionless; the authors report this largest magic angle to be approximately $\\theta\\approx 1.12^{\\circ}$, at which the two low-energy moire bands around charge neutrality are nearly flat in the minimal model. Fig. 1(g,h).\n"
        "7. State the conclusion that at this magic angle two nearly flat moire bands appear: combine the minimal-model parameter choice ($\\gamma_{0}=2464\\ \\mathrm{meV}$, $\\gamma_{1}=400\\ \\mathrm{meV}$, $\\gamma_{3}=\\gamma_{4}=\\Delta'=0$) with the computed band structures and conclude that for continuum-model twisted trilayer graphene there exists a largest magic twist angle $\\theta\\approx 1.12^{\\circ}$ at which the two low-energy moire bands near charge neutrality become nearly flat. Fig. 1(g,h)."
    ),
    prior=0.95,
)
