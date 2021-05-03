import os
from dbfread import DBF
from pandas import DataFrame
#Cambiar directorio por carpeta con dbf
directorio = 'C:\\Users\\mherr\\Desktop\\CAMP6W\\OBRAS\\CAJONDEP'
#Convertir toma los datos del dbf seleccionado y los convierte a un data frame para exportarlo a una carpeta con los csv
def convertir(nombre):
    carpeta = "csv"
    dbf = DBF(str(nombre), encoding='1252')
    if not os.path.exists(carpeta):
        os.makedirs(carpeta)
    frame = DataFrame(iter(dbf))
    frame.to_csv(directorio + "\\" + carpeta +"\\" + nombre[:-4] + ".csv", index=False)
#archivos toma una lista de los archivos que estan en el directorio de la obra y si su terminación es dbf los convierte a dataframe
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
        convertir(lista[i])
main()