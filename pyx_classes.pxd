cdef class Particle:
    cdef:
        public double x, y, mass, radius, volume, torque
        public double[2] velocity, force, momentum
        public int active
<<<<<<< HEAD:cython_particle.pxd
=======

cdef class Sun:
    cdef:
        public double x, y, mass, radius
>>>>>>> 8b7db69876a795c35211b4cead09408ca8f3a303:pyx_classes.pxd
