import pygame
import random
import math

from screen import height, width

from settings import flockDistance, flockAngleDivision, turnDivision

def pointOutside(point):
    if(point[0] > width or point[0] < 0):
        return True

    if(point[1] > height or point[1] < 0):
        return True

def pointInside(distance, x1, y1, x2, y2):
    if(math.hypot(x1-x2, y1-y2) < distance):
        return True

#this is a test object
class birdLikeObject():
    def __init__(self, me):
        #me refers to the parrent object
        #self refers to the parrent parrent object (the engine)
        #meaning this code runs in the engine scope

        #initializing boids with different speeds
        me.direction = pygame.math.Vector3(3, 0, 0)
        
        
    def tick(self, me, screen):
        #me refers to the parrent object
        #self refers to the parrent parrent object (the engine)
        #meaning this code runs in the engine scope
                

        #creating vectors used for navigation
        currpos = pygame.math.Vector3(me.x, me.y, me.z)
        currpos += me.direction
        direction = pygame.math.Vector2(me.direction[0], me.direction[1])
        lineStart = pygame.math.Vector2(currpos[0], currpos[1])
        lineLength = pygame.math.Vector2(1000, 0)
        direction.rotate_ip(40)
        lineCollisionDown = lineStart + direction * 10
        lineDown = lineStart + direction * 30
        direction.rotate_ip(-80)
        lineCollisionUp = lineStart + direction * 10
        lineUp = lineStart + direction * 30


        color = (0, 255, 0)
        collision = False


        #collision detection (steering away from screen edges)
        if(pointOutside(lineUp) and pointOutside(lineDown)):
            color = (255, 0, 0)
            me.angle = -2
            collision = True

        if(pointOutside(lineDown) and not pointOutside(lineUp) and not collision):
            color = (255, 0, 0)
            me.angle -= 0.5
            collision = True

        if(pointOutside(lineUp) and not pointOutside(lineDown) and not collision):
            color = (255, 0, 0)
            me.angle += 0.5
            collision = True
        

        #setting boid to nearby boids angle slowly
        if(not collision):
            for _object in self.objects:
                if(not _object.ignore):
                    if(pointInside(flockDistance, me.x, me.y, _object.x, _object.y)):
                        pygame.draw.line(screen, (69, 69, 69), (me.x, me.y), (_object.x, _object.y))
                        #dividing by a large number to make the transition slow
                        me.angle = ((me.spriteAngle - _object.spriteAngle) + me.angle) / flockAngleDivision

            #steering away from other boids
            for _object in self.objects:
                if(_object != me):
                    if(pointInside(30, lineCollisionDown[0], lineCollisionDown[1], _object.x, _object.y)):
                        color = (255, 0, 0)
                        me.angle -= 0.2
                        collision = True

                    if(pointInside(30, lineCollisionUp[0], lineCollisionUp[1], _object.x, _object.y)):
                        color = (255, 0, 0)
                        me.angle += 0.2
                        collision = True

            #slowly stopping turns
            me.angle = me.angle / turnDivision


                    

        #debgug lines:
        #pygame.draw.line(screen, color, lineStart, lineDown)
        #pygame.draw.line(screen, color, lineStart, lineUp)

        #pygame.draw.line(screen, color, (1920/2, 1080/2), (me.x, me.y))


        #if a bird is currently avoiding screen edges it gets ignored by other boids
        me.ignore = collision

        me.x = currpos[0]
        me.y = currpos[1]
        me.z = currpos[2]

        me.direction.rotate_z_ip(me.angle)

        me.spriteAngle -= me.angle
        me.spriteAngleOffset = -90


    def collision(self, other):
        pass