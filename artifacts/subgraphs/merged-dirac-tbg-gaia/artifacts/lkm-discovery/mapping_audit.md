# Mapping audit log -- merged-dirac-tbg-gaia

## 9-step batch checklist

| step | status | audit note |
|---|---|---|
| 1. Bootstrap | done | Loaded only `input/evidence_gcn_8159f32dda354258.json` for the chain backbone. |
| 2. Refine | done | Rewrote both distinct `gcn_*` claims to include twisted-bilayer-graphene system context, small-angle/moire-K conditions, mechanism scope, and citation; verbatim LKM text is preserved in `lkm_original`. |
| 3. Decompose | done | No extra helper decomposition was emitted. The LKM root is conjectural but not a two-sided conflict or agreement with independently grounded atomic claims. |
| 4. Hunt open problems | done | The chain itself flags the key open problem: whether the moderate-angle four-Dirac-point merging mechanism survives in realistic small-angle TBG with negligible K-K' gap, lattice relaxation, and interactions. This was logged as a dismissed contradiction/scope risk, not promoted to an unsupported `contradiction()` edge. |
| 5. Mark suspicions | done | Scope suspicion recorded through `dismissed/small_angle_conjecture_scope.md` and the leaf prior justification. |
| 6. Compile + infer | done | `gaia compile .` and `gaia infer .` passed with IR hash `sha256:12db4378e1a97efebc879b51b797b36b3953985db891e7bc980241d8a06cd5da`; inference used JT exact BP and converged. |
| 7. Review obligations/holes | done | `gaia check --brief .` and `gaia check --hole .` passed with 0 holes across 1 independent claim. |
| 8. Search supports | done | No extra support claims were formalized because this worker is constrained to the selected raw evidence and `data.papers`. |
| 9. Repeat/exit rationale | done | Exit condition met: selected root chain is fully mapped, no holes remain, no real contradiction/equivalence was promoted, and no unsupported extra evidence was added. |

## Claims

| label | lkm id | source paper | self-contained transformation | lkm_original preserved |
|---|---|---|---|---|
| `gcn_7687975d_small_angle_merging_conjecture` | `gcn_7687975d32314167` | `paper:867773689762938981` | Added explicit small-angle continuum limit, moire-K K-K' gap, upper-band near-degeneracy, continuity assumption, and omitted-physics scope. | yes |
| `gcn_8159f32d_merged_dirac_magic_angle_flat_band` | `gcn_8159f32dda354258` | `paper:867773689762938981` | Added explicit small-angle TBG setting, moire-K band-gap condition, vanishing K-point velocity, and magic-angle flat-band consequence. | yes |

## Factors -> deductions

| factor_id | source_paper | premises | conclusion | dsl_kind | prior |
|---|---|---|---|---|---|
| `gfac_3970f30041424709` | `paper:867773689762938981` | `gcn_7687975d32314167` | `gcn_8159f32dda354258` | `deduction` | 0.95 |

## Open-problem and contradiction pass

| candidate | origin | decision | rationale |
|---|---|---|---|
| Small-angle persistence of the four-Dirac-point merging mechanism | selected root and factor step 4 | dismissed as formal contradiction; retained as open-problem risk | The evidence calls the mechanism a conjecture and notes missing proof, but does not provide a counterclaim that cannot coexist with it. |
| Lattice relaxation and electron-electron interactions changing the mechanism | selected premise assumptions | retained as parent-synthesis risk | The selected evidence names these effects as possible qualitative modifiers, but does not assert their actual effect for the same conditions. |

## Equivalences

| pair | decision | dsl_action |
|---|---|---|
| `gcn_7687975d32314167` / `gcn_8159f32dda354258` | related same-paper premise and conclusion, not the same proposition | none |

## Dismissed

| pair | origin | rationale |
|---|---|---|
| See `dismissed/small_angle_conjecture_scope.md` | selected evidence open-problem audit | Conjectural limitation and missing proof are evidentiary-strength issues, not an incompatible claim pair. |

## Gaia CLI verification

| command | status | note |
|---|---|---|
| `uv run --project /home/rsw/ThisIsDP/dev/test_lkm2gaia gaia compile .` | pass | Compiled 3 knowledge, 1 strategy, 0 operators; IR hash `sha256:12db4378e1a97efebc879b51b797b36b3953985db891e7bc980241d8a06cd5da`. |
| `uv run --project /home/rsw/ThisIsDP/dev/test_lkm2gaia gaia check --brief .` | pass | 1 independent premise with prior, 1 derived conclusion, and 1 Gaia-generated internal implication helper. |
| `uv run --project /home/rsw/ThisIsDP/dev/test_lkm2gaia gaia check --hole .` | pass | 0 holes / 1 independent claim; prior assigned to `gcn_7687975d_small_angle_merging_conjecture`. |
| `uv run --project /home/rsw/ThisIsDP/dev/test_lkm2gaia gaia infer .` | pass | Inferred 2 beliefs with JT exact method; converged in 2 iterations. |
