# -*- coding: utf-8 -*-
import csv
from ClaseEmail import Email

if __name__ == '__main__':

    print("01- Ingresar el nombre de una persona y su dirección de e-mail (instancia de la clase Email)")
    email1 = Email()
    nombre = input("Ingrese su nombre: ")
    direccion = input("Ingrese su dirección de correo electrónico: ")
    email1.crear_cuenta(direccion)

    print("Luego imprima el siguiente mensaje:")
    print("Estimado <nombre> te enviaremos tus mensajes a la dirección <dirección de correo>.")
    email1.saludo(nombre)

    print("02- Para la instancia creada en el ítem anterior, modificar la contraseña")
    pass_actual = input("Ingrese la contraseña actual (por defecto es contraseña: ")
    contador_intentos_cambio_pass = 0
    cambio_exitoso_pass = False
    while contador_intentos_cambio_pass <= 3 and not cambio_exitoso_pass:
        if email1.validar_contrasenia(pass_actual):
            pass_nueva = input("Ingrese la nueva contraseña: ")
            email1.cambiar_contrasenia(pass_actual, pass_nueva)
            print("Contraseña actualizada!!")
            cambio_exitoso_pass = True
        else:
            print("La contraseña ingresada no coincide!!")
            contador_intentos_cambio_pass += 1
            print("Intento de cambio numero: ", contador_intentos_cambio_pass)

    print("03- Crear un objeto de clase Email, a partir de una dirección de correo")
    email2 = Email()
    email2.crear_cuenta("informatica.fcefn@gmail.com")
    email2.retorna_email()

    print("04- a) Leer de un archivo separado por comas 10 direcciones de email, crear las cuentas correspondientes,")
    print("solo para las direcciones válidas comprobadas con expresiones regulares, y guardarlas en una lista")

    lista_emails = []
    try:
        with open("lista.csv") as archivo:
            reader = csv.reader(archivo, delimiter=',')
            for fila in reader:
                email = Email()
                if email.validar_direccion(fila[0]):
                    email.crear_cuenta(fila[0])
                    lista_emails.append(email)
                else:
                    print("Sintaxis Email inválida: ", fila[0])
    except FileNotFoundError:
        print("El archivo lista.csv no se encontró")

    n = 0
    for email in lista_emails:
        n += 1
        print("Cuenta valida numero: ", n)
        print(email.retorna_email())

    print("04- b) Ingresar un dominio e indicar cuántos objetos de la clase Email, tienen dominio igual al ingresado.")
    dominio = input("Ingrese un dominio a contabilizar: ")
    dominio_contador = 0
    for email in lista_emails:
        if email.get_dominio() == dominio:
            print("Email: ", email.retorna_email())
            dominio_contador += 1
    print(f"Se encontraron {dominio_contador} cuentas con el dominio {dominio}.")
