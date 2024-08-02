import random
class JuegoAdivinarNumero:
    def __init__(self,valorminimo = 1,valormaximo = 50,intentosMaximos=3):
        self.valorminimo = valorminimo
        self.valormaximo = valormaximo
        self.numeroRandom = random.randint(self.valorminimo,self.valormaximo)
        self.intentosMaximos = intentosMaximos
        self.intentos = 0
        
    def Bienvenida(self):
        print("""Que tal usuario :D !!!         
        Bienvenido al juego de Adivanzas de Numeros
        OJO: El numero random ha adivinar va desde 1 al 50
        """) 
        
    def SolicitarNumero(self):
        while (self.intentos <= self.intentosMaximos):
            print("Numero de intento: ", (self.intentos+1))
            try:
                respuesta = int(input("Ingrese Numero: "))
                if (respuesta < self.valorminimo or respuesta > self.valormaximo):
                    print("ERROR! Ingresa numero valido")
                    break
            except ValueError:
                print("ERROR! Ingresa numero valido")