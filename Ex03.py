import threading 
import time 
import random


def correr(id, distancia_maxima):

    distancia = 0

    tamanho_maximo = random.randint(1, 5)
     
    while distancia < distancia_maxima:

        salto = random.randint(0, tamanho_maximo)
        distancia = distancia + salto 

        print( "Sapo", id,  "pulou", salto, "cm")
        print("Distância_percorrida:", distancia, "cm")

        time.sleep(0.2)

    print("Sapo", id, "CHEGOU!")

threads = []

distancia_maxima = 30
for i in range (1, 6):

    t = threading.Thread(target=correr, args=(i, distancia_maxima))

    threads.append(t)
    t.start()

for t in threads:
    t.join()

print("FIM DA CORRIDA!")

