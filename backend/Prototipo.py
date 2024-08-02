import random
class JuegoAdivinarNumero:
    def __init__(self,numeroRandom,intentosMaximos=3):
        self.numeroRandom = random.randint(1,50)
        self.intentosMaximos = intentosMaximos
        self.intentos = 0
    def Bienvenida(self):
        print("""Que tal usuario :D !!!         
        Bienvenido al juego de Adivanzas de Numeros
        OJO: El numero random ha adivinar va desde 1 al 50
        """) 
        print(self.numeroRandom)