# Merge audit -- alternating-twist-quadrilayer-gaia

| pair | verdict | reason | dsl_action |
|---|---|---|---|
| `gcn_51a6d18a02c4407d` / `gcn_225da7b340cb47b8` | keep distinct | The premise concerns a heuristic ATQG-to-TBG twist-angle mapping; the root concerns device-specific superconducting-like and correlated-insulator behavior versus ATQG twist angle. | Separate `claim()` declarations linked by `deduction(..., prior=0.95)`. |
| decomposition helpers / `gcn_225da7b340cb47b8` | keep as derived helpers | Helpers isolate grounded parts of the compound root for synthesis readability, but they are not independent LKM conclusions. | `support([root], helper, prior=0.90)` or `support([mapping premise], helper, prior=0.90)`; no `equivalence()` emitted. |
