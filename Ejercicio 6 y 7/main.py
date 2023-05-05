from viajero2 import FrequentTrav
from manejadorviajero import TravList

if __name__ == '__main__':
   
    travelers = TravList()
    travelers.instantiateFromCSV('travelers.csv')

    
    max_miles = 0
    max_travelers = []
    for traveler in travelers.get_list():
        if traveler > max_miles:
            max_miles = traveler
            max_travelers = [traveler]
        elif traveler == max_miles:
            max_travelers.append(traveler)
    print("Viajero(s) con mayor cantidad de millas acumuladas:")
    for traveler in max_travelers:
        print(traveler)

    
    traveler1 = travelers.list(0)
    traveler2 = travelers.list(1)
    print(f"Antes de acumular millas:\n{traveler1}\n{traveler2}")
    traveler1 += 1000
    traveler2 += 500
    print(f"Después de acumular millas:\n{traveler1}\n{traveler2}")

    
    traveler3 = travelers.list(2)
    print(f"Antes de canjear millas:\n{traveler3}")
    traveler3 -= 200
    print(f"Después de canjear millas:\n{traveler3}")

