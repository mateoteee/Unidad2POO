from Materia import Materia
import csv
from Alumno import Alumno

class ManejadorMateria:

    def __init__(self):
        self.__materias = []
    
    def cargarLista(self,):
        archivo = open("materiasAprobadas.csv")
        r=csv.reader(archivo, delimiter=';')
        next(r)

        for fila in r:
            dni= fila[0]
            nombreMat= fila[1]
            fecha=fila[2]
            nota=fila[3]
            aprobacion=fila[4]

            unaMateria=Materia(dni, nombreMat, fecha, nota, aprobacion)
            self.__materias.append(unaMateria)
    


    def PromedioSinAplazos(self, dni_b):
        i=0
        c=0
        sum=0
        while (i < len(self.__materias)):
            if (self.__materias[i].getdni() == dni_b):
                if(self.__materias[i].getnota >= 7):
                    c += 1
                    sum += self.__materias[i].getnota()
            i+= 1
        prom = sum / c
        return prom
    
    def PromedioConAplazos (self, dni_b):
        i=0
        c=0
        sum=0
        while (i < len(self.__materias)):
            if (self.__materias[i].getdni() == dni_b):
                    c += 1
                    sum += self.__materias[i].getnota()
            i+= 1
        prom = sum / c
        return prom

    
 