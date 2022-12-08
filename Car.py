import os
import random
import pygame
from pygame.locals import *  # Constants
import math
import sys


class Car(object):
    def __init__(self, screen, width, height, x, y, speed, angle, color):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.speed = speed
        self.screen = screen
        self.angle = angle
        self.color = color
        self.rect = pygame.draw.rect(self.screen, self.color, (self.x, self.y, self.width, self.height))

    def move(self):
        # self.screen.fill((255, 255, 255))
        dx = math.cos(math.radians(self.angle)) * self.speed
        dy = math.sin(math.radians(self.angle)) * self.speed
        self.rect.move_ip(dx, dy)
        pygame.draw.rect(self.screen, self.color, self.rect)
        pygame.display.update()
