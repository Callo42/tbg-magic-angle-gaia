# Merge audit log - hbn-aligned-tbg-gaia

## Duplicate and equivalence decisions

| pair/group | verdict | reason | action |
|---|---|---|---|
| selected payload `gcn_*` claims | keep distinct | The four premise ids and the root conclusion play different roles: approximation hierarchy, mass estimate, active-band isolation/topology, empty placeholder premise, and final model-result conclusion. | no merge |
| empty premise `gcn_1d940e84a3744c85` | keep as placeholder | The LKM factor explicitly includes the id but provides no content; merging it into a scientific premise would invent evidence. | retained with `todo` metadata and neutral prior |

## Contradiction decisions

No contradiction operator was emitted. The selected chain's most important tensions are modeling-scope questions rather than mutually exclusive same-scope claims: ignoring the h-BN moire potential matrices even though the reported active-band gap is small, mapping a monolayer h-BN gap to a TBG mass parameter, and relying on numerical isolation/Chern computation without an independent convergence chain in this payload.
