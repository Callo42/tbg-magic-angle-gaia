# Merge audit log -- tbg-dft-relaxation-gaia

## Duplicate and equivalence decisions

| pair/group | verdict | reason | action |
|---|---|---|---|
| gcn_6463be97083b44fd vs gcn_abaf80790d664630 | keep distinct | one is a quasiparticle/correlation comparability assumption and the other is a structural-relaxation diagnostic assumption | no merge |
| DFT and tight-binding low-energy agreement inside gcn_de1d329f326f4e75 | keep inside root | same source paper and same selected LKM conclusion; not independent evidence | no equivalence edge |
| full relaxation vs in-plane-only/out-of-plane-only relaxation clauses inside gcn_de1d329f326f4e75 | keep inside root | the clauses are scoped comparisons from one evidence chain, not separate independent claims | no merge or contradiction edge |

## Contradiction decisions

No `contradiction()` operator was emitted. The selected JSON contains only one chain and no counter-claim asserting incompatible gap values or relaxation outcomes for the same system and conditions.
