import numpy as np
import pygame
from functions import get_force

class Asteorid(object):
	def __init__(self,phi,radius):
		self.x = np.cos(phi) * radius
		self.y = np.sin(phi) * radius
		self.radius = np.random.randint(1,3)
		self.mass = 6.687e15
		self.velocity = np.sqrt(G * 1.989e30/radius) * np.array([-np.sin(phi), np.cos(phi)])
		self.force = np.array([0.,0.])
		self.colour = (100,100,100)

	def move(self):
		self.x += 0.5 * self.velocity[0] * dt
		self.y +=  0.5 * self.velocity[1] * dt
		self.velocity += self.force/self.mass * dt
		self.x += 0.5 * self.velocity[0] * dt
		self.y +=  0.5 * self.velocity[1] * dt

class Sun(object):
    """Our Sun in the point of origin
    """
    def __init__(self):
        self.x = 0
        self.y = 0
        self.radius = 20
        self.mass = 1.989e30
        self.colour = (255,255,0)

def draw(a):
    """Draws an object and its trail on the screen
    """
    pygame.draw.circle(screen, a.colour, (int(a.x * 0.5e-9) + width/2,
    int(a.y * 0.5e-9) + height/2), a.radius, 0)

def draw2(a):
    """Draws an object in the middle of the screen
    """
    pygame.draw.circle(screen, a.colour, (width/2, height/2), a.radius, 0)

G = 6.673e-11
AE = 1.496e11
n = 2000
dt = 36000
liste = []

(width, height) = (1000,600)
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption(" ")
background_colour = (10,10,10)

for i in xrange(n):
	phi = 2 * np.random.random() * np.pi
	radius = np.random.uniform(2.,3.4) * AE
	obj = Asteorid(phi, radius)
	liste.append(obj)

sonne = Sun()

running = True
while running:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			running = False

    # display everything
	screen.fill(background_colour)
	draw2(sonne)
	for i in liste:
		draw(i)
		i.force = get_force(i, sonne)
		i.move()
	pygame.display.update()
