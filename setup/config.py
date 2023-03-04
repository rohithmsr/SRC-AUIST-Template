import os

ALGORITHM = 'rf'
TECHNIQUE = 'dwt'
VARIANT = 'sine 250 mv'
KIND = 'all-cols'

TRAIN_SET_PATH = "D:\\Final Year Project\\Play with DWT\\Sine\\dataset\\{}\\train".format(VARIANT)
TEST_SET_PATH = "D:\\Final Year Project\\Play with DWT\\Sine\\dataset\\{}\\test".format(VARIANT)

PRED_DIR = os.path.join('predictions', VARIANT)

ASSETS_DIR = 'assets'
METRICS_DIR = 'metrics'
METRIC_FILE ='{}_{}_{}-{}.csv'.format(ALGORITHM, TECHNIQUE, VARIANT, KIND)

RST_GRAPH = os.path.join('graphs', 'outputs', VARIANT)
METRICS_GRAPH = os.path.join('graphs', 'metrics', VARIANT)

VINN_FILES_TRAIN = os.path.join('transformed_dataset', 'train', VARIANT)
VINN_FILES_TEST = os.path.join('transformed_dataset', 'test', VARIANT)

MODEL_NAME = "model_{}_{}_{}_{}.pkl".format(ALGORITHM, TECHNIQUE, VARIANT, KIND)
SCALER_NAME = "scaler_{}_{}_{}_{}.pkl".format(ALGORITHM, TECHNIQUE, VARIANT, KIND)
ENCODER_NAME = "encoder_{}_{}_{}_{}.pkl".format(ALGORITHM, TECHNIQUE, VARIANT, KIND)

MODEL_PATH = os.path.join('assets', MODEL_NAME)
SCALER_PATH = os.path.join('assets', SCALER_NAME)
ENCODER_PATH = os.path.join('assets', ENCODER_NAME)
