import csv
from claseMateriaAprobada import MateriaAprobada
from claseManejadorAlumno import ManejadorAlumno

class ManejadorMateria:
    def __init__(self):
        self.__materias=[]

    def cargaMateria(self):
        archivo=open('materiasAprobadas.csv')
        reader=csv.reader(archivo,delimiter=";")
        next(reader)
        for fila in reader:
            materia=MateriaAprobada(fila[0],fila[1],fila[2],fila[3],fila[4])
            self.__materias.append(materia)

    def buscaMaterias(self, dni):
        materiaAprobada=[]
        for materia in self.__materias:
            if materia.getDni()==dni:
                materiaAprobada.append(materia)
        return materiaAprobada
    
    def promedioSinAplazos(self,materias):
        notasin=[]
        for materia in materias:
            if materia.getNota()>=4:
                notasin.append(materia.getNota())
        print(f"Promedio sin aplazos:{self.muestraPromedio(notasin)}")

    def promedioConAplazos(self,materias):
        notacon=[]
        for materia in materias:
                notacon.append(materia.getNota())
        print(f"Promedio con aplazos:{self.muestraPromedio(notacon)}")

    def muestraPromedio(self,notas):
        promedio=sum(notas)/len(notas)
        return round(promedio,2)
    
    def aprobadosPromocional(self,nombreMateria,manejadorAlumno):
        promocional=[]
        for materia in self.__materias:
            if materia.getNombreMateria()==nombreMateria and materia.getAprobacion()=="P":
                dni=materia.getDni()
                alumnop=manejadorAlumno.buscaDni(dni)
                promocional.append([alumnop.getDni(), alumnop.getApellido(), alumnop.getNombre(), materia.getFecha(), materia.getNota(), alumnop.getAnioCursa()])
        return promocional

