import threading
import time

def executar(id):
    time.sleep(0.5)
    print("Thread #" + str(id))


threads = []
for i in range(1, 6):
    t = threading.Thread( target=executar , args=(i,))
    threads.append(t)
    t.start()

for t in threads:
    t.join()

