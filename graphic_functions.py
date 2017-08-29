from pygame.draw import circle
from config import *

def draw(a, screen):
    """Draws an object on the screen
    """
    circle(screen, (100,100,100), (norm_pos(a.x) + width/2,
    norm_pos(a.y) + height/2), norm_rad(a.radius), 0)

def draw2(a, screen):
    """Draws an object in the middle of the screen
    """
    circle(screen, (255, 255, 0), (width/2, height/2), int(a.radius/5e7), 0)

def norm_pos(x):
	return int(x * 0.5e-9)

def norm_rad(x):
	return int(x * 1e-9)
