from libc.math cimport sqrt
import numpy as np
cimport numpy as np
from config import *
from pyx_classes cimport Particle

ctypedef np.float64_t FLOAT64;

cdef get_force(Particle body1, Particle body2, FLOAT64[:] force):

    cdef FLOAT64 min_radius = body1.radius + body2.radius
    cdef FLOAT64 l = sqrt((body1.x - body2.x)**2 + (body1.y - body2.y)**2)

    if l > min_radius:
        force[0] = G * (((body1.mass * body2.mass)/l**3) * (body2.x - body1.x))
        force[1] = G * (((body1.mass * body2.mass)/l**3) * (body2.y - body1.y))

    else:
        body1.actualize(body2)
        return [body1.momentum[0]/dt, body1.momentum[1]/dt]

cpdef FLOAT64[:,:,:] get_force_matrix(data):

    cdef FLOAT64[:,:,:] temp = np.zeros((n, n, 2), dtype=np.float64)
    cdef int i, j

    for i, part_1 in enumerate(data):
        for j, part_2 in enumerate(data):
            if part_1.active == 0 or part_2.active == 0:
                temp[i][j][:] = 0.
                temp[j][i][:] = 0.
            elif i < j:
                get_force(part_1, part_2, temp[j][i][:])
            elif i == j:
                temp[i][j][:] = 0.
    return temp
