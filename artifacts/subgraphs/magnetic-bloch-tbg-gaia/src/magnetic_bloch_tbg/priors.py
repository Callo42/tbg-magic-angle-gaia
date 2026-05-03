"""Leaf priors for the magnetic Bloch TBG subgraph.

Auto-seeded from LKM chain premises. Values are capped at 0.90 and marked for
review because they encode numerical-convergence and model-interpretation
judgments rather than direct experimental facts.
"""

from .paper_herzogarbeitman2022 import (
    gcn_06caff12a4d84b26,
    gcn_fedb8c2683fb48c7,
)


PRIORS = {
    gcn_06caff12a4d84b26: (
        0.74,
        "LKM premise asserts numerical Landau-level cutoff convergence for the phi=2pi BM Hamiltonian; plausible but requires explicit cutoff scans. TODO:review",
    ),
    gcn_fedb8c2683fb48c7: (
        0.68,
        "LKM premise packages convergence, parameter-grid extrapolation, and BM-model approximations into a physical interpretation; credible but more assumption-laden than the numerical setup claim. TODO:review",
    ),
}
