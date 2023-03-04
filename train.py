from setup import config, folders
from utils import dwt, create_dataframe

folders.create_folders()
dwt.load_dwt(config.TEST_SET_PATH, config.VINN_FILES_TEST)

df = create_dataframe.create_combined_dataframe(config.VINN_FILES_TEST)
print(df)


