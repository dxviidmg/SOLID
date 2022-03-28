"""
Una interfaz es una descripción de los comportamientos 
que puede realizar un objeto. Por ejemplo, cuando presiona 
el botón de encendido en el control remoto del televisor, 
enciende el televisor y no necesita preocuparse de cómo.

Python usa clases abstractas como interfaces 

El principio de segregación de interfaces aconseja que 
las interfaces sean pequeñas en términos de cohesión.

Cree interfaces detalladas que sean específicas del 
cliente. No se debe obligar a los clientes a implementar 
interfaces que no utilizan.

"""
from abc import ABC, abstractmethod


class Movible(ABC):
    @abstractmethod
    def go(self):
        pass


class Volable(Movable):
    @abstractmethod
    def fly(self):
        pass


class Avion(Flyable):
    def go(self):
        print("Taxiing")

    def fly(self):
        print("Flying")


class Carro(Movable):
    def go(self):
        print("Going")