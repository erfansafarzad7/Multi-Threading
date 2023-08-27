from threading import Thread, currentThread, enumerate
from time import sleep, perf_counter
import sys

start = perf_counter()


def show(name):
    print(f'Starting {name}\n')
    print(currentThread().getName())
    print(currentThread().ident)
    print(enumerate())
    sleep(3)
    print(f'Finishing {name}\n')


t1 = Thread(target=show, args=('One', ), daemon=False, name='First Thread Named')
t2 = Thread(target=show, args=('Two', ), daemon=False)

t1.start()
t2.start()
end = perf_counter()
print(round(end - start))
sys.exit()
