import os

from dbfread import DBF

# Cambiar directorio por carpeta con dbf
directorio = 'C:\\Users\\mherr\\Desktop\\CAMP6W\\OBRAS\\CAJONDEP'


def convertir(nombre):
    """ Aqui se pone la explicacion"""
    # Convertir toma los datos del dbf seleccionado y los convierte a un data frame
    # para exportarlo a una carpeta con los csv
    carpeta = "csv"
    dbf = DBF(str(nombre), encoding='1252')
    if not os.path.exists(carpeta):
        os.makedirs(carpeta)

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
        convertir(lista[i])


if __name__ == "__main__":
    main()
