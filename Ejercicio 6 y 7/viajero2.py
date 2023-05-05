import csv

class FrequentTrav():
    def __init__(self, num = None, dni = None, name = None, surname = None, miles = None):
        self.__num = num
        self.__dni = dni
        self.__name = name
        self.__surname = surname
        self.__miles = miles
    
    def get_Num(self):
        return int(self.__num)
    
    def get_Miles(self):
        return self.__miles
    
    def accumulateMiles(self, miles):
        self.__miles += miles
        return self.__miles
    
    def redeemMiles(self, miles):
        if miles <= self.__miles:
            self.__miles -= miles
            print(f"\nSe canjearon exitosamente {miles} millas")
        else:
            print(f"\nERROR: Millas insuficientes, no se pudo realizar correctamente la operacion")
        return self.__miles
    
    def __gt__(self, other):
        return self.__miles > other.__miles
    
    def __eq__(self, other):
        if type(other) == int:
            return self.__miles == other
        elif type(other)== FrequentTrav:
            return self.__miles == other.__miles


    def __radd__(self, other):
        if type(other) == int:
            self.miles += other
            return self

    def __rsub__(self, other):
        if type(other) == int:
            self.miles = other - self.miles
            return self