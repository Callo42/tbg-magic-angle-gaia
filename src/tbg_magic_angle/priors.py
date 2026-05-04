"""Leaf-claim priors for the May 4 TBG magic-angle package."""

from .paper_dassarma2020 import (
    gcn_671ceef053a64aa7,
    gcn_d3808439ccf6496b,
)
from .paper_wu2018 import (
    gcn_b411dd99a41e4de2,
    gcn_570f7bfc906e4dbd,
)
from .paper_dassarma2022 import (
    gcn_1cb7675d5185405d,
)
from .paper_qin2021 import (
    gcn_1b0c5250d2574e24,
    gcn_4eda4fedb8364912,
    gcn_993c306ad37c4dfb,
    gcn_2bc94d32817142f7,
    gcn_324b385e04254463,
)
from .paper_uchida2014 import (
    gcn_159120a419184e9e,
    gcn_75a1c2477ca448b0,
    gcn_390a496067b94209,
)
from .paper_tritsaris2020 import (
    gcn_af432bff_ab_initio_tb_workflow,
    gcn_be5d1975_detector_interpolation,
)
from .paper_liu2020 import (
    gcn_8cd2984a6296435c,
    gcn_ed8fa9253ea24982,
)
from .paper_cantele2020 import (
    gcn_6463be97083b44fd,
    gcn_abaf80790d664630,
)
from .paper_herzogarbeitman2022 import (
    gcn_06caff12a4d84b26,
    gcn_fedb8c2683fb48c7,
)
from .paper_yamada2020 import (
    gcn_7687975d_small_angle_merging_conjecture,
)


PRIORS = {
    gcn_d3808439ccf6496b: (
        0.82,
        "LKM premise reports a numerical BM-continuum fit and its angular window for v_F*(theta); capped below 0.90 pending reviewer audit. TODO:review",
    ),
    gcn_671ceef053a64aa7: (
        0.84,
        "LKM premise states how the BM continuum velocity is used as a noninteracting input in the selected root paper; capped below 0.90 pending reviewer audit. TODO:review",
    ),
    gcn_b411dd99a41e4de2: (
        0.76,
        "LKM premise derives a perturbative moire spinor-overlap factor for electron-phonon matrix elements; it depends on a truncated four-component construction. TODO:review",
    ),
    gcn_570f7bfc906e4dbd: (
        0.78,
        "LKM premise reports continuum-model parameters w_0=90 meV and w_1=117 meV and a theta_magic estimate, while noting sample-dependent relaxation and strain. TODO:review",
    ),
    gcn_1cb7675d5185405d: (
        0.80,
        "LKM premise is a BM-model velocity-suppression statement with explicit caveats excluding lattice relaxation and many-body self-energy corrections. TODO:review",
    ),
    gcn_1b0c5250d2574e24: (
        0.72,
        "LKM premise treats optical-phonon interactions as instantaneous because phonon energies exceed the modeled flat-band bandwidth; model assumption. TODO:review",
    ),
    gcn_4eda4fedb8364912: (
        0.68,
        "LKM premise treats intravalley Coulomb strength u as a phenomenological tuning parameter rather than a direct microscopic value. TODO:review",
    ),
    gcn_993c306ad37c4dfb: (
        0.74,
        "LKM premise neglects intervalley Coulomb scattering relative to intravalley repulsion in the MATBG BdG model; plausible but approximation-heavy. TODO:review",
    ),
    gcn_2bc94d32817142f7: (
        0.70,
        "LKM premise assumes non-reconstructed continuum bands capture VHS locations despite neglected interaction-driven flavor symmetry breaking. TODO:review",
    ),
    gcn_324b385e04254463: (
        0.76,
        "LKM premise summarizes the modeled coincidence between T_c maxima and v_F* minima at VHSs across parameter scans; model-scoped. TODO:review",
    ),
    gcn_159120a419184e9e: (
        0.70,
        "LKM premise reconstructs small-angle corrugation by extrapolating Fourier coefficients from larger-angle optimized geometries. TODO:review",
    ),
    gcn_75a1c2477ca448b0: (
        0.66,
        "LKM premise explicitly ties the theta_M about 1.08 degrees Kohn-Sham zero to geometry extrapolation and numerical approximations. TODO:review",
    ),
    gcn_390a496067b94209: (
        0.55,
        "LKM premise is an interpretive magnetic-ordering tendency from half-filled Kohn-Sham flat bands without explicit spin-polarized or many-body proof. TODO:review",
    ),
    gcn_af432bff_ab_initio_tb_workflow: (
        0.78,
        "The LKM chain treats the Wannier-derived ab initio tight-binding workflow and detector setup as established, but premise text itself is empty and reconstructed from factor steps. TODO:review",
    ),
    gcn_be5d1975_detector_interpolation: (
        0.72,
        "The LKM chain describes converting detector outputs into p(theta), but the interpolation/blending prescription is only indirectly described and premise text is empty. TODO:review",
    ),
    gcn_8cd2984a6296435c: (
        0.80,
        "LKM premise states a continuum-model result for relaxation-broadened and more isolated flat bands, with explicit heterostrain omission. TODO:review",
    ),
    gcn_ed8fa9253ea24982: (
        0.72,
        "LKM premise records a heterostrain explanation for additional STS fine splitting using cited prior literature not otherwise present in data.papers. TODO:review",
    ),
    gcn_6463be97083b44fd: (
        0.62,
        "LKM premise is an interpretive assumption comparing Kohn-Sham vdW-DF2 gaps to spectroscopic gaps despite possible self-energy renormalization. TODO:review",
    ),
    gcn_abaf80790d664630: (
        0.70,
        "LKM premise is a methodological diagnostic assumption separating in-plane and out-of-plane relaxation while acknowledging nonlinear coupling. TODO:review",
    ),
    gcn_06caff12a4d84b26: (
        0.74,
        "LKM premise asserts numerical Landau-level cutoff convergence for the phi=2pi BM Hamiltonian; plausible but requires explicit cutoff scans. TODO:review",
    ),
    gcn_fedb8c2683fb48c7: (
        0.68,
        "LKM premise packages convergence, parameter-grid extrapolation, and BM-model approximations into a physical interpretation. TODO:review",
    ),
    gcn_7687975d_small_angle_merging_conjecture: (
        0.64,
        "The LKM chain explicitly marks small-angle continuity of the four-Dirac-point mechanism as a conjecture with omitted relaxation and interaction effects. TODO:review",
    ),
}
