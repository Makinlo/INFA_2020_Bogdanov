import pygame
# from pygame.draw import*
import pygame.draw as d

pygame.init()

yellow = (255, 255, 0)
red = (255, 0, 0)
black = (0,0,0)

screen = pygame.display.set_mode((1000, 1000))
FPS = 30
screen.fill(red)
pygame.display.set_caption("Angry toy$")
pygame.display.flip()


d.circle(screen, yellow,(500,300), 150,0)
d.circle(screen, red, (430,270), 30, 0)
d.circle(screen, red, (570,270), 23, 0)
d.circle(screen, black, (430,270), 13, 0)
d.circle(screen, black, (570,270), 11, 0)
d.rect(screen, black, (425, 365, 150, 31))
d.line(screen, black, (350,180), (480,260), 15)
d.line(screen, black, (520,258), (640,218), 15)





pygame.display.update()
pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()


