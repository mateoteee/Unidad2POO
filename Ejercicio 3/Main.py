from Registro import Registro
from ManejadorRegistro import ManejadorRegistro

## Se crea una instancia de ManejadorRegistro y se llama al método leer_archivo() para leer 
# los datos del archivo de texto y almacenarlos en la lista bidimensional.

if __name__ == '__main__':
    manejador_registros = ManejadorRegistro()
    manejador_registros.leer_archivo("datosmet.txt")

# Se muestra un menú con tres opciones que llaman a los métodos correspondientes en 
# ManejadorRegistro según la opción seleccionada, La opción "4" permite salir del bucle y 
# finalizar la ejecución del programa.

    while True:
        print("\nSeleccione una opción:")
        print("1. Mostrar para cada variable el día y hora de menor y mayor valor.")
        print("2. Dada una hora, Indicar la temperatura promedio mensual para esa hora.")
        print("3. Dado un número de día, listar los valores de las tres variables para cada hora del día dado.")
        print("4. Salir\n")
        
        opcion = input("Ingrese una opción: ")

        if opcion == "1":
            manejador_registros.mayor_valor_temp()
            manejador_registros.menor_valor_temp()
            manejador_registros.mayor_valor_humedad()
            manejador_registros.menor_valor_humedad()        
            manejador_registros.mayor_valor_presion()
            manejador_registros.menor_valor_presion()
            
        elif opcion == "2":
            manejador_registros.promedio_temperatura()
            una_hora = int(input("Ingrese una hora: "))
            prome = manejador_registros.obtener_valores_por_dia(num_dia)
            print("El Promedio mensual de Temperatura para la hora ", una_hora, "es de:  ", prome) 

        elif opcion == "3":
            num_dia = int(input("Ingrese un número de día: "))
          
        elif opcion == "4":
            exit
        
        else:
            print("Opción inválida. Por favor ingrese una opción válida.")



