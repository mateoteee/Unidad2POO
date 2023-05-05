# -*- coding: utf-8 -*-

import re
class Email:
    __id_cuenta = str
    __dominio = str
    __tipo_dominio = str
    __contrasenia = str
    __nombre = str

    def __init__(self, id_cuenta='alumno', dominio='gmail', tipo_dominio='.com', contrasenia='contraseña'):
        self.__id_cuenta = id_cuenta
        self.__dominio = dominio
        self.__tipo_dominio = tipo_dominio
        self.__contrasenia = contrasenia

    def retorna_email(self):
        return f"Email: {self.__id_cuenta}@{self.__dominio}.{self.__tipo_dominio}"

    def crear_cuenta(self, direccion):
        usuario = direccion.split("@")
        self.__id_cuenta = usuario[0]
        self.__dominio = usuario[1].split(".")[0]
        self.__tipo_dominio = usuario[1].split(".")[1]

    def get_dominio(self):
        return self.__dominio

    def validar_contrasenia(self,contrasenia):
        return self.__contrasenia == contrasenia

    def cambiar_contrasenia(self, pass_actual, pass_nueva):
        if self.validar_contrasenia(pass_actual):
            self.__contrasenia = pass_nueva

    def saludo(self, nombre):
        print(
            f"{nombre}, enviaremos tus mensajes a la dirección {self.retorna_email()}.")

    def validar_direccion(self, direccion):
        # Comprobar si la dirección de correo electrónico cumple con la estructura correcta
        # y contiene solo caracteres válidos
        validacion: bool = True
        expresion_regular = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
        caracteres_validos = set(
            'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789._%+-@')
        if (not re.match(expresion_regular, direccion)) or (not (set(direccion) <= caracteres_validos)):
            validacion = False
        return validacion
