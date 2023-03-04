import os

ALGORITHM = 'rf'
TECHNIQUE = 'dwt'
VARIANT = 'sine 250 mv'
KIND = 'all-cols'

PRED_DIR = os.path.join('predictions', VARIANT)

METRICS_DIR = 'metrics'
METRIC_FILE ='{}_{}_{}-{}.csv'.format(ALGORITHM, TECHNIQUE, VARIANT, KIND)

RST_GRAPH = os.path.join('graphs', 'outputs', VARIANT)
METRICS_GRAPH = os.path.join('graphs', 'metrics', VARIANT)

VINN_FILES_TRAIN = os.path.join('transformed_dataset', 'train', VARIANT)
VINN_FILES_TEST = os.path.join('transformed_dataset', 'test', VARIANT)

