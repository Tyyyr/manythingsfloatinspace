from numpy import dtype, float64

acc_vars = ["x", "y", "velocity", "force", "mass", "radius",
            "volume", "momentum", "active"]

c_float = dtype(float64)

background_colour = (10, 10, 10)
(width, height) = (1000, 600)
TITLE = "SUPER COOLE WELTRAUMSIMULATION!!!!!!"

G = 6.673e-11
AE = 1.496e11

dt = 3600
n = 1000
