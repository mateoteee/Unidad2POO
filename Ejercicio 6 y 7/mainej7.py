from viajero2 import FrequentTrav

# Comparar millas con un valor entero
v1 = FrequentTrav(num=1, dni=12345678, name='Juan', surname='Perez', miles=500)
if v1 == 500:
    print("El viajero", v1.name, "tiene 500 millas acumuladas.")

# Acumular millas
v2 = FrequentTrav(num=2, dni=87654321, name='Ana', surname='Gonzalez', miles=300)
v2 = 100 + v2
print("Después de acumular 100 millas, el viajero", v2.name, "tiene", v2.miles, "millas acumuladas.")

# Canjear millas
v3 = FrequentTrav(num=3, dni=11223344, name='Pedro', surname='Garcia', miles=1000)
v3 = 500 - v3
print("Después de canjear 500 millas, el viajero", v3.name, "tiene", v3.miles, "millas acumuladas.")