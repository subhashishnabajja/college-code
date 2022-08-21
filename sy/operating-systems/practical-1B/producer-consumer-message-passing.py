import threading 
import random
import time
import queue


queue = queue.Queue(10)

def Producer():
    while True:
        item = random.randint(1, 100)
        print(f"Produced : {item}")
        queue.put(item)
        time.sleep(random.random())


def Consumer():
    while True:
        num = queue.get()
        queue.task_done()
        print(f"Consumed : {num}")
        time.sleep(random.randint(2, 5))

t1 = threading.Thread(target=Producer)
t2 = threading.Thread(target=Consumer)


t1.start()
t2.start()

t1.join()
t2.join()
queue.join()