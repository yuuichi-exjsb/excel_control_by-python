# -*- coding: utf-8 -*
import pandas as pd
import glob
import openpyxl
import xlrd

import_file_path = "sample.xlsx"
excel_sheet_name = "総得点管理"
export_file_path = "個人成績"

df_order = pd.read_excel(import_file_path, sheet_name= excel_sheet_name)
student_name = df_order['学籍番号'].unique()

for i in student_name:
    df_order_company = df_order[df_order['学籍番号']== i]
    df_order_company.to_excel(export_file_path+'/'+i+'.xlsx')
