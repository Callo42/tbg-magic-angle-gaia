# Mapping audit log - hbn-aligned-tbg-gaia

## Claims

| lkm_id | label | source_paper | transformation |
|---|---|---|---|
| `gcn_464f6413fccb48be` | `gcn_464f6413fccb48be` | `paper:812707666555043841` | Rewritten as a self-contained premise about the hierarchy `|V_j| <= 10 meV` vs `w_1 ~= 110 meV` and the first-approximation omission of the `V_j` term; `lkm_original` preserved. |
| `gcn_a7252e5aaaf84d38` | `gcn_a7252e5aaaf84d38` | `paper:812707666555043841` | Rewritten as a self-contained premise mapping the about 35 meV monolayer graphene/h-BN neutral-point gap to `M ~= 17 meV`; `lkm_original` preserved. |
| `gcn_ca5e0f32e91c459b` | `gcn_ca5e0f32e91c459b` | `paper:812707666555043841` | Rewritten as a self-contained premise about active-band isolation and valley + Chern numbers under the stated continuum-model parameters; `lkm_original` preserved. |
| `gcn_1d940e84a3744c85` | `gcn_1d940e84a3744c85` | `paper:812707666555043841` | Empty LKM premise retained as a placeholder claim with `todo="revisit when LKM populates this premise"` and no invented scientific content. |
| `gcn_584669e24c6145a7` | `gcn_584669e24c6145a7` | `paper:812707666555043841` | Rewritten as a self-contained root conclusion covering the h-BN-aligned TBG Hamiltonian, realistic parameter estimates, gapped Dirac crossings, valley-resolved active-band Chern numbers, and about 5 meV indirect gap; `lkm_original` preserved. |

## Factors -> deductions

| factor_id | source_paper | premises | conclusion | dsl_kind | prior |
|---|---|---|---|---|---|
| `gfac_ff1f36e6840c42ba` | `paper:812707666555043841` | `gcn_464f6413fccb48be`, `gcn_a7252e5aaaf84d38`, `gcn_ca5e0f32e91c459b`, `gcn_1d940e84a3744c85` | `gcn_584669e24c6145a7` | `deduction` | 0.95 |

## Decomposition

No root decomposition was emitted. The root is compound in presentation but the selected factor already separates the available evidence into grounded premises for the approximation hierarchy, mass estimate, and active-band topology. The remaining conjunction is kept as the source conclusion rather than split into unsupported atomic claims.

## Equivalences

| pair | decision | dsl_action |
|---|---|---|
| (none in this run) | No independent same-proposition pair in the selected payload. | None |

## Contradictions and open problems

| item | decision | dsl_action |
|---|---|---|
| The `V_j` matrices are dropped because `|V_j| << w_1`, while the reported indirect active-band gap is only about 5 meV. | Open modeling-scope question: `V_j` is small against `w_1`, not necessarily against all low-energy gaps. The selected payload does not contain a counter-calculation with `V_j` retained, so this is not a same-scope contradiction. | No `contradiction(...)`; lower-prior/context in `gcn_464f6413fccb48be`. |
| The mass estimate maps a monolayer graphene/h-BN neutral-point gap to the top-layer TBG mass parameter. | Open transferability question, not a contradiction within the selected evidence. | No `contradiction(...)`; review-marked prior for `gcn_a7252e5aaaf84d38`. |
| Active-band isolation and Chern computation depend on numerical discretization and parameter choices. | Open numerical-convergence review target because the payload states the condition but does not provide an independent convergence chain. | No `contradiction(...)`; review-marked prior for `gcn_ca5e0f32e91c459b`. |
| Premise `gcn_1d940e84a3744c85` has empty content. | Provenance gap in the LKM payload. | Placeholder claim retained with neutral prior and `todo` metadata. |

## Dismissed

| pair | origin | rationale |
|---|---|---|
| (none in this run) | | |
