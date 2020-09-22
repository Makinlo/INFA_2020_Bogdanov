import pygame
# from pygame.draw import*
import pygame.draw as d

pygame.init()

screen = pygame.display.set_mode((1000, 1000))
FPS = 30

yellow = (255, 255, 0)
red = (255, 0, 0)
black = (0,0,0)

d.circle(screen, yellow,(500,300), 150,0)
d.circle(screen, red, (430,270), 30, 0)
d.circle(screen, red, (570,270), 20, 0)
d.circle(screen, black, (430,270), 13, 0)
d.circle(screen, black, (570,270), 11, 0)
d.line(screen, black,[])






pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()

