"""priors.py -- leaf-claim priors for this audited LKM subgraph."""
from .paper_dassarma2020 import gcn_671ceef053a64aa7, gcn_d3808439ccf6496b

PRIORS = {
    gcn_d3808439ccf6496b: (
        0.82,
        "LKM premise reports a numerical continuum-model fit and its stated angular window from the selected chain; capped below 0.90 pending reviewer audit. TODO:review",
    ),
    gcn_671ceef053a64aa7: (
        0.84,
        "LKM premise states how the BM continuum velocity is used as the noninteracting input in the selected paper; capped below 0.90 pending reviewer audit. TODO:review",
    ),
}
