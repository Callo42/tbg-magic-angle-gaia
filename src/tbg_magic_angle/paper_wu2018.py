"""paper_wu2018 -- continuum velocity and electron-phonon form factor in MATBG.

Source: Phonon-induced giant linear-in-T resistivity in magic angle twisted
bilayer graphene: Ordinary strangeness and exotic superconductivity
DOI: 10.48550/arXiv.1811.04920
Reference key: Wu2018
"""

from gaia.lang import claim, deduction


moire_spinor_phonon_form_factor = claim(
    "For a moire Dirac point in twisted bilayer graphene, Wu, Hwang, and Das Sarma construct degenerate Dirac-point eigenstates from four layer/momentum spinors with amplitudes set by alpha_j=w_j/(hbar v_F |kappa_{+1}|), define beta=3(alpha_0^2+alpha_1^2), and approximate the deformation-potential electron-phonon spinor-overlap factor as F(theta)=(1+beta^2)/(1+beta)^2, with 0.5 <= F(theta) <= 1 used as a transport matrix-element correction [@Wu2018].",
    lkm_id="gcn_b411dd99a41e4de2",
    source_paper="paper:867772031297389371",
    provenance_source="lkm",
    provenance_file="artifacts/lkm-discovery/input/may4_evidence_gcn_93c279f20f364a40.json",
    lkm_original=r"""For a moiré Dirac point at momentum $\boldsymbol{\kappa}_{+1}$, define two degenerate Dirac-point eigenstates $|\Psi_A\rangle$ and $|\Psi_B\rangle$ as normalized linear combinations of four layer/momentum spinors $\{|\Psi^{(0)}\rangle,|\Psi^{(1)}\rangle,|\Psi^{(2)}\rangle,|\Psi^{(3)}\rangle\}$ with amplitudes determined by dimensionless parameters $\alpha_j=w_j/(\hbar v_F|\boldsymbol{\kappa}_{+1}|)$ for $j=0,1$, where $w_0$ and $w_1$ are the AA and AB/BA interlayer tunneling parameters and $v_F$ is the monolayer Dirac velocity; defining $\beta=3(\alpha_0^2+\alpha_1^2)$, the moiré spinor-overlap correction entering deformation-potential electron–phonon matrix elements is approximated by the single-parameter form factor $F(\theta)=(1+\beta^{2})/(1+\beta)^{2}$. This truncated four-component perturbative construction is assumed to yield an accurate estimate of the overlap factor $F(\theta)$ down to the largest magic angle predicted by the chosen continuum parameters, so that $0.5\lesssim F(\theta)\le1$ can be used as a multiplicative correction to electron–phonon matrix elements in transport calculations.""",
)

relaxed_tunneling_magic_angle_velocity = claim(
    "Using continuum-model interlayer tunneling parameters w_0=90 meV and w_1=117 meV to incorporate atomic-relaxation effects, Wu, Hwang, and Das Sarma obtain a largest magic angle theta_magic about 1.025 degrees and a strongly suppressed twist-angle-dependent Dirac velocity v_F*(theta), while noting sample-dependent relaxation and strain can shift theta_magic and v_F* by order tens of percent [@Wu2018].",
    lkm_id="gcn_570f7bfc906e4dbd",
    source_paper="paper:867772031297389371",
    provenance_source="lkm",
    provenance_file="artifacts/lkm-discovery/input/may4_evidence_gcn_93c279f20f364a40.json",
    lkm_original=r"""Using continuum-model interlayer tunneling parameters $w_0=90\ \mathrm{meV}$ and $w_1=117\ \mathrm{meV}$ (intended to incorporate atomic relaxation effects) yields a largest-magnitude magic angle $\theta_{\rm magic}\approx1.025^\circ$ in the continuum moiré Hamiltonian band structure and produces a twist-angle dependence $v_F^*(\theta)$ with strong suppression near $\theta_{\rm magic}$; these parameter choices are assumed to be representative of experimental samples up to uncertainties from sample-dependent relaxation and strain that can shift $\theta_{\rm magic}$ and $v_F^*$ by order tens of percent.""",
)

wu_velocity_phonon_form_factor = claim(
    "In Wu, Hwang, and Das Sarma's continuum moire Hamiltonian calculation for twisted bilayer graphene, v_F*(theta) is strongly suppressed near theta_magic about 1.025 degrees, and a perturbative moire-wavefunction calculation gives the electron-phonon matrix-element form factor F(theta)=(1+beta^2)/(1+beta)^2 with beta=3(alpha_0^2+alpha_1^2), where alpha_j=w_j/(hbar v_F |kappa_{+1}|) for the AA and AB/BA tunneling parameters [@Wu2018].",
    lkm_id="gcn_93c279f20f364a40",
    source_paper="paper:867772031297389371",
    provenance_source="lkm",
    provenance_file="artifacts/lkm-discovery/input/may4_evidence_gcn_93c279f20f364a40.json",
    lkm_original=r"""A continuum moiré Hamiltonian calculation for twisted bilayer graphene yields a twist-angle-dependent renormalized Dirac velocity $v_F^*(\theta)$ that is strongly suppressed near a model magic angle $\theta_{\rm magic}\approx 1.025^\circ$ (the largest magic angle for the specified continuum-Hamiltonian parameters). A perturbative moiré-wavefunction calculation gives the electron–phonon matrix-element form factor
$$
F(\theta)=\frac{1+\beta^{2}}{(1+\beta)^{2}},\quad \beta=3(\alpha_0^2+\alpha_1^2),
$$
where $\alpha_{j}=w_{j}/(\hbar v_{F}|\boldsymbol{\kappa}_{+1}|)$ for $j=0,1$, $w_0$ and $w_1$ are the AA and AB/BA interlayer tunneling parameters in the continuum model, $v_F$ is the monolayer graphene Dirac velocity, and $|\boldsymbol{\kappa}_{+1}|$ is the magnitude of the moiré Dirac-point momentum in the chosen valley. In this model, $F(\theta)$ varies between $0.5$ (strong interlayer mixing near magic angle) and $1$ (vanishing interlayer tunneling).""",
)

derive_wu_velocity_phonon_form_factor = deduction(
    [moire_spinor_phonon_form_factor, relaxed_tunneling_magic_angle_velocity],
    wu_velocity_phonon_form_factor,
    reason=(
        "1. Define the valley +K moire continuum Hamiltonian as a 4x4 block "
        "matrix with layer Dirac Hamiltonians and spatially periodic interlayer "
        "tunneling.\n"
        "2. Define h_l(k) with twist angle theta, monolayer velocity v_F about "
        "10^8 cm/s, and layer-shifted Dirac momenta kappa_l.\n"
        "3. Expand interlayer tunneling in three moire Fourier components with "
        "AA and AB/BA tunneling parameters w_0 and w_1.\n"
        "4. Use w_0=90 meV and w_1=117 meV, diagonalize the continuum "
        "Hamiltonian, and obtain strong v_F*(theta) suppression with a largest "
        "magic angle theta_magic about 1.025 degrees.\n"
        "5. Construct perturbative moire wavefunctions from four layer/momentum "
        "components near a moire Dirac point.\n"
        "6. Define alpha_j=w_j/(hbar v_F |kappa_{+1}|) and beta=3(alpha_0^2+alpha_1^2), "
        "which also defines v_F* in the Dirac form of the projected Hamiltonian.\n"
        "7. Derive F(theta)=(1+beta^2)/(1+beta)^2 as the electron-phonon "
        "matrix-element form factor, varying from 0.5 near strong interlayer "
        "mixing to 1 for vanishing tunneling.\n"
        "8. Treat v_F*(theta) and F(theta) as known twist-angle inputs for "
        "transport and superconductivity calculations."
    ),
    prior=0.95,
)
