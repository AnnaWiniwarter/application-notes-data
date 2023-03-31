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
    / r"C:\Users\AnnaWiniwarter\Dropbox (Spectro Inlets)\Development\Data\Quantification Application Note\gas cal tests"
)

start_data = MSMeasurement.read(
    data_directory
    / r"2022-06-24 12_37_28 HER_low_conc_gas_flow_cal_w_cell_start/2022-06-24 12_37_28 HER_low_conc_gas_flow_cal_w_cell_start.tsv",
    reader="zilien",
    technique="MS",
)

rest_data = MSMeasurement.read(
    data_directory
    / r"2022-06-24 13_19_04 HER_low_conc_gas_flow_cal_w_cell/2022-06-24 13_19_04 HER_low_conc_gas_flow_cal_w_cell.tsv",
    reader="zilien",
    technique="MS",
)


full_data_zilien = start_data + rest_data

ec_directory = (
    Path.home()
    / r"C:\Users\AnnaWiniwarter\Dropbox (Spectro Inlets)\Development\Data\Quantification Application Note\\gas cal tests\2022-06-24 13_19_04 HER_low_conc_gas_flow_cal_w_cell"
)

cvs_ec_only_1 = ixdat.Measurement.read(
    ec_directory
    / "2022-06-24 13_19_04 HER_low_conc_gas_flow_cal_w_cell_01_01_CVA_DUSB0_C01.mpt",
    reader="biologic",
)
cvs_ec_only_2 = ixdat.Measurement.read(
    ec_directory
    / "2022-06-24 13_19_04 HER_low_conc_gas_flow_cal_w_cell_02_01_CVA_DUSB0_C01.mpt",
    reader="biologic",
)
cps_ec_only_1 = ixdat.Measurement.read(
    ec_directory
    / "2022-06-24 13_19_04 HER_low_conc_gas_flow_cal_w_cell_01_02_CP_DUSB0_C01.mpt",
    reader="biologic",
)
cps_ec_only_2 = ixdat.Measurement.read(
    ec_directory
    / "2022-06-24 13_19_04 HER_low_conc_gas_flow_cal_w_cell_02_02_CP_DUSB0_C01.mpt",
    reader="biologic",
)
# These two lines get rid of the EC data from the zilien-read file,
# since we will use the EC data from the biologic file instead.
full_data_zilien.replace_series("Ewe/V", None)
full_data_zilien.replace_series("I/mA", None)
# full_data_zilien.replace_series("Potential time [s]", None)
full_data = (
    full_data_zilien + cvs_ec_only_1 + cvs_ec_only_2 + cps_ec_only_1 + cps_ec_only_2
)
axes_a = full_data.plot_measurement(tspan=[0, 100000])
full_plot = axes_a[0].get_figure()


mychip = ixdat.techniques.ms.MSInlet()
# mychip = ixdat.techniques.ms.MSInlet(T=300, p=20000) #optional: select T (in Kelvin) and p (in Pa)

H2_lowc_cal = mychip.gas_flux_calibration_curve(
    full_data,
    mol="H2",
    mass="M2",
    tspan_list=[[5800, 6230], [7288, 7653], [8704, 9076], [9862, 10193]],
    carrier_mol="He",
    mol_conc_ppm=[10000, 5000, 1000, 500],
    tspan_bg=[10342, 10516],
    p_inlet=1.030e5,
    return_ax=True,
)
H2_lowc_cal[1].annotate(
    "F = {:.3f} C/mol".format(H2_lowc_cal[0].F),
    (0.2, 0.8),
    xycoords="subfigure fraction",
)

full_data.calibrate(ms_cal_results=[H2_lowc_cal[0]])
full_data.plot_measurement(mol_list=["H2"], logplot=False)

cps_1 = full_data.cut(tspan=[11500, 14900])
axes_c = cps_1.plot_measurement(mass_list=["M2"])
H2_ec_cal_1 = cps_1.ecms_calibration_curve(
    "H2",
    "M2",
    -2,
    selector_list=[1, 3, 5, 7, 9],
    selector_name="selector",
    t_steady_pulse=100,
    tspan_bg=[12150, 12250],
    ax="new",
    axes_measurement=axes_c,
    return_ax=True,
)
print("HER calibration factor F= {:.3f} C/mol".format(H2_ec_cal_1[0].F))
H2_ec_cal_1[1].annotate(
    "F = {:.3f} C/mol".format(H2_ec_cal_1[0].F),
    (0.2, 0.8),
    xycoords="subfigure fraction",
)

cps_2 = full_data.cut(tspan=[16000, 19000])
axes_d = cps_2.plot_measurement(mass_list=["M2"])
H2_ec_cal_2 = cps_2.ecms_calibration_curve(
    "H2",
    "M2",
    -2,
    selector_list=[1, 3, 5, 7, 9],
    selector_name="selector",
    t_steady_pulse=100,
    tspan_bg=[16400, 16500],
    ax="new",
    axes_measurement=axes_d,
    return_ax=True,
)
print("HER calibration factor F= {:.3f} C/mol".format(H2_ec_cal_2[0].F))
H2_ec_cal_2[1].annotate(
    "F = {:.3f} C/mol".format(H2_ec_cal_2[0].F),
    (0.2, 0.8),
    xycoords="subfigure fraction",
)
