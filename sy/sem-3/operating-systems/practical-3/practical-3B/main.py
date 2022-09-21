import random
import threading
import time

rw_mutex = threading.Semaphore(1)
mutex = threading.Semaphore(1)
read_count = 0


def Reader(thread_name:str):
    global rw_mutex, mutex, read_count

    while True:
    

        mutex.acquire()
        read_count += 1

        if read_count == 1: 
            rw_mutex.acquire()

        mutex.release()

        file = open("file.txt", "r")
        print(f"Started reading - {thread_name} \n" + file.read() + f"\n Finished Reading {thread_name}")
        file.close()


        mutex.acquire()
        read_count -= 1
        if read_count == 0:
            rw_mutex.release()
        mutex.release()


        time.sleep(random.randrange(2,4))

def Writer(thread_name:str):
    global rw_mutex, mutex, read_count
    

    while True:

        print(f"Writing to file - {thread_name}")
        rw_mutex.acquire()
        file = open("file.txt", "a")
        file.write(str(random.randrange(1, 100)))
        file.write("\n")
        file.close()
        rw_mutex.release()
        print(f"Finished Writing - {thread_name}")
        

        time.sleep(random.randrange(5,10))



threading.Thread(target=Reader, args=("Reader 1", )).start()
threading.Thread(target=Reader, args=("Reader 2", )).start()
threading.Thread(target=Writer, args=("Writer 1",)).start()