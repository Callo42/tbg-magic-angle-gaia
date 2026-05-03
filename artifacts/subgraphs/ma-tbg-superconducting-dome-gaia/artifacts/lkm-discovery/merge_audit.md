# Merge audit -- ma-tbg-superconducting-dome-gaia

| pair | verdict | reason | dsl_action |
|---|---|---|---|
| `gcn_ffd6d31f7b2642e6` / `gcn_006f88d8df3548fa` | keep distinct | The premise concerns interpreting half-filling insulating temperature dependence as correlated/Mott-like phenomenology; the root concerns the full MA-TBG temperature-density phase diagram with superconducting domes adjacent to that insulator. | Separate `claim()` declarations linked by `deduction(..., prior=0.95)`. |
| decomposition helpers / `gcn_006f88d8df3548fa` | keep as derived helpers | Helpers isolate grounded components of the compound root for synthesis readability, but they are not independent LKM claims. | `support([root], helper, prior=0.90)`; no `equivalence()` emitted. |
