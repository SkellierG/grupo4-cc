import random
intentos = 0
NumeroAleatorio = random.randint(1,50) #---------Se utiliza el .randint para que aparezcan solo enteros, y lo que esta entre parentesis es para crear parametros
print(NumeroAleatorio) #------------Hacer trampa sabiendo el numero random, para verificar
print("""Que tal usuario :D !!!         
Bienvenido al juego de Adivanzas de Numeros
OJO: El numero random ha adivinar va desde 1 al 50
""")        #-----------------Bienvenida
while (intentos <= 3):
    print("Numero de intento: ", intentos)
    print("Ingrese Numero:") #-------------Solicitud de numero
    Respuesta = int(input())
    if (Respuesta <=0):
        print("ERROR! Numero no valido")
        break #---------------------Use el break para terminar el juego / Validacion
    elif(Respuesta >=50):
        print("ERROR! Numero no valido") 
        break #---------------------Use el break para terminar el juego / Validacion
    if(Respuesta == NumeroAleatorio):
        print("Felicidades! Adivinaste el Numero!")
        print("Solo te tomo ", intentos, "intentos xd")
        print("Fin del juego...")
        break 
    elif(Respuesta > NumeroAleatorio):
        print("El numero ingresado es mayor al numero random")
        intentos += 1
    elif(Respuesta < NumeroAleatorio):
        print("El numero ingresado es menor al numero random")
        intentos += 1
if intentos > 3: #--------------Aqui ya acaba el juego, revelando el numero aleatorio
    print("============RESULTADOS============")
    print("Has agotado tus 3 intentos :( ----> El numero era:", NumeroAleatorio)
    print("==================================")