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
DATA_SOURCE = "ixdat"
# DATA_SOURCE can be "raw" (for importing EC and MS data from Zilien .tsv file),
# or "ixdat" (for importing ixdat .csv files)
# in either case, for plotting the CV only, the biologic CVA file is imported
# automatically
WHICH_PART = "plot+cal_OER"
# WHICH_PART can be "import_only", "plot_CVs", "plot+cal_HER", "plot+cal_OER"

SAVE_FIGURES = True
# SAVE_FIGURES set to True: figures will be saved automatically.
FIGURE_TYPE = ".png"
# FIGURE_TYPE can be any format matplotlib accepts for saving figures, eg.
# ".png", ".svg", ".pdf" etc.

# select the directory of the raw data.
EXP_NAME = "HERonPt_RnD1_oldMS"
THIS_DIR = Path(__file__).parents[1].resolve()
data_directory = Path(
    r"C:\Users\AnnaWiniwarter\Dropbox (Spectro Inlets)\Development\Data\Quantification Application Note\HER on Pt repeatability")
PARENT_DIR = Path(
    r"C:\Users\AnnaWiniwarter\Dropbox (Spectro Inlets)\Development\Data\Quantification Application Note")

# select the filenames of the raw data.
zilien_filename = "2022-03-16 10_41_29 HER_on_Pt_repeatability_test_1.tsv"
biologic_filename_cv = "2022-03-16 10_41_29 HER_on_Pt_repeatability_test_1_04_01_CVA_DUSB0_C01.mpt"
biologic_filename_cp = "2022-03-16 10_41_29 HER_on_Pt_repeatability_test_1_04_02_CP_DUSB0_C01.mpt"

file_dict_HER = {"HERonPt_RnD1_oldMS": {"DIR": r"HER on Pt repeatability\2022-03-16 10_41_29 HER_on_Pt_repeatability_test_1",
                                        "ZIL": "2022-03-16 10_41_29 HER_on_Pt_repeatability_test_1.tsv",
                                        "CV": "2022-03-16 10_41_29 HER_on_Pt_repeatability_test_1_04_01_CVA_DUSB0_C01.mpt",
                                        "CP": "2022-03-16 10_41_29 HER_on_Pt_repeatability_test_1_04_02_CP_DUSB0_C01.mpt",
                                        "cp_tspan": [2600, 6000],
                                        "tspan_list": [[3142, 3192], [3672, 3787], [4263, 4389], [4862, 4992], [5471, 5590]],
                                        "tspan_bg": [4494, 4657], },
                 "HERonPt_RnD1_2ndMS": {"DIR": r"HER on Pt repeatability\2022-03-30 10_39_47 HER on Pt repeatability",
                                        "ZIL": r"2022-03-30 10_39_47 HER on Pt repeatability.tsv",
                                        "CV": "2022-03-30 10_39_47 HER on Pt repeatability_05_01_CVA_DUSB0_C01.mpt",
                                        "CP": "2022-03-30 10_39_47 HER on Pt repeatability_05_02_CP_DUSB0_C01.mpt",
                                        "cp_tspan": [4086, 7132],
                                        "tspan_list": [[4361, 4446], [4937, 5044], [5524, 5645], [6122, 6246], [6719, 6847]],
                                        "tspan_bg": [4503, 4708], },
                 "HERonPt_RnD1_2ndMS_2": {"DIR": r"HER on Pt repeatability\2022-03-30 14_15_06 HER on Pt repeatability",
                                          "ZIL": "2022-03-30 14_15_06 HER on Pt repeatability.tsv",
                                          "CV": "2022-03-30 14_15_06 HER on Pt repeatability_01_01_CVA_DUSB0_C01.mpt",
                                          "CP": "2022-03-30 14_15_06 HER on Pt repeatability_01_02_CP_DUSB0_C01.mpt",
                                          "cp_tspan": [1210, 4490],
                                          "tspan_list": [[1686, 1755], [2258, 2353], [2839, 2954], [3427, 3543], [4033, 4141]],
                                          "tspan_bg": [1840, 2019], },
                 "HERonPt_RnD1_newMS": {"DIR": r"HER on Pt repeatability\2022-04-06 14_48_52 HER on Pt repeatability",
                                        "ZIL": "2022-04-06 14_48_52 HER on Pt repeatability.tsv",
                                        "CV": "2022-04-06 14_48_52 HER on Pt repeatability_03_01_CVA_DUSB0_C01.mpt",
                                        "CP": "2022-04-06 14_48_52 HER on Pt repeatability_03_02_CP_DUSB0_C01.mpt",
                                        "cp_tspan": [1639, 4916],
                                        # [2157, 2197],
                                        "tspan_list": [[2699, 2803], [3276, 3399], [3872, 4006], [4475, 4605]],
                                        "tspan_bg": [2272, 2482], },
                 "HERonPt_RnD1_newMS_2": {"DIR": r"HER on Pt repeatability\2022-04-07 11_53_00 HER on Pt repeatability",
                                          "ZIL": "2022-04-07 11_53_00 HER on Pt repeatability.tsv",
                                          "CV": "2022-04-07 11_53_00 HER on Pt repeatability_01_01_CVA_DUSB0_C01.mpt",
                                          "CP": "2022-04-07 11_53_00 HER on Pt repeatability_01_02_CP_DUSB0_C01.mpt",
                                          "cp_tspan": [599, 3840],
                                          "tspan_list": [[1047, 1128], [1608, 1725], [2191, 2329], [2803, 2926], [3474, 3520]],
                                          "tspan_bg": [1216, 1396], },
                 "HERonPt_RnD1_newMS_nonaqu": {"DIR": r"HER on Pt repeatability\2022-04-07 13_20_11 HER on Pt repeatability non-aqu",
                                               "ZIL": "2022-04-07 13_20_11 HER on Pt repeatability non-aqu.tsv",
                                               "CV": "2022-04-07 13_20_11 HER on Pt repeatability non-aqu_01_01_CVA_DUSB0_C01.mpt",
                                               "CP": "2022-04-07 13_20_11 HER on Pt repeatability non-aqu_01_02_CP_DUSB0_C01.mpt",
                                               "cp_tspan": [1379, 4738],
                                               "tspan_list": [[1859, 1955], [2425, 2553], [3023, 3151], [3617, 3745], [4215, 4357]],
                                               "tspan_bg": [2030, 2222], },
                 }

file_dict_OER = {"OERonPt_RnD1_2ndMS": {"DIR": r"OER on Pt repeatability\2022-03-30 12_51_35 OER on Pt repeatability",
                                        "ZIL": "2022-03-30 12_51_35 OER on Pt repeatability.tsv",
                                        "CV": "2022-03-30 12_51_35 OER on Pt repeatability_01_01_CVA_DUSB0_C01.mpt",
                                        "CP": "2022-03-30 12_51_35 OER on Pt repeatability_01_02_CP_DUSB0_C01.mpt",
                                        "cp_tspan": [1070, 4258],
                                        "tspan_list": [[1994, 2102], [2597, 2696], [3196, 3290], [3776, 3902]],
                                        "tspan_bg": [1684, 1792], },
                 "OERonPt_RnD1_newMS": {"DIR": r"OER on Pt repeatability\2022-04-07 10_10_27 OER on Pt repeatability",
                                        "ZIL": "2022-04-07 10_10_27 OER on Pt repeatability.tsv",
                                        "CV": "2022-04-07 10_10_27 OER on Pt repeatability_01_01_CVA_DUSB0_C01.mpt",
                                        "CP": "2022-04-07 10_10_27 OER on Pt repeatability_01_02_CP_DUSB0_C01.mpt",
                                        "cp_tspan": [1788, 5081],
                                        "tspan_list": [[2247, 2274], [2753, 2866], [3351, 3471], [3950, 4063], [4542, 4675]],
                                        "tspan_bg": [2333, 2560], },
                 "OERonPt_RnD1_newMS_nonaqu": {"DIR": r"OER on Pt repeatability\2022-04-07 14_39_29 OER on Pt repeatability non-aqu",
                                               "ZIL": "2022-04-07 14_39_29 OER on Pt repeatability non-aqu.tsv",
                                               "CV": "2022-04-07 14_39_29 OER on Pt repeatability non-aqu_02_01_CVA_DUSB0_C01.mpt",
                                               "CP": "2022-04-07 14_39_29 OER on Pt repeatability non-aqu_02_02_CP_DUSB0_C01.mpt",
                                               "cp_tspan": [1881, 5306],
                                               "tspan_list": [[2432, 2476], [2981, 3078], [3569, 3666], [4164, 4268], [4780, 4870]],
                                               "tspan_bg": [2552, 2760], },
                 }


# ----------------------- END OF EDIT SETTINGS --------

def main():
    if DATA_SOURCE == "raw":  # option 1: import both EC and MS data from Zilien data file
        print(data_directory / zilien_filename)
        full_data = ixdat.Measurement.read(data_directory / zilien_filename, reader="zilien")
        axes_a = full_data.plot_measurement(tspan=[0, 10000])
        full_plot = axes_a[0].get_figure()
        if SAVE_FIGURES is True:
            full_plot.savefig("./" + EXP_NAME + "full_experiment" + FIGURE_TYPE)
        full_data.export("./" + EXP_NAME + ".csv")

    elif DATA_SOURCE == "ixdat":  # option 2: import from ixdat-datafiles
        full_data = ixdat.Measurement.read("./" + EXP_NAME + ".csv", reader="ixdat")
        # axes_a = full_data.plot_measurement(tspan=[0,10000])
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
# h2_F_list=[]
o2_F_list = []

# for file in file_dict_HER:

file_dict = file_dict_OER

for file in file_dict:
    EXP_NAME = file
    data_directory = PARENT_DIR / file_dict[file]["DIR"]
    zilien_filename = file_dict[file]["ZIL"]
    biologic_filename_cv = file_dict[file]["CV"]
    biologic_filename_cp = file_dict[file]["CP"]
    cp_tspan = file_dict[file]["cp_tspan"]
    cp_tspan_list = file_dict[file]["tspan_list"]
    cp_bg = file_dict[file]["tspan_bg"]
    # full_data_list.append(main())
    # h2_F_list.append(main())
    o2_F_list.append(main())
