from threading import Thread, Lock


num = 0
lock = Lock()


def add():
    global num
    # lock.acquire()
    with lock:
        for _ in range(100000):
            num += 1
    # lock.release()


def subtract():
    global num
    # lock.acquire()
    with lock:
        for _ in range(100000):
            num -= 1
    # lock.release()


t1 = Thread(target=add)
t2 = Thread(target=subtract)

t1.start()
t2.start()

t1.join()
t2.join()

print(num)
