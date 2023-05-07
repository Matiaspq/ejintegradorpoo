class Alumno:
    def __init__(self,dni, apellido, nombre, carrera,añocursa):
        self.__dni=dni
        self.__apellido=apellido
        self.__nombre=nombre
        self.__carrera=carrera
        self.__añocursa=añocursa
    
    def getDni(self):
        return self.__dni
    
    def getApellido(self):
        return self.__apellido
    
    def getNombre(self):
        return self.__nombre
    
    def getAnioCursa(self):
        return self.__añocursa
    
    def __lt__(self, otro):
        return (self.__añocursa, self.__apellido, self.__nombre) < (otro.__añocursa, otro.__apellido, otro.__nombre)

    def __str__(self):
        return f"{self.__dni} {self.__apellido} {self.__nombre} {self.__carrera} {self.__añocursa}"
