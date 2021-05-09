from pathlib import *
import os
import xlwings as xw
from dbfread import DBF


def dbf_reader(path):
    table = DBF(path, encoding="850")
    return table


def archivos(path):
    lista = []
    archivos = os.listdir(path)
    for i in range(len(archivos)):
        if "DBF" == archivos[i][-3:]:
            lista.append(archivos[i])
        else:
            pass
    return lista


def excel(archivos, path):
    wb = xw.Book()
    # wb.save("C:\\Users\\mherr\\Desktop\\CAMP6W\\OBRAS\\MEDIA_LU\\CSV.xlsx")
    for x in range(len(archivos)):
        strcol = "A"
        strng = 2
        hoja = wb.sheets.add(archivos[x])
        table = dbf_reader(path / archivos[x])
        hoja.range("A1").value = table.field_names
        for record in table:
            hoja.range(strcol + str(strng)).value = list(record.values())
            strng += 1
        del strcol, strng


def main():
    path = PureWindowsPath('C:\\Users\\mherr\\Desktop\\CAMP6W\\OBRAS\\MEDIA_LU')
    excel(archivos(path), path)
    print(archivos(path))


if __name__ == "__main__":
    main()
