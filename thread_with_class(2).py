from threading import Thread
from time import sleep, perf_counter


start = perf_counter()


def show(name, delay):
    print(f'Starting {name}')
    sleep(delay)
    print(f'Finishing {name}')


class ShowThread(Thread):
    def __init__(self, name, delay):
        super().__init__()
        self.name = name
        self.delay = delay

    def run(self):
        show(self.name, self.delay)


t1 = ShowThread('One', 3)
t2 = ShowThread('Two', 7)

t1.start()
t2.start()
t1.join()
t2.join()
end = perf_counter()
print(round(end - start))
