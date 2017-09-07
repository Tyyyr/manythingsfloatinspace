from config import *
from functions import *
from graphic_functions import *
from classes import Teilchen, Sun
from colourset_mass import *
import pygame

liste_teilchen = init_particle_list(n, width, height)
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption(TITLE)

sonne = Sun()

massen = colour_list(liste_teilchen)
hmass = massen[0]
mmass = massen[1]

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
		if particle.active == True:
			draw(particle, screen)
	pygame.display.update()

	colour_list(liste_teilchen)
	hmass = massen[0]
	mmass = massen[1]

	#values
	force_matrix = get_force_matrix(liste_teilchen)
	for a, particle in enumerate(liste_teilchen):
		particle.force = total_force_per_part(force_matrix,a) + get_force(particle, sonne)
		particle.move()
		particle.colour = fcolourset(particle, hmass, mmass)
