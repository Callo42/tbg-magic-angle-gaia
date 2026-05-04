"""paper_wu2018 -- continuum velocity and electron-phonon form factor in MATBG.

Source: Phonon-induced giant linear-in-T resistivity in magic angle twisted
bilayer graphene: Ordinary strangeness and exotic superconductivity
DOI: 10.48550/arXiv.1811.04920
Reference key: Wu2018
"""

from gaia.lang import claim, deduction


gcn_b411dd99a41e4de2 = claim(
    "For a moire Dirac point in twisted bilayer graphene, Wu, Hwang, and Das Sarma construct degenerate Dirac-point eigenstates from four layer/momentum spinors with amplitudes set by alpha_j=w_j/(hbar v_F |kappa_{+1}|), define beta=3(alpha_0^2+alpha_1^2), and approximate the deformation-potential electron-phonon spinor-overlap factor as F(theta)=(1+beta^2)/(1+beta)^2, with 0.5 <= F(theta) <= 1 used as a transport matrix-element correction [@Wu2018].",
    lkm_id="gcn_b411dd99a41e4de2",
    source_paper="paper:867772031297389371",
    provenance_source="lkm",
    provenance_file="artifacts/lkm-discovery/input/may4_evidence_gcn_93c279f20f364a40.json",
    lkm_original="For a moire Dirac point at momentum kappa_{+1}, define two degenerate Dirac-point eigenstates as normalized linear combinations of four layer/momentum spinors with amplitudes determined by alpha_j=w_j/(hbar v_F |kappa_{+1}|); defining beta=3(alpha_0^2+alpha_1^2), the moire spinor-overlap correction entering deformation-potential electron-phonon matrix elements is approximated by F(theta)=(1+beta^2)/(1+beta)^2.",
)

gcn_570f7bfc906e4dbd = claim(
    "Using continuum-model interlayer tunneling parameters w_0=90 meV and w_1=117 meV to incorporate atomic-relaxation effects, Wu, Hwang, and Das Sarma obtain a largest magic angle theta_magic about 1.025 degrees and a strongly suppressed twist-angle-dependent Dirac velocity v_F*(theta), while noting sample-dependent relaxation and strain can shift theta_magic and v_F* by order tens of percent [@Wu2018].",
    lkm_id="gcn_570f7bfc906e4dbd",
    source_paper="paper:867772031297389371",
    provenance_source="lkm",
    provenance_file="artifacts/lkm-discovery/input/may4_evidence_gcn_93c279f20f364a40.json",
    lkm_original="Using continuum-model interlayer tunneling parameters w_0=90 meV and w_1=117 meV yields a largest-magnitude magic angle theta_magic approximately 1.025 degrees in the continuum moire Hamiltonian band structure and produces a twist-angle dependence v_F*(theta) with strong suppression near theta_magic.",
)

gcn_93c279f20f364a40 = claim(
    "In Wu, Hwang, and Das Sarma's continuum moire Hamiltonian calculation for twisted bilayer graphene, v_F*(theta) is strongly suppressed near theta_magic about 1.025 degrees, and a perturbative moire-wavefunction calculation gives the electron-phonon matrix-element form factor F(theta)=(1+beta^2)/(1+beta)^2 with beta=3(alpha_0^2+alpha_1^2), where alpha_j=w_j/(hbar v_F |kappa_{+1}|) for the AA and AB/BA tunneling parameters [@Wu2018].",
    lkm_id="gcn_93c279f20f364a40",
    source_paper="paper:867772031297389371",
    provenance_source="lkm",
    provenance_file="artifacts/lkm-discovery/input/may4_evidence_gcn_93c279f20f364a40.json",
    lkm_original="A continuum moire Hamiltonian calculation for twisted bilayer graphene yields a twist-angle-dependent renormalized Dirac velocity v_F*(theta) that is strongly suppressed near a model magic angle theta_magic approximately 1.025 degrees. A perturbative moire-wavefunction calculation gives the electron-phonon matrix-element form factor F(theta)=(1+beta^2)/(1+beta)^2 with beta=3(alpha_0^2+alpha_1^2).",
)

gfac_4dfdc41c1d7c4f0b = deduction(
    [gcn_b411dd99a41e4de2, gcn_570f7bfc906e4dbd],
    gcn_93c279f20f364a40,
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
