# Merge audit log -- twisted-monolayer-bilayer-gaia

| pair | verdict | reason | source pointers |
|---|---|---|---|
| `gcn_14a55aff3de24a3a` / `gcn_42c7afbd21b5483d` | keep distinct | The root is a compound conclusion about isolated flat bands, reduced flatness versus TBLG, and layer-resolved localization; the premise is the narrower layer-decomposed DOS result used in the factor. | `input/evidence_gcn_14a55aff3de24a3a.json` claim and factor premise |
| decomposition helpers / mapped LKM source claims | keep distinct as downstream helpers | Helper claims are explicitly marked `provenance_source="lkm_decomposition"` and connected by `support(...)`; they are not independent LKM claims or duplicate evidence. | `src/twisted_monolayer_bilayer/paper_nguyen2022.py` |

No exact duplicate, same-paper version merge, or independent same-proposition equivalence was identified inside the selected evidence chain.
