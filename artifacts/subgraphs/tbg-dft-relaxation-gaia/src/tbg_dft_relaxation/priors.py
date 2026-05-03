"""Leaf-claim priors for the TBG DFT-relaxation subgraph."""

from .paper_cantele2020 import (
    gcn_6463be97083b44fd,
    gcn_abaf80790d664630,
)


PRIORS = {
    gcn_6463be97083b44fd: (
        0.62,
        "Selected LKM premise is an explicit interpretive assumption that Kohn-Sham vdW-DF2 gaps can be quantitatively compared to spectroscopic gaps despite possible correlation and quasiparticle self-energy renormalization; capped below 0.90. TODO:review",
    ),
    gcn_abaf80790d664630: (
        0.70,
        "Selected LKM premise is a methodological diagnostic assumption for separating in-plane and out-of-plane relaxation effects while acknowledging possible nonlinear coupling in full relaxation; capped below 0.90. TODO:review",
    ),
}
