import pywt
import glob
import time

import pandas as pd
from tqdm import tqdm

def compute_dwt(df, wavelet='db4', mode='per', level=None, columns=[]):
    list_of_dwt = list()
    
    for col in columns:
        col = df[col]
        col_list = col.tolist()
        
        if level is None:
            level = pywt.dwt_max_level(len(col_list), wavelet)

        coeffs = pywt.wavedec(col_list, wavelet, level=level, mode=mode)
        dwt_col = pywt.coeffs_to_array(coeffs)
        dwt_col_list = dwt_col[0]
        list_of_dwt.append(dwt_col_list)
    
    return list_of_dwt

def convert_to_coeff_arrays(coeffs, sz, wavelet='db4', mode='per', level=None):
    if level is None:
        level = pywt.dwt_max_level(sz, wavelet)

    dummy_vinn = [i for i in range(0, sz)]
    coeffs_dummy_vinn = pywt.wavedec(dummy_vinn, wavelet, level=level, mode=mode)
    dwt_coeff_slices = pywt.coeffs_to_array(coeffs_dummy_vinn)[1]
    
    res = pywt.array_to_coeffs(coeffs, dwt_coeff_slices, output_format='wavedec')
    return res

def load_dwt(file_path, export, dwt_columns=['vdd', 'xpd', 'pd', 'vinp', 'vinn'], usecols=['process', 'temperature']):
    start = time.time()

    new_df = pd.DataFrame()
    t1 = glob.glob(file_path + "\\*.csv")
    
    for file in tqdm(t1, desc=f"Generating DWT Coefficients for {len(t1)} files"):
        volts = float(file.split('_')[1][:-1])
        
        filename = file.replace(file_path, "")

        df = pd.read_csv(file, usecols=usecols)

        # dwt_vinn, dwt_vdd, dwt_xpd, dwt_pd, dwt_vinp = compute_dwt(df, columns=dwt_columns)
        # Don't change the order!
        # new_df['vdd'] = dwt_vdd
        # new_df['xpd'] = dwt_xpd
        # new_df['pd'] = dwt_pd
        # new_df['vinp'] = dwt_vinp
        # new_df['vinn'] = dwt_vinn
        
        # Don't change the order!
        dwt_values = compute_dwt(df, columns=dwt_columns)
        for index, column in enumerate(dwt_columns):
            new_df[column] = dwt_values[index]
        
        new_df['process'] = df['process'][0]
        new_df['temperature'] = df['temperature'][0]
        new_df['volts'] = volts
        
        new_df.to_csv(export + '\\' + filename)

    end = time.time()
    print(f"DWT computed in {end - start} seconds")
    return