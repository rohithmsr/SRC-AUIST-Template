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
    t2 = glob.glob(os.path.join(config.IDWT_PRED_DIR, "*.csv"))
    index = 0
    for file in tqdm(t1, desc="Plotting the waveforms!"):
        title = os.path.basename(file).replace('.csv', '')
        file_name = 'z2-{}-{}_{}_{}_{}.jpg'.format(title, 'idwt-plot', config.TECHNIQUE, config.VARIANT, config.KIND)

        df = pd.read_csv(file)
        df2 = pd.read_csv(t2[index])
        df2 = df2.head(len(df))

        xlabel = "Time (ns) "
        ylabel = "vinn"
        legend = ["Actual vinn", "Predicted vinn"]
        index += 1

        draw(df["vinn"], df2["pred_vinn"], title, file_name, xlabel, ylabel, legend)