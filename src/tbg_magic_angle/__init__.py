"""tbg-magic-angle-gaia -- May 4 single-root LKM-backed TBG package."""

from .paper_dassarma2020 import *
from .paper_wu2018 import *
from .paper_dassarma2022 import *
from .paper_qin2021 import *
from .paper_uchida2014 import *
from .paper_tritsaris2020 import *
from .paper_liu2020 import *
from .paper_cantele2020 import *
from .paper_herzogarbeitman2022 import *
from .paper_yamada2020 import *
from .cross_paper import *

__all__ = [
    'bm_magic_angle_velocity_suppression',
    'wu_velocity_phonon_form_factor',
    'phonon_resistivity_velocity_enhancement',
    'phonon_bdg_vhs_tc_hc2_velocity_extrema',
    'kohn_sham_magic_angle_flat_bands',
    'ab_initio_magic_angle_flat_band_likelihood',
    'relaxation_reproduces_sts_flat_band_trends',
    'full_relaxation_reproduces_flat_band_gaps',
    'magnetic_bloch_reentrant_flat_bands',
    'merged_dirac_magic_angle_flat_band',
]
