import pyximport
import numpy as np
from time import time
pyximport.install(setup_args={"include_dirs":np.get_include()})

from struct_array import f

start = time()
x = f()
print time()-start

print x


#cython struct   0.007405       103.499095917
#cython array    0.006449       030.424901009
#pure python     0.022174       115.128932953
