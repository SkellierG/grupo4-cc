# aqui tienes que hacer el nuevo modulo con todo lo necesario segun
# la interfaz, cualquier cosa me pregunta, recuerda que esto va a ser
# usado en un a interfaz html no un CLI (linea de comandos), hazlo teniendo
# esto en cuenta
import random
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
        return {'hiddennumber': self.hidden_number}
    
    def setNumber(self):
        self.refresh()
        self.hidden_number = random.randint(self.valorminimo, self.valormaximo)
        self.intentos = self.intentosMaximos
        return {'created': True}
    
    def compareNumbers(self, number):
        self.intentos -= 1
        feedback = self.feedback(number)
        if feedback.get('f') == True:
            return {'feedback': feedback.get('d'), 'finded': True}
        
        return {'feedback': feedback.get('d'), 'finded': False}
    
    def feedback(self, number):
        if self.intentos <= 0:
            return { 'd': f"Perdiste, Fin del juego! El número era: {self.hidden_number}" , 'f': False }
            self.refresh()
        if number < self.hidden_number:
            return { 'd': "El número es mayor.", 'f': False }
        elif number > self.hidden_number:
            return { 'd': "El número es menor.", 'f': False }
        else:
            return { 'd': f"¡Has acertado! El número escondido era {self.hidden_number}.", 'f': True }
    
    def refresh(self):
        self.hidden_number = None
        self.intentos = 0