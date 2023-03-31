# -*- coding: utf-8 -*-
"""
Created on Tue Apr  5 13:57:04 2022

@author: AnnaWiniwarter
"""

import numpy as np
import ixdat
import matplotlib

from pathlib import Path
from matplotlib import pyplot as plt
from ixdat.techniques.ms import MSMeasurement
from ixdat.techniques.ec import ECMeasurement

# change the fontsize for all figures
font = {"family": "normal", "weight": "normal", "size": 14}
matplotlib.rc("font", **font)

# -----------------------EDIT SETTINGS HERE----------------------------------
# Settings for choosing which part of the script is executed:
DATA_SOURCE = "raw_plus"
# DATA_SOURCE can be "raw" (for importing EC and MS data from Zilien .tsv file),
# "raw_plus" (for importing MS data from Zilien .tsv file and EC data from
# biologic .mpt files),
# or "ixdat" (for importing ixdat .csv files)
# in either case, for plotting the CV only, the biologic CVA file is imported
# automatically
WHICH_PART = "plot+cal"
# WHICH_PART can be "import_only", "plot_CVs", "plot+cal"
FOLLOW_SIGNALS = True
# set to true to print a plot with the signal development of selected masses over time

SAVE_FIGURES = True
# SAVE_FIGURES set to True: figures will be saved automatically.
FIGURE_TYPE = ".png"
# FIGURE_TYPE can be any format matplotlib accepts for saving figures, eg.
# ".png", ".svg", ".pdf" etc.

# select the directory of the raw data.
EXP_NAME = "HERonPt_repeated"
PARENT_PATH = Path(
    r"C:\Users\AnnaWiniwarter\Spectro Inlets Dropbox\Development\Data\Quantification Application Note"
)

# select the filenames of the raw data.
# zilien_filename = "2022-03-16 10_41_29 HER_on_Pt_repeatability_test_1.tsv"
# biologic_filename_cv = "2022-03-16 10_41_29 HER_on_Pt_repeatability_test_1_04_01_CVA_DUSB0_C01.mpt"
# biologic_filename_cp = "2022-03-16 10_41_29 HER_on_Pt_repeatability_test_1_04_02_CP_DUSB0_C01.mpt"

file_dict = {
    # "HERonPt_RnD1_2019W4D2_noSEM_5+": {
    #     "DIR": r"HER on Pt repeatability\2022-06-28 11_16_22 HER_repetition_SEM_off_3",
    #     "ZIL": "2022-06-28 11_16_22 HER_repetition_SEM_off_3.tsv",
    #     "CV": "2022-06-28 11_16_22 HER_repetition_SEM_off_3_01_01_CVA_DUSB0_C01.mpt",
    #     "CP": "2022-06-28 11_16_22 HER_repetition_SEM_off_3_01_02_CP_DUSB0_C01.mpt",
    #     "cv_tspan": [0, 1500],  # note: this is just a guess
    #     "cp_tspan": [0, 85000],
    #     "Ns_lists": [
    #         [x + 16 * y for x in [6, 8, 10, 12, 14]] for y in [17, 18, 19]
    #     ],  # np.arange(20)
    #     # "tspan_list": [[1396, 1496], [1983, 2102], [2582, 2701], [3188, 3288], [3780, 3899]],
    #     "tspan_bg_list": [
    #         [x + 4155 * y for x in [1930, 2030]] for y in [17, 18, 19]
    #     ],  # np.arange(20)
    # },
    # "HERonPt_RnD1_2019W4C5_noSEM_1-2": {
    #     "DIR": r"HER OER chip crosscheck\2022-07-06 09_33_53 HER_chip crosscheck_SEM_off",
    #     "ZIL": "2022-07-06 09_33_53 HER_chip crosscheck_SEM_off.tsv",
    #     "CV": "2022-07-06 09_33_53 HER_chip crosscheck_SEM_off_01_01_CVA_DUSB0_C01.mpt",
    #     "CP": "2022-07-06 09_33_53 HER_chip crosscheck_SEM_off_01_02_CP_DUSB0_C01.mpt",
    #     "cv_tspan": [0, 1500],  # note: this is just a guess
    #     "cp_tspan": [0, 10000],
    #     "Ns_lists": [[x + 16 * y for x in [6, 8, 10, 12, 14]] for y in np.arange(2)],
    #     # "tspan_list": [[1396, 1496], [1983, 2102], [2582, 2701], [3188, 3288], [3780, 3899]],
    #     "tspan_bg_list": [[2362, 2479], [6498, 6639]],
    # },
    # "HERonPt_RnD1_2021bW1D3_noSEM_1-2": {
    #     "DIR": r"HER OER chip crosscheck\2022-07-06 15_54_35 HER_chip crosscheck_newchip_SEM_off",
    #     "ZIL": "2022-07-06 15_54_35 HER_chip crosscheck_newchip_SEM_off.tsv",
    #     "CV": "2022-07-06 15_54_35 HER_chip crosscheck_newchip_SEM_off_01_01_CVA_DUSB0_C01.mpt",
    #     "CP": "2022-07-06 15_54_35 HER_chip crosscheck_newchip_SEM_off_01_02_CP_DUSB0_C01.mpt",
    #     "cv_tspan": [0, 1500],  # note: this is just a guess
    #     "cp_tspan": [0, 10000],
    #     "Ns_lists": [[x + 16 * y for x in [6, 8, 10, 12, 14]] for y in np.arange(2)],
    #     # "tspan_list": [[1396, 1496], [1983, 2102], [2582, 2701], [3188, 3288], [3780, 3899]],
    #     "tspan_bg_list": [[2062, 2198], [6241, 6366]],
    # },
    "HERonPt_RnD1_2021bW2D3_noSEM_all": {
        "DIR": r"application note data\2022-07-19 10_02_32 AIO_HER_OER_2021bW2D3",
        "ZIL": "2022-07-19 10_02_32 AIO_HER_OER_2021bW2D3.tsv",
        "CV": "2022-07-19 10_02_32 AIO_HER_OER_2021bW2D3_01_01_CVA_DUSB0_C01.mpt",
        "CP": "2022-07-19 10_02_32 AIO_HER_OER_2021bW2D3_01_02_CP_DUSB0_C01.mpt",
        "cv_tspan": [0, 1500],  # note: this is just a guess
        "cp_tspan": [0, 10000],
        "Ns_lists": [[x + 16 * y for x in [6, 8, 10, 12, 14]] for y in [0, 1, 2]],
        # "tspan_list": [[1396, 1496], [1983, 2102], [2582, 2701], [3188, 3288], [3780, 3899]],
        "tspan_bg_list": [[2900, 3100], [10645, 10798], [18963, 19078]],
    },
}


# ----------------------- END OF EDIT SETTINGS --------
def plot_cvs(full_data, cv_tspan):
    """Plot CVs."""
    cvs = full_data.cut(tspan=cv_tspan)
    cvs.tstamp += 1600
    cvs = cvs.as_cv()
    cvs.redefine_cycle(start_potential=0.9, redox=True)
    axes_b = cvs.plot_measurement()
    cvs_vs_time = axes_b[0].get_figure()
    if SAVE_FIGURES is True:
        cvs_vs_time.savefig("./" + EXP_NAME + "CVs_vs_time" + FIGURE_TYPE)
    # plot one of the CVs (the 4th out of 5) vs potential.
    axes_c = cvs[3].ec_plotter.plot_vs_potential()
    cvs_ec_vs_pot = axes_c.get_figure()
    if SAVE_FIGURES is True:
        cvs_ec_vs_pot.savefig("./" + EXP_NAME + "CV_vs_potential_EC" + FIGURE_TYPE)
    # To instead plot averaged (less noisy) EC data, import biologic file directly
    cvs_ec_only = ECMeasurement.read(
        data_directory / biologic_filename_cv, reader="biologic"
    )
    cvs_ec_only = cvs_ec_only.as_cv()
    cvs_ec_only.redefine_cycle(start_potential=0.9, redox=True)
    axes_c = cvs_ec_only[3].plot_vs_potential()
    cvs_ec_vs_pot = axes_c.get_figure()
    if SAVE_FIGURES is True:
        cvs_ec_vs_pot.savefig(
            "./" + EXP_NAME + "CV_vs_potential_EC_biologic" + FIGURE_TYPE
        )


def plot_and_calibrate(
    full_data,
    cp_tspan,
    cp_tspan_list,
    cp_selector_list,
    selector_name,
    t_steady_pulse,
    cp_bg,
    cal_type,
):
    """Plot HER and calibrate hydrogen."""
    # select the t_span automatically based on selector input
    t_start = full_data.select_values(**{selector_name: cp_selector_list[0]}).grab("t")[
        0
    ][0]
    t_end = full_data.select_values(**{selector_name: cp_selector_list[-1]}).grab("t")[
        0
    ][-1]
    cps = full_data.cut(tspan=[t_start, t_end])
    # save t_stamp for later on processing
    tstamp = cps.tstamp + t_start
    selector_list_new = [x - cp_selector_list[0] for x in cp_selector_list]
    axes_c = cps.plot_measurement(mass_list=["M2"])
    if cal_type == "HER":
        mol = "H2"
        mass = "M2"
        electrons = -2
    elif cal_type == "OER":
        mol = "O2"
        mass = "M32"
        electrons = 4
    else:
        raise NameError("No such cal_type found.")
    cal = cps.ecms_calibration_curve(
        mol,
        mass,
        electrons,
        selector_list=selector_list_new,
        selector_name=selector_name,
        t_steady_pulse=t_steady_pulse,
        tspan_bg=cp_bg,
        ax="new",
        axes_measurement=axes_c,
        return_ax=True,
    )
    print("HER calibration factor F= {:.3f}".format(cal[0].F))
    cal[1].annotate(
        "F = {:.3f} C/mol".format(cal[0].F),
        (0.15, 0.88),
        xycoords="subfigure fraction",  # (0.2, 0.8)
    )
    cal[1].annotate(
        "t_start = {:.0f} s".format(t_start),
        (0.15, 0.83),
        xycoords="subfigure fraction",  # (0.2, 0.75)
    )

    cps_vs_time = axes_c[0].get_figure()
    cps_vs_time.tight_layout(pad=0.3)
    if SAVE_FIGURES is True:
        cps_vs_time.savefig(
            "./" + EXP_NAME + cal_type + "_CPs_" + str(t_start) + FIGURE_TYPE
        )
    cal_curve = cal[1].get_figure()
    cal_curve.tight_layout(pad=0.3)
    if SAVE_FIGURES is True:
        cal_curve.savefig(
            "./" + EXP_NAME + cal_type + "_cal_curve_" + str(t_start) + FIGURE_TYPE
        )
    return (cal[0], tstamp)


# plot the the difference in value between two times in a list of times
def value_diff_t_list(data, tstamp_list, value_name_list, plot=True):
    time_abs = [tstamp_list[x] for x in np.arange(len(tstamp_list))]
    time = [(t - time_abs[0]) for t in time_abs]
    time_diff_hours = [
        (time[t] + time[t + 1]) / 2 / 3600 for t in np.arange(len(time) - 1)
    ]
    if plot:
        fig1, ax1 = plt.subplots()
        ax1.plot([0, max(time_diff_hours)], [0, 0], "k:")
    for value_name in value_name_list:
        values = [
            np.average(data.grab(value_name, tspan=[tstamp - 10, tstamp + 10])[1])
            for tstamp in time
        ]
        values_diff = [
            (values[x + 1] - values[x]) / values[x] * 100 / (time[x + 1] - time[x])
            for x in np.arange(len(values) - 1)
        ]
        if plot:
            color = ixdat.plotters.ms_plotter.STANDARD_COLORS[value_name]
            ax1.plot(
                time_diff_hours,
                values_diff,
                linestyle="",
                marker="*",
                markerfacecolor=color,
                markeredgecolor=color,
                label=value_name,
            )
    ax1.legend()
    ax1.set_ylabel("delta signal/time [%/h]")
    ax1.set_xlabel("experiment time / [h]")


def main():
    """Run main function."""
    if (
        DATA_SOURCE == "raw"
    ):  # option 1: import both EC and MS data from Zilien data file
        print(data_directory / zilien_filename)
        full_data = ixdat.Measurement.read(
            data_directory / zilien_filename, reader="zilien"
        )
        axes_a = full_data.plot_measurement(tspan=[0, 100000])
        full_plot = axes_a[0].get_figure()
        if SAVE_FIGURES is True:
            full_plot.savefig("./" + EXP_NAME + "full_experiment" + FIGURE_TYPE)
        full_data.export("./" + EXP_NAME + ".csv")
    elif DATA_SOURCE == "raw_plus":  # option 1: import MS data from Zilien data file
        # and EC data from biologic files
        print(data_directory / zilien_filename)
        full_data_zilien = ixdat.Measurement.read(
            data_directory / zilien_filename, reader="zilien", technique="MS"
        )
        cvs_ec_only = ixdat.Measurement.read(
            data_directory / biologic_filename_cv, reader="biologic"
        )
        cps_ec_only = ixdat.Measurement.read(
            data_directory / biologic_filename_cp, reader="biologic"
        )
        # These two lines get rid of the EC data from the zilien-read file,
        # since we will use the EC data from the biologic file instead.
        full_data_zilien.replace_series("Ewe/V", None)
        full_data_zilien.replace_series("I/mA", None)
        # full_data_zilien.replace_series("Potential time [s]", None)
        full_data = full_data_zilien + cvs_ec_only + cps_ec_only
        axes_a = full_data.plot_measurement(tspan=[0, 100000])
        full_plot = axes_a[0].get_figure()
        if SAVE_FIGURES is True:
            full_plot.savefig("./" + EXP_NAME + "full_experiment" + FIGURE_TYPE)
        full_data.export("./" + EXP_NAME + ".csv")
    elif DATA_SOURCE == "ixdat":  # option 2: import from ixdat-datafiles
        full_data = ixdat.Measurement.read("./" + EXP_NAME + ".csv", reader="ixdat")
        axes_a = full_data.plot_measurement(tspan=[0, 70000])
    else:
        raise NameError("DATA_SOURCE not recognized.")
    if WHICH_PART == "import_only":
        return full_data
    elif WHICH_PART == "plot_CVs":  # plot the CV part
        plot_cvs(full_data=full_data, cv_tspan=cv_tspan)
    elif WHICH_PART == "plot+cal":
        F_and_tstamp_list = []
        for cp_selector_list, cp_bg in zip(
            file_dict[file]["Ns_lists"], file_dict[file]["tspan_bg_list"]
        ):
            F_and_tstamp_list.append(
                plot_and_calibrate(
                    full_data=full_data,
                    cp_tspan=cp_tspan,
                    cp_tspan_list=cp_tspan_list,
                    cp_selector_list=cp_selector_list,
                    selector_name=selector_name,
                    t_steady_pulse=t_steady_pulse,
                    cp_bg=cp_bg,
                    cal_type=cal_type,
                )
            )
        if FOLLOW_SIGNALS:
            value_diff_t_list(
                full_data,
                [F_and_tstamp_list[x][1] for x in np.arange(len(F_and_tstamp_list))],
                value_name_list,
                plot=True,
            )
        return F_and_tstamp_list
    else:
        raise NameError("WHICH_PART not recognized.")


# if __name__ == "__main__":
#     main()

full_data_list = []
h2_F_and_tstamp_list = []
# tstamp_list = []

for file in file_dict:
    EXP_NAME = file
    data_directory = PARENT_PATH / file_dict[file]["DIR"]
    zilien_filename = file_dict[file]["ZIL"]
    biologic_filename_cv = file_dict[file]["CV"]
    biologic_filename_cp = file_dict[file]["CP"]
    cv_tspan = file_dict[file]["cv_tspan"]
    cp_tspan = file_dict[file]["cp_tspan"]
    # cp_tspan_list = file_dict[file]["tspan_list"]
    # cp_bg = file_dict[file]["tspan_bg"]
    selector_name = "selector"
    t_steady_pulse = 100
    cp_tspan_list = None
    cal_type = "HER"
    value_name_list = ["M2", "M4", "M18", "M28", "M32", "M40", "M44"]
    if WHICH_PART == "import_only":
        full_data_list.append(main())
    elif WHICH_PART == "plot+cal":
        h2_F_and_tstamp_list = h2_F_and_tstamp_list + main()
# Now plot the time development of F
# time_abs = [h2_F_and_tstamp_list[x][1] for x in np.arange(len(h2_F_and_tstamp_list))]
# time = [(t - time_abs[0]) / 3600 for t in time_abs]
# x = [x for x in np.arange(len(h2_F_and_tstamp_list))]
# namelist = [
#     "2019W4D2",
#     "2019W4D2",
#     "2019W4D2",
#     "2019W4C5",
#     "2019W4C5",
#     "2021bW1D3",
#     "2021bW1D3",
# ]
# Fs = [h2_F_and_tstamp_list[x][0].F for x in np.arange(len(h2_F_and_tstamp_list))]
# fig1, ax1 = plt.subplots()
# ax1.plot(x, Fs, linestyle="", marker="o", label=cal_type)
# ax1.set_xticks(ax1.get_xticks()[1:-1])
# ax1.set_xticklabels(
#     namelist, rotation=45,
# )
# ax1.legend()
# ax1.set_ylabel("F$_{H2}$ from HER / [C/mol]")
# ax1.set_xlabel("time / [h]")
# plt.tight_layout(pad=0.3)
# fig1.savefig("./F_HER_chip_crosscheck.png")

# np.savetxt(
#     "./F_HER_chip_crosscheck.csv", np.array([namelist, Fs]), delimiter=", ", fmt="%s",
# )

# np.savetxt(
#     "./F_HER_chip_crosscheck.csv", np.array([namelist, Fs]), delimiter=", ", fmt="%s",
# )
