import pyximport
from time import time
import numpy as np

pyximport.install(setup_args={"include_dirs":np.get_include()})
from cyfib import cyfib

def fib(n):
    a, b = 0, 1
    y = np.zeros(n, dtype=np.float64)
    for i in xrange(n):
        a, b = a + b, a
        y[i] = a
    return y

start = time()
x = fib(1000)
end = time()
print start, end

print "erfolg python %f" % (end - start)

start = time()
y = cyfib(1000)
end = time()

print "erfolg cython %f" % (end - start)
