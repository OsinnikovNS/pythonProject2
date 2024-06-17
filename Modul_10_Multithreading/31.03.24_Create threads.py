import threading
import time


def num():
    for i in range(1, 11):
        time.sleep(1)
        print(i)


def my_list():
    spisok = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']
    for i in range(10):
        time.sleep(1.001)
        print(spisok[i])


t1 = threading.Thread(target=num)
t2 = threading.Thread(target=my_list)

t1.start()
# t1.join()
t2.start()

