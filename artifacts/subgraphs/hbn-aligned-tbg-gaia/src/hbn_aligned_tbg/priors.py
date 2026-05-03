"""priors.py -- leaf-claim priors for this audited LKM subgraph."""
from .paper_zhang2019 import (
    gcn_1d940e84a3744c85,
    gcn_464f6413fccb48be,
    gcn_a7252e5aaaf84d38,
    gcn_ca5e0f32e91c459b,
)

PRIORS = {
    gcn_464f6413fccb48be: (
        0.82,
        "LKM premise states the hierarchy between the h-BN moire potentials and the TBG interlayer coupling scale, then uses it as a first-approximation modeling choice; capped below 0.90 pending reviewer audit. TODO:review",
    ),
    gcn_a7252e5aaaf84d38: (
        0.78,
        "LKM premise maps a measured monolayer-graphene/h-BN neutral-point gap to a staggered mass parameter for h-BN-aligned MA-TBG; credible but model-dependent. TODO:review",
    ),
    gcn_ca5e0f32e91c459b: (
        0.80,
        "LKM premise reports numerical band isolation and Chern-number computation for a specified continuum-model parameter regime; capped below 0.90 pending convergence and implementation review. TODO:review",
    ),
    gcn_1d940e84a3744c85: (
        0.50,
        "The selected LKM factor contains this premise id with empty content, so it is retained only as an unspecified premise placeholder and assigned a neutral prior. TODO:review",
    ),
}
