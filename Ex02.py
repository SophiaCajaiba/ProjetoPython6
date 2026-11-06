import threading
import time
import random

def somar(id, valores):

    soma = 0

    for numero in valores:
        soma = soma + numero
        time.sleep(0.2)


    print("Linha", id, "Soma:", soma)


threads = []

for id in range(1,4):

    valores = []

    for i in range(5):
        numero = random.randint(1,100)
        valores.append(numero)

    t = threading.Thread(target=somar, args=(id, valores))


    threads.append(t)
    t.start()

for t in threads:
    t.join()
