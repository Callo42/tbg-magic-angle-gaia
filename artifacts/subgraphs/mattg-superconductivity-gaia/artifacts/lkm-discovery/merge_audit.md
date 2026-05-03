# Merge audit log - mattg-superconductivity-gaia

| labels | verdict | reason | source pointers |
|---|---|---|---|
| `gcn_c680c239_mattg_continuum_approximations`, `gcn_3618ccee_mattg_theta_over_sqrt2_mapping`, `gcn_71314760_mattg_displacement_field_modeling`, `gcn_b4e3bdff_mattg_mirror_flat_dirac_control` | keep distinct | These labels occupy different roles in the selected chain: global continuum-model assumptions, theta/sqrt(2) flat-band reduction, displacement-field modeling, and the root band-structure conclusion. Merging would erase premise structure and inflate confidence. | `input/turn2_evidence_gcn_b4e3bdff3c0c439a.json` |
| `helper_mattg_zero_d_mirror_protected_flat_dirac`, `helper_mattg_magic_angle_larger_than_matbg`, `helper_mattg_displacement_field_hybridizes_bands` | keep distinct from root and from each other | The helper claims are decomposition targets for different subclaims of the compound root. They are not independent evidence and are connected by support from the root rather than merged or equivalenced. | `src/mattg_superconductivity/paper_park2021.py` |

No same-paper duplicate or independent equivalent claim was found inside the selected single-chain payload.
