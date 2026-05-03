# Open-problem and scope-caution audit -- tbg-lattice-reconstruction-gaia

| candidate | origin | decision | rationale |
|---|---|---|---|
| Relaxation broadens and isolates flat bands vs heterostrain produces additional fine splitting | `gcn_8cd2984a6296435c`, `gcn_ed8fa9253ea24982`, factor step 5 | scope caution, not contradiction | The selected evidence explicitly separates the modeled relaxation trend from omitted heterostrain effects. Both can be true: relaxation may explain broadening/isolation while heterostrain may explain extra subpeaks. |
| Continuum calculation reproduces key STS trends but omits explicit heterostrain | root `gcn_c220df1acc8b476a` | open modeling limitation | The chain leaves a synthesis question for the parent package: how much of the observed spectral line shape requires heterostrain beyond registry-driven relaxation? The selected JSON does not include counter-evidence sufficient for a Gaia `contradiction()`. |
| Prior literature refs `[54-55]` for heterostrain | `gcn_ed8fa9253ea24982` | provenance caution | The selected `data.papers` contains only Liu et al. 2020, so no external reference records were imported for refs `[54-55]`; the heterostrain premise receives a lower TODO-marked prior. |
