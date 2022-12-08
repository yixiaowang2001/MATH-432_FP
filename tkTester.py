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


if __name__ == "__main__":
    screen_height = 800
    screen_width = 800
    road_width = screen_width
    road_height = 30
    speed = 4
    fps = 50
    car_width1 = 40
    car_height = 20
    car_color = (73, 69, 194)
    road_color = (197, 212, 240)

    screen = pygame.display.set_mode((screen_width, screen_height))
    pygame.display.set_caption("Traffic Flow")
    clock = pygame.time.Clock()
    pygame.init()

    road1 = Road(screen, road_width, road_height, 0, (screen_height - road_height) / 2, road_color)
    screen.fill("white")
    road1.create()
    pygame.display.update()

    running = True
    pause = False
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    pause = True
                elif event.key == pygame.K_ESCAPE:
                    running = False
        screen.fill("white")
        road1.create()
        clock.tick(fps)
        while pause:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pause = False
                    running = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        pause = False
                    elif event.key == pygame.K_ESCAPE:
                        pause = False
                        running = False