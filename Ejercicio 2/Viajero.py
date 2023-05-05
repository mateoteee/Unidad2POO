class Viajero():
    __num_viajero = 0
    __dni = 0
    __nombre = ''
    __apellido = ''
    __millas_acum = 0

## Metodo del Constructor

    def __init__(self, num_viajero, dni, nombre, apellido, millas_acum):
        self.__num_viajero = num_viajero
        self.__dni = dni
        self.__nombre = nombre
        self.__apellido = apellido
        self.__millas_acum = millas_acum

        def __str__(self):
            return "%s %s %s %s %s %s" % (self.__num_viajero, self.__dni, self.__nombre, self.__apellido, self.__millas_acum)
        
        def getnum_viajero():
            return self.__num_viajero
        def getdni():
            return self.__dni
        def getnombre():
            return self.__nombre
        def getapellido():
            return self.__apellido
        def getmillas_acum():
            return self.__millas_acum
        

           
            
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
    

