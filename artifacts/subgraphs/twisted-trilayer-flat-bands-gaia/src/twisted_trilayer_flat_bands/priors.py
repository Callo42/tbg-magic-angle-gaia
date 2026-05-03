"""priors.py -- leaf-claim priors for this audited LKM subgraph."""
from .paper_ma2019 import (
    gcn_2a4995cfc44a4638,
    gcn_4249f998947d4ee0,
    gcn_768268d063184cb8,
    gcn_ba18ade2bb8145ee,
)

PRIORS = {
    gcn_768268d063184cb8: (
        0.84,
        "LKM premise states the continuum minimal-model assumptions used for the reported twisted-trilayer magic-angle calculation; capped below 0.90 pending reviewer audit. TODO:review",
    ),
    gcn_ba18ade2bb8145ee: (
        0.83,
        "LKM premise records parameter values gamma_0 and gamma_1 and their role in setting the reported magic angle; capped below 0.90 pending reviewer audit. TODO:review",
    ),
    gcn_2a4995cfc44a4638: (
        0.74,
        "LKM premise is a numerical-convergence assumption for finite plane-wave and k-point sampling rather than an independently checked result; capped below 0.90 pending reviewer audit. TODO:review",
    ),
    gcn_4249f998947d4ee0: (
        0.72,
        "LKM premise is a finite twist-angle-grid sufficiency assumption for locating the largest magic angle; capped below 0.90 pending reviewer audit. TODO:review",
    ),
}
