import pyximport
pyximport.install()

from cfib_wrapper import fib

print fib(10)
