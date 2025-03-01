from pygame.locals import *
import pygame
import sys
from Player import Player
from byFish import byFish
from cig import Cig
from cap import Cap


# 2 - Define constants
BLACK = (0, 0, 0)
FRAMES_PER_SECOND = 30
windowWidth = 1700
windowHeight = 1150


# 3 - Initialize the world
pygame.init()
# window = pygame.display.set_mode((windowWidth, windowHeight))
clock = pygame.time.Clock()
window= pygame.display.set_mode((0, 0), pygame.FULLSCREEN)

# 4 - Load assets: image(s), sound(s), etc.
background = pygame.image.load('images/ocean.jpg')
background = pygame.transform.scale(background, (windowWidth, windowHeight))

# 5 - Initialize variables
oTurtle = Player(window, windowWidth, windowHeight)

pollution = []

fishes = []
for i in range(5):
    Fish = byFish(window, windowWidth, windowHeight)
    fishes.append(Fish)

cigs = []
for i in range(3):
    cig= Cig(window, windowWidth, windowHeight)
    cigs.append(cig)
    pollution.append(cig)

caps = []
for i in range(3):
    cap = Cap(window, windowWidth, windowHeight)
    caps.append(cap)
    pollution.append(cap)


running = True
# 6 - Loop forever
while running:
    # 7 - Check for and handle events
    for event in pygame.event.get():
         if event.type == pygame.QUIT:
             running = False
         elif event.type == pygame.KEYDOWN:
             if event.key == pygame.K_ESCAPE:
                 if pygame.FULLSCREEN:
                    pygame.display.set_mode((windowWidth, windowHeight))
                 else:
                    pygame.display.set_mode((0, 0), pygame.FULLSCREEN)



    # 8 - Do any "per frame" actions
    oTurtle.update()
    for fish in fishes:
        fish.update()
    for cap in caps:
        cap.update()
    for cig in cigs:
        cig.update()

    for fish in fishes:
        if oTurtle.check_collide(fish):
            fishes.remove(fish)

    for cap in caps:
        if oTurtle.check_collide(cap):
            caps.remove(cap)
            pollution.remove(cap)

    for cig in cigs:
        if oTurtle.check_collide(cig):
            cigs.remove(cig)
            pollution.remove(cig)

    if len(pollution) == 0:
        print("Game over! The pollution killed the turtle :(")
        pygame.quit()
        sys.exit()


    # 9 - Clear the window before drawing it again
    window.blit(background, (0, 0))

    # 10 - Draw the window elements
    oTurtle.draw()
    for fish in fishes:
        fish.draw()
    for cap in caps:
        cap.draw()
    for cig in cigs:
        cig.draw()

    pygame.display.update()

    # 12 - Slow things down a bit
    clock.tick(FRAMES_PER_SECOND)