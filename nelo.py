import csv
from datetime import datetime

inscritos = []

def inscripcion (nom_inscrito = '', fecha = ''):
    fecha = datetime.now().strftime("%d/%m/%Y")
    inscritos.append([nom_inscrito, fecha])
    return inscritos

def buscar_inscritos (nom_inscrito = ''):
    with open('asistencia.csv', 'r', newline = '' ) as archivo_csv:
        reader = csv.reader(archivo_csv)
        for fila in reader:
            if (fila[0] == nom_inscrito):
                return 'La persona ' + nom_inscrito + ' está inscrita.'
        return 'No se encuentra en la lista.'


while True:
    
    opcion = int(input("Desea añadir mas nombres?: 1.- Si, 2.- No"))
    
    if opcion == 1:
        nom_inscrito = input("Ingrese nombre: ")
        inscritos = inscripcion(nom_inscrito)
    elif opcion == 2:
        print("No se añaden mas nombres")
        with open('asistencia.csv','w',newline='') as archivo_csv:
            writer = csv.writer(archivo_csv)
            writer.writerows(inscritos)
        break
    else:
        print("Ingrese una opcion de la lista")

nom_inscrito = input("Buscar a un inscrito. Ingresa su nombre")
print(buscar_inscritos(nom_inscrito = nom_inscrito))

