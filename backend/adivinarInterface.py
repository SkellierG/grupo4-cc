from abc import ABC, abstractmethod

class Iadivinar(ABC):
    
    def __init__(self):
        self.number = 0

    @abstractmethod
    def getNumber(self):
        # {
        #     hidennumber: int
        # }
        # devuelve el numero escondido de ser necesario
        # se puede usar en otros metodos para evitar redundancia
        pass
    
    @abstractmethod
    def setNumber(self):
        # {
        #     created: bool
        # }
        # crea el numero escondido que hay que adiviinar y devuelve si este
        # se ha creado
        # puede no devolver nada
        pass

    @abstractmethod
    def compareNumbers(self, number):
        # input: int

        # {
        #     feedback: str
        # }
        # compara los numeros y baja el contador de intentos
        # llama a feedback y segun eso se devuelve un string
        # el string debe decir si es mayor o menor y en caso
        # de que sea el numero debe de entregar el numero escondido y que acerto
        pass

    @abstractmethod
    def feedback(self, who, number):
        # aqui estan todos los estados posibles de los string
        # osea los mensajes de feedback, anade solo el numero en caso
        # de acertar, esto se devuelve a compare numbers, al ser logica
        # interna no te voy a pedir un return especifico
        pass

    @abstractmethod
    def refresh(self):
        # resetea todo como si fuera recien ejecutado
        pass

