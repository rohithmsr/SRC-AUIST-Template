import os
from utils import config

def create_folders():
    if not os.path.exists(config.PRED_DIR):
        os.makedirs(config.PRED_DIR)

    if not os.path.exists(config.METRICS_DIR):
        os.makedirs(config.METRICS_DIR)

    if not os.path.exists(config.METRICS_GRAPH):
        os.makedirs(config.METRICS_GRAPH)

    if not os.path.exists(config.RST_GRAPH):
        os.makedirs(config.RST_GRAPH)

    if not os.path.exists(config.VINN_FILES_TRAIN):
        os.makedirs(config.VINN_FILES_TRAIN)

    if not os.path.exists(config.VINN_FILES_TEST):
        os.makedirs(config.VINN_FILES_TEST)