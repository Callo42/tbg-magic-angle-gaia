"""Leaf-claim priors for the ab initio twisted multilayer subgraph."""

from .paper_tritsaris2020 import (
    gcn_af432bff_ab_initio_tb_workflow,
    gcn_be5d1975_detector_interpolation,
)


PRIORS = {
    gcn_af432bff_ab_initio_tb_workflow: (
        0.78,
        "The selected LKM chain treats the Wannier-derived ab initio tight-binding workflow and detector setup as established, but the premise text itself is empty and relies on chain-step reconstruction; TODO:review",
    ),
    gcn_be5d1975_detector_interpolation: (
        0.72,
        "The selected LKM chain describes converting detector outputs into p(theta), but the exact interpolation/blending prescription is only referenced indirectly and the premise text itself is empty; TODO:review",
    ),
}
