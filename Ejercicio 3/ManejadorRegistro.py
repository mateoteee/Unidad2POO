
from Registro import Registro
import csv

class ManejadorRegistro:
    def __init__(self):
        self.registros = []
        for i in range(31):
            dia = []
            for j in range(24):
                dia.append(None)
            self.registros.append(dia)

    def agregar_registro(self, registro):
        dia = registro.dia - 1
        hora = registro.hora
        self.registros[dia][hora] = registro

    def generar_registro(self, archivo):
        with open(archivo, "datosmet.txt") as f:
            lineas = f.readlines()
            for linea in lineas:
                datos = linea.strip().split(",")
                dia = int(datos[0])
                hora = int(datos[1])
                temperatura = float(datos[2])
                humedad = float(datos[3])
                presion = float(datos[4])
                registro = Registro(dia, hora, temperatura, humedad, presion)
                self.agregar_registro(registro)



    def menor_valor_temp(self):
        menor = self.registros[0][0].get_temperatura
        dia_menor = 1
        hora_menor = 0
        for i in range(31):
            for j in range(24):
                if self.registros[i][j] is not None:
                    valor = self.registros[i][j].get_temperatura
                    if valor < menor:
                        menor = valor
                        dia_menor = i + 1
                        hora_menor = j
        print("Temperatura máxima:", menor, "registrada el día", dia_menor, "a las", hora_menor, "horas.")
            
      

    def mayor_valor_temp(self):
        mayor = self.registros[0][0].get_temperatura
        dia_mayor = 1
        hora_mayor = 0
        for i in range(31):
            for j in range(24):
                if self.registros[i][j] is not None:
                    valor = self.registros[i][j].get_temperatura
                    if valor > mayor:
                        mayor = valor
                        dia_mayor = i + 1
                        hora_mayor = j
        print("Temperatura mínima:", mayor, "registrada el día", dia_mayor, "a las", hora_mayor, "horas.")
    

    def menor_valor_humedad(self):
        menor = self.registros[0][0].get_humedad
        dia_menor = 1
        hora_menor = 0
        for i in range(31):
            for j in range(24):
                if self.registros[i][j] is not None:
                    valor = self.registros[i][j].get_humedad
                    if valor < menor:
                        menor = valor
                        dia_menor = i + 1
                        hora_menor = j
        print("Humedad mínima:", menor, "registrada el día", dia_menor, "a las", hora_menor, "horas.")

    def mayor_valor_humedad(self):
        mayor = self.registros[0][0].get_humedad
        dia_mayor = 1
        hora_mayor = 0
        for i in range(31):
            for j in range(24):
                if self.registros[i][j] is not None:
                    valor = self.registros[i][j].get_humedad
                    if valor > mayor:
                        mayor = valor
                        dia_mayor = i + 1
                        hora_mayor = j
        print("Humedad máxima:", mayor, "registrada el día", dia_mayor, "a las", hora_mayor, "horas.")

    def menor_valor_presion(self):
        menor = self.registros[0][0].get_presion
        dia_menor = 1
        hora_menor = 0
        for i in range(31):
            for j in range(24):
                if self.registros[i][j] is not None:
                    valor = self.registros[i][j].get_presion
                    if valor < menor:
                        menor = valor
                        dia_menor = i + 1
                        hora_menor = j
        print("Presion mínima:", menor, "registrada el día", dia_menor, "a las", hora_menor, "horas.")

    def mayor_valor_presion(self):
        mayor = self.registros[0][0].get_presion
        dia_mayor = 1
        hora_mayor = 0
        for i in range(31):
            for j in range(24):
                if self.registros[i][j] is not None:
                    valor = self.registros[i][j].get_presion
                    if valor > mayor:
                        mayor = valor
                        dia_mayor = i + 1
                        hora_mayor = j
        print("Presion máxima:", mayor, "registrada el día", dia_mayor, "a las", hora_mayor, "horas.")
    
## Indicar la temperatura promedio mensual por hora seleccionada: Se debe recorrer la lista 
# bidimensional y calcular el promedio de temperatura para la hora elegida.

    def promedio_temperatura(self, hora):
        suma = 0
        n = 0
        for i in range(31):
            if self.registros[i][hora] is not None:
                suma += self.registros[i][hora].get_temperatura
                n += 1
        if n == 0:
            return 0
        else:
            return suma / n
        
## Dado un número de día listar los valores de las tres variables para cada hora del día dado: 
# Se debe solicitar al usuario el número de día y luego recorrer la lista bidimensional para 
# encontrar los registros correspondientes al día ingresado. Luego se debe presentar la información 
# en el formato solicitado.
        
    def obtener_valores_por_dia(self, dia):
        print("Hora   Temperatura   Humedad   Presión")
        for hora, registro in enumerate(self.registros[dia - 1]):
            print(f"{hora:02d}      {registro.get_temperatura:.2f}        {registro.get_humedad:.2f}      {registro.get_presion:.2f}")
