import math

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