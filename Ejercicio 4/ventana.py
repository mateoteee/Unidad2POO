


class Ventana:
    def __init__(self, titulo, x1=0, y1=0, x2=500, y2=500):
        if x1 > x2 or y1 > y2:
            raise ValueError('Las coordenadas del vértice inferior derecho deben ser mayores que las del vértice superior izquierdo')
        self.titulo = titulo
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2

    def moverIzquierda(self, unidades=1):
        if self.x1 - unidades < 0:
            self.x1 = 0
            self.x2 -= unidades - self.x1
        else:
            self.x1 -= unidades
            self.x2 -= unidades

    def moverDerecha(self, unidades=1):
        if self.x2 + unidades > 500:
            self.x2 = 500
            self.x1 += unidades - (self.x2 - 500)
        else:
            self.x1 += unidades
            self.x2 += unidades

    def subir(self, unidades=1):
        if self.y1 - unidades < 0:
            self.y1 = 0
            self.y2 -= unidades - self.y1
        else:
            self.y1 -= unidades
            self.y2 -= unidades

    def bajar(self, unidades=1):
        if self.y2 + unidades > 500:
            self.y2 = 500
            self.y1 += unidades - (self.y2 - 500)
        else:
            self.y1 += unidades
            self.y2 += unidades

    def mostrar(self):
        print('Título: {}'.format(self.titulo))
        print('Vértice superior izquierdo: ({}, {})'.format(self.x1, self.y1))
        print('Vértice inferior derecho: ({}, {})'.format(self.x2, self.y2))

    def getTitulo(self):
        return self.titulo

    def alto(self):
        return self.y2 - self.y1

    def ancho(self):
        return self.x2 - self.x1
