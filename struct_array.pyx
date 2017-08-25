import numpy as np
cimport numpy as np

ctypedef class Vec3d:
    cdef double x, y, z

def f():
    vectors = np.zeros(10000, dtype=object)
    for i in range(10000):
        vectors[i] = Vec3d(i**0.5, i, i**1.5)
    return vectors
