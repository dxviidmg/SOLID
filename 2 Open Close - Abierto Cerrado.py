"""
El Principio de Abierto/Cerrado indica que 
las clases deberían estar abiertas para su 
extensión, pero cerradas para su modificación.
"""
from abc import ABC
class AbstractForma(ABC):
    def area(self):
        pass

class Rectangulo(AbstractForma):
    def __init__(self, alto, ancho):
        self.alto = alto
        self.ancho = ancho

    def area(self):
        return self.alto * self.ancho


class Triangulo(AbstractForma):
    def __init__(self, alto, ancho):
        self.alto = alto
        self.ancho = ancho

    def area(self):
        return self.alto * self.ancho / 2


class CalculadorArea():
    def calcula_area(formas):

        for forma in formas:
            print(forma.area())
    
    def calcula_area_2(forma: AbstractForma):
        return forma.area()


t1 = Triangulo(1, 1)
t2 = Triangulo(2, 1)
r1 = Rectangulo(1, 1)
r2 = Rectangulo(2, 1)

figuras = [t1, t2, r1, r2]

CalculadorArea.calcula_area(figuras)
CalculadorArea.calcula_area_2(t1)