class Conjunto:
    def __init__(self, elementos):
        self.__elementos = elementos

    def __add__(self, otro):
        return Conjunto(self.__elementos.union(otro.__elementos))

    def __sub__(self, otro):
        return Conjunto(self.__elementos.difference(otro.__elementos))

    def __eq__(self, otro):
        return len(self.__elementos) == len(otro.__elementos) and self.__elementos == otro.__elementos

    def __str__(self):
        return str(self.__elementos)