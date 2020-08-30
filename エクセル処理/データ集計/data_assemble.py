import pandas as pd
import openpyxl
import xlrd
import glob

export_file_path = "提出用データ"
import_foloder_path = '授業評価アンケート'

path = import_foloder_path + '/' + '*.xlsx'

file_path = glob.glob(path)

df_concat = pd.DataFrame()

for i in file_path:
    df_read_excel = pd.read_excel(i)
    df_concat = pd.concat([df_read_excel,df_concat])

df_concat.to_excel(export_file_path + '/' + '授業評価アンケート集計.xlsx')