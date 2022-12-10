from Car import Car
from Road import Road
import pygame

scale = 8
screen_height = 800
screen_width = 800
road_width = screen_width
road_height = 3 * scale
speed = 4
fps = 50
car_width1 = 4 * scale
car_height = 2 * scale
car_color = (29, 97, 184)
road_color = (197, 212, 240)

screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Traffic Flow")
clock = pygame.time.Clock()
pygame.init()

road1 = Road(screen, road_width, road_height, 0, (screen_height - road_height) / 2, road_color)
car = Car(screen, car_width1, car_height, 0, (screen_height - car_height) / 2, speed, 0, car_color)
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
    car.move()
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