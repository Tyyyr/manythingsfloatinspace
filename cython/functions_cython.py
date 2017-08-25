# -*- coding: utf8 -*-
import pyximport
import numpy as np
pyximport.install(setup_args={"include_dirs":np.get_include()})
from config import *

from pyx_functions import get_force_matrix
from cython_particle import Particle

def init_particle_list(n):
	"""
	Gibt eine Liste von n Teilchen-Objekten zurück.
	"""
	temp = []
	for i in xrange(n):
		phi = 2 * np.random.random() * np.pi
		radius = np.random.normal(2.6, 0.2) * AE
		vel = np.sqrt(G * 1.989e30/radius)
		temp.append(Particle(phi, radius, vel))
	return temp

def total_force_per_part(force_mat,i):
	"""
	Gibt die Gesamtkraft, die auf ein Teilchen wirkt, zurück.
	"""
	return np.sum(force_mat[i],axis = 0)

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
