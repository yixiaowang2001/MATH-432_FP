import os
import random
import pygame
from pygame.locals import *  # Constants
import math
import sys


class Road(object):
    def __init__(self, screen, width, height, x, y, color):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.screen = screen
        self.color = color
        self.rect = pygame.draw.rect(self.screen, self.color, (self.x, self.y, self.width, self.height))

    def create(self):
        scale = self.height / 10
        delta = (self.height - scale * 8) / 2
        num = math.floor((self.width - delta * 2) / (8 * scale))
        pygame.draw.rect(self.screen, self.color, self.rect)
        for i in range(num):
            if i % 2 == 0:
                self.arrow(self.x + delta + 8*scale*i, self.y + delta, (169, 187, 217), scale)

    def arrow(self, x, y, color, scale):
        A = (x + 0.5 * scale, y + 0.5 * scale)
        B = (x + 1 * scale, y + 0)
        C = (x + 5 * scale, y + 4 * scale)
        E = (x + 1 * scale, y + 8 * scale)
        F = (x + 0.5 * scale, y + 7.5 * scale)
        D = (x + 4 * scale, y + 4 * scale)
        pygame.draw.polygon(self.screen, color, (A, B, C, E, F, D))

