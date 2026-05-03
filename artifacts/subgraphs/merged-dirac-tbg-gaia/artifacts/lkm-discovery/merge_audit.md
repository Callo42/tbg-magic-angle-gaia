# Merge audit

No formal Gaia merge decisions have been made in this subgraph.

## Subgraph mapping pass

| pair_or_item | verdict | reason | source pointers |
|---|---|---|---|
| Root evidence chain `gcn_8159f32dda354258` | keep both `gcn_*` claims distinct | `gcn_7687975d32314167` states the small-angle continuity conjecture and assumptions; `gcn_8159f32dda354258` states the inferred vanishing-velocity / flat-band consequence. Merging would hide the leaf assumption that needs reviewer prior judgment. | `input/evidence_gcn_8159f32dda354258.json` |
| Discovery contradiction scan | no `contradiction()` promoted | The selected evidence provides no independent same-system counterclaim. The conjectural status is recorded as a prior risk and dismissal note rather than a logical conflict. | `contradictions.md`; `dismissed/small_angle_conjecture_scope.md` |
| Discovery equivalence scan | no `equivalence()` promoted | The root and premise are related but not the same proposition; no external same-proposition claim is available under the selected-evidence-only constraint. | `equivalences.md` |
