# Mapping audit log -- tbg-magic-angle-gaia

Parent synthesis date: 2026-05-04

## Source subgraphs copied unchanged

| subgraph | parent module | selected root id | exported label | chain deductions |
|---|---|---|---|---|
| ma-tbg-superconducting-dome-gaia | paper_cao2018.py | gcn_006f88d8df3548fa | gcn_006f88d8_ma_tbg_superconducting_domes | strat_gfac_1433dc8665164d11_phase_diagram |
| bm-velocity-suppression-gaia | paper_dassarma2020.py | gcn_7bca73ad98eb4ed4 | gcn_7bca73ad98eb4ed4 | gfac_2f2334a945114bf3 |
| magnetic-bloch-tbg-gaia | paper_herzogarbeitman2022.py | gcn_afdfbd0c013048d8 | gcn_afdfbd0c013048d8 | gfac_9fc5b7efdef44e14 |
| pressure-flat-band-tbg-gaia | paper_ge2021.py | gcn_105d2fc961f949b6 | gcn_105d2fc961f949b6 | strat_gfac_b4366b0e9b4a4f0f |
| merged-dirac-tbg-gaia | paper_yamada2020.py | gcn_8159f32dda354258 | gcn_8159f32d_merged_dirac_magic_angle_flat_band | strat_gfac_3970f30041424709 |
| twisted-few-layer-graphite-gaia | paper_ma2020.py | gcn_f23eff9c755840f2 | gcn_f23eff9c755840f2 | gfac_6988d3b9bea84c0f |
| twisted-trilayer-flat-bands-gaia | paper_ma2019.py | gcn_2cf09f115b814154 | gcn_2cf09f115b814154 | gfac_0046298fbcb144c4 |
| alternating-twist-quadrilayer-gaia | paper_burg2022.py | gcn_225da7b340cb47b8 | gcn_225da7b3_atqg_angle_phase_decoupling | strat_gfac_b160d54c_atqg_angle_phase_decoupling |
| twisted-monolayer-bilayer-gaia | paper_nguyen2022.py | gcn_14a55aff3de24a3a | gcn_14a55aff_smab2_flat_band_localization | gfac_f1d4418d_smab2_flat_band_localization |
| ab-initio-twisted-multilayer-gaia | paper_tritsaris2020.py | gcn_5f58746bcc0b4098 | gcn_5f58746b_magic_angle_flat_band_likelihood | strat_gfac_c4fed52224164214 |
| tbg-lattice-reconstruction-gaia | paper_liu2020.py | gcn_c220df1acc8b476a | gcn_c220df1acc8b476a | gfac_e5303e2e42664d99 |
| tbg-dft-relaxation-gaia | paper_cantele2020.py | gcn_de1d329f326f4e75 | gcn_de1d329f326f4e75 | strat_gfac_3a3936eff4a1434c |
| hbn-aligned-tbg-gaia | paper_zhang2019.py | gcn_584669e24c6145a7 | gcn_584669e24c6145a7 | gfac_ff1f36e6840c42ba |
| substrate-chern-flat-band-gaia | paper_wang2020.py | gcn_9f7dbaf8f0014316 | gcn_9f7dbaf8_substrate_flat_band_topology_regime | gfac_c68ea7fe_magic_angle_regime_to_reconstruction_scope |
| mattg-superconductivity-gaia | paper_park2021.py | gcn_b4e3bdff3c0c439a | gcn_b4e3bdff_mattg_mirror_flat_dirac_control | gfac_170b7417_mattg_bandstructure_deduction |

## Parent cross-paper synthesis

| synthesis label | premises | decision | dsl_action |
|---|---|---|---|
| parent_tbg_flat_band_to_correlated_phenomenology | BM velocity suppression; ab initio flat-band likelihood; MA-TBG superconducting domes | grounded support bridge from flat-band mechanism/context to correlated phase phenomenology | support(), no equivalence |
| parent_scoped_flat_band_variants | pressure flat bands; merged Dirac mechanism; magnetic Bloch flat bands; few-layer graphite; ab initio detection | scoped variant bridge across flat-band formation/detection routes | support(), no equivalence |
| parent_multilayer_extensions_not_equivalent_to_tbg | twisted trilayer; ATQG; SM-(AB)2 | nearby moire graphene extensions, kept distinct from TBG | support(), no equivalence |
| parent_no_same_scope_contradiction_found | all fifteen roots | scope audit says no same-system/same-condition incompatible pair found | support() audit claim; no contradiction() |
| parent_relaxation_dft_realistic_flat_band_modeling | lattice reconstruction; DFT relaxation; ab initio flat-band likelihood | relaxation-aware continuum and first-principles roots support realistic flat-band modeling scope | support(), no equivalence |
| parent_substrate_topological_perturbation_scope | h-BN-aligned MA-TBG; TBG-on-TMD substrate topology | substrate perturbations support topological active-band scope while preserving h-BN vs TMD distinctions | support(), no equivalence |
| parent_mattg_superconducting_moire_extension_not_equivalent | MATTG mirror-flat/Dirac control; MA-TBG superconducting domes | MATTG extends superconducting magic-angle moire family but is not equivalent to bilayer TBG | support(), no equivalence |

## Contradictions

| pair | decision | dsl_action |
|---|---|---|
| all selected roots | no same-system/same-condition contradiction in parent candidates or validated subgraphs; relaxation, substrate, topology, and MATTG differences are scope boundaries | no contradiction() emitted |
