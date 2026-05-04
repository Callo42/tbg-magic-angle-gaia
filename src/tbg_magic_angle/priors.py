"""Leaf-claim priors for the May 4 TBG magic-angle package."""

from .paper_dassarma2020 import (
    bm_velocity_bare_input,
    bm_velocity_linear_fit,
)
from .paper_wu2018 import (
    moire_spinor_phonon_form_factor,
    relaxed_tunneling_magic_angle_velocity,
)
from .paper_dassarma2022 import (
    bm_velocity_suppression_caveated,
)
from .paper_qin2021 import (
    continuum_vhs_pairing_band_assumption,
    intervalley_scattering_neglect,
    intravalley_coulomb_tuning_parameter,
    optical_phonons_instantaneous_couplings,
    vhs_tc_velocity_extrema_coincidence,
)
from .paper_uchida2014 import (
    half_filled_flat_band_magnetism_tendency,
    kohn_sham_magic_angle_numerical_scope,
    small_angle_corrugation_extrapolation,
)
from .paper_tritsaris2020 import (
    ab_initio_tb_flat_band_workflow,
    flat_band_detector_interpolation,
)
from .paper_liu2020 import (
    heterostrain_flat_band_fine_splitting,
    relaxation_broadens_isolates_flat_bands,
)
from .paper_cantele2020 import (
    dft_gap_spectroscopy_comparison_assumption,
    relaxation_component_diagnostic_assumption,
)
from .paper_herzogarbeitman2022 import (
    magnetic_bloch_cutoff_convergence,
    reentrant_flat_band_parameter_convergence,
)
from .paper_yamada2020 import (
    small_angle_dirac_merging_conjecture,
)


PRIORS = {
    bm_velocity_linear_fit: (
        0.82,
        "LKM premise reports a numerical BM-continuum fit and its angular window for v_F*(theta); capped below 0.90 pending reviewer audit. TODO:review",
    ),
    bm_velocity_bare_input: (
        0.84,
        "LKM premise states how the BM continuum velocity is used as a noninteracting input in the selected root paper; capped below 0.90 pending reviewer audit. TODO:review",
    ),
    moire_spinor_phonon_form_factor: (
        0.76,
        "LKM premise derives a perturbative moire spinor-overlap factor for electron-phonon matrix elements; it depends on a truncated four-component construction. TODO:review",
    ),
    relaxed_tunneling_magic_angle_velocity: (
        0.78,
        "LKM premise reports continuum-model parameters w_0=90 meV and w_1=117 meV and a theta_magic estimate, while noting sample-dependent relaxation and strain. TODO:review",
    ),
    bm_velocity_suppression_caveated: (
        0.80,
        "LKM premise is a BM-model velocity-suppression statement with explicit caveats excluding lattice relaxation and many-body self-energy corrections. TODO:review",
    ),
    optical_phonons_instantaneous_couplings: (
        0.72,
        "LKM premise treats optical-phonon interactions as instantaneous because phonon energies exceed the modeled flat-band bandwidth; model assumption. TODO:review",
    ),
    intravalley_coulomb_tuning_parameter: (
        0.68,
        "LKM premise treats intravalley Coulomb strength u as a phenomenological tuning parameter rather than a direct microscopic value. TODO:review",
    ),
    intervalley_scattering_neglect: (
        0.74,
        "LKM premise neglects intervalley Coulomb scattering relative to intravalley repulsion in the MATBG BdG model; plausible but approximation-heavy. TODO:review",
    ),
    continuum_vhs_pairing_band_assumption: (
        0.70,
        "LKM premise assumes non-reconstructed continuum bands capture VHS locations despite neglected interaction-driven flavor symmetry breaking. TODO:review",
    ),
    vhs_tc_velocity_extrema_coincidence: (
        0.76,
        "LKM premise summarizes the modeled coincidence between T_c maxima and v_F* minima at VHSs across parameter scans; model-scoped. TODO:review",
    ),
    small_angle_corrugation_extrapolation: (
        0.70,
        "LKM premise reconstructs small-angle corrugation by extrapolating Fourier coefficients from larger-angle optimized geometries. TODO:review",
    ),
    kohn_sham_magic_angle_numerical_scope: (
        0.66,
        "LKM premise explicitly ties the theta_M about 1.08 degrees Kohn-Sham zero to geometry extrapolation and numerical approximations. TODO:review",
    ),
    half_filled_flat_band_magnetism_tendency: (
        0.55,
        "LKM premise is an interpretive magnetic-ordering tendency from half-filled Kohn-Sham flat bands without explicit spin-polarized or many-body proof. TODO:review",
    ),
    ab_initio_tb_flat_band_workflow: (
        0.78,
        "The LKM chain treats the Wannier-derived ab initio tight-binding workflow and detector setup as established, but premise text itself is empty and reconstructed from factor steps. TODO:review",
    ),
    flat_band_detector_interpolation: (
        0.72,
        "The LKM chain describes converting detector outputs into p(theta), but the interpolation/blending prescription is only indirectly described and premise text is empty. TODO:review",
    ),
    relaxation_broadens_isolates_flat_bands: (
        0.80,
        "LKM premise states a continuum-model result for relaxation-broadened and more isolated flat bands, with explicit heterostrain omission. TODO:review",
    ),
    heterostrain_flat_band_fine_splitting: (
        0.72,
        "LKM premise records a heterostrain explanation for additional STS fine splitting using cited prior literature not otherwise present in data.papers. TODO:review",
    ),
    dft_gap_spectroscopy_comparison_assumption: (
        0.62,
        "LKM premise is an interpretive assumption comparing Kohn-Sham vdW-DF2 gaps to spectroscopic gaps despite possible self-energy renormalization. TODO:review",
    ),
    relaxation_component_diagnostic_assumption: (
        0.70,
        "LKM premise is a methodological diagnostic assumption separating in-plane and out-of-plane relaxation while acknowledging nonlinear coupling. TODO:review",
    ),
    magnetic_bloch_cutoff_convergence: (
        0.74,
        "LKM premise asserts numerical Landau-level cutoff convergence for the phi=2pi BM Hamiltonian; plausible but requires explicit cutoff scans. TODO:review",
    ),
    reentrant_flat_band_parameter_convergence: (
        0.68,
        "LKM premise packages convergence, parameter-grid extrapolation, and BM-model approximations into a physical interpretation. TODO:review",
    ),
    small_angle_dirac_merging_conjecture: (
        0.64,
        "The LKM chain explicitly marks small-angle continuity of the four-Dirac-point mechanism as a conjecture with omitted relaxation and interaction effects. TODO:review",
    ),
}
