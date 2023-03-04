import pandas as pd
import glob

def create_combined_dataframe(files_path):
    train_files = glob.glob(files_path + "\\*.csv")
    df_list = (pd.read_csv(file) for file in train_files)

    # Concatenate all DataFrames
    df = pd.concat(df_list, ignore_index=True)
    df.rename(columns = {'Unnamed: 0':'itime'}, inplace = True)

    return df