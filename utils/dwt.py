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

def load_dwt(file_path, export):
    start = time.time()

    new_df = pd.DataFrame()
    t1 = glob.glob(file_path + "\\*.csv")
    
    for file in tqdm(t1, desc=f"Generating DWT Coefficients for {len(t1)} files"):
        volts = float(file.split('_')[1][:-1])
        
        filename = file.replace(file_path, "")

        df = pd.read_csv(file, usecols = ['process', 'temperature', 'vinn', 'vdd', 'xpd', 'pd', 'vinp'])
        dwt_vinn, dwt_vdd, dwt_xpd, dwt_pd, dwt_vinp = compute_dwt(df, columns = ['vinn', 'vdd', 'xpd', 'pd', 'vinp'])
        
        # Don't change the order!
        new_df['vdd'] = dwt_vdd
        new_df['xpd'] = dwt_xpd
        new_df['pd'] = dwt_pd
        new_df['vinp'] = dwt_vinp
        new_df['vinn'] = dwt_vinn
        
        new_df['process'] = df['process'][0]
        new_df['temperature'] = df['temperature'][0]
        new_df['volts'] = volts
        
        new_df.to_csv(export + '\\' + filename)

    end = time.time()
    print(f"DWT computed in {end - start} seconds")
    return