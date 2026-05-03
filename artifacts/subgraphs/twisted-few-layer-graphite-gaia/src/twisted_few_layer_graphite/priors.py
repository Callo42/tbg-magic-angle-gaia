"""priors.py -- leaf-claim priors for this audited LKM subgraph."""
from .paper_ma2020 import gcn_2ceab67f16f34d1e, gcn_2fcfd55afc454c94

PRIORS = {
    gcn_2fcfd55afc454c94: (
        0.82,
        "LKM premise states the modeling assumptions used for the selected continuum calculation; capped below 0.90 pending reviewer audit. TODO:review",
    ),
    gcn_2ceab67f16f34d1e: (
        0.80,
        "LKM premise records the minimal-model parameter scan and the full-parameter sensitivity caveat; capped below 0.90 pending reviewer audit. TODO:review",
    ),
}
