import pygame
import sys

pygame.init()

default_window_size=(1000,800)
screen = pygame.display.set_mode((default_window_size))
pygame.display.set_caption('Space Invaders')
clock = pygame.time.Clock()
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False 
    pygame.display.flip()
    clock.tick(60)

# Quit Pygame
pygame.quit()
sys.exit()
