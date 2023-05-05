# -*- coding: utf-8 -*-
from ClaseEmail import Email


def test_crear_cuenta():
    email = Email()
    email.crear_cuenta('usuario@dominio.com')
    assert email.retorna_email() == "Email: usuario@dominio.com"


def test_retorna_email():
    email = Email('alumno', 'gmail', 'com', 'contraseña')
    assert email.retorna_email() == "Email: alumno@gmail.com"


def test_get_dominio():
    email = Email('alumno', 'gmail', 'com', 'contraseña')
    assert email.get_dominio() == "gmail"


def test_validar_contrasenia():
    email = Email()
    assert email.validar_contrasenia('contraseña')


def test_cambiar_contrasenia():
    email = Email()
    pass_actual = "contraseña"
    pass_nueva = "nueva_contraseña"
    email.cambiar_contrasenia(pass_actual, pass_nueva)
    assert email.validar_contrasenia(pass_nueva), "La contraseña actualizada no es válida"

def test_validar_direccion():
    email = Email()
    assert email.validar_direccion("alumno@gmail.com")


def saludo(self, nombre):
    return f"{nombre}, enviaremos tus mensajes a la dirección {self.retorna_email()}."
