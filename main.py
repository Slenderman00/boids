import time

import sys
import pygame


from pathlib import Path

from engine import engine, engineObject, sprite, sprites
from sprites import blueBoid, json, pinkBoid, _sprites

from objects import birdLikeObject

from screen import height, width, screen

_engine = engine()

#populating the engine with engineObjects containing birdLikeObjects
for i in range(0, 100):
    _engine.push(engineObject("Boids", "", 200 + (i*10), height / 2, 0, 10, 10, _sprites.fetchSprite(blueBoid), birdLikeObject))
_engine.push(engineObject("Boids", "", 200 + (i*10), height / 2, 0, 10, 10, _sprites.fetchSprite(pinkBoid), birdLikeObject))


count = 0

while(True):
    #handling the pygame quit event
    for event in pygame.event.get():
        if event.type == pygame.QUIT: 
            sys.exit()

        if event.type == pygame.MOUSEMOTION:
            if count < 25:
                count += 1
            else:
                sys.exit()

    #clearign screen
    screen.fill((0, 0, 0))

    #calculating and drawing birds
    _engine.tick(screen)
    _engine.draw(screen)

    pygame.display.flip()