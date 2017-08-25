from functions import *
import pygame

class Sun(object):
    """Our Sun in the point of origin
    """
    def __init__(self):
        self.x = 0
        self.y = 0
        self.radius = 20
        self.mass = 1.989e30
        self.colour = (255,255,0)

class Planet(object):
    """An ordinary planet, in this case our Earth
    """
    def __init__(self,color):
        self.x = 1.49e11
        self.y = 0.
        self.radius = 10
        self.mass = 5.97e24
        self.velocity = np.array([0.,2.978e4])
        self.force = np.array([0,0])
        self.colour = (color)
        self.positions = [(int(self.x * 1e-9 + width/2),
        int(self.y * 1e-9 + height/2))]

    # leapfrog method for DE-solving
    def move(self):
        self.x += 0.5 * self.velocity[0] * dt
        self.y +=  0.5 * self.velocity[1] * dt
        self.velocity += self.force/self.mass * dt
        self.x += 0.5 * self.velocity[0] * dt
        self.y +=  0.5 * self.velocity[1] * dt

    # euler method for DE-solving
    def move2(self):
        self.x += self.velocity[0] * dt
        self.y += self.velocity[1] * dt
        self.velocity += self.force/self.mass * dt

def draw(a, points):
    """Draws an object and its trail on the screen
    """
    pygame.draw.circle(screen, a.colour, (int(a.x * 10e-10) + width/2,
    int(a.y * 10e-10) + height/2), a.radius, 0)
    pygame.draw.aalines(screen, a.colour, False, points, 2)

def draw2(a):
    """Draws an object in the middle of the screen
    """
    pygame.draw.circle(screen, a.colour, (width/2, height/2), a.radius, 0)

def last_elems(elems, k):
    """Returns the last k elements of a list
    """
    tmp = []
    for i in xrange(k):
        if i > len(elems):
            break
        elif i < len(elems):
            tmp.append(elems[-(i+1)])
    return tmp

dt = 36000
(width, height) = (1000,600)
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption(" ")
background_colour = (10,10,10)

erde = Planet((0,0,255))
kerbin = Planet((50,150,255))
sonne = Sun()

count = 0
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    #every ten steps, the trail is updated
    if count % 10 == 0:
        erde.positions.append((int(1e-9 * erde.x) + width/2,
        int(1e-9 * erde.y) + height/2))
        kerbin.positions.append((int(1e-9 * kerbin.x) + width/2,
        int(1e-9 * kerbin.y) + height/2))
        linepoints1 = last_elems(erde.positions, 200)
        linepoints2 = last_elems(kerbin.positions, 200)

    # display everything
    screen.fill(background_colour)
    draw(erde, linepoints1)
    draw(kerbin, linepoints2)
    draw2(sonne)
    pygame.display.update()

    # calculate everything
    erde.force = get_force(erde, sonne)
    kerbin.force = get_force(kerbin, sonne)
    erde.move()
    kerbin.move2()

    count += 1
