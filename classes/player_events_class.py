import pygame
class Events:
    def __init__(self):
        pass
    def update(self,event,player,screen):
        self.event=event
        if self.event.type == pygame.KEYUP:
            if self.event.key == pygame.K_UP:
                player.shooting=False
                print(player.shooting)
        if self.event.type == pygame.KEYDOWN:
            player.update(screen,event)
        player.handlePlayerBullets()