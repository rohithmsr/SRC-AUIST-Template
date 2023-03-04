import os

KIND = 'all-cols'
VARIANT = 'sine 250 mv'

PRED_DIR = os.path.join('predictions', VARIANT)
METRICS_DIR = 'metrics'

RST_GRAPH = os.path.join('graphs', 'outputs', VARIANT)
METRICS_GRAPH = os.path.join('graphs', 'metrics', VARIANT)

VINN_FILES_TRAIN = os.path.join('transformed_dataset', 'train', VARIANT)
VINN_FILES_TEST = os.path.join('transformed_dataset', 'test', VARIANT)