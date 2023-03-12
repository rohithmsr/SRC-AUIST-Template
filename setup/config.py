import os

ALGORITHM = 'rf'
TECHNIQUE = 'dwt'
VARIANT = 'sine 750 mv'
KIND = 'all-cols'
REGION = 'fall'

TRAIN_SET_PATH = "D:\\Final Year Project\\Play with DWT\\Sine\\dataset\\{}\\train".format(VARIANT)
TEST_SET_PATH = "D:\\Final Year Project\\Play with DWT\\Sine\\dataset\\{}\\test".format(VARIANT)

REGIONS = ["rise1", "rise2", "rise3", "functional", "fall"]
SPLIT_FILES_TRAIN_DIR = os.path.join('split', 'train', VARIANT)
SPLIT_FILES_TEST_DIR = os.path.join('split', 'test', VARIANT)
SPLIT_TRAIN_SET_PATH = "D:\\Final Year Project\\Play with DWT\\Sine\\SRC-AnnaUniv-Template\\split\\train\\{}".format(VARIANT)
SPLIT_TEST_SET_PATH = "D:\\Final Year Project\\Play with DWT\\Sine\\SRC-AnnaUniv-Template\\split\\test\\{}".format(VARIANT)

PRED_DIR = os.path.join('predictions', VARIANT, REGION)

ASSETS_DIR = 'assets'
METRICS_DIR = 'metrics'
METRIC_FILE ='{}_{}_{}-{}-{}.csv'.format(ALGORITHM, TECHNIQUE, VARIANT, KIND, REGION)

RST_GRAPH = os.path.join('graphs', 'outputs', VARIANT, REGION)
METRICS_GRAPH = os.path.join('graphs', 'metrics', VARIANT, REGION)

VINN_FILES_TRAIN = os.path.join('transformed_dataset', 'train', VARIANT)
VINN_FILES_TEST = os.path.join('transformed_dataset', 'test', VARIANT)

SPLIT_VINN_FILES_TRAIN = os.path.join('split', 'transformed_dataset', 'train', VARIANT)
SPLIT_VINN_FILES_TEST = os.path.join('split', 'transformed_dataset', 'test', VARIANT)

MODEL_NAME = "model_{}_{}_{}_{}_{}.pkl".format(ALGORITHM, TECHNIQUE, VARIANT, KIND, REGION)
SCALER_NAME = "scaler_{}_{}_{}_{}_{}.pkl".format(ALGORITHM, TECHNIQUE, VARIANT, KIND, REGION)
ENCODER_NAME = "encoder_{}_{}_{}_{}_{}.pkl".format(ALGORITHM, TECHNIQUE, VARIANT, KIND, REGION)

MODEL_PATH = os.path.join('assets', MODEL_NAME)
SCALER_PATH = os.path.join('assets', SCALER_NAME)
ENCODER_PATH = os.path.join('assets', ENCODER_NAME)
