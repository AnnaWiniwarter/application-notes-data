"""
Do a low concentration calibration.

Created on Thu Mar  3 14:55:33 2022

@author: AnnaWiniwarter
"""
import numpy as np
from matplotlib import pyplot as plt
import ixdat
from ixdat.techniques import MSMeasurement
from pathlib import Path

data_directory = (
    Path.home()
    / r"C:\Users\AnnaWiniwarter\Dropbox (Spectro Inlets)\Development\Data\Quantification Application Note\gas cal tests"
)

lowH2_cell_data = MSMeasurement.read(
    data_directory
    / r"2022-07-07 09_32_09 low_c_H2_cal_w_cell_2021W1D3/2022-07-07 09_32_09 low_c_H2_cal_w_cell_2021W1D3.tsv",
    reader="zilien",
)

lowH2_cell_data.plot_measurement()

mychip = ixdat.techniques.ms.MSInlet()
# mychip = ixdat.techniques.ms.MSInlet(T=300, p=20000) #optional: select T (in Kelvin) and p (in Pa)

lowH2_cell_cal = mychip.gas_flux_calibration_curve(
    lowH2_cell_data,
    mol="H2",
    mass="M2",
    tspan_list=[[3017, 3741], [4484, 5171], [6081, 6712], [7622, 7975]],
    carrier_mol="He",
    mol_conc_ppm=[500, 1000, 5000, 10000],
    tspan_bg=[2218, 2478],  # alternatively [8216, 8346]
    return_ax=True,
)
lowH2_cell_cal[1].annotate(
    "F = {:.3f} C/mol".format(lowH2_cell_cal[0].F),
    (0.2, 0.8),
    xycoords="subfigure fraction",
)

lowH2_cell_cal_fig = lowH2_cell_cal[1].get_figure()
lowH2_cell_cal_fig.savefig("./low_H2_cell_cal_curve.png")

# lowH2_cell_data.calibrate(ms_cal_results=[lowH2_cell_cal[0]])
# lowH2_cell_data.plot_measurement(mol_list=["H2"], logplot=False)


highH2_cell_data = MSMeasurement.read(
    data_directory
    / r"2022-07-07 11_52_03 high_c_H2_cal_w_cell_2021W1D3/2022-07-07 11_52_03 high_c_H2_cal_w_cell_2021W1D3.tsv",
    reader="zilien",
)

highH2_cell_data.plot_measurement()

# mychip = ixdat.techniques.ms.MSInlet()
# mychip = ixdat.techniques.ms.MSInlet(T=300, p=20000) #optional: select T (in Kelvin) and p (in Pa)

highH2_cell_cal = mychip.gas_flux_calibration_curve(
    highH2_cell_data,
    mol="H2",
    mass="M2",
    tspan_list=[[2486, 3298], [4109, 5027], [8102, 8956]],  # [5710, 6415],
    carrier_mol="He",
    mol_conc_ppm=[50000, 100000, 10000],  # 200000,
    tspan_bg=[1205, 1334],
    # p_inlet=1.047e5,
    return_ax=True,
)
highH2_cell_cal[1].annotate(
    "F = {:.3f} C/mol".format(highH2_cell_cal[0].F),
    (0.2, 0.8),
    xycoords="subfigure fraction",
)

highH2_cell_cal_fig = highH2_cell_cal[1].get_figure()
highH2_cell_cal_fig.savefig("./high_H2_cell_cal_curve.png")

# highH2_cell_data.calibrate(ms_cal_results=[highH2_cell_cal[0]])
# highH2_cell_data.plot_measurement(mol_list=["H2"], logplot=False)

O2_cell_data = MSMeasurement.read(
    data_directory
    / r"2022-07-07 14_32_55 O2_cal_w_cell_2021W1D3/2022-07-07 14_32_55 O2_cal_w_cell_2021W1D3.tsv",
    reader="zilien",
)

O2_cell_data.plot_measurement()

# mychip = ixdat.techniques.ms.MSInlet()
# mychip = ixdat.techniques.ms.MSInlet(T=300, p=20000) #optional: select T (in Kelvin) and p (in Pa)

O2_cell_cal = mychip.gas_flux_calibration_curve(
    O2_cell_data,
    mol="O2",
    mass="M32",
    tspan_list=[
        [2846, 3201],
        [3888, 4375],
        [5639, 6104],
        [6901, 7699],
    ],  # [8608, 9117]
    carrier_mol="He",
    mol_conc_ppm=[5000, 10000, 50000, 100000],  # , 200000
    tspan_bg=[1052, 1539],
    # p_inlet=1.047e5,
    return_ax=True,
)
O2_cell_cal[1].annotate(
    "F = {:.3f} C/mol".format(O2_cell_cal[0].F),
    (0.2, 0.8),
    xycoords="subfigure fraction",
)

O2_cell_cal_fig = O2_cell_cal[1].get_figure()
O2_cell_cal_fig.savefig("./O2_cell_cal_curve.png")

# O2_cell_data.calibrate(ms_cal_results=[O2_cell_cal[0]])
# O2_cell_data.plot_measurement(mol_list=["O2"], logplot=False)

# lowH2_cell_data = MSMeasurement.read(
#     data_directory
#     / r"",
#     reader="zilien",
# )

# lowH2_kapton_data.plot_measurement()

# mychip = ixdat.techniques.ms.MSInlet()
# # mychip = ixdat.techniques.ms.MSInlet(T=300, p=20000) #optional: select T (in Kelvin) and p (in Pa)

# lowH2_kapton_cal = mychip.gas_flux_calibration_curve(
#     lowH2_kapton_data,
#     mol="H2",
#     mass="M2",
#     tspan_list=[[3017, 3741], [4484, 5171], [6081, 6712], [7622, 7975]],
#     carrier_mol="He",
#     mol_conc_ppm=[500, 1000, 5000, 10000],
#     tspan_bg=[2218, 2478],  # alternatively [8216, 8346]
#     return_ax=True,
# )
# lowH2_kapton_cal[1].annotate(
#     "F = {:.3f} C/mol".format(lowH2_kapton_cal[0].F),
#     (0.2, 0.8),
#     xycoords="subfigure fraction",
# )

# lowH2_kapton_data.calibrate(ms_cal_results=[lowH2_kapton_cal[0]])
# lowH2_kapton_data.plot_measurement(mol_list=["H2"], logplot=False)


highH2_kapton_data = MSMeasurement.read(
    data_directory
    / r"2022-07-11 12_59_29 H2_high_c_cal_kapton_2021W1D3/2022-07-11 12_59_29 H2_high_c_cal_kapton_2021W1D3.tsv",
    reader="zilien",
)

highH2_kapton_data.plot_measurement()

# mychip = ixdat.techniques.ms.MSInlet()
# mychip = ixdat.techniques.ms.MSInlet(T=300, p=20000) #optional: select T (in Kelvin) and p (in Pa)

highH2_kapton_cal = mychip.gas_flux_calibration_curve(
    highH2_kapton_data,
    mol="H2",
    mass="M2",
    tspan_list=[
        [2737, 3370],
        [4265, 4824],
        [5345, 5680],
        [10785, 10971],
    ],  # [7395, 8774],
    carrier_mol="He",
    mol_conc_ppm=[10000, 50000, 100000, 10000],  # 200000,
    tspan_bg=[1545, 1731],
    # p_inlet=1.047e5,
    return_ax=True,
)
highH2_kapton_cal[1].annotate(
    "F = {:.3f} C/mol".format(highH2_kapton_cal[0].F),
    (0.2, 0.8),
    xycoords="subfigure fraction",
)

highH2_kapton_cal_fig = highH2_kapton_cal[1].get_figure()
highH2_kapton_cal_fig.savefig("./high_H2_kapton_cal_curve.png")

# highH2_kapton_data.calibrate(ms_cal_results=[highH2_kapton_cal[0]])
# highH2_kapton_data.plot_measurement(mol_list=["H2"], logplot=False)

O2_kapton_data = MSMeasurement.read(
    data_directory
    / r"2022-07-11 09_47_13 O2_cal_kapton_2021W1D3/2022-07-11 09_47_13 O2_cal_kapton_2021W1D3.tsv",
    reader="zilien",
)

O2_kapton_data.plot_measurement()

# mychip = ixdat.techniques.ms.MSInlet()
# mychip = ixdat.techniques.ms.MSInlet(T=300, p=20000) #optional: select T (in Kelvin) and p (in Pa)

O2_kapton_cal = mychip.gas_flux_calibration_curve(
    O2_kapton_data,
    mol="O2",
    mass="M32",
    tspan_list=[
        [3226, 3481],
        [4374, 4808],
        [6287, 7027],
        [7894, 8430],
    ],  # [9655, 10318]
    carrier_mol="He",
    mol_conc_ppm=[5000, 10000, 50000, 100000,],  # 200000
    tspan_bg=[1925, 2078],
    # p_inlet=1.047e5,
    return_ax=True,
)
O2_kapton_cal[1].annotate(
    "F = {:.3f} C/mol".format(O2_kapton_cal[0].F),
    (0.2, 0.8),
    xycoords="subfigure fraction",
)

O2_kapton_cal_fig = O2_kapton_cal[1].get_figure()
O2_kapton_cal_fig.savefig("./O2_kapton_cal_curve.png")
# O2_kapton_data.calibrate(ms_cal_results=[O2_kapton_cal[0]])
# O2_kapton_data.plot_measurement(mol_list=["O2"], logplot=False)
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

lowH2_cell_data = MSMeasurement.read(
    data_directory
    / r"2022-07-07 09_32_09 low_c_H2_cal_w_cell_2021W1D3/2022-07-07 09_32_09 low_c_H2_cal_w_cell_2021W1D3.tsv",
    reader="zilien",
)

lowH2_cell_data_fig = lowH2_cell_data.plot_measurement().get_figure()
lowH2_cell_data_fig.savefig("./lowH2_cell_cal_vs_time.png")


mychip = ixdat.techniques.ms.MSInlet()
# mychip = ixdat.techniques.ms.MSInlet(T=300, p=20000) #optional: select T (in Kelvin) and p (in Pa)

lowH2_cell_cal = mychip.gas_flux_calibration_curve(
    lowH2_cell_data,
    mol="H2",
    mass="M2",
    tspan_list=[[3017, 3741], [4484, 5171], [6081, 6712], [7622, 7975]],
    carrier_mol="He",
    mol_conc_ppm=[500, 1000, 5000, 10000],
    tspan_bg=[2218, 2478],  # alternatively [8216, 8346]
    return_ax=True,
)
lowH2_cell_cal[1].annotate(
    "F = {:.3f} C/mol".format(lowH2_cell_cal[0].F),
    (0.2, 0.8),
    xycoords="subfigure fraction",
)

lowH2_cell_cal_fig = lowH2_cell_cal[1].get_figure()
lowH2_cell_cal_fig.savefig("./low_H2_cell_cal_curve.png")

# lowH2_cell_data.calibrate(ms_cal_results=[lowH2_cell_cal[0]])
# lowH2_cell_data.plot_measurement(mol_list=["H2"], logplot=False)


highH2_cell_data = MSMeasurement.read(
    data_directory
    / r"2022-07-07 11_52_03 high_c_H2_cal_w_cell_2021W1D3/2022-07-07 11_52_03 high_c_H2_cal_w_cell_2021W1D3.tsv",
    reader="zilien",
)

highH2_cell_data_fig = highH2_cell_data.plot_measurement().get_figure()
highH2_cell_data_fig.savefig("./high_H2_cell_cal_vs_time.png")

# mychip = ixdat.techniques.ms.MSInlet()
# mychip = ixdat.techniques.ms.MSInlet(T=300, p=20000) #optional: select T (in Kelvin) and p (in Pa)

highH2_cell_cal = mychip.gas_flux_calibration_curve(
    highH2_cell_data,
    mol="H2",
    mass="M2",
    tspan_list=[[2486, 3298], [4109, 5027], [8102, 8956]],  # [5710, 6415],
    carrier_mol="He",
    mol_conc_ppm=[50000, 100000, 10000],  # 200000,
    tspan_bg=[1205, 1334],
    # p_inlet=1.047e5,
    return_ax=True,
)
highH2_cell_cal[1].annotate(
    "F = {:.3f} C/mol".format(highH2_cell_cal[0].F),
    (0.2, 0.8),
    xycoords="subfigure fraction",
)

highH2_cell_cal_fig = highH2_cell_cal[1].get_figure()
highH2_cell_cal_fig.savefig("./high_H2_cell_cal_curve.png")

# highH2_cell_data.calibrate(ms_cal_results=[highH2_cell_cal[0]])
# highH2_cell_data.plot_measurement(mol_list=["H2"], logplot=False)

O2_cell_data = MSMeasurement.read(
    data_directory
    / r"2022-07-07 14_32_55 O2_cal_w_cell_2021W1D3/2022-07-07 14_32_55 O2_cal_w_cell_2021W1D3.tsv",
    reader="zilien",
)

O2_cell_data_fig = O2_cell_data.plot_measurement().get_figure()
O2_cell_data_fig.savefig("./O2_cell_cal_vs_time.png")


# mychip = ixdat.techniques.ms.MSInlet()
# mychip = ixdat.techniques.ms.MSInlet(T=300, p=20000) #optional: select T (in Kelvin) and p (in Pa)

O2_cell_cal = mychip.gas_flux_calibration_curve(
    O2_cell_data,
    mol="O2",
    mass="M32",
    tspan_list=[
        [2846, 3201],
        [3888, 4375],
        [5639, 6104],
        [6901, 7699],
    ],  # [8608, 9117]
    carrier_mol="He",
    mol_conc_ppm=[5000, 10000, 50000, 100000],  # , 200000
    tspan_bg=[1052, 1539],
    # p_inlet=1.047e5,
    return_ax=True,
)
O2_cell_cal[1].annotate(
    "F = {:.3f} C/mol".format(O2_cell_cal[0].F),
    (0.2, 0.8),
    xycoords="subfigure fraction",
)

O2_cell_cal_fig = O2_cell_cal[1].get_figure()
O2_cell_cal_fig.savefig("./O2_cell_cal_curve.png")

# O2_cell_data.calibrate(ms_cal_results=[O2_cell_cal[0]])
# O2_cell_data.plot_measurement(mol_list=["O2"], logplot=False)

lowH2_kapton_data = MSMeasurement.read(
    data_directory
    / r"2022-07-13 09_54_24 H2_low_c_cal_kapton_2021W1D3/2022-07-13 09_54_24 H2_low_c_cal_kapton_2021W1D3.tsv",
    reader="zilien",
)

lowH2_kapton_data_fig = lowH2_kapton_data.plot_measurement().get_figure()
lowH2_kapton_data_fig.savefig("./lowH2_kapton_cal_vs_time.png")

mychip = ixdat.techniques.ms.MSInlet()
# mychip = ixdat.techniques.ms.MSInlet(T=300, p=20000) #optional: select T (in Kelvin) and p (in Pa)

lowH2_kapton_cal = mychip.gas_flux_calibration_curve(
    lowH2_kapton_data,
    mol="H2",
    mass="M2",
    tspan_list=[[2236, 2695], [3429, 4118], [5012, 5494], [6320, 6656]],
    carrier_mol="He",
    mol_conc_ppm=[500, 1000, 5000, 10000],
    tspan_bg=[974, 1387],  # alternatively [8216, 8346]
    return_ax=True,
)
lowH2_kapton_cal[1].annotate(
    "F = {:.3f} C/mol".format(lowH2_kapton_cal[0].F),
    (0.2, 0.8),
    xycoords="subfigure fraction",
)
lowH2_kapton_cal_fig = lowH2_kapton_cal[1].get_figure()
lowH2_kapton_cal_fig.savefig("./low_H2_kapton_cal_curve.png")

# lowH2_kapton_data.calibrate(ms_cal_results=[lowH2_kapton_cal[0]])
# lowH2_kapton_data.plot_measurement(mol_list=["H2"], logplot=False)


highH2_kapton_data = MSMeasurement.read(
    data_directory
    / r"2022-07-11 12_59_29 H2_high_c_cal_kapton_2021W1D3/2022-07-11 12_59_29 H2_high_c_cal_kapton_2021W1D3.tsv",
    reader="zilien",
)

highH2_kapton_data_fig = highH2_kapton_data.plot_measurement().get_figure()
highH2_kapton_data_fig.savefig("./highH2_kapton_cal_vs_time.png")

# mychip = ixdat.techniques.ms.MSInlet()
# mychip = ixdat.techniques.ms.MSInlet(T=300, p=20000) #optional: select T (in Kelvin) and p (in Pa)

highH2_kapton_cal = mychip.gas_flux_calibration_curve(
    highH2_kapton_data,
    mol="H2",
    mass="M2",
    tspan_list=[
        [2737, 3370],
        [4265, 4824],
        [5345, 5680],
        [10785, 10971],
    ],  # [7395, 8774],
    carrier_mol="He",
    mol_conc_ppm=[10000, 50000, 100000, 10000],  # 200000,
    tspan_bg=[1545, 1731],
    # p_inlet=1.047e5,
    return_ax=True,
)
highH2_kapton_cal[1].annotate(
    "F = {:.3f} C/mol".format(highH2_kapton_cal[0].F),
    (0.2, 0.8),
    xycoords="subfigure fraction",
)

highH2_kapton_cal_fig = highH2_kapton_cal[1].get_figure()
highH2_kapton_cal_fig.savefig("./high_H2_kapton_cal_curve.png")

# highH2_kapton_data.calibrate(ms_cal_results=[highH2_kapton_cal[0]])
# highH2_kapton_data.plot_measurement(mol_list=["H2"], logplot=False)

O2_kapton_data = MSMeasurement.read(
    data_directory
    / r"2022-07-11 09_47_13 O2_cal_kapton_2021W1D3/2022-07-11 09_47_13 O2_cal_kapton_2021W1D3.tsv",
    reader="zilien",
)

O2_kapton_data_fig = O2_kapton_data.plot_measurement().get_figure()
O2_kapton_data_fig.savefig("./O2_kapton_cal_vs_time.png")

# mychip = ixdat.techniques.ms.MSInlet()
# mychip = ixdat.techniques.ms.MSInlet(T=300, p=20000) #optional: select T (in Kelvin) and p (in Pa)

O2_kapton_cal = mychip.gas_flux_calibration_curve(
    O2_kapton_data,
    mol="O2",
    mass="M32",
    tspan_list=[
        [3226, 3481],
        [4374, 4808],
        [6287, 7027],
        [7894, 8430],
    ],  # [9655, 10318]
    carrier_mol="He",
    mol_conc_ppm=[5000, 10000, 50000, 100000,],  # 200000
    tspan_bg=[1925, 2078],
    # p_inlet=1.047e5,
    return_ax=True,
)
O2_kapton_cal[1].annotate(
    "F = {:.3f} C/mol".format(O2_kapton_cal[0].F),
    (0.2, 0.8),
    xycoords="subfigure fraction",
)

O2_kapton_cal_fig = O2_kapton_cal[1].get_figure()
O2_kapton_cal_fig.savefig("./O2_kapton_cal_curve.png")
# O2_kapton_data.calibrate(ms_cal_results=[O2_kapton_cal[0]])
# O2_kapton_data.plot_measurement(mol_list=["O2"], logplot=False)

namelist = [
    "high H2 cell",
    "high H2 kapton",
    "low H2 cell",
    "low H2 kapton",
    "O2 cell",
    "O2 kapton",
]
Fs = [
    highH2_cell_cal[0].F,
    highH2_kapton_cal[0].F,
    lowH2_cell_cal[0].F,
    lowH2_kapton_cal[0].F,
    O2_cell_cal[0].F,
    O2_kapton_cal[0].F,
]
x = [x + 1 for x in np.arange(len(Fs))]
# colorlist = ["b", "b", "b", "b", "k", "k"]
fig1, ax1 = plt.subplots()
ax1.plot(
    x, Fs, linestyle="", marker="o", markerfacecolor="g", markeredgecolor="g",
)
ax1.set_xticks(ax1.get_xticks()[1:-1])
ax1.set_xticklabels(
    namelist, rotation=45,
)
# ax1.legend()
ax1.set_ylabel("F from gas calibration / [C/mol]")
ax1.set_xlabel("time / [h]")
plt.tight_layout()
fig1.savefig("./F_gas_flux_cell_vs_kapton.png")

np.savetxt(
    "./F_gas_flux_cell_vs_kapton.csv",
    np.array([namelist, Fs]),
    delimiter=", ",
    fmt="%s",
)
