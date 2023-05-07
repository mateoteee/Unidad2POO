class PlanAhorro:
    __cantcuotas: 60
    __cuotlicitas: 10

    def __init__(self, a, b, c, d):
        self.__codigo = a
        self.__modelo = b
        self.__version = c
        self.__precio = d
        self.__importecuota = (self.__precio/self.__cantcuotas) + self.__precio * 0.10
    
    def getprecio(self):
        return self.__precio
    
    def getValorCuota(self):
        return self.__importecuota
    
    def MostrarVehiculo(self):
        print(f"{self.__codigo}, {self.__modelo} {self.__version}")
    

    def ActualizarPrecio(self):
        print(f"Codigo de plan: {self.__codigo}, Vehiculo: {self.__modelo} {self.__version}")
        self.__precio = float(input( "Ingrese el valor actualizado del vehículo: "))
        print("Valor del vehículo actualizado.")
    
    def ValorCuotasParaLicitar(self):
        cuot=self.__cuotlicitas*self.__importecuota
        return cuot
    
    @classmethod
    def ModificarCuotasLicitas(cls):
        print("Modificación de cuotas licitas para pagar un Plan de Ahorro: ")
        x=float(input("Ingrese la nueva cantidad de cuotas licitas de los planes de ahorro: "))
        cls.__cuotlicitas=x
        print ("Se modificó la cantidad de cuotas licitas para todos los planes")
      
    
