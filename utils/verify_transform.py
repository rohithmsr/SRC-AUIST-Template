import os

import pandas as pd

from visualize import draw
from setup import config
from utils import wavelet_transform

def plot_verify(column, file_name):
    actual_df = pd.read_csv(os.path.join(config.TEST_SET_PATH, file_name), usecols=[column])
    coeff_df = pd.read_csv(os.path.join(config.VINN_FILES_TEST, file_name), usecols=[column])
    values_list = coeff_df[column].tolist()

    coeffs = wavelet_transform.convert_to_coeff_arrays(values_list, len(actual_df))
    pred_values = wavelet_transform.idwt(coeffs, wavelet='db4', mode='per')

    title = f"{column} verification of transform"
    file_name = title
    xlabel = "Time (ns) "
    ylabel = column
    legend = ["Actual vinn", "IDWT to Time vinn"]

    draw(actual_df[column], pred_values, title, file_name, xlabel, ylabel, legend, show_only=True)