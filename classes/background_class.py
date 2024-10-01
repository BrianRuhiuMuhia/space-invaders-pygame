from .sprite_class import Sprite
from .vector_class import Vector
from .size_class import Size
class Background:
    def __init__(self,image_src,position,size,angle) -> None:
        self.angle=angle
        self.image=Sprite(image_src,position,size,angle)
        self.position=Vector(position)
        self.size=Size(size)
    def draw(self,screen):
        self.image.draw(screen)