import os
import sys
import csv
from dbfread import DBF

# Cambiar directorio por carpeta con dbf
directorio = 'C:\\Users\\mherr\\Desktop\\CAMP6W\\OBRAS\\CAJONDEP'

def dbf_to_csv(dbf_table_pth):
    carpeta = "csv"
    if not os.path.exists(carpeta):
        os.makedirs(carpeta)
    csv_fn = directorio + "\\" + carpeta + "\\" + dbf_table_pth[:-4] + ".csv"
    table = DBF(dbf_table_pth, encoding="1252")
    with open(csv_fn, 'w', newline = '') as f:
        writer = csv.writer(f)
        writer.writerow(table.field_names)
        for record in table:
            writer.writerow(list(record.values()))
    return csv_fn
# archivos toma una lista de los archivos que estan en el directorio de la obra
# y si su terminación es dbf los convierte a dataframe
def archivos():
    lista = []
    archivos = os.listdir()
    for i in range(len(archivos)):
        if "DBF" == archivos[i][-3:]:
            lista.append(archivos[i])
        else:
            pass
    return lista

#main conecta los archivos del directorio a la función convertir
def main():
    os.chdir(directorio)
    lista = archivos()
    for i in range(0,len(lista)):
        dbf_to_csv(lista[i])


if __name__ == "__main__":
    main()
