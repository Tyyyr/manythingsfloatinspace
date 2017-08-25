# -*- coding: utf8 -*-
import numpy as np
from classes import Teilchen
from config import *

def init_particle_list(n,width,height):
	"""
	Gibt eine Liste von n Teilchen-Objekten zurück.
	"""
	temp = []
	for i in xrange(n):
		phi = 2 * np.random.random() * np.pi
		radius = np.random.normal(2.6, 0.2) * AE
		vel = np.sqrt(G * 1.989e30/radius)
		temp.append(Teilchen(phi, radius, vel))
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
		f_x = G*(((part_1.mass * part_2.mass)/l**3)*(part_2.x - part_1.x))
		f_y = G*(((part_1.mass * part_2.mass)/l**3)*(part_2.y - part_1.y))
		f_ges = [f_x,f_y]
		return np.array(f_ges)

	elif l <= min_radius:
		part_1.actualize(part_2)
		return part_1.momentum/dt

def get_force_matrix(liste_part):
	"""
	Gibt eine Matrix, welche mit den Gravitationskräften zwischen den
	einzelnen Teilchen gefüllt ist, zurück.
	"""
	temp = init_matrix(len(liste_part),object)
	for i,part_1 in enumerate(liste_part):
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

def get_torque(part_1, part_2):
	"""
	Drehimpulsberechnung für neu entstandenes Teilchen nach Kollision
	"""
	newpoint_x = (part_1.mass * part_1.x + part_2.mass * part_2.x) / (part_1.mass + part_2.mass)
	newpoint_y = (part_1.mass * part_1.y + part_2.mass * part_2.y) / (part_1.mass + part_2.mass)
	newpoint = ([newpoint_x, newpoint_y]) 		#Schwerpunkt zwischen beiden Teilchen

	r_1 = ([part_1.x - newpoint_x, part_1.y - newpoint_y])		#Richtungsvektoren
	r_2 = ([part_2.x - newpoint_x, part_2.y - newpoint_y])

	torq_1 = part_1.mass * np.cross(r_1, part_1.velocity) 		#Drehimpulse der einzelnen Teilchen zum Schwerpunkt
	torq_2 = part_2.mass * np.cross(r_2, part_2.velocity)
	torq = torq_1 + torq_2 		#Gesammtdrehimpuls (+ Eigendrehimpulse falls vorhanden)
	return newpoint, torq
