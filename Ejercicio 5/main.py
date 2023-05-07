from claseee import PlanAhorro
from manejador import ManejadorPlan


if __name__ == '__main__':

    MP= ManejadorPlan()
    MP.CargarLista()
    
    

    print("MENU DE OPCIONES")
    print ("1. Actualizar valor de vehiculo")
    print ("2. Informar plan segun cuota menor a valor ingresado")
    print("3. Informar monto para licitar vehiculo")
    print("4. Modificar cantidad de cuotas p/licitar segun codigo de plan")

    opcion = int (input("INGRESE LA OPCION Q DESEE: "))

    if opcion == 1:
        MP.ActualizarValor()
        
        
    elif opcion == 2:
        MP.MostrarMenores()
        
    elif opcion == 3:
        MP.MostrarMonto()
    elif opcion ==4:
        PlanAhorro.ModificarCuotasLicitas()
        
