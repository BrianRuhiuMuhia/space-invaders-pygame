import pygame
import sys
from classes.game_class import Game
# Initialize Pygame
pygame.init()

default_window_size=(1000,800)
screen = pygame.display.set_mode((default_window_size))
pygame.display.set_caption('Space Invaders')
clock = pygame.time.Clock()
def init():
    game=None
    if game==None:
        game=Game(screen)
    return game
game=init()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    game.draw()
    game.update(event) 
    pygame.display.flip()
    clock.tick(60)

# Quit Pygame
pygame.quit()
sys.exit()
