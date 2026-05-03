"""priors.py -- leaf-claim priors for pressure-flat-band-tbg-gaia.

Every entry is auto-seeded from the selected LKM evidence and marked for review.
"""

from .paper_ge2021 import gcn_ba97172fd9264409, gcn_e83deb9969844b33


PRIORS = {
    gcn_e83deb9969844b33: (
        0.68,
        "LKM premise extrapolates from a highlighted 9.4 degree compressed cell to the broader 9-27.8 degree commensurate large-angle set; plausible but explicitly a generalization. TODO:review",
    ),
    gcn_ba97172fd9264409: (
        0.35,
        "LKM premise treats single-particle DOS/VHS indicators as suggestive of many-body phases while the same chain notes no explicit many-body calculation or experimental proof. TODO:review",
    ),
}
