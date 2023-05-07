import numpy as np
from Alumno import Alumno
import csv

class ManejadorAlumno:
    
    def __init__(self):
        self.__len=0
        self.__incremento = 5
        self.__cantidad = 0
        self.__alumnos= np.empty(self.__len, dtype=Alumno)
    
    def CargarNumpy(self, unAlumno):
        if (self.__len == self.__cantidad):
            self.__len += self.__incremento
            self.__alumnos.resize(self.__len)
        self.__alumnos[self.__cantidad] = unAlumno
        self.__cantidad += 1

    def cargar_alumnos(self, archivo):
       archivo = open("alumnos.csv")
       r = csv.reader (archivo, delimiter=";")
       next(r)
       for fila in r:
           dni= fila[0]
           apellido= fila[1]
           nombre= fila[2]
           carrera= fila[3]
           anio=fila[4]
           alumnote=Alumno(dni,apellido,nombre,carrera,anio)
           self.__CargarNumpy(alumnote)
    
    def getAlumno(self, indice):
        return self.__alumnos[indice]
    


    def ListaOrdenada(self):
        listaO= np.sort(self.__alumnos)
        return listaO

