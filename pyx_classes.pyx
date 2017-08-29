import numpy as np
cimport numpy as np
from config import *

cdef class Particle:

    def __init__(self, phi, radius, vel):
        self.x = np.cos(phi) * radius
        self.y = np.sin(phi) * radius
        self.velocity = vel * np.array([-np.sin(phi), np.cos(phi)])
        self.force = np.array([0.,0.])
        self.mass = np.random.randint(1,100) * 1e15
        self.radius = np.random.uniform(3.,5.) * 1e9
        self.volume = 4/3 * np.pi * self.radius**3
        self.momentum[0] = self.velocity[0] * self.mass
        self.momentum[1] = self.velocity[1] * self.mass
        self.torque = 0
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
        other.active = 0

cdef class Sun:

    def __init__(self):
        self.x = 0
        self.y = 0
        self.radius = 6.957e8
        self.mass = 1.989e30
