import os
import glob

import pandas as pd
import matplotlib.pyplot as plt

from setup import config

def bar_plot(df, metric, color):
    plt.bar(df['File name'], df[metric], width = 0.45, color = color)
    plt.ylabel(metric)
    plt.xlabel('Test conditions')
    plt.xticks(rotation=75)
    plt.rc('font', size=10) 
    ax = plt.gca()
    ax.tick_params(which='major', labelsize=10)

    plt.title("Metrics - RF & DWT - {} - {}".format(config.VARIANT, config.KIND))
    name =  metric + ".jpg"
    path = os.path.join(config.METRICS_GRAPH,name)
    plt.savefig(path, bbox_inches='tight')
    plt.show()

if __name__ == '__main__':
    t1 = glob.glob(os.path.join(config.METRICS_DIR, "*.csv"))
    metrics_results = pd.read_csv(t1[0])

    bar_plot(metrics_results, 'MAE', '#18A558')
    bar_plot(metrics_results, 'RMSE', '#DB1F48')
    bar_plot(metrics_results, 'R2', '#A45C40')
    bar_plot(metrics_results, 'SNR', '#FAD02C')