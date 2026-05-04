"""cross_paper -- LKM-backed support edges for the May 4 connected TBG graph."""

from gaia.lang import support

from .paper_dassarma2020 import bm_magic_angle_velocity_suppression
from .paper_wu2018 import wu_velocity_phonon_form_factor
from .paper_dassarma2022 import phonon_resistivity_velocity_enhancement
from .paper_qin2021 import phonon_bdg_vhs_tc_hc2_velocity_extrema
from .paper_uchida2014 import kohn_sham_magic_angle_flat_bands
from .paper_tritsaris2020 import ab_initio_magic_angle_flat_band_likelihood
from .paper_liu2020 import relaxation_reproduces_sts_flat_band_trends
from .paper_cantele2020 import full_relaxation_reproduces_flat_band_gaps
from .paper_herzogarbeitman2022 import magnetic_bloch_reentrant_flat_bands
from .paper_yamada2020 import merged_dirac_magic_angle_flat_band

link_wu_velocity_supports_bm_velocity = support(
    [wu_velocity_phonon_form_factor],
    bm_magic_angle_velocity_suppression,
    reason=(
        "The Wu-Hwang-Das Sarma chain independently derives a continuum moire "
        "Hamiltonian with a twist-angle-dependent v_F*(theta) that is strongly "
        "suppressed near a model magic angle. That LKM-backed result supports "
        "the starting BM velocity-suppression root without asserting the same "
        "linear fit or identical parameter set."
    ),
    prior=0.82,
)

link_bm_velocity_to_phonon_resistivity = support(
    [bm_magic_angle_velocity_suppression, wu_velocity_phonon_form_factor],
    phonon_resistivity_velocity_enhancement,
    reason=(
        "Both source claims are LKM-backed BM/continuum velocity claims used as "
        "low-energy inputs for electron-phonon or transport calculations. They "
        "support the strange-metallicity extension's narrower statement that "
        "suppressed v_F* enhances phonon-limited resistivity through the stated "
        "1/v_F*^2 scaling."
    ),
    prior=0.78,
)

link_phonon_inputs_to_pairing_calculation = support(
    [wu_velocity_phonon_form_factor, phonon_resistivity_velocity_enhancement],
    phonon_bdg_vhs_tc_hc2_velocity_extrema,
    reason=(
        "The accepted extensions keep the path within LKM-backed MATBG "
        "continuum calculations where v_F* and electron-phonon inputs are used "
        "for transport or pairing. This supports the Qin-Zou-MacDonald "
        "phonon-mediated BdG extension only as a model-family continuation."
    ),
    prior=0.60,
)

link_kohn_sham_velocity_to_bm_velocity = support(
    [kohn_sham_magic_angle_flat_bands],
    bm_magic_angle_velocity_suppression,
    reason=(
        "The Uchida et al. LKM chain is an independent Kohn-Sham calculation "
        "where the Dirac Fermi velocity vanishes near theta about 1.08 degrees "
        "and flat bands emerge. It supports the BM root's velocity-suppression "
        "phenomenon while preserving the different method and parameter scope."
    ),
    prior=0.72,
)

link_kohn_sham_to_abinitio_flat_band = support(
    [kohn_sham_magic_angle_flat_bands],
    ab_initio_magic_angle_flat_band_likelihood,
    reason=(
        "Both LKM-backed claims are first-principles or ab initio-derived TBG "
        "calculations near the first magic angle that report flat or "
        "low-dispersion bands. The support is scoped to independent agreement "
        "on near-1.1-degree flat-band formation, not equivalence of workflows."
    ),
    prior=0.70,
)

link_abinitio_to_relaxation_roots = support(
    [kohn_sham_magic_angle_flat_bands, ab_initio_magic_angle_flat_band_likelihood],
    full_relaxation_reproduces_flat_band_gaps,
    reason=(
        "The accepted ab initio/Kohn-Sham flat-band claims provide the connected "
        "TBG first-magic-angle context for Cantele et al.'s more specific "
        "DFT result that full atomic relaxation is required to reproduce the "
        "narrow flat-band manifold and gaps at theta=1.08 degrees."
    ),
    prior=0.68,
)

link_relaxation_roots = support(
    [full_relaxation_reproduces_flat_band_gaps],
    relaxation_reproduces_sts_flat_band_trends,
    reason=(
        "The Cantele DFT relaxation chain and the Liu continuum/STS chain both "
        "concern magic-angle TBG relaxation effects on flat-band isolation. "
        "This supports the Liu extension as a connected relaxation-specific "
        "continuation while keeping DFT and continuum/STS scopes distinct."
    ),
    prior=0.70,
)

link_bm_velocity_to_magnetic_bloch = support(
    [bm_magic_angle_velocity_suppression],
    magnetic_bloch_reentrant_flat_bands,
    reason=(
        "The magnetic-Bloch extension explicitly starts from the BM continuum "
        "model at magic-angle parameters. The BM velocity root supplies the "
        "connected zero-field magic-angle BM context, while the extension keeps "
        "its flux=2pi and topology conditions separate."
    ),
    prior=0.66,
)

link_bm_velocity_to_merged_dirac = support(
    [bm_magic_angle_velocity_suppression, kohn_sham_magic_angle_flat_bands],
    merged_dirac_magic_angle_flat_band,
    reason=(
        "The merged-Dirac chain is a conjectural same-system mechanism for "
        "vanishing Dirac velocity and near-flat bands at small magic angles. "
        "The BM and Kohn-Sham velocity roots support it as a connected "
        "mechanistic extension, not as a proved equivalence."
    ),
    prior=0.62,
)
