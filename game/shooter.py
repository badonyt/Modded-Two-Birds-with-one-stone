import pygame
from pygame.constants import TIMER_RESOLUTION
from settingss import *
class Shooter:
    position = pygame.Vector2()
    width = 70
    height = 67
    direction = 0
    hasBullet = True
    def __init__(self):
        self.position.xy = 320 - self.width/2, 400
    def setDirection(self, direction):
        self.direction = direction
    def update(self, dt):
        self.direction = 0
        if inffffinitebbbultes == True:
            self.hasBullet = True
        keys = pygame.key.get_pressed()  #checking pressed keys
        if keys[pygame.K_LEFT]:
            self.direction = -velocityt
        if keys[pygame.K_RIGHT]:
            self.direction = velocityt
        if (not(self.position.x < 0 and self.direction == -velocityt) and not(self.position.x + self.width > 640 and self.direction == velocityt)):
            self.position.xy = (self.position.x + self.direction*120*dt, self.position.y) 
    def reset(self):
        self.hasBullet = True
        self.position.xy = 320 - self.width/2, 400