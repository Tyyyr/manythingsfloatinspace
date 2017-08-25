cdef extern from "cfib.h":
    double cfib "cfib"(int n)

def fib(int n):
    return cfib(n)
