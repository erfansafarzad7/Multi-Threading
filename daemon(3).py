from threading import Thread
from time import sleep, perf_counter
import sys

start = perf_counter()


def show(name):
    print(f'Starting {name}\n')
    sleep(3)
    print(f'Finishing {name}\n')


t1 = Thread(target=show, args=('One', ), daemon=False)
t2 = Thread(target=show, args=('Two', ), daemon=False)

t1.start()
t2.start()

end = perf_counter()

print(round(end - start))
sys.exit()
