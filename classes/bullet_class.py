from .sprite_class import Sprite
class Bullet:
    def __init__(self,image,size,position,angle):
        self.image=Sprite(image,position,size,angle)
        self.velocity=5
    def draw(self,screen):
        self.image.draw(screen)
    def update(self):
       self.image.position.y += -self.velocity
    def is_off_screen(self):
        return self.image.position.y < 0
    def reset_position(self,new_pos):
        self.image.position.x=new_pos.x
        self.image.position.y=new_pos.y
        