# Open-problem audit -- bm-velocity-suppression-gaia

Every mapped claim was checked against the selected evidence chain and the discovery flag files. No contradiction was promoted because the available selected evidence contains one chain from one source paper and the discovery scan reports no same-scope contradictory or equivalent pairs.

## Claim-level notes

| label | audit result |
|---|---|
| `gcn_d3808439ccf6496b` | Scope limitation: the fit is stated for `0 < theta < 3 degrees`; the selected evidence also notes that for `theta > 3 degrees` the authors may take `v_F*(theta) ~= v_F`. This is a regime boundary, not a contradiction. |
| `gcn_671ceef053a64aa7` | Potential future question: how interaction and phonon calculations change if the noninteracting BM velocity is strongly renormalized. The selected evidence frames this as motivation rather than conflicting evidence. |
| `gcn_7bca73ad98eb4ed4` | Potential future question: whether the empirical linear approximation remains adequate extremely close to `theta_M`, where continuum many-body estimates can become singular through `1/v_F*` factors. No conflicting same-system value is present in the selected evidence. |

## Promoted contradictions

(none)

## Deferred risks

A broader graph may later add evidence for relaxed-lattice, chiral-limit, interaction-renormalized, or experimental velocity values. Those should be compared under matched model assumptions and twist-angle regimes before emitting any `contradiction()` operator.
