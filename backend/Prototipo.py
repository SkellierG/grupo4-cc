import random
class JuegoAdivinarNumero:
    def __init__(self,valorminimo = 1,valormaximo = 50,intentosMaximos=3):
        self.valorminimo = valorminimo
        self.valormaximo = valormaximo
        self.numeroRandom = random.randint(self.valorminimo,self.valormaximo)
        self.intentosMaximos = intentosMaximos
        self.intentos = 0
        
    def Bienvenida(self):
        return {
            "message": """Que tal usuario :D !!!         
            Bienvenido al juego de Adivanzas de Numeros
            OJO: El numero random ha adivinar va desde 1 al 50
            """}
        
    def SolicitarNumero(self):
        while (self.intentos < self.intentosMaximos):
            print(f"Numero de intento: ", (self.intentos+1))
            try:
                respuesta = int(input("Ingrese Numero: "))
                if (respuesta < self.valorminimo or respuesta > self.valormaximo):
                    print("ERROR! Ingresa numero valido")
            except ValueError:
                print("ERROR! Ingresa numero valido")
                
    def Resultado(self):
        return {"message": f"Has agotado tus {self.intentosMaximos} intentos :( ----> El numero era: {self.numeroRandom}"}
    
    def juego(self):
        self.Bienvenida()
        while (self.intentos <= self.intentosMaximos):
            respuesta = self.SolicitarNumero()
            self.intentos += 1
            if respuesta == self.numeroRandom:
                return{"message": """Felicidades! Adivinaste el Numero! Solo te tomo {self.intentos} intentos xd
                Fin del juego..."""}
            elif respuesta > self.numeroRandom:
               return{"message": "El numero ingresado es mayor al numero random"}
            elif respuesta < self.numeroRandom:
                return{"message": "El numero ingresado es menor al numero random"}
            
        if self.intentos >= self.intentosMaximos and respuesta != self.numeroRandom:
            return self.Resultado
juegoIniciar =  JuegoAdivinarNumero()
juegoIniciar.juego()