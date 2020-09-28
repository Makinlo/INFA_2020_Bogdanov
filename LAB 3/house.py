import pygame
# from pygame.draw import*
import pygame.draw as d

pygame.init()

yellow = (255, 255, 0)
window = (9, 155, 184)
brick = (115, 100, 6)
brown = (153, 75, 31)
red = (255, 0, 0)
krisha = (232, 74, 74)
white = (255, 255, 255)
black = (23, 23, 23)
green = (37, 189, 34)
blue = (143, 243, 250)
blackgreen = (34, 84, 36)
line = (110, 110, 110)

screen = pygame.display.set_mode((600, 400))

screen.fill(white)
FPS = 60
# Фон
d.rect(screen, green, (0, 200, 600, 200))
d.rect(screen, blue, (0, 0, 600, 200))

# Дерево(правое)
d.rect(screen, brown, (535, 215, 12, 50))
d.circle(screen, blackgreen, (541, 200), 25, 0)
d.circle(screen, black, (541, 200), 25, 1)
d.line(screen, brown, (547, 243), (570, 227), 3)
d.line(screen, brown, (535, 238), (520, 229), 3)
# Дерево(левое)
d.rect(screen, brown, (245, 225, 16, 70))
d.circle(screen, blackgreen, (253, 190), 44, 0)
d.circle(screen, black, (253, 190), 44, 1)
d.line(screen, brown, (261, 250), (305, 230), 6)
# Дом(левый)
d.rect(screen, brick, (50, 225, 140, 100))
d.rect(screen, black, (50, 225, 140, 100), 1)
d.polygon(screen, krisha, [[50, 225], [190, 225], [120, 155]])
d.polygon(screen, black, [[50, 225], [190, 225], [120, 155]], 1)
d.rect(screen, window, (95, 255, 50, 35))
d.rect(screen, brown, (95, 255, 50, 35), 2)
d.line(screen, brown, (120, 255), (120, 290), 2)
d.line(screen, brown, (95, 272), (145, 272), 2)
d.polygon(screen, black, [[155, 145], [155, 190], [167, 200], [167, 145]])

# Дом(правый)
d.rect(screen, brick, (400, 205, 93, 66))
d.rect(screen, black, (400, 205, 93, 66), 1)
d.polygon(screen, krisha, [[400, 205], [493, 205], [446, 160]])
d.polygon(screen, black, [[400, 205], [493, 205], [446, 160]], 1)
d.rect(screen, window, (430, 225, 33, 23))
d.rect(screen, brown, (430, 225, 33, 23), 2)
d.line(screen, brown, (446, 225), (446, 248), 2)
d.line(screen, brown, (430, 236), (463, 236), 2)
d.polygon(screen, black, [[470, 150], [470, 183], [477, 191], [477, 150]])


# Солнце
d.circle(screen, yellow, (45, 45), 30)
d.line(screen, yellow, (45, 0), (45, 90), 3)
d.line(screen, yellow, (0, 45), (90, 45), 3)
d.line(screen, yellow, (11, 11), (79, 79), 3)
d.line(screen, yellow, (79, 11), (11, 79), 3)

# Облака
# Левое
r = 22
x = 95
d.circle(screen, white, (x, 80), r)
d.circle(screen, line, (x, 80), r, 1)
d.circle(screen, white, (x + 25, 80), r)
d.circle(screen, line, (x + 25, 80), r, 1)
d.circle(screen, white, (x + 50, 80), r)
d.circle(screen, line, (x + 50, 80), r, 1)
d.circle(screen, white, (x + 75, 80), r)
d.circle(screen, line, (x + 75, 80), r, 1)
d.circle(screen, white, (x + 20, 60), r)
d.circle(screen, line, (x + 20, 60), r, 1)
d.circle(screen, white, (x + 55, 60), r)
d.circle(screen, line, (x + 55, 60), r, 1)

# Центровое
d.circle(screen, white, (95 + 205, 80 + 50), 22 - 5)
d.circle(screen, line, (95 + 205, 80 + 50), 22 - 5, 1)
d.circle(screen, white, (120 + 200, 80 + 50), 22 - 5)
d.circle(screen, line, (120 + 200, 80 + 50), 22 - 5, 1)
d.circle(screen, white, (145 + 195, 80 + 50), 22 - 5)
d.circle(screen, line, (145 + 195, 80 + 50), 22 - 5, 1)
d.circle(screen, white, (170 + 195, 80 + 53), 22 - 5)
d.circle(screen, line, (170 + 195, 80 + 53), 22 - 5, 1)
d.circle(screen, white, (115 + 204, 60 + 53), 22 - 5)
d.circle(screen, line, (115 + 204, 60 + 53), 22 - 5, 1)
d.circle(screen, white, (150 + 196, 60 + 53), 22 - 5)
d.circle(screen, line, (150 + 196, 60 + 53), 22 - 5, 1)

# Правое
d.circle(screen, white, (95 + 400, 100), 22)
d.circle(screen, line, (95 + 400, 100), 22, 1)
d.circle(screen, white, (120 + 400, 100), 22)
d.circle(screen, line, (120 + 400, 100), 22, 1)
d.circle(screen, white, (145 + 400, 100), 22)
d.circle(screen, line, (145 + 400, 100), 22, 1)
d.circle(screen, white, (170 + 400, 100), 22)
d.circle(screen, line, (170 + 400, 100), 22, 1)
d.circle(screen, white, (115 + 400, 80), 22)
d.circle(screen, line, (115 + 400, 80), 22, 1)
d.circle(screen, white, (150 + 400, 80), 22)
d.circle(screen, line, (150 + 400, 80), 22, 1)





pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()
