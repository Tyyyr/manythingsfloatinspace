cdef class Particle:
    cdef:
        public double x, y, mass, radius, volume, torque
        public double[2] velocity, force, momentum
        public int active

    
