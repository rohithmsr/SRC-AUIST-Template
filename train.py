import os
import pandas as pd
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.ensemble import RandomForestRegressor
from pickle import dump

from setup import config
from utils import prepare_data

if __name__ == '__main__':
    df = prepare_data.create_combined_dataframe(os.path.join(config.SPLIT_VINN_FILES_TRAIN, config.REGION))
    # config.VINN_FILES_TRAIN
        
    features = ['vdd', 'xpd', 'pd', 'vinp','itime', 'process', 'temperature', 'volts']
    target = ['vinn']

    X = df[features]
    Y = df[target]

    num_col= prepare_data.generate_features(X, columns=['vdd', 'xpd', 'pd', 'vinp'])
    cat_col = prepare_data.generate_features(X, data_type='object')

    scaler = StandardScaler()
    num = pd.DataFrame(scaler.fit_transform(num_col))

    encoder = OneHotEncoder(categories=[['fastnfastp','slownfastp','typical','fastnslowp', 'slownslowp']])
    cat = pd.DataFrame(encoder.fit_transform(cat_col).toarray())

    X_train = pd.concat([num, df[['itime']], df[['temperature', 'volts']], cat], axis = 1)
    X_train.columns = ['vdd', 'xpd', 'pd', 'vinp', 'itime', 'temperature', 'volts', 'process_0', 'process_1', 'process_2', 'process_3', 'process_4']
    Y_train = Y

    print("Training.........")
    model = RandomForestRegressor(n_estimators = 10, max_depth = 10, random_state = 0)
    model.fit(X_train, Y_train)

    dump(model, open(config.MODEL_PATH, 'wb'))
    print("MODEL_SAVED")

    dump(scaler, open(config.SCALER_PATH, 'wb'))
    print("SCALER_SAVED")

    dump(encoder, open(config.ENCODER_PATH, 'wb'))
    print("ENCODER_SAVED")

