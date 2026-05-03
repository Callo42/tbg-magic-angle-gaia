"""Leaf-claim priors for the merged Dirac TBG subgraph."""

from .paper_yamada2020 import gcn_7687975d_small_angle_merging_conjecture


PRIORS = {
    gcn_7687975d_small_angle_merging_conjecture: (
        0.64,
        "The selected LKM chain explicitly marks small-angle continuity of the four-Dirac-point mechanism as a plausible conjecture with unproven persistence and omitted relaxation/interaction effects; TODO:review",
    ),
}
