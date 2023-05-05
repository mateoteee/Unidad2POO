
from ManViajero import ManejadorViajero
from Viajero import Viajero

if __name__ == '__main__':
    mv = ManejadorViajero()
    unViajero = Viajero()

    mv.CargarViajeros()
    print("Lista")
    print(mv)

## Leer por teclado un numero de via\jero frecuente y presentar un menu con las siguientes 
## opciones:
##  a- Consultar Cantidad de Millas
##  b- Acumular Millas
##  c- Canjear Millas

    vfi = int(input('Ingrese Numero de Viajero Frecuente: '))
    Viajeros = []

    print("Menu")
    print("a. Consultar Cantidad de Millas")
    print("b. Acumular Millas")
    print("c. Canjear Millas")
    opcion = input()
    
    if opcion=='a':
        CantMillas = mv.CanTotMillas(vfi)
        if CantMillas < 0:
            print("El Numero de Viajero Frecuente Ingresado es Incorrecto")
        else:
            print("La Cantidad de Millas Acumuladas por el Viajero Frecuente", vfi, "es igual a ", CantMillas)
   
    elif opcion=='b':
        cmr = int(input('Ingrese La Cantidad de Millas Recorridas: '))
        MillActual = mv.AcumularMillas(cmr, vfi)
        if MillActual < 0:
            print("El Numero de Viajero Frecuente Ingresado es Incorrecto")
        else:
            print("La Cantidad de Millas Actualizadas por el Viajero Frecuente", vfi, "es igual a ", MillActual)
   
    elif opcion=='c':
        cmc = int(input('Ingrese La Cantidad de Millas a Canjear: '))
        MillCanje = mv.CanjearMillas(cmc, vfi)
        if MillCanje == 0:
            print("El Viajero no posee Millas Acumuladas suficientes para realizar el Canje")
        elif MillCanje < 0:
            print("El Numero de Viajero Frecuente Ingresado es Incorrecto")
        else:
            print("La Cantidad de Millas Actualizadas por el Viajero Frecuente", vfi, "es igual a ", MillCanje)