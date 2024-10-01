import pygame
from .vector_class import Vector 
class Sprite():
    def __init__(self, image, position, size,angle):
        self.image_sprite = pygame.image.load(image)
        self.image = pygame.transform.scale(self.image_sprite, (size["width"], size["height"]))
        self.position = Vector(position)
        self.size = size
        self.angle=angle
    def draw(self, screen):
        rotated_image = pygame.transform.rotate(self.image, self.angle)
        sprite_rect = rotated_image.get_rect()
        sprite_rect.x = self.position.x
        sprite_rect.y = self.position.y
        screen.blit(rotated_image, sprite_rect)
    def get_width(self):
        return self.size["width"]
    def get_height(self):
        return self.size["height"]
    def  get_angle(self):
        return self.angle
    def get_pos(self):
        return self.position