from threading import Thread
from concurrent.futures import ThreadPoolExecutor
from time import sleep


def show(name):
    print(f'Starting {name}')
    sleep(3)
    print(f'Finishing {name}')


with ThreadPoolExecutor(max_workers=2) as execute:
    names = ['One', 'Two', 'Three', 'Four']
    execute.map(show, names)

print('Done..')
