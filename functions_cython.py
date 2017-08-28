# -*- coding: utf8 -*-
import pyximport
import numpy as np
pyximport.install(setup_args={"include_dirs":np.get_include()})
from config import *

from pyx_functions import get_force_matrix
from pyx_classes import Particle

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

def sun_attrac(body):

    force = np.zeros(2, dtype=np.float64)
    l = np.sqrt(body.x**2 + body.y**2)
    if l > 4 * 6.957e8:
        force[0] = G * (((body.mass * 1.989e30)/l**3) * (-body.x))
        force[1] = G * (((body.mass * 1.989e30)/l**3) * (-body.y))
        return force
    else:
        body.active = 0
        return np.array([0.,0.])

def total_force_per_part(force_mat, teil, i):
	"""
	Gibt die Gesamtkraft, die auf ein Teilchen wirkt, zurück.
	"""
	return np.sum(force_mat[i],axis = 0) + sun_attrac(teil)
