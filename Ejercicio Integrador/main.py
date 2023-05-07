from Alumno import Alumno
from Materia import Materia
from ManejadorAlumno import ManejadorAlumno
from ManejadorMateria import ManejadorMateria

if __name__ == '__main__':

    MA=ManejadorAlumno()
    MA.cargar_alumnos('alumnos.csv')
    MM=ManejadorMateria()
    MM.cargarLista('materiasAprobadas.csv')

    print("MENU DE OPCIONES")
    print ("1. Leer por teclado el dni de un alumno e informar sus promedios con aplazos y sin aplazos")
    print ("2. Informar estudiantes q aprobaron de manera promocional una materia")
    print("3. Obtener listado de alumnos ordenado por año q cursan y alfabeticamente por AyP")

    opcion = int (input("INGRESE LA OPCION Q DESEE: "))

    if opcion == 1:
        alum_buscado = input("Ingrese el DNI del alumno")
        print(f"El promedio sin aplazos del alumno con DNI {alum_buscado} es de {MM.PromedioSinAplazos(alum_buscado)}, y su promedio con aplazos es {MM.PromedioConAplazos(alum_buscado)}")
        
    elif opcion == 2:
        materia_buscada = input("Ingrese la materia que desea buscar: ")
        mat = MM.BuscarPorMateriaAprobada(materia_buscada)
        
    elif opcion == 3:
        lista_ordenada = MA.ListaOrdenada()
        print(lista_ordenada)
