# Dismissed contradiction candidate: structural relaxation caveat

Origin: mandatory open-problem audit of `gcn_5f58746bcc0b4098`, `gcn_af432bff1d3e4cf0`, and `gcn_be5d1975ecac4211`.

Candidate tension:

- The selected root concludes that the ab initio Wannier-derived tight-binding workflow and automated detector pipeline maximize the flat-band likelihood near theta* approximately 1.1 degrees for commensurate twisted bilayer graphene.
- The same LKM factor explicitly warns that below about 1.0 degree, atomic relaxation effects can significantly modify band structures, including widening single-particle gaps, and that these relaxation effects are not included in the high-throughput workflow.

Decision: dismissed as a Gaia `contradiction()` because the selected evidence does not assert a competing relaxed-structure magic angle, a competing p(theta), or an incompatible same-quantity result. It is a model-scope and evidentiary-strength concern. The package records it through premise priors, `todo` metadata for empty-content premises, and the mapping audit.

Open problem for parent synthesis: How robust is the ab initio TB flat-band-likelihood maximum near 1.1 degrees once atomic relaxation and reconstruction are included near or below the 1 degree small-angle regime?
