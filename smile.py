import pygame
from pygame.draw import *

pygame.init()

FPS = 30
screen = pygame.display.set_mode((400, 400))


# colors
yellow = (255, 255, 1)
black = (0, 0, 0)
red = (255, 0, 0)

screen.fill(red)
# face
circle(screen, yellow, (200, 200), 150)
circle(screen, black, (200, 200), 150, 5)
# mouth
rect(screen, black, (130, 250, 150, 20))
# left eye
circle(screen, black, (150, 150), 30)
circle(screen, red, (150, 150), 10)
# right eye
circle(screen, black, (250, 150), 30)
circle(screen, red, (250, 150), 10)
# nose
polygon(screen, black, [(200, 200), (195, 195)], 30)

pygame.display.update()
clock = pygame.time.Clock()
finished = False
# main cycle
while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()