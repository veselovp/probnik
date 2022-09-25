import pygame
import random
from pygame.draw import *

pygame.init()

FPS = 30
screen = pygame.display.set_mode((600, 600))

# eto fon
rect(screen, (250, 250, 120), (0, 0, 600, 400))
rect(screen, (0, 250, 250), (0, 400, 600, 200))
rect(screen, (0, 250, 0), (0, 0, 40, 450))
rect(screen, (0, 250, 0), (500, 0, 70, 560))
rect(screen, (0, 250, 0), (195, 0, 57, 420))
rect(screen, (0, 250, 0), (289, 0, 40, 540))

# eto jozik
# 4 randomnie tochki a vokrug nix delaju jeza pasuja zncenija



# circle(screen, (255, 255, 255), (pervajax, pervajay), 30, 5)

def telo_jeza():
    pervajax = random.randint(1, 550)
    pervajay = random.randint(450, 550)
    wirinajeza = random.randint(120, 170)
    tost = random.randint(40, 70)
    ellipse(screen, "Brown", (pervajax, pervajay, wirinajeza, tost))
    ellipse(screen, "Black", (pervajax, pervajay, wirinajeza, tost), 1)
    # ellipse(screen, "Brown", (x, y, radius, swirina))
    # ellipse(screen, "Black", (x, y, radius, swirina), 1)
    for i in range(70):
        first_nx = int(pervajax + wirinajeza / 2)
        first_ny = int(pervajay + tost / 2)
        first_x = random.randint(first_nx - 65, first_nx + 65)
        first_y = random.randint(first_ny - 20, first_ny + 20)
        ran1 = random.randint(-20, 20)
        ran2 = random.randint(45, 65)
        polygon(screen, (80, 5, 0), ((first_x, first_y), (first_x + 7, first_y), (first_x - ran1, first_y - ran2)))
        polygon(screen, (0, 0, 0), ((first_x, first_y), (first_x + 7, first_y), (first_x - ran1, first_y - ran2)), 1)

telo_jeza()
telo_jeza()
telo_jeza()

# telo_jeza(410, 525, 30, 19)
# telo_jeza(420, 535, 30, 19)
# telo_jeza(550, 525, 30, 19)
# telo_jeza(540, 535, 30, 19)

# eclipse i rec 4 cifri ,1 eto krajnaja levaja stenka , 2 , krajnja verhnaja , 3 dlinna figuri , 4 wirina

# eto igolki jeza


pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()
