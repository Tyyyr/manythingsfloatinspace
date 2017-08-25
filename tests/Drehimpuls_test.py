# -*- coding: utf8 -*-
from functions import *
import numpy as np
n = 2
liste_teilchen = init_particle_list(n)
part_1,part_2=liste_teilchen
part_1.velocity = np.array([1.,0.])
part_2.velocity = np.array([0.,1.])


def get_torque(part_1, part_2):
	"""
	Drehimpulsberechnung für neu entstandenes Teilchen nach Kollision
	"""
	newpoint_x = (part_1.mass * part_1.x + part_2.mass * part_2.x) / (part_1.mass + part_2.mass)
	newpoint_y = (part_1.mass * part_1.y + part_2.mass * part_2.y) / (part_1.mass + part_2.mass)
	newpoint = ([newpoint_x, newpoint_y]) 		#Schwerpunkt zwischen beiden Teilchen
	print part_1.x,part_1.y
	print part_2.x,part_2.y
	print newpoint
	r_1 = ([part_1.x - newpoint_x, part_1.y - newpoint_y])		#Richtungsvektoren
	r_2 = ([part_2.x - newpoint_x, part_2.y - newpoint_y])
	print r_1
	print r_2
	torq_1 = part_1.mass * np.cross(r_1, part_1.velocity) 		#Drehimpulse der einzelnen Teilchen zum Schwerpunkt
	torq_2 = part_2.mass * np.cross(r_2, part_2.velocity)
	torq = torq_1 + torq_2 		#Gesammtdrehimpuls (+ Eigendrehimpulse falls vorhanden)
	print torq
	return newpoint,torq

for i,part_1 in enumerate(liste_teilchen):
	for j,part_2 in enumerate(liste_teilchen):
		if i < j:
			get_torque(part_1, part_2)
