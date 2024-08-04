import random
class JuegoAdivinarNumero:
    def __init__(self, valorminimo=1, valormaximo=50, intentosMaximos=3):
        self.valorminimo = valorminimo
        self.valormaximo = valormaximo
        self.numeroRandom = random.randint(self.valorminimo, self.valormaximo)
        self.intentosMaximos = intentosMaximos
        self.intentos = 0
        
    def Bienvenida(self):
        print("""Que tal usuario :D !!!         
        Bienvenido al juego de Adivanzas de Numeros
        OJO: El numero random ha adivinar va desde 1 al 50
        """)
        
    def SolicitarNumero(self):
        while True:
            try:
                respuesta = int(input("Ingrese Numero: "))
                if self.valorminimo <= respuesta <= self.valormaximo:
                    return respuesta
                else:
                    print(f"ERROR! Ingresa un número entre {self.valorminimo} y {self.valormaximo}")
            except ValueError:
                print("ERROR! Ingresa un número válido")
                
    def Resultado(self):
        print(f"Has agotado tus {self.intentosMaximos} intentos :( ----> El numero era: {self.numeroRandom}")
    
    def juego(self):
        self.Bienvenida()
        while self.intentos < self.intentosMaximos:
            print(f"Numero de intento: {self.intentos + 1}")
            respuesta = self.SolicitarNumero()
            self.intentos += 1

            if respuesta == self.numeroRandom:
                print(f"Felicidades! Adivinaste el Numero! Solo te tomó {self.intentos} intentos xd")
                return
            elif respuesta > self.numeroRandom:
                print("El número ingresado es mayor al número random")
            else:
                print("El número ingresado es menor al número random")
        
        self.Resultado()
juegoIniciar = JuegoAdivinarNumero()
juegoIniciar.juego()