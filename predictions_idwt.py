import os
import glob

import pandas as pd

from tqdm import tqdm

from setup import config
from utils import wavelet_transform

def predict_idwt(test_row, file_location):
    y_pred = test_row['predicted vinn']
    coeffs = wavelet_transform.convert_to_coeff_arrays(y_pred, 15000)

    pred_vinn = wavelet_transform.idwt(coeffs, wavelet='db4', mode='per')
    pred_vinn = pd.Series(pred_vinn)
    
    # Store results in df
    df_result = pd.DataFrame()
    df_result["time"] = test_row['Time']
    # df_result["vinn"] = vinn
#     df_result["pred_vinn_dwt"] = y_pred[0]
    df_result["pred_vinn"] = pred_vinn

    file_name = os.path.basename(file_location)
    pred_file = file_name
    df_result.to_csv('{}/{}'.format(config.IDWT_PRED_DIR, pred_file), index = False)
    
    return df_result

if __name__ == '__main__':
    t1 = glob.glob(os.path.join(config.IDWT_RESULTS_PATH, "*.csv"))
    for file in tqdm(t1, desc=f"Generating time-domain values for {len(t1)} test files"):
        test_df = pd.read_csv(file)
        pred_df = predict_idwt(test_df, file)