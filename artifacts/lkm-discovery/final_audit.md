# Final audit -- tbg-magic-angle-gaia

Date: 2026-05-04

Verdict: PASS with documented coherent stopping point below the 100-node target.

## Evidence fidelity

- Raw LKM JSON under `artifacts/lkm-discovery/input/` is the only science evidence used for executable claims.
- Executable claims in `src/tbg_magic_angle/` preserve `lkm_id`, `source_paper`, `provenance_source`, and `lkm_original` or source evidence pointers.
- New May 4 evidence files are preserved with `may4_match_*` and `may4_evidence_*` names.

## No executable agent synthesis

- `src/tbg_magic_angle/cross_paper.py` contains only `support(...)` operators between LKM-backed claims.
- No executable `claim(...)` node uses the prohibited May 4 agent-authored synthesis provenance markers or empty bridge metadata.
- Scope, non-equivalence, and rejected-bridge judgments are recorded in `candidates.md`, `mapping_audit.md`, and `merge_audit.md`.

## Connectivity

- Starting root: `gcn_7bca73ad98eb4ed4`.
- Science-facing claims: 32.
- Science-facing connected components after ignoring internal generated helpers: 1.
- Full IR includes 31 internal generated helper structural holes (`__conjunction_result_*` / `__implication_result_*`) reported by strict review; these are not science-facing disconnected claims.

## Duplicate and contradiction audit

- `gaia inquiry review --strict .` reports 0 possible duplicate claims, 0 warnings, 0 errors, and 0 independent claims missing priors.
- No `equivalence()` is emitted because no accepted pair asserts the same proposition under the same method/scope.
- No `contradiction()` is emitted because no accepted pair asserts mutually incompatible same-system/same-condition values.

## Priors and belief sanity

- `gaia check --hole .` reports 0 holes across 22 independent claims.
- Leaf priors are capped at 0.90 and include `TODO:review`.
- LKM factor deductions use `prior=0.95`.

## Final checks

- `gaia compile .`: pass, 63 knowledge, 19 strategies, 0 operators.
- `gaia check --brief .`: pass.
- `gaia check --hole .`: pass, 0 holes.
- `gaia infer .`: pass, exact JT, 44 beliefs.
- `gaia inquiry review --strict .`: pass with 0 duplicate candidates; internal helper structural holes logged.
- `gaia render . --target github`: pass.
- `gaia render . --target docs`: pass.
- `gaia starmap . --out docs/starmap.html`: pass, 51 nodes, 54 edges.

## Stopping rationale

The graph stops at 63 knowledge nodes because accepted growth must remain connected through chain-backed LKM evidence. Bridge searches did not find admissible paths to the Cao superconducting dome observation, pressure-tuned large-angle TBG, substrate topology, or multilayer/MATTG roots without generic agent-authored synthesis. Those roots are preserved in artifacts but excluded from executable source.
