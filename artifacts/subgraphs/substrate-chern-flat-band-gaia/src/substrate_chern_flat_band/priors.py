"""Leaf-claim priors for the substrate Chern flat-band subgraph."""

from .paper_wang2020 import gcn_fb78cfd7_magic_angle_continuum_regime


PRIORS = {
    gcn_fb78cfd7_magic_angle_continuum_regime: (
        0.82,
        "The premise is the selected Wang et al. continuum-model applicability regime for magic-angle TBG on a transition metal dichalcogenide; it is directly grounded in the LKM factor but remains model- and parameter-regime scoped, so the prior is capped below 0.90. TODO:review",
    ),
}
