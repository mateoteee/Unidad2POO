from viajero2 import FrequentTrav
import csv

class TravList():
    
    def __init__(self):
        self.__list = []
    
    def instantiateFromCSV(self,csv_file):
        with open(csv_file, 'r') as f:
            reader = csv.reader(f)
            list_travelers = list(reader)
        
        for traveler in list_travelers:
            if((traveler[0] != None) and 
               (traveler[1] != None) and 
               (traveler[2] != None) and 
               (traveler[3] != None) and 
               (traveler[4] != None)):
                instance = FrequentTrav(num = int(traveler[0]),dni = int(traveler[1]),name = traveler[2],surname = traveler[3],miles = int(traveler[4]))
                self.__list.append(instance)
                
    def get_len(self):
        return len(self.__list)
    
    def list(self,i):
        return self.__list[i]
        
    def __iter__(self):
        return iter(self.__list)
    
    def __add__(self, other):
        if isinstance(other, int):
            return TravList([i + other for i in self.__list])
        elif isinstance(other, FrequentTrav):
            return TravList(self.__list + [other])
        elif isinstance(other, TravList):
            return TravList(self.__list + other.__list)
        else:
            raise TypeError(f"unsupported operand type(s) for +: 'TravList' and '{type(other)}'")
    
    def __sub__(self, other):
        if isinstance(other, int):
            return TravList([i - other for i in self.__list])
        elif isinstance(other, FrequentTrav):
            return TravList([i for i in self.__list if i != other])
        elif isinstance(other, TravList):
            return TravList([i for i in self.__list if i not in other.__list])
        else:
            raise TypeError(f"unsupported operand type(s) for -: 'TravList' and '{type(other)}'")
        
    def max_miles(self):
        if len(self.__list) > 0:
            max_miles = self.__list[0].get_Miles()
            for traveler in self.__list:
                if traveler.get_Miles() > max_miles:
                    max_miles = traveler.get_Miles()
            return [traveler for traveler in self.__list if traveler.get_Miles() == max_miles]