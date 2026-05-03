"""priors.py -- leaf-claim priors for this audited LKM subgraph."""

from .paper_park2021 import (
    gcn_3618ccee_mattg_theta_over_sqrt2_mapping,
    gcn_71314760_mattg_displacement_field_modeling,
    gcn_c680c239_mattg_continuum_approximations,
)


PRIORS = {
    gcn_c680c239_mattg_continuum_approximations: (
        0.76,
        "LKM premise states the continuum-model approximations that ground the MATTG calculation, but several are quantitative modeling assumptions: no direct top-bottom coupling, fixed hopping parameters, empirical relaxation via w', and non-self-consistent displacement-field modeling. TODO:review",
    ),
    gcn_3618ccee_mattg_theta_over_sqrt2_mapping: (
        0.80,
        "LKM premise directly states the theta/sqrt(2) reduction and larger MATTG magic-angle trend, while also noting dependence on higher-order coupling, relaxation, and ideal mirror symmetry. TODO:review",
    ),
    gcn_71314760_mattg_displacement_field_modeling: (
        0.74,
        "LKM premise treats Delta V=dD/epsilon_0 as qualitatively adequate for mirror-symmetry breaking, but explicitly warns that neglected screening and non-local corrections can shift quantitative hybridization and Van Hove features. TODO:review",
    ),
}
