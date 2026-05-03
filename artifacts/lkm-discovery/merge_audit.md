# Merge audit log -- tbg-magic-angle-gaia

Parent synthesis date: 2026-05-04

## Duplicate and equivalence decisions

| pair/group | verdict | reason | action |
|---|---|---|---|
| BM velocity suppression vs ab initio flat-band likelihood | keep distinct | both concern TBG near the first magic angle, but one is a continuum velocity-suppression formula and the other is an ab initio/Wannier workflow likelihood across commensurate supercells | no merge; scoped support bridge |
| BM velocity suppression vs merged-Dirac mechanism | keep distinct | both address velocity/flat-band formation, but the mechanisms and source models differ and the merged-Dirac claim is explicitly conjectural in small-angle TBG | no merge; scoped variant bridge |
| pressure flat-band TBG vs magic-angle TBG roots | keep distinct | pressure-tuned large-angle TBG is a different control parameter and angle regime | no merge; scoped variant bridge |
| few-layer graphite vs TBG magic-angle roots | keep distinct | same approximate numerical angle appears, but the system has few-layer graphite slabs and the claim is scoped to a primary two-band pair | no equivalence |
| twisted trilayer / ATQG / SM-(AB)2 vs TBG | keep distinct | nearby moire graphene extensions use different layer count, stacking, or heuristic angle mapping; not the same proposition as TBG | no equivalence |
| all parent synthesis claims | keep as synthesis nodes | each records cross-paper scope/support rather than replacing a source claim | no source claim merged |
| lattice reconstruction vs DFT relaxation roots | keep distinct | both support realistic TBG flat-band modeling with atomic relaxation, but Liu et al. use relaxation-aware continuum spectroscopy trends while Cantele et al. use plane-wave DFT/TB at theta=1.08 degrees with explicit gap values and partial-relaxation comparisons | no merge; scoped support bridge |
| lattice/DFT relaxation roots vs ab initio flat-band likelihood | keep distinct | all strengthen realistic flat-band modeling, but the source workflows differ: relaxation-aware continuum modeling, first-magic-angle DFT/TB, and Wannier-based ab initio flat-band detection | no equivalence; scoped support bridge |
| h-BN-aligned TBG vs TBG-on-TMD substrate topology | keep distinct | both concern substrate-induced topological perturbations of MA-TBG, but h-BN is modeled through a top-layer staggered mass and weak moire potentials while TMD proximity uses Rashba, Ising, and sublattice terms with a different active-band reconstruction regime | no equivalence; scoped support bridge |
| MATTG mirror-flat/Dirac control vs MA-TBG superconducting domes | keep distinct | Park et al. describe mirror-symmetric magic-angle twisted trilayer graphene with theta/sqrt(2) mapping and displacement-field control; Cao et al. describe bilayer MA-TBG superconducting domes adjacent to correlated insulating states | no equivalence; scoped family-extension support |
| MATTG root vs prior multilayer-extension roots | keep distinct | MATTG, twisted trilayer, ATQG, and SM-(AB)2 all lie in nearby moire graphene territory but differ by layer count, stacking symmetry, field control, and reported observable | no merge |

## Contradiction decisions

No contradiction() operator was emitted. Discovery flags reported no pairs, and the selected roots differ by system, twist angle, pressure, magnetic flux, relaxation protocol, substrate perturbation, layer count, computational method, or observable. Apparent differences are logged as scope distinctions.

## Strict review snapshot

`gaia inquiry review --strict .` after the Turn-2 merge reported 0 warnings, 0 errors, 0 independent claims missing priors, and 0 possible duplicate claims. It also reported 57 structural holes/orphaned internal generated helper claims (`__conjunction_result_*` / `__implication_result_*`) and 39 unreviewed warrants; these are not science-facing duplicate source claims and remain review-work items rather than merge/equivalence actions.
