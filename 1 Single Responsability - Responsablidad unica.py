"""
La funcionalidad principal de esta clase es definir un pato. 
Si hay que cambiar esta definición, se cambiará esta clase. 
El problema yace en el método greet(), que se encarga de poder 
hablar con otros patos. Si se quisiera cambiar la funcionalidad 
de la conversación entre patos, se estaría cambiando también la 
clase Duck, es decir, habría una razón adicional para cambiar la 
clase. Las consecuencias de no respetar este principio pueden ser 
varias, como dificultar la depuración de errores, ya que varios 
errores apuntan al mismo sitio y las funcionalidades están más acopladas.
"""

class Duck:   
    def __init__(self, name):
        self.name = name
   
    def fly(self):
        print(f"{self.name} is flying not very high")

    def swim(self):
        print(f"{self.name} swims in the lake and quacks")

    def do_sound(self) -> str:
        return "Quack"

    def greet(self, duck2):
        print(f"{self.name}: {self.do_sound()}, hello {duck2.name}")

"""
Para resolver este problema en el caso del ejemplo, 
se define una nueva clase Communicator que se encarga 
de toda la funcionalidad de comunicación. 
Esta nueva clase permite entablar una conversación entre dos patos, 
donde estos se saludan. De esta manera, se ha cambiado el 
funcionamiento de la comunicación sin que la clase Duck se haya visto afectada.
"""

class Duck:
   
    def __init__(self, name):
        self.name = name
   
    def fly(self):
        print(f"{self.name} is flying not very high")

    def swim(self):
        print(f"{self.name} swims in the lake and quacks")

    def do_sound(self) -> str:
        return "Quack"

class Communicator:

    def __init__(self, channel):
        self.channel = channel

    def communicate(self, duck1 : Duck, duck2: Duck):
        sentence1 = f"{duck1.name}: {duck1.do_sound()}, hello {duck2.name}"
        sentence2 = f"{duck2.name}: {duck2.do_sound()}, hello {duck1.name}"
        conversation = [sentence1, sentence2]
        print(*conversation,
              f"(via {self.channel})",
              sep = '\n')