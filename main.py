import os
from setup import config, folders
from utils import wavelet_transform, verify_transform, split_regions

if __name__ == '__main__':
    folders.create_folders()

    # split_regions.split(config.TRAIN_SET_PATH, config.SPLIT_TRAIN_SET_PATH)
    # split_regions.split(config.TEST_SET_PATH, config.SPLIT_TEST_SET_PATH)

    # for region in config.REGIONS:
    #     wavelet_transform.load_dwt(
    #         os.path.join(config.SPLIT_TRAIN_SET_PATH, region), 
    #         os.path.join(config.SPLIT_VINN_FILES_TRAIN, region), 
    #         dwt_columns=['vdd', 'xpd', 'pd', 'vinp', 'vinn'],
    #         usecols=['process', 'temperature', 'vinn', 'vdd', 'xpd', 'pd', 'vinp']
    #     )

    #     wavelet_transform.load_dwt(
    #         os.path.join(config.SPLIT_TEST_SET_PATH, region), 
    #         os.path.join(config.SPLIT_VINN_FILES_TEST, region), 
    #         dwt_columns=['vdd', 'xpd', 'pd', 'vinp', 'vinn'],
    #         usecols=['process', 'temperature', 'vinn', 'vdd', 'xpd', 'pd', 'vinp']
    #     )

    #     verify_transform.plot_verify(
    #         'vinn', 
    #         'typical_3.3V_-15.csv', 
    #         os.path.join(config.SPLIT_TRAIN_SET_PATH, region), 
    #         os.path.join(config.SPLIT_VINN_FILES_TRAIN, region)
    #     )