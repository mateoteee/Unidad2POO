from Viajero import ViajeroFrecuente

## Leer un archivo csv separqdoi por ; para crear instancias de la clase ViajeroFrecuente
## y almacenarlas en una lista Viajeros

import csv

class ManejadorViajero:
    def __init__(self):
        self.__Viajeros = []

    def agregarViajeros(self,unViajero):
        self.__Viajeros.append(unViajero)

##  Calcular todas las Millas Acumuladas de un Viajero

        def CanTotMillas (self,vfi):
            Indice = 0
            Valorret = -3
            Bandera = False
            while not Bandera and Indice < len(self.__Viajeros):
                if self.__Viajeros[Indice].getnum_viajero() == vfi:
                      Bandera = True
                      Valorret = Indice
                else:
                     Indice +=1
            return Valorret
                      



'''


          
##  Metodo CantidadTotaldeMillas que retorna la cantidad de millas acumuladas

    def cantidaddemillastotales(self, vfi, Viajeros):
        if vfi in Viajeros:
            Indice = Viajeros(vfi).getmillas_acum
        else:
            Indice = -3
        return Indice

## def AcumularMillas recibe como parametro la cantidad de millas recorridas
## las suma con el atributo correspondiente y retorna el valor del atributo actualizado

    def AcumularMillas(self, cmr, vfi, Viajeros):
        if vfi in Viajeros:
            Indice = cmr + int (Viajeros(vfi).millas_acum)
            Viajeros(vfi).millas_acum = Indice
        else:
            Indice = -3
        return Indice

## def CanjearMillas recibe como parametro la cantidad de millas a canjear, debe verificarse
## que esta sea menor a las millas acumuladas, caso contrario retorna mensaje de error.
## Retorna el valor de la cantidad de millas que quedan.

    def CanjearMillas(self, cmc, vfi, Viajeros):
        if vfi in Viajeros:
            if cmc > int(Viajeros(vfi).millas_acum):
                Indice = cmc - Viajeros(vfi).millas_acum
                Viajeros(vfi).millas_acum = Indice
            else:
                print("No tiene suficientes millas acumuladas para realizar este Canje")
        else:
            Indice = -3
        return Indice

''' 
def CargarViajeros(self, unViajero):
        Viajeros = []
        with open('DatosViajeros.csv') as archivo:
            reader = csv.reader(archivo,delimiter=';')
            for fila in reader:

## si el archivo tiene la primera fila con los titulos de las columnas, se utiliza
## next(archivo None) lo que hace esta sentencia es borrar la 1era fila y seguir con la 2da
                num_viajero = int(fila[0])
                dni = fila[1]
                nombre = fila[2]
                apellido = fila[3]
                millas_acum = int(fila[4])
                unViajero = Viajeros(num_viajero, dni, nombre, apellido, millas_acum)
                self.agregarViajeros(unViajero)
        archivo.close()


