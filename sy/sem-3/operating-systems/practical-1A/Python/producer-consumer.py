
from random import randint
import random
import threading
import time

lock = threading.Lock()


shared_var = []
count = 0


def Producer():
    global shared_var, count, lock
    for _ in range(10):
        produced_item = random.randint(0, 100)
        print(f"Produced : {produced_item}")
        lock.acquire()
        shared_var.append(produced_item)
        lock.release()
        count += 1


        time.sleep(random.randint(1,2))



def Consumer():
    global shared_var, lock

    while True:
    
        if count == 10 and len(shared_var) == 0: 
            break

        if not shared_var:
            continue

        lock.acquire()
        print(f"Consumed : {shared_var.pop(0)}")
        lock.release()
 

        time.sleep(random.randint(2, 5))

print("Program started")

t1 = threading.Thread(target = Producer)
t2 = threading.Thread(target = Consumer)

t1.start()
t2.start()

t1.join()
t2.join()

print("Program Ended")