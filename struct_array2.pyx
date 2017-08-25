import numpy as np
cimport numpy as np

def f():
    cdef double[3] vectors[10000]
    for t in range(10000):
        for i in range(10000):
            vectors[i] = [i**0.5, i, i**1.5]
    return vectors
