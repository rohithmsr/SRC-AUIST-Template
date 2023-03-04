
def generate_features(X, columns=None, data_type=None):
    if columns is None:
        columns = list(X.select_dtypes(data_type).columns)
    else:
        columns = list(X[columns])

    return X[columns]