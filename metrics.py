import math
import os
import glob

import pandas as pd

from sklearn.metrics import mean_squared_error, r2_score, mean_absolute_error
from tqdm import tqdm

from setup import config

def SNR(y, y_pred):
    n = len(y)
    upper = 0
    lower = 0
    for ind in range(0,n):
        out = y.iloc[ind]
        pred_out = y_pred.iloc[ind]
        upper += (out ** 2)
        lower += (out - pred_out) ** 2
        
    snr = 10 * math.log10(upper / lower)
    return snr

def compute_metrics(values, pred_values, file_name):
    # Metrics using values & pred_values
    mae = mean_absolute_error(values, pred_values)
    mse = mean_squared_error(values, pred_values)
    rmse = math.sqrt(mse)
    r2 = r2_score(values, pred_values)
    snr = SNR(values, pred_values)

    metrics_format = {
        'File name': file_name, 
        'RMSE': round(rmse, 4), 
        'MSE': round(mse, 4), 
        'MAE': round(mae, 4), 
        'R2': round(r2, 4), 
        'SNR': round(snr, 4)
    }

    return metrics_format
    
metrics = []

t1 = glob.glob(os.path.join(config.PRED_DIR, "*.csv"))
for file in tqdm(t1, desc=f"Finding metrics for the {len(t1)} test files"):
    file_name = os.path.basename(file)
    df = pd.read_csv(file)

    result = compute_metrics(df['vinn'], df['pred_vinn'], file_name)
    metrics.append(result)

metrics_df = pd.DataFrame.from_dict(metrics)
metrics_df.to_csv(os.path.join(config.METRICS_DIR, config.METRIC_FILE), index = False)
print(metrics_df)