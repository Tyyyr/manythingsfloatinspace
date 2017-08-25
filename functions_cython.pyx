import numpy as np
cimport numpy as np

G = 6.673e-11
float64 = np.dtype(np.float64_t)

cdef float64 get_abstand(float64 x1, float64 x2, float64 y1, float64 y2):
    	return ((x1-x2)**2 + (y1-y2)**2)**0.5

cdef float64 get_force():
    cdef float64[:] f_ges = np.zeros(2, dtype=np.float64)
    # min_radius = part_1.radius + part_2.radius
    r = get_abstand(part_1,part_2)
    if l > min_radius:
        f_x = G*(((part_1.mass * part_2.mass)/r**3)*(part_2.x - part_1.x))
        f_y = G*(((part_1.mass * part_2.mass)/r**3)*(part_2.y - part_1.y))
        f_ges = [f_x,f_y]
        return np.array(f_ges)

    elif l <= min_radius:
        part_1.actualize(part_2)
        return part_1.momentum/dt
