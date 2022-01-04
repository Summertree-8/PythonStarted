import pandas as pd
from glob import glob

#get path of excel file
filepaths = glob('source/*.xlsx')
# print(filepaths)

filepath = filepaths[0]
_df = pd.read_excel(filepath)

