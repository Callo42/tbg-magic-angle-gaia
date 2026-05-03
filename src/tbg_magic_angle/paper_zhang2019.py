"""paper_zhang2019 -- LKM claims and deduction from Zhang et al. (2019).

Source: Twisted bilayer graphene aligned with hexagonal boron nitride:
    Anomalous Hall effect and a lattice model
DOI: 10.1103/physrevresearch.1.033126
Authors: Ya-Hui Zhang | Dan Mao | T. Senthil
Reference key (CSL): Zhang2019
"""
from gaia.lang import claim, deduction


gcn_464f6413fccb48be = claim(
    """For Zhang, Mao, and Senthil's single-valley continuum Hamiltonian for h-BN-aligned magic-angle TBG, the h-BN moire-potential matrices V_j have typical norms |V_j| less than or about 10 meV while the principal TBG moire interlayer coupling is w_1 about 110 meV; therefore their first-approximation band-structure calculation drops the V_j term and retains the top-layer staggered sublattice mass M in H_hBN [@Zhang2019].""",
    lkm_id="gcn_464f6413fccb48be",
    source_paper="paper:812707666555043841",
    provenance_source="lkm",
    lkm_original=r"""For the single‑valley continuum Hamiltonian $H=H_{TBG}+H_{hBN}$ with
      $$
      H_{hBN}=\sum_{\mathbf{k}} M\,\psi_t^{\dagger}(\mathbf{k})\mu_z\psi_t(\mathbf{k})
      +\sum_{j=1}^{6}\psi_t^{\dagger}(\mathbf{k}+\mathbf{Q}_j')V_j\psi_t(\mathbf{k}),
      $$
      the moiré potential matrices $V_j$ produced by the lattice mismatch between h‑BN and graphene have typical matrix norms $|V_j|\lesssim 10\,$meV whereas the principal TBG moiré interlayer coupling energy scale is $w_1\approx110\,$meV; consequently, as a first approximation for computing the moiré‑band structure and topological indices one may ignore the $\sum_{j=1}^6$ term proportional to $V_j$, retaining only the staggered sublattice mass term proportional to $M$ acting on the top‑layer sublattice spinor $\psi_t(\mathbf{k})$ (with $\mu_z$ the Pauli matrix in sublattice space).""",
)

gcn_a7252e5aaaf84d38 = claim(
    """In Zhang, Mao, and Senthil's h-BN-aligned MA-TBG continuum-model parameterization, an experimentally measured about 35 meV neutral-point gap in monolayer graphene aligned to h-BN is mapped to a top-layer staggered sublattice mass M about 17 meV, using the relation that the single-layer Dirac mass splitting is twice the mass amplitude [@Zhang2019].""",
    lkm_id="gcn_a7252e5aaaf84d38",
    source_paper="paper:812707666555043841",
    provenance_source="lkm",
    lkm_original=r"""Mapping experimentally measured neutral‑point gaps in monolayer graphene aligned to h‑BN (observed gap $\approx35\,$meV) onto the staggered‑sublattice mass term in the continuum Hamiltonian for the top graphene layer,
      $$
      H_{hBN}=M\sum_{\mathbf{k}}\psi_t^\dagger(\mathbf{k})\mu_z\psi_t(\mathbf{k}),
      $$
      and using that the single‑layer Dirac mass splitting corresponds to twice the mass amplitude, yields the estimate $M\approx\frac{1}{2}\times35\,$meV $\approx17\,$meV for the staggered mass parameter $M$ to be used in continuum‑model diagonalization of MA‑TBG aligned to h‑BN.""",
)

gcn_ca5e0f32e91c459b = claim(
    """For Zhang, Mao, and Senthil's h-BN-aligned MA-TBG continuum-model calculations with w_1 about 110 meV, w_0/w_1 = 0.7, magic-angle twist parameters, and staggered mass M about 15-17 meV, the active conduction and valence bands in one valley are numerically isolated across the MBZ so their Chern numbers are well defined; the reported valley + values are C = +1 for the conduction active band and C = -1 for the valence active band [@Zhang2019].""",
    lkm_id="gcn_ca5e0f32e91c459b",
    source_paper="paper:812707666555043841",
    provenance_source="lkm",
    lkm_original=r"""For continuum‑model parameters $w_1\approx110\,$meV, $w_0/w_1=0.7$, twist angle in the magic‑angle range used in the calculations, and staggered mass $M\sim15$–$17\,$meV, the two active bands (conduction and valence) within a given valley are energetically isolated from other bands across the moiré Brillouin zone (MBZ), i.e., there exists a positive spectral separation $\Delta(\mathbf{k})\equiv\min_{\text{other bands}}|E_{\text{active}}(\mathbf{k})-E_{\text{other}}(\mathbf{k})|>\epsilon$ for all $\mathbf{k}$ with $\epsilon$ exceeding numerical discretization error; under these conditions the band Chern numbers of the isolated active bands are well defined and can be reliably computed with a standard discretized‑Brillouin‑zone numerical algorithm (Fukui–Hatsugai–Suzuki style), yielding for valley $+$ the values $C=+1$ for the conduction active band and $C=-1$ for the valence active band.""",
)

gcn_1d940e84a3744c85 = claim(
    """The selected Zhang, Mao, and Senthil LKM evidence factor contains premise id gcn_1d940e84a3744c85 with empty premise content; this placeholder records that an unspecified premise was present in the LKM chain but supplies no independent scientific assertion beyond the chain membership [@Zhang2019].""",
    lkm_id="gcn_1d940e84a3744c85",
    source_paper="paper:812707666555043841",
    provenance_source="lkm",
    lkm_original="",
    todo="revisit when LKM populates this premise",
)

gcn_584669e24c6145a7 = claim(
    """In Zhang, Mao, and Senthil's single-valley continuum model for magic-angle TBG with the top graphene layer nearly aligned to h-BN, H = H_TBG + H_hBN combines the standard TBG continuum Hamiltonian with a top-layer h-BN term containing a staggered sublattice mass M and weaker V_j moire potentials; for M about 15-17 meV and |V_j| much smaller than w_1 about 110 meV, numerical diagonalization gives gapped MBZ-corner Dirac crossings, one isolated conduction and one isolated valence active band per valley, valley + Chern numbers C = +1 and C = -1 for the conduction and valence active bands respectively, and an indirect active-band gap of order 5 meV at M = 15 meV and theta_M = 1.20 degrees [@Zhang2019].""",
    lkm_id="gcn_584669e24c6145a7",
    source_paper="paper:812707666555043841",
    provenance_source="lkm",
    lkm_original=r"""The single‑valley continuum Hamiltonian for magic‑angle twisted bilayer graphene with the top graphene layer nearly aligned to an h‑BN substrate is $H=H_{TBG}+H_{hBN}$ with
      $$
      H_{hBN}=\sum_{\mathbf{k}} M\,\psi_t^{\dagger}(\mathbf{k})\mu_z\psi_t(\mathbf{k})
      +\sum_{j=1}^{6}\psi_t^{\dagger}(\mathbf{k}+\mathbf{Q}_j')V_j\psi_t(\mathbf{k}),
      $$
      where $\psi_{t}(\mathbf{k})$ and $\psi_{b}(\mathbf{k})$ are two‑component spinors describing the $A,B$ sublattice degrees of freedom on the top and bottom graphene layers, $\mu_z$ is the Pauli matrix acting in the $A,B$ sublattice space, $M$ is the staggered sublattice mass induced on the top graphene layer by near alignment to h‑BN, $V_j$ are the weaker moiré potential matrices generated by the lattice mismatch between h‑BN and graphene with typical matrix norms $|V_j|\lesssim 10\,$meV, and the dominant TBG moiré interlayer coupling scale is $w_1\approx110\,$meV. For parameter estimates $M\sim15$–$17\,$meV and $|V_j|\ll w_1$, explicit numerical diagonalization of $H$ in the moiré Brillouin zone (MBZ) produces gapped Dirac crossings at the MBZ corners in each graphene valley and yields an isolated pair of active bands (one conduction, one valence) per valley; for valley labeled $+$ the computed Chern numbers are $C=+1$ for the conduction active band and $C=-1$ for the valence active band (the opposite signs occur in the time‑reversed valley). For the representative parameters $M=15\,$meV and twist angle $\theta_M=1.20^\circ$ the computed indirect gap between these conduction and valence active bands is of order $\sim5\,$meV.""",
)

gfac_ff1f36e6840c42ba = deduction(
    [
        gcn_464f6413fccb48be,
        gcn_a7252e5aaaf84d38,
        gcn_ca5e0f32e91c459b,
        gcn_1d940e84a3744c85,
    ],
    gcn_584669e24c6145a7,
    reason=r"""1. State the single-valley continuum Hamiltonian for magic-angle twisted bilayer graphene (MA-TBG) aligned with hexagonal boron nitride (h-BN) as the sum of a TBG continuum-model term and an h-BN-induced term: H=H_TBG+H_hBN, where H_TBG is the standard continuum-model Hamiltonian for twisted bilayer graphene and H_hBN encodes effects of the aligned h-BN on the top graphene layer. [56]
2. Write explicitly the h-BN-induced part of the Hamiltonian as H_hBN = sum_k M psi_t^\dagger(k) mu_z psi_t(k) + sum_{j=1}^6 psi_t^\dagger(k+Q'_j) V_j psi_t(k), and define k, top and bottom layer spinors, sublattice Pauli matrix mu_z, staggered mass M, h-BN mismatch wavevectors Q'_j, and moire potential matrices V_j. [56]
3. Explain the origin and role of the M term: aligned h-BN breaks in-plane C_2 symmetry of graphene and produces a staggered sublattice potential on the top graphene layer, acting as a mass for that layer's Dirac cones. [57]
4. Provide empirical and theoretical parameter estimates: monolayer graphene nearly aligned with h-BN shows a neutral-point gap around 35 meV, implying M about 17 meV; DFT estimates give V_j about 10 meV; the dominant TBG moire interlayer coupling is w_1 about 110 meV and lattice relaxation is represented by w_0/w_1 = 0.7, establishing M about 15-17 meV and |V_j| much smaller than w_1. [56] [10]
5. State the band-structure approximation: because V_j is estimated to be significantly smaller than the principal TBG moire scale, the authors ignore the sum_j V_j moire-potential term as a first approximation and diagonalize H_TBG + M sum_k psi_t^\dagger(k) mu_z psi_t(k) in the TBG moire Brillouin zone. [10]
6. Describe the continuum-model ingredients diagonalized: H_TBG is the Bistritzer-MacDonald continuum Hamiltonian for one valley, with Dirac Hamiltonians for top and bottom layers coupled by interlayer moire tunneling matrices T_j at wavevectors Q_j; the sublattice spinors and single-valley layer Dirac Hamiltonian form the basis for numerical diagonalization. [56]
7. Report the numerical diagonalization for representative realistic parameters: for theta_M = 1.20 degrees and M = 15 meV, with w_1 = 110 meV and w_0/w_1 = 0.7, the computed single-valley band structure gaps the MBZ-corner Dirac crossings, isolates the conduction and valence active bands from other bands, and gives an indirect active-band gap of order 5 meV. Fig. 1
8. Explain how band Chern numbers are determined and report their values: because the active bands are isolated, their Chern numbers are well defined and computed numerically; for valley + the conduction band has C=+1 and the valence band has C=-1, with opposite signs in the time-reversed valley. [8] Fig. 3
9. Connect the band-gap and topology statements into the final assertion: the explicit H_hBN form plus diagonalization of H_TBG+H_hBN under realistic parameter estimates yields gapped Dirac crossings, isolated conduction and valence active bands, valley-resolved Chern numbers +1 and -1 for valley +, and an about 5 meV indirect gap for M=15 meV and theta_M=1.20 degrees. Fig. 1""",
    prior=0.95,
)
