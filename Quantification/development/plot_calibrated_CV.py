# -*- coding: utf-8 -*-
"""
Created on Thu Jul 21 11:40:48 2022

@author: AnnaWiniwarter
"""
import ixdat
import matplotlib
from ixdat.techniques import MSMeasurement
from ixdat.techniques.ec_ms import ECMSCalibration
from ixdat.techniques.ms import MSCalResult
from pathlib import Path

# change the fontsize for all figures
font = {"family": "normal", "weight": "normal", "size": 14}
matplotlib.rc("font", **font)

data_directory = (
    Path.home()
    / r"C:\Users\AnnaWiniwarter\Spectro Inlets Dropbox\02 EC-MS\2.1 Development projects\0.0 Raw Data\Quantification Application Note\application note data\2022-07-19 10_02_32 AIO_HER_OER_2021bW2D3"
)

full_data_zilien = ixdat.Measurement.read(
    data_directory / "2022-07-19 10_02_32 AIO_HER_OER_2021bW2D3.tsv",
    reader="zilien",
    technique="MS",
)
cvs_ec_only_her = ixdat.Measurement.read(
    data_directory
    / "2022-07-19 10_02_32 AIO_HER_OER_2021bW2D3_01_01_CVA_DUSB0_C01.mpt",
    reader="biologic",
)
cps_ec_only_her = ixdat.Measurement.read(
    data_directory / "2022-07-19 10_02_32 AIO_HER_OER_2021bW2D3_01_02_CP_DUSB0_C01.mpt",
    reader="biologic",
)
cvs_ec_only_oer = ixdat.Measurement.read(
    data_directory
    / "2022-07-19 10_02_32 AIO_HER_OER_2021bW2D3_01_03_CVA_DUSB0_C01.mpt",
    reader="biologic",
)
cps_ec_only_oer = ixdat.Measurement.read(
    data_directory / "2022-07-19 10_02_32 AIO_HER_OER_2021bW2D3_01_04_CP_DUSB0_C01.mpt",
    reader="biologic",
)


# These two lines get rid of the EC data from the zilien-read file,
# since we will use the EC data from the biologic file instead.
full_data_zilien.replace_series("Ewe/V", None)
full_data_zilien.replace_series("I/mA", None)
# full_data_zilien.replace_series("Potential time [s]", None)
full_data = (
    full_data_zilien
    + cvs_ec_only_her
    + cps_ec_only_her
    + cvs_ec_only_oer
    + cps_ec_only_oer
)
axes_a = full_data.plot_measurement(tspan=[0, 100000])
full_plot = axes_a[0].get_figure()
full_plot.tight_layout(pad=0.3)
full_plot.savefig("./" + "AIO_HER_OER_full_experiment.png")
full_data.export("./" + "AIO_HER_OER_full_experiment.csv")

# select and plot one of the CV(sequences) recorded between the calibration sequences
cv_sequence = full_data.cut(tspan=[4944, 5800]).as_cv()
cv_sequence.redefine_cycle(start_potential=0.9, redox=True)
axes_b = cv_sequence.plot_measurement()
cvs_vs_time = axes_b[0].get_figure()
cvs_vs_time.tight_layout(pad=0.3)
# cvs_vs_time.savefig("./AIO_HER_OER_CV_vs_time_uncalibrated.png")
# plot one of the CVs (the 2nd out of 5) vs potential.
axes_c = cv_sequence[2].plot_vs_potential(logplot=True)
cvs_vs_pot = axes_c[0].get_figure()
cvs_vs_pot.tight_layout(pad=0.3)
# cvs_vs_pot.savefig("./AIO_HER_OER_CV_vs_potential_uncalibrated.png")

cv_sequence.calibrate(RE_vs_RHE=0, A_el=0.196)
axes_b2 = cv_sequence[2].plot_vs_potential(
    mass_lists=[[], ["M2", "M32"]],
    tspan_bg=[[], [5125, 5135]],
    linestyle=":",
    logplot=False,
    legend=False,
)

# calibrate O2 from first OER and H2 from first HER sequence
# TODO: ACTUALLY ADD THE CODE HERE INSTEAD OF JUST DEFINING CAL

OER_cal = MSCalResult(
    name="O2_OER_faraday", mol="O2", mass="M32", cal_type="ec_ms", F=0.105
)

HER_cal = MSCalResult(
    name="H2_HER_faraday", mol="H2", mass="M2", cal_type="ec_ms", F=0.335
)

# use the calibration to calibrate the data of the above CV sequence
cv_sequence.calibrate(ms_cal_results=[OER_cal, HER_cal], RE_vs_RHE=0, A_el=0.196)
# cv_sequence.calibrate(RE_vs_RHE=0, A_el=0.196)
axes_d = cv_sequence.plot_measurement(
    mol_list=["O2", "H2"], tspan_bg=[4950, 4970], logplot=False, unit="pmol/s"
)
cvs_vs_time = axes_d[0].get_figure()
cvs_vs_time.tight_layout(pad=0.3)
# cvs_vs_time.savefig("./AIO_HER_OER_CV_vs_time_calibrated.png")
# plot one of the CVs (the 2nd out of 5) vs potential.
axes_e = cv_sequence[2].plot_vs_potential(
    mol_list=["O2", "H2"], tspan_bg=[5125, 5135], logplot=False, unit="pmol/s"
)
cvs_vs_pot = axes_e[0].get_figure()
cvs_vs_pot.tight_layout(pad=0.3)
# cvs_vs_pot.savefig("./AIO_HER_OER_CV_vs_potential_calibrated.png")

# plot one of the CVs (the 2nd out of 5) vs potential both cal& uncalibrated
axes_e = cv_sequence[2].plot_vs_potential(
    mol_list=["O2", "H2"],
    tspan_bg=[5125, 5135],
    logplot=False,
    unit="pmol/s",
    axes=axes_b2,
    legend=False,
)
cvs_vs_pot = axes_e[0].get_figure()
cvs_vs_pot.tight_layout(pad=0.3)
# cvs_vs_pot.savefig("./AIO_HER_OER_CV_vs_potential_calibrated.png")
# cvs_vs_pot.savefig("./AIO_HER_OER_CV_vs_potential_uncal+calibrated.svg")
