import numpy as np
cimport numpy as np
from config import *

cdef class Particle:
    cdef public double x, y, mass, radius, volume, torque
    cdef public double[2] velocity, force, momentum
    cdef public int active

    def __init__(self, phi, radius, vel):
        self.x = np.cos(phi) * radius
        self.y = np.sin(phi) * radius
        self.velocity = vel * np.array([-np.sin(phi), np.cos(phi)])
        self.force = np.array([0.,0.])
        self.mass = np.random.randint(1,100) * 1e15
        self.radius = np.random.uniform(3.,5.) * 1e4
        self.volume = 4/3 * np.pi * self.radius**3
        self.momentum[0] = self.velocity[0] * self.mass
        self.momentum[1] = self.velocity[1] * self.mass
        self.torque = 0
        # self.colour = (100,100,100)
        self.active = 1

    def move(self):
        self.x += 0.5 * self.velocity[0] * dt
        self.y +=  0.5 * self.velocity[1] * dt
        self.velocity[0] += dt * self.force[0]/self.mass
        self.velocity[1] += dt * self.force[1]/self.mass
        self.x += 0.5 * self.velocity[0] * dt
        self.y +=  0.5 * self.velocity[1] * dt

    def actualize(self, other):
        self.momentum[0] = (self.mass * self.velocity[0] + other.mass
        * other.velocity[0])/(self.mass + other.mass)
        self.momentum[1] = (self.mass * self.velocity[1] + other.mass
        * other.velocity[1])/(self.mass + other.mass)
        self.mass += other.mass
        self.volume += other.volume
        self.radius = np.cbrt((3*self.volume)/(4*np.pi))
        self.velocity[0] = self.momentum[0]/self.mass
        self.velocity[1] = self.momentum[1]/self.mass
        other.active = False
        other.color = (10,10,10)
