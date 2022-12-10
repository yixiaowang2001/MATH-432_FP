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
        self.update_speed()
        dx = math.cos(math.radians(self.angle)) * self.speed
        dy = math.sin(math.radians(self.angle)) * self.speed
        self.rect.move_ip(dx, dy)
        pygame.draw.rect(self.screen, self.color, self.rect)
        self.draw_text(10, 10)
        pygame.display.update()

    def draw_text(self, x, y):
        my_font = pygame.font.SysFont('arial', 15)
        text_surface = my_font.render(f'Car Speed: {round(self.speed, 4)}', True, (0, 0, 0))
        self.screen.blit(text_surface, (x, y))

    def update_speed(self):
        self.speed = self.speed + random.uniform(0, 1)
        self.speed = self.speed - random.uniform(0, 1)