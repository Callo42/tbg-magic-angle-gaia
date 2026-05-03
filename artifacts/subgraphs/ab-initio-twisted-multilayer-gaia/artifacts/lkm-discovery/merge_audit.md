# Merge audit

No formal Gaia merge decisions have been made in this subgraph.

## Subgraph mapping pass

| pair_or_item | verdict | reason | source pointers |
|---|---|---|---|
| Empty premise IDs `gcn_af432bff1d3e4cf0` and `gcn_be5d1975ecac4211` | keep distinct | The first premise captures the established Wannier-derived TB workflow/detector setup used by the chain; the second captures the detector-output-to-p(theta) interpolation/blending step. Merging would hide two separate leaf assumptions. | `input/evidence_gcn_5f58746bcc0b4098.json` steps 1 and 3 |
| Root `gcn_5f58746bcc0b4098` vs premise IDs | keep distinct | The root is the derived magic-angle flat-band-likelihood conclusion, while the premises are workflow and detector/interpolation assumptions. | `input/evidence_gcn_5f58746bcc0b4098.json` |
| Discovery contradiction scan | no `contradiction()` promoted | The selected evidence contains no independent same-system counterclaim. The structural-relaxation caveat is recorded as a model-scope risk rather than an incompatible claim pair. | `contradictions.md`; `dismissed/structural_relaxation_scope.md` |
| Discovery equivalence scan | no `equivalence()` promoted | No independent same-proposition claim is available under the selected evidence. | `equivalences.md` |
