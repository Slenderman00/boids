#consists of a spriteloader and manager
#engine objects that accepts engine object classes
#engine object classes are classes that spesifies the behaviour of an object
#game loop functions
#some sort of fake 3D? (x, y, z) where z is the scale

import pygame
from pathlib import Path

class engine():
    def __init__(self):
        self.objects = []

    def push(self, _object):
        _object.objectBehaviourClass.__init__(self, _object)
        self.objects.append(_object)

    def draw(self, screen):
        for _object in self.objects:

            z = _object.z

            if(_object.width + z < 5):
                z = - _object.width + 5
            sprite = pygame.transform.scale(_object.sprite, (_object.width + int(z) , _object.height + int(z) ))
            sprite = pygame.transform.rotate(sprite, _object.spriteAngle + _object.spriteAngleOffset)
            screen.blit(sprite, (_object.x - (_object.width / 2), _object.y - (_object.height / 2)))

    def tick(self, screen):
        for _object in self.objects:
            _object.objectBehaviourClass.tick(self, _object, screen)


    def collision(self, _object):
        pass

    def delete(self, _object):
        pass


class engineObject():
    def __init__(self, _class, _id, x, y, z, width, height, sprite, objectBehaviourClass):
        self._class = _class
        self.id = _id
        self.x = x
        self.y = y
        self.z = z
        self.width = width
        self.height = height
        self.sprite = sprite
        self.direction = 0
        self.speed = 0
        self.angle = 0
        self.spriteAngle = 0
        self.spriteAngleOffset = 0
        self.ignore = True

        #defines the behaviour of an object
        self.objectBehaviourClass = objectBehaviourClass

#stores sprites in memory, sprites are loaded into the sprites class on game start

class sprites():
    def __init__(self):
        self.sprites = []

    def pushSprite(self, sprite):
        self.sprites.append(sprite)
        return len(self.sprites) - 1

    def fetchSprite(self, id):
        return self.sprites[id].sprite

class sprite(): 
    def __init__(self, name):
        self.name = name
        self.sprite = pygame.image.load(Path(".") / 'sprites' / name)
        print(f'loaded: {name}')


#sprite1 = sprites.pushSprite("sprite1.png")
#sprites.fetchSprite(sprite1)