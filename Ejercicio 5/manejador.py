from claseee import PlanAhorro
import csv

class ManejadorPlan:

    def __init__(self):
        self.__lista=[]

    def CargarLista(self):
        with open('planes.csv', 'r') as f:
            reader= csv.reader(f, delimiter ';')
            
            for fila in reader:
                if ((fila[0] != None) and 
               (fila[1] != None) and 
               (fila[2] != None) and 
               (fila[3] != None) and 
               (fila[4] != None)):
                    obj= PlanAhorro(fila[1],fila[2],fila[3],fila[4])
                    self.__lista.append(obj)
    
    def ActualizarValor(self):
        print("Modificación de valores")
        for i in range (len(self.__lista)):
            self.__lista[i].ActualizarPrecio()

    def MostrarMenores (self):
        print("Mostrar inferiores al valor dado.")
        x=float(input("Ingrese el valor pivote: "))
        print("Los vehículos que son menores al precio ingresado son los siguientes:")

        for i in range(len(self.__lista)):
            if (self.__lista[i].getValorCuota() < x):
                self.__lista[i].MostrarVehiculo()
    
    def MostrarMonto (self):
        i=0
        while (i < len(self.__lista)):
            j = self.__lista[i].ValorCuotasParaLicitar()
            print(f"El monto para licitar el vehiculo {self.__lista[i].MostrarVehiculo()} es de {j}")

    


