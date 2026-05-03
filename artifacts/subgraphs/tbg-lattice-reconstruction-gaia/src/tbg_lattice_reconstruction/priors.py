"""priors.py -- leaf-claim priors for this audited LKM subgraph."""
from .paper_liu2020 import gcn_8cd2984a6296435c, gcn_ed8fa9253ea24982

PRIORS = {
    gcn_8cd2984a6296435c: (
        0.80,
        "LKM premise states a continuum-model result for relaxation-broadened and more isolated flat bands, but it remains a model-scoped qualitative calculation without explicit heterostrain; capped below 0.90. TODO:review",
    ),
    gcn_ed8fa9253ea24982: (
        0.72,
        "LKM premise records a heterostrain explanation for additional STS fine splitting using cited prior literature not otherwise present in data.papers; credible but more indirect in this selected JSON. TODO:review",
    ),
}
