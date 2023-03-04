import os
import glob

import pandas as pd
import matplotlib.pyplot as plt

from tqdm import tqdm

from setup import config

def draw(actual_values, pred_values, title, file_name, xlabel, ylabel, legend, show_only=False):
    X_time = [i for i in range(len(actual_values))]
    
    plt.figure(figsize=(16,9), facecolor='w', edgecolor='k')
    plt.plot(X_time, actual_values, color="red", linewidth=5, label=actual_values)
    plt.plot(X_time, pred_values, color="blue", linewidth=3, label=pred_values)
    
    plt.xlabel(xlabel, fontsize=10)
    plt.ylabel(ylabel, fontsize=10)

    plt.grid(True)
    plt.legend(legend, loc ="lower right")
    plt.title(title)
    
    if show_only:
        plt.show()
    else:
        path = os.path.join(config.RST_GRAPH, file_name)
        plt.savefig(path)

if __name__ == "__main__":
    t1 = glob.glob(os.path.join(config.PRED_DIR, "*.csv"))
    for file in tqdm(t1, desc="Plotting the waveforms!"):
        title = os.path.basename(file).replace('.csv', '')
        file_name = '{}-{}_{}_{}_{}.jpg'.format(title, config.ALGORITHM, config.TECHNIQUE, config.VARIANT, config.KIND)

        df = pd.read_csv(file)

        xlabel = "Time (ns) "
        ylabel = "vinn"
        legend = ["Actual vinn", "Predicted vinn"]

        draw(df["vinn"], df["pred_vinn"], title, file_name, xlabel, ylabel, legend)