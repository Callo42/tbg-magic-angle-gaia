"""Leaf-claim priors for the twisted monolayer-bilayer subgraph."""

from .paper_nguyen2022 import gcn_42c7afbd_smab2_layer_resolved_dos


PRIORS = {
    gcn_42c7afbd_smab2_layer_resolved_dos: (
        0.82,
        "The premise is a selected Nguyen et al. relaxed tight-binding and layer-resolved DOS result for SM-(AB)_2, directly grounded in the LKM factor and figures, but it remains a computational result tied to the stated model and relaxation protocol; TODO:review",
    ),
}
