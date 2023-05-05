from clase import Conjunto

if __name__ == '__main__':
    A = Conjunto([1, 2, 3, 4])
    B = Conjunto([3, 6, 9])

    print("Menú de opciones:")
    print("1- Unión de conjuntos") 
    print("2- Diferencia de conjuntos")
    print("3- Verificar si dos conjuntos son iguales")

    opcion = int(input("Ingrese la opción deseada: "))

    if opcion == 1:
        C = A + B
        print("Unión de conjuntos:", C)

    elif opcion == 2:
        C = A - B
        print("Diferencia de conjuntos:", C)

    elif opcion == 3:
        if A == B:
            print("Los conjuntos son iguales")
        else:
            print("Los conjuntos son diferentes")

    else:
        print("Opción inválida. Por favor, elija una opción del menú.")




