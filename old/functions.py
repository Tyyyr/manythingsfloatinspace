# -*- coding: utf8 -*-
import numpy as np
import matplotlib.pyplot as plt
from scipy import constants as const

zeitschritt = 10000
c_float = np.dtype(np.float64)

class Teilchen(object):
	def __init__(self,m = np.random.normal(10**12,10**2)):
		self.x = 100000*np.random.normal()
		self.y = 100000*np.random.normal()
		self.mass = m
		self.density = np.random.normal(950,50)
		self.velocity = np.array([0.,0.])
		self.force = np.array([0.,0.])
		self.volume = self.mass/self.density
		self.radius = np.cbrt(3*self.volume/(4*np.pi))
		self.pulse = [0.,0.]
		self.active = True
	def actualize(self):
		self.radius = np.cbrt(3*self.volume/(4*np.pi))

class Planet(object):
	def __init__(self,m = 5 * 10**24):
		self.x = 0
		self.y = 0
		self.mass = m
		self.radius = 6371000

def init_particle_list(n):
	"""
	Gibt eine Liste von n Teilchen-Objekten zurück.
	"""
	temp = []
	for i in xrange(n):
		temp.append(Teilchen())
	return temp

def init_matrix(n,datatype = c_float):
	"""
	Gibt eine mit Nullen gefüllte n x n Matrix mit einem spezifiziertem
	Datentyp (standardmäßig float) zurück.
	"""
	return np.zeros((n,n),dtype = datatype)

def get_force(part_1,part_2):
	"""
	Berechnet die Kraft zwischen zwei Körpern in x- und y-Richtung.
	"""
	min_radius = part_1.radius + part_2.radius
	l = get_abstand(part_1,part_2)
	if l > min_radius:
		f_x = const.G*(((part_1.mass * part_2.mass)/l**3)*(part_2.x - part_1.x))
		f_y = const.G*(((part_1.mass * part_2.mass)/l**3)*(part_2.y - part_1.y))
		f_ges = [f_x,f_y]
		return np.array(f_ges)
	elif l <= min_radius:
		part_1.mass += part_2.mass
		part_1.volume += part_2.volume
		part_1.actualize()
		part_2.active = False
		part_2.velocity = [0.,0.]
		part_2.mass = 0
		return part_1.force
		#f_x = const.G*(((part_1.mass * part_2.mass)/min_radius**3)*(part_2.x - part_1.x))
		#f_y = const.G*(((part_1.mass * part_2.mass)/min_radius**3)*(part_2.y - part_1.y))
		#f_ges = [f_x,f_y]
		#return np.array(f_ges)

def get_force_matrix(liste_part):
	"""
	Gibt eine Matrix, welche mit den Gravitationskräften zwischen den
	einzelnen Teilchen gefüllt ist, zurück.
	"""
	temp = init_matrix(len(liste_part),object)
	for i,part_1 in enumerate(liste_part):
		#print "\n", """%s. Teilchen""" % (z+1)
		for j,part_2 in enumerate(liste_part):
			if part_1.active == False or part_2.active == False:
				 temp[i,j] = np.array([0.,0.])
				 temp[j,i] = np.array([0.,0.])
			elif i < j:
				temp[i,j] = get_force(part_1,part_2)
				temp[j,i] = -temp[i,j]
			elif i == j:
				temp[i,j] = np.array([0.,0.])
	return temp

def total_force_per_part(force_mat,i):
	"""
	Gibt die Gesamtkraft, die auf ein Teilchen wirkt, zurück.
	"""
	#temp = np.array([0.,0.])
	#for j in force_mat[i]:
		#temp += j
	return np.sum(force_mat[i],axis = 0)

def get_abstand(part_1,part_2):
	"""
	Bestimmt den Abstand zweier Teilchen zueinander.
	"""
	return np.sqrt((part_1.x-part_2.x)**2 + (part_1.y-part_2.y)**2)

def move(liste_part):
	"""
	Bewegt jedes Teilchen aus der Liste in dem bestimmten Zeitschritt.
	"""
	for i in liste_part:
		i.x += zeitschritt*i.velocity[0]
		i.y += zeitschritt*i.velocity[1]

def get_velocity(liste_part):
	"""
	Bestimmt die Momentangeschwindigkeit des Teilchens
	"""
	for i in liste_part:
		# if i.active == False:

		i.velocity[0] += zeitschritt*i.force[0]/i.mass
		i.velocity[1] += zeitschritt*i.force[1]/i.mass
