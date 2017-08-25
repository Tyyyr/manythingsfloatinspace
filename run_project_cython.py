from config import *
from functions_cython import *
from graphic_functions import *
from classes import Teilchen, Sun
import pygame

liste_teilchen = init_particle_list(n)
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption(TITLE)

sonne = Sun()

#for _ in xrange(100):
running = True
while running:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			running = False
	#graphics
	screen.fill(background_colour)
	draw2(sonne, screen)
	for particle in liste_teilchen:
		if particle.active == 1:
			draw(particle, screen)
	pygame.display.update()

	#values
	force_matrix = get_force_matrix(liste_teilchen)
	for a, particle in enumerate(liste_teilchen):
		particle.force = total_force_per_part(force_matrix,a) #get_force()
		particle.move()
