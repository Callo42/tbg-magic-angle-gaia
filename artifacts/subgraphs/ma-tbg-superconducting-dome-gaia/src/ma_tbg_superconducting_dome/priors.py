"""Leaf-claim priors for the MA-TBG superconducting dome subgraph."""

from .paper_cao2018 import gcn_ffd6d31f_correlated_insulator_phenomenology


PRIORS = {
    gcn_ffd6d31f_correlated_insulator_phenomenology: (
        0.78,
        "The premise is grounded in the selected Cao et al. transport phenomenology and flat-band interaction scale, but the LKM text explicitly cautions that insulating temperature dependence alone is not a microscopic proof of a Mott mechanism; TODO:review",
    ),
}
