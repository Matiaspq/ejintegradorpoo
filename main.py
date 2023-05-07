from claseManejadorMateria import ManejadorMateria
from claseManejadorAlumno import ManejadorAlumno

if __name__=='__main__':
    m=ManejadorMateria()
    m.cargaMateria()
    a=ManejadorAlumno()
    a.cargaAlumno()
    a.listadoOrdenado()
    """dni=input("Ingresa dni: ")
    materia=m.buscaMaterias(dni)
    m.promedioSinAplazos(materia)
    m.promedioConAplazos(materia)"""
    nombreMateria=input("Ingresa nombre materia: ")
    promocion=m.aprobadosPromocional(nombreMateria, a)
    print("DNI         Apellido y nombre    Fecha            Nota         Año que cursa")
    for datos in promocion:
        print(f"{datos[0]}   {datos[1]}   {datos[2]}   {datos[3]}           {datos[4]}              {datos[5]}")

