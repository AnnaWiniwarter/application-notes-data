# -*- coding: utf-8 -*-
"""
Created on Tue Apr  5 13:57:04 2022

@author: AnnaWiniwarter
"""

import numpy as np
import ixdat

from pathlib import Path
from matplotlib import pyplot as plt
from ixdat.techniques.ms import MSMeasurement
from ixdat.techniques.ec import ECMeasurement


# -----------------------EDIT SETTINGS HERE----------------------------------
# Settings for choosing which part of the script is executed:
DATA_SOURCE = "raw_plus"
# DATA_SOURCE can be "raw" (for importing EC and MS data from Zilien .tsv file),
# "raw_plus" (for importing MS data from Zilien .tsv file and EC data from
# biologic .mpt files),
# or "ixdat" (for importing ixdat .csv files)
# in either case, for plotting the CV only, the biologic CVA file is imported
# automatically
WHICH_PART = "import_only"
# WHICH_PART can be "import_only", "plot_CVs", "plot+cal_HER", "plot+cal_OER"

SAVE_FIGURES = True
# SAVE_FIGURES set to True: figures will be saved automatically.
FIGURE_TYPE = ".png"
# FIGURE_TYPE can be any format matplotlib accepts for saving figures, eg.
# ".png", ".svg", ".pdf" etc.

# select the directory of the raw data.
EXP_NAME = "HERonPt_repeated"
PARENT_PATH = Path(
    r"C:\Users\AnnaWiniwarter\Dropbox (Spectro Inlets)\Development\Data\Quantification Application Note\HER on Pt repeatability")

# select the filenames of the raw data.
# zilien_filename = "2022-03-16 10_41_29 HER_on_Pt_repeatability_test_1.tsv"
# biologic_filename_cv = "2022-03-16 10_41_29 HER_on_Pt_repeatability_test_1_04_01_CVA_DUSB0_C01.mpt"
# biologic_filename_cp = "2022-03-16 10_41_29 HER_on_Pt_repeatability_test_1_04_02_CP_DUSB0_C01.mpt"

file_dict = {"HERonPt_RnD1_1": {"DIR": r"2022-04-26 12_31_02 HER_repetition_1",
                                "ZIL": "2022-04-26 12_31_02 HER_repetition_1.tsv",
                                "CV": "2022-04-26 12_31_02 HER_repetition_1_01_01_CVA_DUSB0_C01.mpt",
                                "CP": "2022-04-26 12_31_02 HER_repetition_1_01_02_CP_DUSB0_C01.mpt",
                                "cp_tspan": [1500, 4600],
                                "tspan_list": [[1808, 1901], [2387, 2499], [2984, 3108], [3581, 3700], [4166, 4310]],
                                "tspan_bg": [1982, 2175], },
             "HERonPt_RnD1_2": {"DIR": r"2022-04-26 13_53_02 HER_repetition_2",
                                "ZIL": r"2022-04-26 13_53_02 HER_repetition_2.tsv",
                                "CV": "2022-04-26 13_53_02 HER_repetition_2_01_01_CVA_DUSB0_C01.mpt",
                                "CP": "2022-04-26 13_53_02 HER_repetition_2_01_02_CP_DUSB0_C01.mpt",
                                "cp_tspan": [1290, 4380],
                                "tspan_list": [[1578, 1665], [2153, 2272], [2748, 2867], [3343, 3468], [3943, 4075]],
                                "tspan_bg": [1778, 1940], },
             "HERonPt_RnD1_3": {"DIR": r"2022-04-26 15_09_49 HER_repetition_3",
                                "ZIL": "2022-04-26 15_09_49 HER_repetition_3.tsv",
                                "CV": "2022-04-26 15_09_49 HER_repetition_3_01_01_CVA_DUSB0_C01.mpt",
                                "CP": "2022-04-26 15_09_49 HER_repetition_3_01_02_CP_DUSB0_C01.mpt",
                                "cp_tspan": [1050, 4290],
                                "tspan_list": [[1401, 1491], [1966, 2097], [2567, 2703], [3169, 3296], [3770, 3888]],
                                "tspan_bg": [1591, 1771], },
             "HERonPt_RnD1_4_01": {"DIR": r"2022-04-26 16_27_01 HER_repetition_4+",
                                   "ZIL": "2022-04-26 16_27_01 HER_repetition_4+.tsv",
                                   "CV": "2022-04-26 16_27_01 HER_repetition_4+_01_01_CVA_DUSB0_C01.mpt",
                                   "CP": "2022-04-26 16_27_01 HER_repetition_4+_01_02_CP_DUSB0_C01.mpt",
                                   "cp_tspan": [1150, 4200],
                                   "tspan_list": [[1396, 1496], [1983, 2102], [2582, 2701], [3188, 3288], [3780, 3899]],
                                   "tspan_bg": [1590, 1758], },
             # "HERonPt_RnD1_4_02": {"DIR": r"2022-04-26 16_27_01 HER_repetition_4+",
             #                       "ZIL": "2022-04-26 16_27_01 HER_repetition_4+.tsv",
             #                       "CV": "2022-04-26 16_27_01 HER_repetition_4+_01_01_CVA_DUSB0_C01.mpt",
             #                       "CP": "2022-04-26 16_27_01 HER_repetition_4+_01_02_CP_DUSB0_C01.mpt",
             #                       "cp_tspan": [599, 3840],
             #                       "tspan_list": [[1047, 1128], [1608, 1725], [2191, 2329], [2803, 2926], [3474, 3520]],
             #                       "tspan_bg": [1216, 1396], },
             # "HERonPt_RnD1_4_03": {"DIR": r"2022-04-26 16_27_01 HER_repetition_4+",
             #                       "ZIL": "2022-04-26 16_27_01 HER_repetition_4+.tsv",
             #                       "CV": "2022-04-26 16_27_01 HER_repetition_4+_01_01_CVA_DUSB0_C01.mpt",
             #                       "CP": "2022-04-26 16_27_01 HER_repetition_4+_01_02_CP_DUSB0_C01.mpt",
             #                       "cp_tspan": [1379, 4738],
             #                       "tspan_list": [[1859, 1955], [2425, 2553], [3023, 3151], [3617, 3745], [4215, 4357]],
             #                       "tspan_bg": [2030, 2222], },
             }


# ----------------------- END OF EDIT SETTINGS --------
def main():
    """Run main function."""
    if DATA_SOURCE == "raw":  # option 1: import both EC and MS data from Zilien data file
        print(data_directory / zilien_filename)
        full_data = ixdat.Measurement.read(data_directory / zilien_filename, reader="zilien")
        axes_a = full_data.plot_measurement(tspan=[0, 10000])
        full_plot = axes_a[0].get_figure()
        if SAVE_FIGURES is True:
            full_plot.savefig("./" + EXP_NAME + "full_experiment" + FIGURE_TYPE)
        full_data.export("./" + EXP_NAME + ".csv")

    elif DATA_SOURCE == "raw_plus":  # option 1: import MS data from Zilien data file
        # and EC data from biologic files
        print(data_directory / zilien_filename)
        full_data_zilien = ixdat.Measurement.read(
            data_directory / zilien_filename, reader="zilien")
        cvs_ec_only = ixdat.Measurement.read(
            data_directory / biologic_filename_cv, reader="biologic")
        cps_ec_only = ixdat.Measurement.read(
            data_directory / biologic_filename_cp, reader="biologic")
        # These two lines get rid of the EC data from the zilien-read file,
        # since we will use the EC data from the biologic file instead.
        full_data_zilien.replace_series("Ewe/V", None)
        full_data_zilien.replace_series("I/mA", None)
        full_data = full_data_zilien + cvs_ec_only + cps_ec_only
        axes_a = full_data.plot_measurement(tspan=[0, 10000])
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

    if WHICH_PART == "plot_CVs":  # plot the CV part
        cvs = full_data.cut(tspan=[1600, 2800])
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
            data_directory / biologic_filename_cv, reader="biologic")
        cvs_ec_only = cvs_ec_only.as_cv()
        cvs_ec_only.redefine_cycle(start_potential=0.9, redox=True)
        axes_c = cvs_ec_only[3].plot_vs_potential()
        cvs_ec_vs_pot = axes_c.get_figure()
        if SAVE_FIGURES is True:
            cvs_ec_vs_pot.savefig(
                "./" + EXP_NAME + "CV_vs_potential_EC_biologic" + FIGURE_TYPE)

    elif WHICH_PART == "plot+cal_HER":
        cps = full_data.cut(tspan=cp_tspan)
        # cps.tstamp += 2594
        axes_c = cps.plot_measurement(mass_list=["M2"])
        HER_cal = cps.ecms_calibration_curve(
            "H2", "M2", -2, tspan_list=cp_tspan_list, tspan_bg=cp_bg, ax="new",
            axes_measurement=axes_c, return_axes=True)
        print("HER calibration factor F= {:.3f}".format(HER_cal[0].F))
        HER_cal[1].annotate("F = {:.3f}".format(HER_cal[0].F),
                            (0.2, 0.8), xycoords="subfigure fraction")

        cps_vs_time = axes_c[0].get_figure()
        if SAVE_FIGURES is True:
            cps_vs_time.savefig("./" + EXP_NAME + "HER_CPs" + FIGURE_TYPE)
        her_cal_curve = HER_cal[1].get_figure()
        if SAVE_FIGURES is True:
            her_cal_curve.savefig("./" + EXP_NAME + "HER_cal_curve" + FIGURE_TYPE)

        return HER_cal[0]

    elif WHICH_PART == "plot+cal_OER":
        cps = full_data.cut(tspan=cp_tspan)
        # cps.tstamp += 2594
        axes_c = cps.plot_measurement(mass_list=["M32"])
        OER_cal = cps.ecms_calibration_curve(
            "O2", "M32", 4, tspan_list=cp_tspan_list, tspan_bg=cp_bg, ax="new",
            axes_measurement=axes_c, return_axes=True)
        print("OER calibration factor F= {:.3f}".format(OER_cal[0].F))
        OER_cal[1].annotate("F = {:.3f}".format(OER_cal[0].F),
                            (0.2, 0.8), xycoords="subfigure fraction")

        cps_vs_time = axes_c[0].get_figure()
        if SAVE_FIGURES is True:
            cps_vs_time.savefig("./" + EXP_NAME + "OER_CPs" + FIGURE_TYPE)
        oer_cal_curve = OER_cal[1].get_figure()
        if SAVE_FIGURES is True:
            oer_cal_curve.savefig("./" + EXP_NAME + "OER_cal_curve" + FIGURE_TYPE)

        return OER_cal[0]

    else:
        raise NameError("WHICH_PART not recognized.")


# if __name__ == "__main__":
#     main()

# full_data_list = []
h2_F_list = []

for file in file_dict:
    EXP_NAME = file
    data_directory = PARENT_PATH / file_dict[file]["DIR"]
    zilien_filename = file_dict[file]["ZIL"]
    biologic_filename_cv = file_dict[file]["CV"]
    biologic_filename_cp = file_dict[file]["CP"]
    cp_tspan = file_dict[file]["cp_tspan"]
    cp_tspan_list = file_dict[file]["tspan_list"]
    cp_bg = file_dict[file]["tspan_bg"]
    # full_data_list.append(main())
    h2_F_list.append(main())
    h2_F_list.append(main())
