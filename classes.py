import numpy as np
from config import *

class Teilchen(object):
	
	def __init__(self, phi, radius, vel):
		self.x = np.cos(phi) * radius
		self.y = np.sin(phi) * radius
		self.velocity = vel * np.array([-np.sin(phi), np.cos(phi)])
		self.force = np.array([0.,0.])

		self.mass = np.random.randint(1,100) * 1e15
		self.radius = np.random.uniform(3.,5.) * 1e4
		self.volume = 4/3 * np.pi * self.radius**3
		self.momentum = self.velocity * self.mass
		self.torque = 0
		self.colour = (100,100,100)
		self.active = True

	def move(self):
		self.x += 0.5 * self.velocity[0] * dt
		self.y +=  0.5 * self.velocity[1] * dt
		self.velocity[0] += dt * self.force[0]/self.mass
		self.velocity[1] += dt * self.force[1]/self.mass
		self.x += 0.5 * self.velocity[0] * dt
		self.y +=  0.5 * self.velocity[1] * dt

	def actualize(self, other):
		self.momentum = (self.mass * self.velocity + other.mass * other.velocity)/(self.mass + other.mass)
		self.mass += other.mass
		self.volume += other.volume
		self.radius = np.cbrt((3*self.volume)/(4*np.pi))
		self.velocity = self.momentum/self.mass
		other.active = False
		other.color = (10,10,10)

class Planet(object):

    def __init__(self,color):
        self.x = 1.49e11
        self.y = 0.
        self.radius = 10
        self.mass = 5.97e24
        self.velocity = np.array([0.,2.978e4])
        self.force = np.array([0,0])
        self.colour = (color)

    # leapfrog method for DE-solving
    def move(self):
        self.x += 0.5 * self.velocity[0] * dt
        self.y +=  0.5 * self.velocity[1] * dt
        self.velocity += self.force/self.mass * dt
        self.x += 0.5 * self.velocity[0] * dt
        self.y +=  0.5 * self.velocity[1] * dt

class Sun(object):
    def __init__(self):
        self.x = 0
        self.y = 0
        self.radius = 20
        self.mass = 1.989e30
        self.colour = (255,255,0)
