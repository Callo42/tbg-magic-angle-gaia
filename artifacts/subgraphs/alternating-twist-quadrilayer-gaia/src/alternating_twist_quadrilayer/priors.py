"""Leaf-claim priors for the alternating-twist quadrilayer subgraph."""

from .paper_burg2022 import gcn_51a6d18a_atqg_tbg_angle_mapping


PRIORS = {
    gcn_51a6d18a_atqg_tbg_angle_mapping: (
        0.76,
        "The premise is grounded in the selected Burg et al. ATQG theoretical-comparison context, but the LKM text explicitly labels theta_TBG = theta_ATQG / phi as heuristic and not quantitatively equivalent across bandwidths, interaction strengths, or exact magic-angle conditions; TODO:review",
    ),
}
