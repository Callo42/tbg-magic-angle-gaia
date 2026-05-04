"""Claims and deduction from Herzog-Arbeitman, Chew, and Bernevig (2022).

Source: Magnetic Bloch Theorem and Reentrant Flat Bands in Twisted Bilayer
Graphene at 2pi Flux.
DOI: 10.48550/arXiv.2206.07717
Reference key: HerzogArbeitman2022
"""

from gaia.lang import claim, deduction


magnetic_bloch_cutoff_convergence = claim(
    r"""For the Bistritzer-MacDonald magnetic Bloch Hamiltonian
$H^{\phi=2\pi}(\mathbf{k})$ of twisted bilayer graphene represented in the
Landau-level basis $|\mathbf{k},n\rangle$, the numerical procedure truncates
the basis to $n \le n_{\max}$, diagonalizes the resulting finite Hermitian
matrix at sampled $\mathbf{k}$ points, and assumes that for the magic-angle BM
parameters and flux $\phi=2\pi$ a numerically accessible cutoff makes the
low-energy flat-band eigenvalues and topological diagnostics converge within
quoted tolerances such as energy errors of order 1 meV [@HerzogArbeitman2022].""",
    lkm_id="gcn_06caff12a4d84b26",
    source_paper="paper:867760961551860070",
    provenance_source="lkm",
    provenance_file="artifacts/lkm-discovery/input/evidence_gcn_afdfbd0c013048d8.json",
    lkm_original=r"""Let $H^{\phi=2\pi}(\mathbf{k})$ be the Bistritzer–MacDonald (BM) magnetic Bloch Hamiltonian represented in the Landau-level basis $|\mathbf{k},n\rangle$ with $n\ge0$. The numerical procedure truncates the Landau-level basis to $n\le n_{\max}$ and diagonalizes the finite Hermitian matrix $H^{\phi=2\pi}_{n,n'}(\mathbf{k})$ at each sampled $\mathbf{k}$. The empirical claim is: for the magic-angle BM parameter values and flux $\phi=2\pi$ studied, there exists a numerically accessible cutoff $n_{\max}$ such that the low-energy (flat-band) eigenvalues and topological diagnostics (for example Wilson-loop windings and computed Chern numbers) converge within the quoted numerical tolerances, e.g., energy errors below O(1 meV). This proposition specifies the truncation procedure and the convergence notion; it is an empirical numerical assumption that must be checked by systematic $n_{\max}$ scans in practice.""",
)

reentrant_flat_band_parameter_convergence = claim(
    r"""For the BM magnetic Bloch Hamiltonian
$H_{BM}^{\phi}(\mathbf{k};w_0,w_1)$ of magic-angle twisted bilayer graphene at
flux $\phi=2\pi$, truncated in Landau levels and diagonalized across sampled
interlayer parameters $(w_0,w_1)$, the observed reentrant two flat bands, their
approximately 40 meV gap to passive bands, and the topology assignments
separating a crystalline regime from a Landau-level regime are interpreted as
physical parameter dependence only after convergence in Landau-level cutoff,
$\mathbf{k}$ mesh, and parameter-grid refinement, subject to the stated BM-model
approximations [@HerzogArbeitman2022].""",
    lkm_id="gcn_fedb8c2683fb48c7",
    source_paper="paper:867760961551860070",
    provenance_source="lkm",
    provenance_file="artifacts/lkm-discovery/input/evidence_gcn_afdfbd0c013048d8.json",
    lkm_original=r"""Let $H_{BM}^\phi(\mathbf{k};w_0,w_1)$ denote the BM magnetic Bloch Hamiltonian at flux $\phi=2\pi$, truncated to a Landau-level cutoff $n_{\max}$ and diagonalized numerically on a grid of interlayer-parameter values $(w_0,w_1)$. The proposition is that the numerically observed features — namely the reentrant two flat bands, the approximate gap to passive bands of order $\sim40\,$meV, and the topology assignments separating a crystalline regime (physical TBG parameters) from a Landau-level regime (including the first chiral limit) — persist upon systematic extrapolation in Landau-level cutoff, Brillouin-zone sampling, and parameter-grid refinement, and therefore reflect the physical parameter dependence of magic-angle TBG. This assertion packages multiple numerical extrapolations (Landau-level cutoff convergence, $\mathbf{k}$-mesh convergence, parameter discretization) together with model approximations (for example neglecting explicit twist-angle dependence in some kinetic terms) into a physical-interpretation claim whose quantitative validity requires the indicated convergence and consistency checks.""",
)

magnetic_bloch_reentrant_flat_bands = claim(
    r"""The continuum Bistritzer-MacDonald model of magic-angle twisted bilayer
graphene, after a layer-dependent momentum shift restores moire periodicity,
can be represented in a magnetic-translation-irrep Landau-level basis at flux
$\phi=2\pi$ and diagonalized with a finite Landau-level cutoff; for the BM
interlayer tunneling parameters studied, this calculation produces two
low-energy reentrant flat bands per valley and spin separated from passive
bands by a gap of order 40 meV, with topology controlled by $(w_0,w_1)$:
physical TBG lies in a crystalline regime with vanishing total Chern number for
the two flat bands, while the first chiral limit $w_0=0$ lies in a
Landau-level-type regime where each flat band has Chern number -1
[@HerzogArbeitman2022].""",
    lkm_id="gcn_afdfbd0c013048d8",
    source_paper="paper:867760961551860070",
    provenance_source="lkm",
    provenance_file="artifacts/lkm-discovery/input/evidence_gcn_afdfbd0c013048d8.json",
    lkm_original=r"""The continuum Bistritzer–MacDonald (BM) model of twisted bilayer graphene, after applying a layer-dependent momentum shift that restores moiré periodicity, can be represented in the magnetic-translation-irrep Landau-level basis at flux $\phi=2\pi$ and diagonalized after truncating to a finite number of Landau levels. For magic-angle geometric parameters and typical BM interlayer tunneling strengths, this numerical diagonalization (with sufficient Landau-level cutoff) reveals two low-energy flat bands per valley and spin that reappear (reenter) at $\phi=2\pi$ and are, for the parameter sets considered, separated from higher-energy passive bands by a sizable gap on the order of 40 meV. The dispersion and topology of these reentrant flat bands depend sensitively on the interlayer hopping parameters $(w_0,w_1)$: scanning $(w_0,w_1)$ produces a phase diagram with a crystalline regime (parameter region including the physical TBG values) where the two flat bands together have vanishing total Chern number, and a Landau-level-type regime (including the first chiral limit $w_0=0$) where each flat band individually carries Chern number $-1$.""",
)

derive_magnetic_bloch_reentrant_flat_bands = deduction(
    [magnetic_bloch_cutoff_convergence, reentrant_flat_band_parameter_convergence],
    magnetic_bloch_reentrant_flat_bands,
    prior=0.95,
    reason=r"""1. Begin with the Bistritzer-MacDonald (BM) continuum model for a single valley at zero flux:
   $$
   H_{BM}=\begin{pmatrix}-i\hbar v_F\boldsymbol{\sigma}\cdot\boldsymbol{\nabla}&T^\dagger(\mathbf{r})\\[4pt]
   T(\mathbf{r})&-i\hbar v_F\boldsymbol{\sigma}\cdot\boldsymbol{\nabla}\end{pmatrix},
   $$
   with moire tunneling $T(\mathbf{r})=\sum_{j=1}^3 e^{2\pi i\mathbf{q}_j\cdot\mathbf{r}}T_j$ and $T_j$ built from interlayer tunneling parameters $w_0,w_1$. Specify moire geometry ($\mathbf{q}_j,\mathbf{a}_i,\mathbf{b}_i$) and the moire unit cell area $\Omega$ so the dimensionless flux $\phi=eB\Omega$ is defined. Sec. VIII A, Eq. (52)-(53); Sec. VIII, geometry discussion [@HerzogArbeitman2022].
2. Introduce magnetic flux by canonical substitution $-i\hbar\boldsymbol{\nabla}\to\boldsymbol{\pi}$ and restore moire periodicity by a layer-dependent unitary momentum-shift:
   $$
   V_1=\mathrm{diag}\big(e^{i\pi\mathbf{q}_1\cdot\mathbf{r}},\,e^{-i\pi\mathbf{q}_1\cdot\mathbf{r}}\big).
   $$
   Conjugating by $V_1$ yields a form with a periodic interlayer potential $\tilde{T}(\mathbf{r})=T_1+T_2 e^{2\pi i\mathbf{b}_1\cdot\mathbf{r}}+T_3 e^{2\pi i\mathbf{b}_2\cdot\mathbf{r}}$ and shifted Dirac kinetic terms, which are readily expressed in Landau-level ladder operators. This step renders the Hamiltonian compatible with the magnetic Bloch construction. Sec. VIII A, Eq. (54)-(55) [@HerzogArbeitman2022].
3. Express the Dirac kinetic term in Landau-level language at $\phi=2\pi$: using $a,a^\dagger$ defined from $\boldsymbol{\pi}$, write
   $$
   v_F\boldsymbol{\sigma}\cdot\boldsymbol{\pi}=v_F\sqrt{2eB}\begin{pmatrix}0&a^\dagger\\[4pt] a&0\end{pmatrix}=v_F k_\theta\Big(\tfrac{3\sqrt{3}}{2\pi}\Big)^{1/2}\begin{pmatrix}0&a^\dagger\\[4pt] a&0\end{pmatrix},
   $$
   so the kinetic energy acts only in Landau-level index space and can be truncated. The momentum-shift terms act as layer-dependent identity contributions on Landau levels and appear as small offsets compared to moire tunneling. Sec. VIII A, Eq. (56) [@HerzogArbeitman2022].
4. Compute the moire tunneling matrix elements in the Landau-level magnetic Bloch basis using the previously derived Landau-level scattering matrices $\mathcal{H}^{\mathbf{q}}$: the periodic tunneling Fourier components scatter Landau levels according to closed-form expressions in terms of Laguerre polynomials, yielding a finite Landau-level matrix Hamiltonian $H^{\phi=2\pi}(\mathbf{k})$ whose off-diagonal blocks are combinations of $T_j$ times phases $e^{\pm i k_i}$ and $\mathcal{H}^{\pm 2\pi\mathbf{b}_i}$ insertions. Truncate the Landau-level basis to a numerically convergent cutoff to obtain a finite matrix to diagonalize. Sec. VIII A; App. A 6; App. D 1 [@HerzogArbeitman2022].
5. Numerically diagonalize the truncated magnetic Bloch Hamiltonian for magic-angle parameters and a range of interlayer tunneling $(w_0,w_1)$: one finds two low-energy flat bands per valley and spin that reenter at $\phi=2\pi$. For magic-angle parameter choices used, these two flat bands are separated from higher passive bands by an energy gap of order $\sim40$ meV. The dispersion and total Chern number of the flat bands depend sensitively on $(w_0,w_1)$, producing a phase diagram where a crystalline regime (physical TBG parameters) has flat bands with vanishing total Chern number, while a Landau-level regime (including the first chiral limit) has each flat band with Chern -1. These numerical band plots, density of states, and Wilson-loop diagnostics are shown in Figs. 5-7 and Fig. 6 panels [@HerzogArbeitman2022].
6. Summarize dependence on $(w_0,w_1)$ and connect to physical regimes: the parameter $w_0$ controlling AA tunneling versus $w_1$ controlling AB/BA tunneling moves the system between a Landau-level-dominated regime and a crystalline regime where the two flat bands together form an elementary band representation with vanishing total Chern number. The calculated reentrant flat bands at $\phi=2\pi$ and the phase diagram in $(w_0,w_1)$ capture this sensitivity, justifying the claim that the BM Hamiltonian expressed in the magnetic Bloch Landau-level basis yields two reentrant low-energy flat bands per valley and spin with significant gaps to passive bands, with topology determined by $(w_0,w_1)$. Sec. VIII A, Figs. 5-7 [@HerzogArbeitman2022].""",
)
