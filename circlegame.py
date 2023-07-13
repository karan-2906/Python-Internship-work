import pygame,random
class coords():
    x=0
    y=0

class circle():
    radius = 0.0
    coords = coords()
    color = ""
    filled = False
    positions = []

colors ={ "white":(255,255,255),
         "blue" : (0,0,255),
         "green" : (0,255,0),
         "red" : (255,0,0)}

(width , height) = (300, 300)

def setup():
    global screen
    pygame.init()
    screen = pygame.display.set_mode((width , height))
    pygame.display.set_caption("Draw Circles")
    pygame.display.update()
 
def drawcircle(c):
    pygame.draw.circle(screen,colors[c.color],
                       (c.coords.x, c.coords.y),
                       c.radius, not c.filled)
    
running = True
setup()
while running:
    ev =pygame.event.get()
    for event in ev:
        if event.type == pygame.MOUSEBUTTONUP:
            pos = pygame.mouse.get_pos()
            c1=circle()
            c1.radius = 20
            c1.coords.x = pos[0]
            c1.coords.y = pos[1]
            c1.color = random.choice(list(colors))
            c1.filled = False
            drawcircle(c1)
            pygame.display.update()