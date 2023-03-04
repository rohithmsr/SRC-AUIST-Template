from setup import config, folders
from utils import wavelet_transform

folders.create_folders()
wavelet_transform.load_dwt(
    config.TRAIN_SET_PATH, 
    config.VINN_FILES_TRAIN, 
    dwt_columns=['vdd', 'xpd', 'pd', 'vinp', 'vinn'],
    usecols=['process', 'temperature', 'vinn', 'vdd', 'xpd', 'pd', 'vinp']
)