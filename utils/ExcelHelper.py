import os

import xlwings as xw
import pandas as pd
import pythoncom
from openpyxl import load_workbook

pd.options.mode.chained_assignment = None

PATH = r'sample input/SiguePay_React_Language.xlsx'
SHEET = 'Data Mapping'


def read_excel_file(file_name, sheet_name):
    file_name = file_name
    pythoncom.CoInitialize()
    xw.App(visible=False)
    excel_book = xw.Book(file_name)
    excel_sheet = excel_book.sheets(sheet_name)
    pd_header = excel_sheet.range('B13').expand('right').value
    num_row = len(excel_sheet.range('B13').expand('down').value) + 12
    num_column = len(pd_header)

    if num_column <= 26:
        # if column name in range B - Z
        last_column_name = chr(65 + num_column)
    else:
        # if number of column > 26 name column change to BA - BZ
        last_column_name = 'B' + chr(65 + (num_column - 26))

    if num_row < 1000:
        range_table = 'B13:' + last_column_name + str(num_row)
        table_values = excel_sheet.range(range_table).value
        data = pd.DataFrame(table_values, columns=pd_header)
    else:
        range_table1 = 'B13:'
        range_table2 = 'B'
        split_point = int(num_row / 2)
        range_table1 += last_column_name + str(split_point)
        range_table2 += str(split_point + 1) + ':' + last_column_name + str(num_row)

        table_value1 = excel_sheet.range(range_table1).value
        table_value2 = excel_sheet.range(range_table2).value

        df1 = pd.DataFrame(table_value1, columns=pd_header)
        df2 = pd.DataFrame(table_value2, columns=pd_header)
        data = df1.append(df2, ignore_index=True)

    length_frame = len(data)
    excel_book.close()
    pythoncom.CoUninitialize()
    # print("number of row of file %s after drop duplicated: %d" % (file_name, len(data)))
    return data, length_frame


def write_excel_file(file_name, sheet_name, data):
    writer = pd.ExcelWriter(file_name)
    # write to dest file. But first remove existing file
    if os.path.exists(file_name):
        path = os.path.abspath(file_name)
        book = load_workbook(path)
        writer.book = book

    # save to file
    data.to_excel(writer, sheet_name=sheet_name, startrow=0, index=False)
    writer.close()


def write_json_file(file_name, data):
    # write to dest file. But first remove existing file
    if os.path.exists(file_name):
        os.remove(file_name)

    # save to file
    f = open(file_name, "w")
    f.write(data)
    f.close()
