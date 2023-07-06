Respuestas_correctas = int(input("Ingrese respuestas correctas "))

Respuestas_incorrectas = int(input("Ingrese respuestas incorrectas "))

Respuestas_blanco = int(input("Ingrese respuestas en blanco "))

puntaje = Respuestas_correctas * 3 + Respuestas_incorrectas * -1

print(puntaje)