import pygame

pygame.init()
pygame.font.init()

# colours
BLACK = (0,0,0)
WHITE = (255,255,255)
RED = (255,0,0)
GREEN = (0,255,0)
BLUE = (0,0,255)

# game variables
size = (700, 500)
screen = pygame.display.set_mode(size)
clock = pygame.time.Clock()

# other variables
nodes = [ [200,50], [200, 100], [200, 150], [200, 200], [200, 250], [200, 300] ]

# classes
class text:
    def __init__(self, text, position, size, colour):
        self.colour, self.position, self.size, self.text = colour, position, size, text
        myfont = pygame.font.SysFont('Comic Sans MS', self.size)
        textsurface = myfont.render(self.text, False, self.colour)
        screen.blit(textsurface, self.position)

class box:
    def __init__(self, position, colour):
        self.colour, self.position  = colour, position
        pygame.draw.rect(screen, self.colour, self.position)

state = True
while state:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            state = False

    screen.fill(BLACK)

    # lines of wires
    pygame.draw.line(screen, WHITE, [200, 50], [500, 50], 5)
    pygame.draw.line(screen, WHITE, [200, 100], [500, 100], 5)
    pygame.draw.line(screen, WHITE, [200, 150], [500, 150], 5)
    pygame.draw.line(screen, WHITE, [200, 200], [500, 200], 5)
    pygame.draw.line(screen, WHITE, [200, 250], [500, 250], 5)
    pygame.draw.line(screen, WHITE, [200, 300], [500, 300], 5)

    # lines of frets
    pygame.draw.line(screen, WHITE, [200, 50], [200, 300], 5)
    pygame.draw.line(screen, WHITE, [300, 50], [300, 300], 5)
    pygame.draw.line(screen, WHITE, [400, 50], [400, 300], 5)
    pygame.draw.line(screen, WHITE, [500, 50], [500, 300], 5)

    # nodes for finger placement
    pygame.draw.circle(screen, WHITE, nodes[0], 10)
    pygame.draw.circle(screen, WHITE, nodes[1], 10)
    pygame.draw.circle(screen, WHITE, nodes[2], 10)
    pygame.draw.circle(screen, WHITE, nodes[3], 10)
    pygame.draw.circle(screen, WHITE, nodes[4], 10)
    pygame.draw.circle(screen, WHITE, nodes[5], 10)

    # box
    generateb = box([290,350,150,50], GREEN)

    # text
    generatet = text("Generate", (300, 350), 30, BLACK)

    # mouse/key presses
    mouse = pygame.mouse.get_pressed()
    mousepos = pygame.mouse.get_pos()
    if mousepos[0] > 300 and mousepos[0] < 400:
        if mousepos[1] > 350 and mousepos[1] < 400:
            if mouse[0]:
                print("1")


    pygame.display.flip()
    clock.tick(60)

pygame.quit()
