from setup import config, folders
from utils import dwt

folders.create_folders()
dwt.load_dwt(config.TRAIN_SET_PATH, config.VINN_FILES_TRAIN)