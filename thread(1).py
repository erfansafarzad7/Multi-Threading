from threading import Thread
from time import sleep, perf_counter


start = perf_counter()


def show(name):
    print(f'starting {name}')
    sleep(3)
    print(f'starting {name}')


t1 = Thread(target=show, args=('One', ))
t2 = Thread(target=show, args=('Two', ))

t1.start()
t2.start()

t1.join()
t2.join()

end = perf_counter()

print(round(end - start))
