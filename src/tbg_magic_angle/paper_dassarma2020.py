"""paper_dassarma2020 -- LKM claims and deduction from Das Sarma and Wu (2020).

Source: Electron-phonon and electron-electron interaction effects in twisted bilayer graphene
DOI: 10.1016/j.aop.2020.168193
Authors: Sankar Das Sarma | Fengcheng Wu
Reference key (CSL): DasSarma2020
"""
from gaia.lang import claim, deduction


bm_velocity_linear_fit = claim(
    "For twisted bilayer graphene in the noninteracting Bistritzer-MacDonald continuum moire-band calculation, with twist angle theta and largest magic angle theta_M measured in degrees and monolayer graphene velocity v_F about 1e8 cm/s, the computed low-energy Dirac-point Fermi velocity v_F*(theta) for 0 < theta < 3 degrees is usefully approximated by v_F*(theta) ~= 0.5 * |theta - theta_M| * v_F [@DasSarma2020].",
    lkm_id="gcn_d3808439ccf6496b",
    source_paper="paper:812646407474249731",
    provenance_source="lkm",
    lkm_original="For twisted bilayer graphene (tBLG) with twist angle \u03b8 measured in degrees, let \u03b8_M denote the largest magic angle at which the noninteracting continuum moir\u00e9-band Dirac-point band velocity vanishes, and let v_F \u2248 10^8 cm/s be the monolayer-graphene Dirac velocity; then the noninteracting continuum Bistritzer\u2013MacDonald moir\u00e9-band calculation of the low-energy Dirac-point Fermi velocity v_F^*(\u03b8) is accurately approximated for 0<\u03b8<3\u00b0 by the linear formula\n      $$\n      v_F^*(\\theta)\\approx 0.5\\,|\\theta-\\theta_M|\\,v_F,\n      $$\n      with \u03b8 and \u03b8_M in degrees, so that the numerical continuum-band outputs for v_F^*(\u03b8) are captured to useful accuracy by this linear fit in the specified angular window.\n      R. Bistritzer and A.H. MacDonald, Proc. Natl. Acad. Sci. USA 108 (2011) 12233; F. Wu, E. Hwang, S. Das Sarma, Phys. Rev. B 99 (2019) 165112.",
)

bm_velocity_bare_input = claim(
    "In twisted bilayer graphene, the Bistritzer-MacDonald continuum moire-band model supplies the noninteracting low-energy band structure, and the Dirac-point band Fermi velocity v_F*(theta) from that model is treated as the bare input velocity for subsequent low-energy many-body and phonon-transport calculations [@DasSarma2020].",
    lkm_id="gcn_671ceef053a64aa7",
    source_paper="paper:812646407474249731",
    provenance_source="lkm",
    lkm_original="The Bistritzer\u2013MacDonald continuum moir\u00e9-band model, a continuum effective model parameterized by intralayer graphene parameters and interlayer tunneling amplitudes, provides the noninteracting low-energy band structure of twisted bilayer graphene (tBLG), and the Dirac-point band Fermi velocity v_F^*(\u03b8) obtained from that noninteracting continuum model is to be treated as the bare (noninteracting) input parameter for subsequent low-energy many-body and phonon-transport calculations.\n      R. Bistritzer and A.H. MacDonald, Proc. Natl. Acad. Sci. USA 108 (2011) 12233.",
)

bm_magic_angle_velocity_suppression = claim(
    "For twisted bilayer graphene, the noninteracting low-energy Dirac-point band Fermi velocity v_F*(theta) produced by the Bistritzer-MacDonald continuum moire-band model is strongly suppressed as theta approaches the largest magic angle theta_M where that velocity vanishes; for 0 < theta < 3 degrees it is usefully described by v_F*(theta) ~= 0.5 * |theta - theta_M| * v_F, with v_F about 1e8 cm/s [@DasSarma2020].",
    lkm_id="gcn_7bca73ad98eb4ed4",
    source_paper="paper:812646407474249731",
    provenance_source="lkm",
    lkm_original="For twisted bilayer graphene (tBLG) the noninteracting low-energy Dirac-point band Fermi velocity v_F^*(\u03b8) produced by the Bistritzer\u2013MacDonald continuum moir\u00e9-band model is strongly suppressed as the twist angle \u03b8 (measured in degrees) approaches the largest magic angle \u03b8_M (the angle at which the noninteracting Dirac-point band velocity vanishes), and for 0<\u03b8<3\u00b0 this noninteracting moir\u00e9-band velocity is well described by the empirical linear approximation\n      $$\n      v_F^*(\\theta)\\approx 0.5\\,|\\theta-\\theta_M|\\,v_F,\n      $$\n      where v_F^*(\u03b8) is the tBLG moir\u00e9-band Dirac-cone Fermi velocity, \u03b8 and \u03b8_M are expressed in degrees, and v_F \u2248 10^8 cm/s is the monolayer-graphene Dirac velocity; this linear fit reproduces the numerical outputs of the continuum Bistritzer\u2013MacDonald moir\u00e9-band calculation to useful accuracy in the stated angular window.",
)

derive_bm_magic_angle_velocity_suppression = deduction(
    [bm_velocity_linear_fit, bm_velocity_bare_input],
    bm_magic_angle_velocity_suppression,
    reason="1. Define $v_F^*(\\theta)$ as the noninteracting low-energy Dirac-point Fermi velocity of twisted bilayer graphene (tBLG), where $\\theta$ is the twist angle expressed in degrees and $\\theta_M$ denotes the largest magic angle at which the noninteracting Dirac velocity vanishes (i.e., $v_F^*(\\theta_M)=0$); the monolayer graphene (MLG) bare Dirac velocity is $v_F\\approx 10^{8}\\ \\mathrm{cm/s}$. \nFig. 1(a)\n2. State the continuum moir\u00e9-band calculation basis: the Bistritzer\u2013MacDonald continuum moir\u00e9-band model (band-structure model) is used to compute $v_F^*(\\theta)$ as a function of $\\theta$, and those calculated values are presented as the tBLG Dirac velocity at the Dirac point versus twist angle. The continuum calculation details are those cited from the band-structure model references and prior work.\n[54]\n[36]\n3. Report the empirical approximation extracted from the continuum moir\u00e9-band calculation: for twist angles $\\theta<3^\\circ$ the computed noninteracting tBLG Dirac velocity is well approximated by the linear formula\n$$\nv_F^*(\\theta)\\approx 0.5\\,|\\theta-\\theta_M|\\,v_F,\n$$\nwhere both $\\theta$ and $\\theta_M$ are measured in degrees, and $v_F\\approx 10^8\\ \\mathrm{cm/s}$. This empirical expression is the explicit formula appearing in the continuum calculation discussion.\n[36]\nFig. 1(a)\n4. Explain the domain of validity of the empirical approximation: the authors state the approximation holds for $\\theta<3^\\circ$, while for $\\theta>3^\\circ$ one may take $v_F^*(\\theta)\\approx v_F$ for the purposes of their low-energy continuum theory; the number $\\theta_M$ from their calculation is $\\theta_M\\approx 1.02^\\circ$ as reported in their continuum-band evaluation.\n[36]\n5. Explicitly connect $v_F^*(\\theta)$ to subsequent low-energy theories: define the Coulomb fine-structure coupling $\\alpha$ in terms of $v_F^*$ by $\\alpha=e^2/(\\kappa\\hbar v_F^*)$, where $e$ is the elementary charge, $\\hbar$ is the reduced Planck constant, and $\\kappa$ is the background dielectric constant; also state that $v_F^*(\\theta)$ is the bare (noninteracting) low-energy parameter entering the continuum electron-phonon resistivity formula (the resistivity formula uses $v_F^{*2}$ in the denominator). Thus the empirical approximation for $v_F^*(\\theta)$ summarizes the noninteracting Bistritzer\u2013MacDonald moir\u00e9-band calculation used throughout the paper to set band-velocity inputs for both phonon and Coulomb interaction theories.",
    prior=0.95,
)
