import os
import glob
import pickle

import pandas as pd

from tqdm import tqdm

from setup import config
from utils import prepare_data, wavelet_transform

def predict(test_row, file_location):
    # Get input features of test  
    test_row.rename(columns = {'Unnamed: 0':'itime'}, inplace = True)

    num_col= prepare_data.generate_features(test_row, columns=['vdd', 'xpd', 'pd', 'vinp'])
    cat_col = prepare_data.generate_features(test_row, data_type='object')

    scaler = pickle.load(open(config.SCALER_PATH, 'rb'))
    encoder = pickle.load(open(config.ENCODER_PATH, 'rb'))

    num = pd.DataFrame(scaler.transform(num_col))
    cat = pd.DataFrame(encoder.transform(cat_col).toarray())
    
    X_test = pd.concat([num, test_row[['itime', 'temperature', 'volts']], cat], axis = 1)
    X_test.columns = ['vdd', 'xpd', 'pd', 'vinp', 'itime', 'temperature', 'volts', 'process_0', 'process_1', 'process_2', 'process_3', 'process_4']
    
    # Get the actual vinn values of the file
    # test_file_path = config.TEST_SET_PATH
    test_file_path = os.path.join(config.SPLIT_TEST_SET_PATH, config.REGION)
    file_name = os.path.basename(file_location)
    file_path = os.path.join(test_file_path, file_name)
    
    file_df = pd.read_csv(file_path, usecols=['time', 'vinn'])

    time = file_df['time']
    vinn = file_df['vinn'] #y_test
    
    # Find the predicted vinn using IDWT
    model = pickle.load(open(config.MODEL_PATH, 'rb'))
    y_pred = model.predict(X_test)
    coeffs = wavelet_transform.convert_to_coeff_arrays(y_pred, len(vinn))

    pred_vinn = wavelet_transform.idwt(coeffs, wavelet='db4', mode='per')
    pred_vinn = pred_vinn[:len(vinn)]
    pred_vinn = pd.Series(pred_vinn)
    
    # Store results in df
    df_result = pd.DataFrame()
    df_result["time"] = time
    df_result["vinn"] = vinn
#     df_result["pred_vinn_dwt"] = y_pred[0]
    df_result["pred_vinn"] = pred_vinn

    pred_file = file_name
    df_result.to_csv('{}/{}'.format(config.PRED_DIR, pred_file), index = False)
    
    return df_result

if __name__ == '__main__':
    t1 = glob.glob(os.path.join(config.SPLIT_VINN_FILES_TEST, config.REGION, "*.csv"))
    for file in tqdm(t1, desc=f"Generating predictions for {len(t1)} test files"):
        test_df = pd.read_csv(file)
        pred_df = predict(test_df, file)