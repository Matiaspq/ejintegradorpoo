import csv
from claseAlumno import Alumno

class ManejadorAlumno:
    def __init__(self):
        self.__alumnos=[]

    def cargaAlumno(self):
        archivo=open('alumnos.csv')
        reader=csv.reader(archivo,delimiter=";")
        next(reader)
        for fila in reader:
            print(fila[0])
            alumno=Alumno(fila[0],fila[1],fila[2],fila[3],fila[4])
            self.__alumnos.append(alumno)

    def buscaDni(self,dni):
        i=0
        while i<len(self.__alumnos) and self.__alumnos[i].getDni()!=dni:
            i+=1
        return self.__alumnos[i]
    
    def listadoOrdenado(self):
        ordenado=sorted(self.__alumnos)
        for alumno in ordenado:
            print(alumno)