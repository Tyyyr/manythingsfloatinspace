import numpy as np
from time import time

def f():
    for t in range(10000):
        vectors = np.zeros((10000, 3), dtype=np.float64)
        for i in range(10000):
            vectors[i] = [i**0.5, i, i**1.5]
    return vectors

start = time()
x = f()
print time()-start
