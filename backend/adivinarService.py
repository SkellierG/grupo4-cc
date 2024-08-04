# aqui tienes que hacer el nuevo modulo con todo lo necesario segun
# la interfaz, cualquier cosa me pregunta, recuerda que esto va a ser
# usado en un a interfaz html no un CLI (linea de comandos), hazlo teniendo
# esto en cuenta
from adivinarInterface import Iadivinar

class Sadivinar(Iadivinar):
    def __init__(self, valorminimo=1, valormaximo=50, intentosMaximos=3):
        super().__init__()
        self.valorminimo = valorminimo
        self.valormaximo = valormaximo
        self.intentosMaximos = intentosMaximos
        self.intentos = 0
        self.hidden_number = None
    
    def getNumber(self):
        return {'hidden_number': self.hidden_number}
    
    def setNumber(self):
        self.hidden_number = random.randint(self.valorminimo, self.valormaximo)
        self.intentos = self.intentosMaximos
        return {'created': True}
    
    def compareNumbers(self, number):
        self.intentos -= 1
        feedback = self.feedback(number)
        return {'feedback': feedback}
    
    def feedback(self, number):
        if number < self.hidden_number:
            return "El número es mayor."
        elif number > self.hidden_number:
            return "El número es menor."
        else:
            return f"¡Has acertado! El número escondido era {self.hidden_number}."
    
    def retry(self):
        self.hidden_number = None
        self.intentos = 0