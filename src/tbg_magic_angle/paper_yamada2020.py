"""paper_yamada2020 -- merged-Dirac-point mechanism in twisted bilayer graphene.

Source: Merged Four Dirac Points at the Critical Interlayer Distance in
Commensurately Twisted Bilayer Graphene: the Origin of the Zero Velocity
DOI: 10.48550/arXiv.2001.01364
Authors: Aya Yamada | Yasumasa Hasegawa
Reference key: Yamada2020
"""

from gaia.lang import claim, deduction


_SMALL_ANGLE_CONJECTURE_ORIGINAL = r"""Define the small-angle (continuum) limit of twisted bilayer graphene as the regime where the twist angle $\alpha\to 0$ (equivalently, commensurate indices become large) and the energy gap at the moire $K$ point due to intervalley ($K$-$K'$) coupling becomes negligibly small, so that the upper two bands near charge neutrality are nearly degenerate. It is conjectured that the four-Dirac-point merging mechanism identified at moderate twist angles in commensurate tight-binding calculations persists continuously into this small-angle limit and provides the microscopic origin of the vanishing Dirac velocity at the magic angles associated with nearly flat bands. This conjecture assumes that no intervening topological or symmetry-driven reconstruction occurs as $\alpha$ decreases, that analogous moving Dirac points and trajectories exist in the small-angle limit, and that additional physical effects such as lattice relaxation and electron-electron interactions do not qualitatively alter the mechanism."""

_ROOT_ORIGINAL = r"""In twisted bilayer graphene at sufficiently small twist angle, where the energy gap at the moire $K$ point between the $2n_0$th and $(2n_0+1)$th bands becomes negligibly small and the upper two bands near charge neutrality become nearly degenerate, the same band-structure mechanism in which three moving Dirac points merge with the fixed Dirac point at $K$ is proposed to persist and to produce vanishing Dirac velocity at $K$. In this conjecture, the resulting suppression of the Dirac velocity at $K$ contributes to the emergence of extremely narrow (nearly flat) bands at the magic angles."""


gcn_7687975d_small_angle_merging_conjecture = claim(
    r"""For twisted bilayer graphene in the small-angle continuum limit considered by Yamada and Hasegawa 2020, the K-K' intervalley gap at moire K is treated as negligibly small, the upper two bands near charge neutrality are nearly degenerate, and the four-Dirac-point merging mechanism seen in commensurate tight-binding calculations at moderate twist angles is conjectured to persist continuously to magic-angle conditions, assuming no intervening topological or symmetry reconstruction and no qualitative change from lattice relaxation or electron-electron interactions [@Yamada2020].""",
    lkm_id="gcn_7687975d32314167",
    source_paper="paper:867773689762938981",
    provenance_source="lkm",
    lkm_original=_SMALL_ANGLE_CONJECTURE_ORIGINAL,
)

gcn_8159f32d_merged_dirac_magic_angle_flat_band = claim(
    r"""In sufficiently small-angle twisted bilayer graphene, where the moire-K gap between the $2n_0$th and $(2n_0+1)$th bands is negligibly small and the upper two bands near charge neutrality are nearly degenerate, Yamada and Hasegawa 2020 propose that three moving Dirac points merge with the fixed K-point Dirac point, producing vanishing Dirac velocity at K; this suppression is conjectured to contribute to extremely narrow nearly flat bands at the magic angles [@Yamada2020].""",
    lkm_id="gcn_8159f32dda354258",
    source_paper="paper:867773689762938981",
    provenance_source="lkm",
    lkm_original=_ROOT_ORIGINAL,
)

strat_gfac_3970f30041424709 = deduction(
    [gcn_7687975d_small_angle_merging_conjecture],
    gcn_8159f32d_merged_dirac_magic_angle_flat_band,
    reason=r"""1. Take as established the upstream mechanism: the zero K-point velocity in commensurate tight-binding calculations at moderate twist angles is caused by the merging of three moving Dirac points with the fixed Dirac point at K, producing a quadratic multi-fold touching at $d_{zc}$ (this is the previously derived merging mechanism).
2. Note the small-angle (continuum) limit characteristics relevant to the conjecture: in the small twist-angle limit the tight-binding K-K' intervalley coupling (the K-K' gap at moire K) becomes exponentially small and the upper two bands near K are nearly degenerate, so the band structure locally resembles the continuum-model limit in which moire K has vanishing gap and near-degenerate bands; experimentally, magic-angle phenomena (extremely narrow bands) occur in this small-angle regime and are known to be pressure tunable.
Fig.1
Fig.3
3. Argue plausibility (as stated by the authors) that the same merging process can continuously evolve into the small-angle regime: because the merging-of-four-Dirac-points mechanism is observed in commensurate tight-binding calculations at moderate angles and because the K-K' gap decreases continuously (exponentially) as the twist angle is reduced, the authors propose that the merging process can persist into the small-angle regime where the K-K' gap is negligible and the upper two bands are nearly degenerate; in that limit the same coalescence of Dirac points would produce vanishing K-point velocity and thus contribute to the formation of extremely narrow (nearly flat) bands at the magic angles.
4. Explicitly label the conjectural nature and the limitation acknowledged by the authors: the authors frame this as a proposal (conjecture) rather than a demonstrated theorem, noting that they have not proved that four-Dirac merging is the full or sole origin of the experimentally observed bandwidth collapse at the smallest magic angles, and they acknowledge that demonstrating the mechanism in the small-angle, almost-degenerate two-band regime is numerically difficult because gaps are exponentially small and the bands are nearly degenerate.
Fig.1""",
    prior=0.95,
)
