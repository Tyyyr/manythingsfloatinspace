from numpy import dtype, float64

c_float = dtype(float64)

background_colour = (10, 10, 10)
(width, height) = (1000, 600)
TITLE = "SUPER COOLE WELTRAUMSIMULATION!!!!!!"

G = 6.673e-11
AE = 1.496e11

dt = 3600
n = 100

#todo: cython get_force, get_abstand, get_force_matrix
