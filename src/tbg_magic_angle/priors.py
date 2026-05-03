"""Leaf-claim priors for the synthesized TBG magic-angle Gaia package."""

from .paper_burg2022 import (
    gcn_51a6d18a_atqg_tbg_angle_mapping,
)

from .paper_cantele2020 import (
    gcn_6463be97083b44fd,
    gcn_abaf80790d664630,
)

from .paper_cao2018 import (
    gcn_ffd6d31f_correlated_insulator_phenomenology,
)

from .paper_dassarma2020 import (
    gcn_671ceef053a64aa7,
    gcn_d3808439ccf6496b,
)

from .paper_ge2021 import (
    gcn_ba97172fd9264409,
    gcn_e83deb9969844b33,
)

from .paper_herzogarbeitman2022 import (
    gcn_06caff12a4d84b26,
    gcn_fedb8c2683fb48c7,
)

from .paper_liu2020 import (
    gcn_8cd2984a6296435c,
    gcn_ed8fa9253ea24982,
)

from .paper_ma2019 import (
    gcn_2a4995cfc44a4638,
    gcn_4249f998947d4ee0,
    gcn_768268d063184cb8,
    gcn_ba18ade2bb8145ee,
)

from .paper_ma2020 import (
    gcn_2ceab67f16f34d1e,
    gcn_2fcfd55afc454c94,
)

from .paper_nguyen2022 import (
    gcn_42c7afbd_smab2_layer_resolved_dos,
)

from .paper_park2021 import (
    gcn_3618ccee_mattg_theta_over_sqrt2_mapping,
    gcn_71314760_mattg_displacement_field_modeling,
    gcn_c680c239_mattg_continuum_approximations,
)

from .paper_tritsaris2020 import (
    gcn_af432bff_ab_initio_tb_workflow,
    gcn_be5d1975_detector_interpolation,
)

from .paper_wang2020 import (
    gcn_fb78cfd7_magic_angle_continuum_regime,
)

from .paper_yamada2020 import (
    gcn_7687975d_small_angle_merging_conjecture,
)

from .paper_zhang2019 import (
    gcn_1d940e84a3744c85,
    gcn_464f6413fccb48be,
    gcn_a7252e5aaaf84d38,
    gcn_ca5e0f32e91c459b,
)


PRIORS = {
    gcn_ffd6d31f_correlated_insulator_phenomenology: (
        0.78,
        'The premise is grounded in the selected Cao et al. transport phenomenology and flat-band interaction scale, but the LKM text explicitly cautions that insulating temperature dependence alone is not a microscopic proof of a Mott mechanism; TODO:review',
    ),
    gcn_d3808439ccf6496b: (
        0.82,
        'LKM premise reports a numerical continuum-model fit and its stated angular window from the selected chain; capped below 0.90 pending reviewer audit. TODO:review',
    ),
    gcn_671ceef053a64aa7: (
        0.84,
        'LKM premise states how the BM continuum velocity is used as the noninteracting input in the selected paper; capped below 0.90 pending reviewer audit. TODO:review',
    ),
    gcn_06caff12a4d84b26: (
        0.74,
        'LKM premise asserts numerical Landau-level cutoff convergence for the phi=2pi BM Hamiltonian; plausible but requires explicit cutoff scans. TODO:review',
    ),
    gcn_fedb8c2683fb48c7: (
        0.68,
        'LKM premise packages convergence, parameter-grid extrapolation, and BM-model approximations into a physical interpretation; credible but more assumption-laden than the numerical setup claim. TODO:review',
    ),
    gcn_e83deb9969844b33: (
        0.68,
        'LKM premise extrapolates from a highlighted 9.4 degree compressed cell to the broader 9-27.8 degree commensurate large-angle set; plausible but explicitly a generalization. TODO:review',
    ),
    gcn_ba97172fd9264409: (
        0.35,
        'LKM premise treats single-particle DOS/VHS indicators as suggestive of many-body phases while the same chain notes no explicit many-body calculation or experimental proof. TODO:review',
    ),
    gcn_7687975d_small_angle_merging_conjecture: (
        0.64,
        'The selected LKM chain explicitly marks small-angle continuity of the four-Dirac-point mechanism as a plausible conjecture with unproven persistence and omitted relaxation/interaction effects; TODO:review',
    ),
    gcn_2fcfd55afc454c94: (
        0.82,
        'LKM premise states the modeling assumptions used for the selected continuum calculation; capped below 0.90 pending reviewer audit. TODO:review',
    ),
    gcn_2ceab67f16f34d1e: (
        0.8,
        'LKM premise records the minimal-model parameter scan and the full-parameter sensitivity caveat; capped below 0.90 pending reviewer audit. TODO:review',
    ),
    gcn_768268d063184cb8: (
        0.84,
        'LKM premise states the continuum minimal-model assumptions used for the reported twisted-trilayer magic-angle calculation; capped below 0.90 pending reviewer audit. TODO:review',
    ),
    gcn_ba18ade2bb8145ee: (
        0.83,
        'LKM premise records parameter values gamma_0 and gamma_1 and their role in setting the reported magic angle; capped below 0.90 pending reviewer audit. TODO:review',
    ),
    gcn_2a4995cfc44a4638: (
        0.74,
        'LKM premise is a numerical-convergence assumption for finite plane-wave and k-point sampling rather than an independently checked result; capped below 0.90 pending reviewer audit. TODO:review',
    ),
    gcn_4249f998947d4ee0: (
        0.72,
        'LKM premise is a finite twist-angle-grid sufficiency assumption for locating the largest magic angle; capped below 0.90 pending reviewer audit. TODO:review',
    ),
    gcn_51a6d18a_atqg_tbg_angle_mapping: (
        0.76,
        'The premise is grounded in the selected Burg et al. ATQG theoretical-comparison context, but the LKM text explicitly labels theta_TBG = theta_ATQG / phi as heuristic and not quantitatively equivalent across bandwidths, interaction strengths, or exact magic-angle conditions; TODO:review',
    ),
    gcn_42c7afbd_smab2_layer_resolved_dos: (
        0.82,
        'The premise is a selected Nguyen et al. relaxed tight-binding and layer-resolved DOS result for SM-(AB)_2, directly grounded in the LKM factor and figures, but it remains a computational result tied to the stated model and relaxation protocol; TODO:review',
    ),
    gcn_af432bff_ab_initio_tb_workflow: (
        0.78,
        'The selected LKM chain treats the Wannier-derived ab initio tight-binding workflow and detector setup as established, but the premise text itself is empty and relies on chain-step reconstruction; TODO:review',
    ),
    gcn_be5d1975_detector_interpolation: (
        0.72,
        'The selected LKM chain describes converting detector outputs into p(theta), but the exact interpolation/blending prescription is only referenced indirectly and the premise text itself is empty; TODO:review',
    ),
    gcn_8cd2984a6296435c: (
        0.80,
        'LKM premise states a continuum-model result for relaxation-broadened and more isolated flat bands, but it remains a model-scoped qualitative calculation without explicit heterostrain; capped below 0.90. TODO:review',
    ),
    gcn_ed8fa9253ea24982: (
        0.72,
        'LKM premise records a heterostrain explanation for additional STS fine splitting using cited prior literature not otherwise present in data.papers; credible but more indirect in this selected JSON. TODO:review',
    ),
    gcn_6463be97083b44fd: (
        0.62,
        'Selected LKM premise is an explicit interpretive assumption that Kohn-Sham vdW-DF2 gaps can be quantitatively compared to spectroscopic gaps despite possible correlation and quasiparticle self-energy renormalization; capped below 0.90. TODO:review',
    ),
    gcn_abaf80790d664630: (
        0.70,
        'Selected LKM premise is a methodological diagnostic assumption for separating in-plane and out-of-plane relaxation effects while acknowledging possible nonlinear coupling in full relaxation; capped below 0.90. TODO:review',
    ),
    gcn_464f6413fccb48be: (
        0.82,
        'LKM premise states the hierarchy between the h-BN moire potentials and the TBG interlayer coupling scale, then uses it as a first-approximation modeling choice; capped below 0.90 pending reviewer audit. TODO:review',
    ),
    gcn_a7252e5aaaf84d38: (
        0.78,
        'LKM premise maps a measured monolayer-graphene/h-BN neutral-point gap to a staggered mass parameter for h-BN-aligned MA-TBG; credible but model-dependent. TODO:review',
    ),
    gcn_ca5e0f32e91c459b: (
        0.80,
        'LKM premise reports numerical band isolation and Chern-number computation for a specified continuum-model parameter regime; capped below 0.90 pending convergence and implementation review. TODO:review',
    ),
    gcn_1d940e84a3744c85: (
        0.50,
        'The selected LKM factor contains this premise id with empty content, so it is retained only as an unspecified premise placeholder and assigned a neutral prior. TODO:review',
    ),
    gcn_fb78cfd7_magic_angle_continuum_regime: (
        0.82,
        'The premise is the selected Wang et al. continuum-model applicability regime for magic-angle TBG on a transition metal dichalcogenide; it is directly grounded in the LKM factor but remains model- and parameter-regime scoped, so the prior is capped below 0.90. TODO:review',
    ),
    gcn_c680c239_mattg_continuum_approximations: (
        0.76,
        'LKM premise states the continuum-model approximations that ground the MATTG calculation, but several are quantitative modeling assumptions: no direct top-bottom coupling, fixed hopping parameters, empirical relaxation via w_prime, and non-self-consistent displacement-field modeling. TODO:review',
    ),
    gcn_3618ccee_mattg_theta_over_sqrt2_mapping: (
        0.80,
        'LKM premise directly states the theta/sqrt(2) reduction and larger MATTG magic-angle trend, while also noting dependence on higher-order coupling, relaxation, and ideal mirror symmetry. TODO:review',
    ),
    gcn_71314760_mattg_displacement_field_modeling: (
        0.74,
        'LKM premise treats Delta V=dD/epsilon_0 as qualitatively adequate for mirror-symmetry breaking, but explicitly warns that neglected screening and non-local corrections can shift quantitative hybridization and Van Hove features. TODO:review',
    ),
}
