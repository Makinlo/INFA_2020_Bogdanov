import pygame
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
black_green = (34, 84, 36)
line = (110, 110, 110)

screen = pygame.display.set_mode((600, 400))

FPS = 60
# Фон
d.rect(screen, green, (0, 200, 600, 200))
d.rect(screen, blue, (0, 0, 600, 200))


def tree(x: int, y: int, scale=1.0, branches=1):
    """
    draws tree of given size in given coordinates

    :param x: x coordinate
    :param y: y coordinate
    :param scale: the size of a tree
    :param branches: number of branches (maximum 2)
    :return: image on "screen" plane
    """
    if branches != 0 and branches != 1 and branches != 2:
        print('error')
    else:
        d.rect(screen, brown, (x, y, int(16 * scale), int(70 * scale)))
        d.circle(screen, black_green, (x + int(8 * scale), y - int(35 * scale)), int(44 * scale), 0)
        d.circle(screen, black, (x + int(8 * scale), y - int(35 * scale)), int(44 * scale), 1)
        if branches == 2:
            d.line(screen, brown, (x + int(16 * scale), y + int(25 * scale)), (x + int(60 * scale), int(y + 5 * scale)),
                   int(6 * scale))
            d.line(screen, brown, (x, y + int(30 * scale)), (x - int(20 * scale), int(y + 18 * scale)),
                   int(6 * scale))
        elif branches == 1:
            d.line(screen, brown, (x + int(16 * scale), y + int(25 * scale)), (x + int(60 * scale), int(y + 5 * scale)),
                   int(6 * scale))


def house(x: int, y: int, scale=1.0):
    """
    draws scaled house in given coordinates

    :param x: x coordinate
    :param y: y coordinate
    :param scale: size of a house
    :return: image on "screen" plane
    """
    d.rect(screen, brick, (x, y, int(140 * scale), int(100 * scale)))
    d.rect(screen, black, (x, y, int(140 * scale), int(100 * scale)), 1)
    d.polygon(screen, krisha, [[x, y], [x + int(140 * scale), y], [x + int(70 * scale), y - int(70 * scale)]])
    d.polygon(screen, black, [[x, y], [x + int(140 * scale), y], [x + int(70 * scale), y - int(70 * scale)]], 1)
    d.rect(screen, window, (x + int(45 * scale), y + int(30 * scale), int(50 * scale), int(35 * scale)))
    d.rect(screen, brown, (x + int(45 * scale), y + int(30 * scale), int(50 * scale), int(35 * scale)), 2)
    d.line(screen, brown, (x + int(70 * scale), y + int(30 * scale)), (x + int(70 * scale), y + int(65 * scale)), 2)
    d.line(screen, brown, (x + int(45 * scale), y + int(47 * scale)), (x + int(95 * scale), y + int(47 * scale)), 2)
    d.polygon(screen, black, [[x + int(105 * scale), y - int(80 * scale)], [x + int(105 * scale), y - int(35 * scale)],
                              [x + int(117 * scale), y - int(25 * scale)], [x + int(105 * scale), y - int(80 * scale)]])


def sun():
    """
    draws sun on a picture

    :return: image on a "screen" plane
    """
    d.circle(screen, yellow, (45, 45), 30)
    d.line(screen, yellow, (45, 0), (45, 90), 3)
    d.line(screen, yellow, (0, 45), (90, 45), 3)
    d.line(screen, yellow, (11, 11), (79, 79), 3)
    d.line(screen, yellow, (79, 11), (11, 79), 3)


tree(535, 215, 0.75, 2)
tree(245, 225)
house(50, 225)
house(400, 205, 0.66)
sun()
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
