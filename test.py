from config import *
from functions import *
from graphic_functions import *
from colorset import *
from classes import Teilchen, Sun
import pygame
import matplotlib.pyplot as plt

test_pos = []

liste_teilchen = init_particle_list(100,width,height)
for i in liste_teilchen:
	i.velocity = np.array([0,0])
	i.x = np.random.randint(-100,100) *5e9
	i.y = np.random.randint(-100,100) *5e9
	#print i.x, " , ", i.y
	#print i.velocity
	#print "----"



screen = pygame.display.set_mode((width, height))
pygame.display.set_caption(TITLE)

#sonne = Sun()

massen = color_list(liste_teilchen)
hmass = massen[0]
mmass = massen[1]

#for counter in xrange(500):
running = True
while running:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			running = False

	#graphics
	screen.fill(background_colour)
	#draw2(sonne, screen)
	for particle in liste_teilchen:
		if particle.active == True:
			draw(particle, screen)
	pygame.display.update()
	
	massen = color_list(liste_teilchen)
	hmass = massen[0]
	mmass = massen[1]

	#values
	force_matrix = get_force_matrix(liste_teilchen)
	for a, particle in enumerate(liste_teilchen):
		particle.force = total_force_per_part(force_matrix,a)# + get_force(particle, sonne)
		particle.move()
		particle.colour = fcolorset(particle, hmass, mmass)
		if a == 0:
			test_pos.append([particle.force[0], particle.force[1]])
	

plt.plot(test_pos)
plt.show()












