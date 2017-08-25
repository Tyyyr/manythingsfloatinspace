import numpy as np
cimport numpy as np

def cyfib(n):
    cdef int i
    cdef np.float64_t a = 0
    cdef np.float64_t b = 1
    cdef np.float64_t[:] y = np.zeros(n, dtype=np.float64)
    for i in range(n):
        a, b = a + b, a
        y[i] = a
    return a
