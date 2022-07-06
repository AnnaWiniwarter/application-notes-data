"""
Do a low concentration calibration.

Created on Thu Mar  3 14:55:33 2022

@author: AnnaWiniwarter
"""

import ixdat
from ixdat.techniques import MSMeasurement
from pathlib import Path

data_directory = (
    Path.home()
    / r"C:\Users\AnnaWiniwarter\Dropbox (Spectro Inlets)\Development\Data\Quantification Application Note"
)

O2_data = MSMeasurement.read(
    data_directory
    / r"2022-05-18 12_53_59 Gas_calibration_O2_kapton_blocked_chip/2022-05-18 12_53_59 Gas_calibration_O2_kapton_blocked_chip.tsv",
    reader="zilien",
)

O2_data.plot_measurement()

mychip = ixdat.techniques.ms.MSInlet()
# mychip = ixdat.techniques.ms.MSInlet(T=300, p=20000) #optional: select T (in Kelvin) and p (in Pa)

O2_cal = mychip.gas_flux_calibration_curve(
    O2_data,
    mol="O2",
    mass="M32",
    tspan_list=[
        [2305, 2680],
        [3431, 4127],
        [5559, 5907],
        [6825, 7479],
        [8202, 9203],
        [10038, 10719],
    ],
    carrier_mol="He",
    mol_conc_ppm=[0, 5000, 10000, 50000, 100000, 200000],
    tspan_bg=[11562, 11907],
    return_ax=True,
)
O2_cal[1].annotate(
    "F = {:.3f} C/mol".format(O2_cal[0].F), (0.2, 0.8), xycoords="subfigure fraction"
)

O2_data.calibrate(ms_cal_results=[O2_cal[0]])
O2_data.plot_measurement(mol_list=["O2"], logplot=False)


H2_lowc_data = MSMeasurement.read(
    data_directory
    / r"2022-05-18 16_13_27 Gas_calibration_lowH2_kapton_blocked_chip/2022-05-18 16_13_27 Gas_calibration_lowH2_kapton_blocked_chip.tsv",
    reader="zilien",
)

H2_lowc_data.plot_measurement()

# mychip = ixdat.techniques.ms.MSInlet()
# mychip = ixdat.techniques.ms.MSInlet(T=300, p=20000) #optional: select T (in Kelvin) and p (in Pa)

H2_lowc_cal = mychip.gas_flux_calibration_curve(
    H2_lowc_data,
    mol="H2",
    mass="M2",
    tspan_list=[[1380, 1907], [3141, 3681], [4999, 5540]],
    carrier_mol="He",
    mol_conc_ppm=[10000, 5000, 1000],
    tspan_bg=[5776, 6053],
    p_inlet=1.047e5,
    return_ax=True,
)
H2_lowc_cal[1].annotate(
    "F = {:.3f} C/mol".format(H2_lowc_cal[0].F),
    (0.2, 0.8),
    xycoords="subfigure fraction",
)

H2_lowc_data.calibrate(ms_cal_results=[H2_lowc_cal[0]])
H2_lowc_data.plot_measurement(mol_list=["H2"], logplot=False)
