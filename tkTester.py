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
        self.text(10, 10)

    def text(self, x, y):
        my_font = pygame.font.SysFont('arial', 15)
        text_surface = my_font.render(f'Some Text: {20}', True, (0, 0, 0))
        screen.blit(text_surface, (x, y))


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