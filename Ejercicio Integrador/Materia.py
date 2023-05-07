class Materia:

    def __init__(self, dni, nombreMateria,date,nota,aprobacion):
        self.__dni=dni
        self.__nombreMateria=nombreMateria
        self.__date=date
        self.__nota=nota
        self.__aprobacion=aprobacion
    
    def getdni(self):
        return self.__dni
    def getnombreMateria(self):
        return self.__nombreMateria
    def getdate(self):
        return self.__date
    def getnota(self):
        return self.__nota
    def getaprobacion(self):
        return self.__aprobacion
    
    