"""
Do a low concentration calibration.

Created on Thu Mar  3 14:55:33 2022

@author: AnnaWiniwarter
"""

import ixdat
import matplotlib
from ixdat.techniques import MSMeasurement
from pathlib import Path

# change the fontsize for all figures
font = {"family": "normal", "weight": "normal", "size": 14}
matplotlib.rc("font", **font)

data_directory = (
    Path.home()
    / r"C:\Users\AnnaWiniwarter\Spectro Inlets Dropbox\Development\Data\Quantification Application Note\application note data"
)

lowH2_cell_data = MSMeasurement.read(
    data_directory
    / r"2022-07-20 09_12_28 AIO_low_H2_2021bW2D3/2022-07-20 09_12_28 AIO_low_H2_2021bW2D3.tsv",
    reader="zilien",
)

lowH2_cell_data_fig = lowH2_cell_data.plot_measurement().get_figure()
# lowH2_cell_data_fig.savefig("./app_note_lowH2_cell_cal_vs_time.png")

highH2_cell_data = MSMeasurement.read(
    data_directory
    / r"2022-07-20 11_24_43 AIO_high_H2_2021bW2D3/2022-07-20 11_24_43 AIO_high_H2_2021bW2D3.tsv",
    reader="zilien",
)

highH2_cell_data_fig = highH2_cell_data.plot_measurement().get_figure()
# highH2_cell_data_fig.savefig("./app_note_high_H2_cell_cal_vs_time.png")

O2_cell_data = MSMeasurement.read(
    data_directory
    / r"2022-07-20 15_32_25 AIO_O2_2021bW2D3/2022-07-20 15_32_25 AIO_O2_2021bW2D3.tsv",
    reader="zilien",
)
O2_cell_data_fig = O2_cell_data.plot_measurement().get_figure()
# O2_cell_data_fig.savefig("./app_note_O2_cell_cal_vs_time.png")

C2H4_cell_data = MSMeasurement.read(
    data_directory
    / r"2022-07-20 13_04_48 AIO_C2H4_2021bW2D3/2022-07-20 13_04_48 AIO_C2H4_2021bW2D3.tsv",
    reader="zilien",
)
C2H4_cell_data_fig = C2H4_cell_data.plot_measurement().get_figure()
# C2H4_cell_data_fig.savefig("./app_note_C2H4_cell_cal_vs_time.png")

full_data = lowH2_cell_data + highH2_cell_data + O2_cell_data + C2H4_cell_data

full_data_ax = full_data.plot_measurement()
full_data_fig = full_data_ax.get_figure()
full_data_fig.tight_layout(pad=0.3)
full_data_fig.savefig("./app_note_full_data_cell_cal_vs_time.png")

mychip = ixdat.techniques.ms.MSInlet()
# mychip = ixdat.techniques.ms.MSInlet(T=300, p=20000) #optional: select T (in Kelvin) and p (in Pa)

all_H2_cell_cal = mychip.gas_flux_calibration_curve(
    full_data,
    mol="H2",
    mass="M2",
    tspan_list=[
        [3037, 3504],
        [4439, 4956],
        [6038, 6456],
        [7243, 7538],
        [10760, 11031],
        [11941, 12236],
        [13023, 13367],
    ],
    carrier_mol="He",
    mol_conc_ppm=[500, 1000, 5000, 10000, 10000, 50000, 100000],
    tspan_bg=[1750, 1950],
    return_ax=True,
    # axes_measurement=full_data_ax, #this doesn't work somehow...
)
all_H2_cell_cal[1].annotate(
    "F = {:.3f} C/mol".format(all_H2_cell_cal[0].F),
    (0.2, 0.875),
    xycoords="subfigure fraction",
)

all_H2_cell_cal_fig = all_H2_cell_cal[1].get_figure()
all_H2_cell_cal_fig.tight_layout(pad=0.3)
all_H2_cell_cal_fig.savefig("./app_note_H2_cal_curve.png")

C2H4_M26_cell_cal = mychip.gas_flux_calibration_curve(
    full_data,
    mol="C2H4",
    mass="M26",
    tspan_list=[
        [17170, 17355],
        [18463, 18740],
        [19725, 19940],
        [20648, 21048],
        [21756, 22126],
    ],
    carrier_mol="He",
    mol_conc_ppm=[5000, 10000, 20000, 50000, 100000],
    tspan_bg=[14369, 15046],
    return_ax=True,
    # axes_measurement=full_data_ax,
)
C2H4_M26_cell_cal[1].annotate(
    "F = {:.3f} C/mol".format(C2H4_M26_cell_cal[0].F),
    (0.2, 0.875),
    xycoords="subfigure fraction",
)

C2H4_M26_cal_fig = C2H4_M26_cell_cal[1].get_figure()
C2H4_M26_cal_fig.tight_layout(pad=0.3)
C2H4_M26_cal_fig.savefig("./app_note_C2H4_M26_cal_curve.png")

mychip_2 = ixdat.techniques.ms.MSInlet(T=305.15)
O2_cell_cal = mychip_2.gas_flux_calibration_curve(
    full_data,
    mol="O2",
    mass="M32",
    tspan_list=[
        [25204, 25419],
        [26404, 26650],
        [27605, 27947],
        [28990, 29236],
        [29975, 30313],
    ],
    carrier_mol="He",
    mol_conc_ppm=[5000, 10000, 20000, 50000, 100000],
    tspan_bg=[23018, 23634],
    # p_inlet=1.047e5,
    return_ax=True,
    # axes_measurement=full_data_ax,
)
O2_cell_cal[1].annotate(
    "F = {:.3f} C/mol".format(O2_cell_cal[0].F),
    (0.2, 0.875),
    xycoords="subfigure fraction",
)

O2_cell_cal_fig = O2_cell_cal[1].get_figure()
O2_cell_cal_fig.tight_layout(pad=0.3)
O2_cell_cal_fig.savefig("./app_note_O2_cal_curve.png")


# namelist = [
#     "high H2 cell",
#     "high H2 kapton",
#     "low H2 cell",
#     "low H2 kapton",
#     "O2 cell",
#     "O2 kapton",
# ]
# Fs = [
#     highH2_cell_cal[0].F,
#     highH2_kapton_cal[0].F,
#     lowH2_cell_cal[0].F,
#     lowH2_kapton_cal[0].F,
#     O2_cell_cal[0].F,
#     O2_kapton_cal[0].F,
# ]
# x = [x + 1 for x in np.arange(len(Fs))]
# # colorlist = ["b", "b", "b", "b", "k", "k"]
# fig1, ax1 = plt.subplots()
# ax1.plot(
#     x, Fs, linestyle="", marker="o", markerfacecolor="g", markeredgecolor="g",
# )
# ax1.set_xticks(ax1.get_xticks()[1:-1])
# ax1.set_xticklabels(
#     namelist, rotation=45,
# )
# # ax1.legend()
# ax1.set_ylabel("F from gas calibration / [C/mol]")
# ax1.set_xlabel("time / [h]")
# plt.tight_layout()
# fig1.savefig("./F_gas_flux_cell_vs_kapton.png")

# np.savetxt(
#     "./F_gas_flux_cell_vs_kapton.csv",
#     np.array([namelist, Fs]),
#     delimiter=", ",
#     fmt="%s",
# )
