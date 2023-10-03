
import time
import random

f = open('out.txt', 'w')


def gen(size):
    ar = []
    for i in range(size):
        ar.append(random.randint(0, 9))
    return ar


def test(iterr, size):
    start = time.time()
    for i in range(iterr):
        gen(size)
    end = (time.time() - start) / iterr

    print(f'{size};{round(end, 5)}', file=f)

i = 1000
while i < 100000:
    test(100, i)
    i += 1000