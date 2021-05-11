from pathlib import PureWindowsPath
import os
import xlwings as xw
from dbfread import DBF
import argparse


def dbf_reader(path):
    """
    Transfers the contents of each column in a dbf file into a list

    :param path: The path in which the dbf files are located
    :return: A table composed of the lists of each record in a dbf and their field names
    """
    latin_1 = "850"
    table = DBF(path, encoding=latin_1)
    return table


def file_iteration(path):
    """
    Iterates over a directory to find the files that correspond to a dbf format

    :param path: The path in which the function will iterate
    :return: A list made up by the names of the files that are in dbf format
    """

    lista = []
    archivos = os.listdir(path)
    for i in range(len(archivos)):
        if "DBF" == archivos[i][-3:]:
            lista.append(archivos[i])
        else:
            pass
    return lista


def excel_file_generator(file, path):
    """
    Rewrites a dbf file into an excel sheet

    :param file: The file which is going to be transformed into an excel sheet
    :param path: The location of tha file mentioned before
    :return: None
    """

    wb = xw.Book("Excel.xlsx")
    start_col = "A"
    start_row   = 2
    sheet = wb.sheets.add(file)
    dbf_file = dbf_reader(path / file)
    sheet.range("A1").value = dbf_file.field_names
    for record in dbf_file:
        sheet.range(start_col + str(start_row)).value = list(record.values())
        start_row += 1


def main():
    """
    Connects the dbf contents with the excel file generator using the files listed in the file iteration function
    :return: None
    """
    parser = argparse.ArgumentParser(description="Excel")
    parser.add_argument("--path",type=str, help="Donde quieres hacer campeon")
    args = parser.parse_args()
    path = PureWindowsPath(args.path)
    dbf_files = file_iteration(path)
    wb = xw.Book()
    wb.save(path / "Excel.xlsx")
    for i in range(len(dbf_files)):
        excel_file_generator(dbf_files[i], path)

    try:
        print("Excel succesfully generated")
    except:
        print("Excel Failed")
if __name__ == "__main__":
    main()
