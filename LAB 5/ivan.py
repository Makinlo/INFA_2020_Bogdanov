import pygame
import pygame.draw as d
from random import randint

pygame.init()

FPS = 30
window_heigth = 600
tablo_height = 10
window_length = 1200
screen = pygame.display.set_mode((window_length, window_heigth))

RED = (255, 0, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
GREEN = (0, 255, 0)
MAGENTA = (255, 0, 255)
CYAN = (0, 255, 255)
BLACK = (0, 0, 0)
COLORS = [RED, BLUE, YELLOW, GREEN, MAGENTA, CYAN]


class Ball():
    def __init__(self, color, x, y, r, speed_x, speed_y, lifes):

        self.x = x


self.y = y
self.r = r
self.color = color
self.lifes = lifes
self.speed_x = speed_x
self.speed_y = speed_y
d.circle(screen, self.color, (self.x, self.y), self.r)


def move(self):
    d.circle(screen, BLACK, (self.x, self.y), self.r)


self.x += self.speed_x
self.y += self.speed_y
d.circle(screen, self.color, (self.x, self.y), self.r)


def change_color(self, color):
    self.color = color


d.circle(screen, self.color, (self.x, self.y), self.r)


def change_speed(self, speed_x, speed_y):
    self.speed_x = speed_x


self.speed_y = speed_y


def lose_life(self):
    self.lifes += -1


def remove_ball(self):
    d.circle(screen, BLACK, (self.x, self.y), self.r)


def click_not_miss(click_x, click_y, ball_x, ball_y, ball_r):
    if (click_x - ball_x) ** 2 + (click_y - ball_y) ** 2 <= ball_r ** 2:
        return True

else:
return False


def near_top_wall(x, y, r, window_length, window_height, tablo_height):


# if ball is touching top of the window
if y - r < 10 + tablo_height:
    return True
else:
    return False


def near_left_wall(x, y, r, window_length, window_height, tablo_height):


# if ball is touching left wall of the window
if x - r < 10:
    return True
else:
    return False


def near_right_wall(x, y, r, window_length, window_height, tablo_height):


# if ball is touching right wall of the window
if window_length - 10 < x + r:
    return True
else:
    return False


def near_bottom_wall(x, y, r, window_length, window_height, tablo_height):


# if ball is touching bottom of the window
if window_height - 10 < y + r:
    return True
else:
    return False

rmin = 5
rmax = 30
a = Ball(COLORS[randint(0, 5)], randint(50, window_length - 50), randint(tablo_height + 50, window_heigth - 50),
         randint(rmin, rmax), randint(-6, 6),
         randint(-6, 6), 10)
b = Ball(COLORS[randint(0, 5)], randint(50, window_length - 50), randint(tablo_height + 50, window_heigth - 50),
         randint(rmin, rmax), randint(-6, 6),
         randint(-6, 6), 10)
c = Ball(COLORS[randint(0, 5)], randint(50, window_length - 50), randint(tablo_height + 50, window_heigth - 50),
         randint(rmin, rmax), randint(-6, 6),
         randint(-6, 6), 10)
e = Ball(COLORS[randint(0, 5)], randint(50, window_length - 50), randint(tablo_height + 50, window_heigth - 50),
         randint(rmin, rmax), randint(-6, 6),
         randint(-6, 6), 10)
pygame.display.update()
clock = pygame.time.Clock()
finished = False
points = 0
all_x = [a.x, b.x, c.x, e.x]
all_y = [a.y, b.y, c.y, e.y]
all_r = [a.r, b.r, c.r, e.r]
all_balls = [a, b, c, e]
all_lifes = [a.lifes, b.lifes, c.lifes, e.lifes]
while not finished:
    clock.tick(FPS)
for event in pygame.event.get():
    if event.type == pygame.QUIT:
        finished = True
elif event.type == pygame.MOUSEBUTTONDOWN:
click_x, click_y = event.pos
for i in range(0, 4):
    if click_not_miss(click_x, click_y, all_x[i], all_y[i], all_r[i]) == True:
        all_balls[i].lose_life()
points += 1
print(points)
all_balls[i].change_color(COLORS[randint(0, 5)])
if all_lifes[i] == 0:
    all_balls[i].remove_ball()
# all_balls[i] = Ball(COLORS[randint(0, 5)], randint(50, window_length - 50),
# randint(tablo_height + 50, window_heigth - 50),
# randint(5, 20), randint(-6, 6),
# randint(-6, 6), 10)
all_balls[i].color = COLORS[randint(0, 5)]
all_balls[i].x = randint(50, window_length - 50)
all_balls[i].y = randint(tablo_height + 50, window_heigth - 50)
all_balls[i].r = randint(rmin, rmax)
all_balls[i].speed_x = randint(-6, 6)
all_balls[i].speed_y = randint(-6, 6)
all_balls[i].lifes = 10

for i in

range(0, 4):
if near_top_wall(all_x[i], all_y[i], all_r[i], window_length, window_heigth, tablo_height) == True:
    all_balls[i].change_speed(randint(-6, 6), randint(1, 6))
if near_bottom_wall(all_x[i], all_y[i], all_r[i], window_length, window_heigth, tablo_height) == True:
    all_balls[i].change_speed(randint(-6, 6), randint(-6, -1))
if near_right_wall(all_x[i], all_y[i], all_r[i], window_length, window_heigth, tablo_height) == True:
    all_balls[i].change_speed(randint(-6, -1), randint(-6, 6))
if near_left_wall(all_x[i], all_y[i], all_r[i], window_length, window_heigth, tablo_height) == True:
    all_balls[i].change_speed(randint(1, 6), randint(-6, 6))
all_balls[i].move()

all_x = [a.x, b.x, c.x, e.x]
all_y = [a.y, b.y, c.y, e.y]
all_r = [a.r, b.r, c.r, e.r]
all_balls = [a, b, c, e]
all_lifes = [a.lifes, b.lifes, c.lifes, e.lifes]
pygame.display.update()
screen.fill(BLACK)

pygame.quit()