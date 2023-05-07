class Alumno:

    def __init__(self, dni, surname, name, career, year):
        self.__dni = dni
        self.__surname= surname
        self.__name= name
        self.__career=career
        self.__year=year
    
    def __str__(self):
        return 'f({self.__dni},{self.__surname}, {self.__name}, {self.__career}, {self.__year})'
    def getdni(self):
        return self.__dni
    def getsurname(self):
        return self.__surname
    def getname(self):
        return self.__name
    def getcareer(self):
        return self.__career
    def getyear(self):
        return self.__year
    
    def __lt__(self, other):
        if self.__year == other.__year:
            if self.__surname == other.__surname:
                return self.__name < other.__name
            else:
                return self.__surname < other.__surname
        
        else: 
            return self.__year < other.__year
