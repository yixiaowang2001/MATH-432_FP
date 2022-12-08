import pygame

# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Initialize pygame
pygame.init()

# Set the width and height of the screen [width, height]
screen_width = 800
screen_height = 800
screen = pygame.display.set_mode((screen_width, screen_height))

# Set the title of the window
pygame.display.set_caption("My Game")

# Loop until the user clicks the close button.
done = False

# Used to manage how fast the screen updates
clock = pygame.time.Clock()


class Car(object):
    def __init__(self, width, height, x, y):
        self.rect = pygame.rect.Rect((x, y, width, height))

    def move(self):
        self.rect.move_ip(-20, 0)

    def draw(self, surface):
        pygame.draw.rect(surface, (0, 0, 128), self.rect)


running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            break
            running = False

    screen.fill((255, 255, 255))
    car = Car(70, 40, 800, 400-20)
    car.draw(screen)
    car.move()
    pygame.display.update()

    clock.tick(40)


# Close the window and quit.
pygame.quit()
