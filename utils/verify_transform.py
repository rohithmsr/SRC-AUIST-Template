import os

import pandas as pd

from visualize import draw
from setup import config
from utils import wavelet_transform

def plot_verify(column, file_name, original_dir, transformed_dir):
    actual_df = pd.read_csv(os.path.join(original_dir, file_name), usecols=[column])
    coeff_df = pd.read_csv(os.path.join(transformed_dir, file_name), usecols=[column])
    values_list = coeff_df[column].tolist()

    coeffs = wavelet_transform.convert_to_coeff_arrays(values_list, len(actual_df))
    pred_values = wavelet_transform.idwt(coeffs, wavelet='db4', mode='per')
    pred_values = pred_values[:len(actual_df)]

    print(len(actual_df), len(pred_values))

    title = f"{column} verification of transform"
    file_name = title
    xlabel = "Time (ns) "
    ylabel = column
    legend = ["Actual vinn", "IDWT to Time vinn"]

    draw(actual_df[column], pred_values, title, file_name, xlabel, ylabel, legend, show_only=True)