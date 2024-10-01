import pygame 
from .sprite_class import Sprite
from .vector_class import Vector
from .size_class import Size
from .player_velocity_class import Velocity
from .bullet_class import Bullet
from sprites.sprites import sprites
class Player:
    def __init__(self,img_src,position,size,angle):
        self.angle=angle
        self.image=Sprite(img_src,position,size,angle)
        self.position=Vector(position)
        self.size=Size(size)
        self.velocity=Velocity(self.image)
        self.isShooting=False
        self.bullet_pool=[Bullet(sprites["bullet"],{"width":20,"height":20},{"x":self.image.position.x,"y":self.image.position.y},0) for bullet in range(10)]
        self.active_bullets=[]
    def draw(self,screen):
        self.image.draw(screen)
        for bullet in self.active_bullets:
            bullet.draw(screen)      
    def update_player(self):
        self.handlePlayerBullets()
    def update(self,screen,event):
        self.player_move(event,screen)
        self.player_shoot(event,screen)
        self.update_player()
    def handlePlayerBullets(self):
        self.update_bullets()
    def player_move(self,event,screen):
        if event.key == pygame.K_LEFT:
            self.velocity.update("L",screen)
        elif event.key == pygame.K_RIGHT:
            self.velocity.update("R",screen)
    def player_shoot(self,event,screen):
        if event.key == pygame.K_UP:
            self.shooting=True
            self.shoot()
           
    def shoot(self):
        if self.shooting:
           if len(self.bullet_pool)<=0:
               print("reloading")
           else:
               bullet=self.bullet_pool.pop()
               bullet.image.position.x = self.image.position.x 
               bullet.image.position.y = self.image.position.y  
               self.active_bullets.append(bullet)
        
    def update_bullets(self):
        for bullet in self.active_bullets:
            bullet.update()
            if bullet.is_off_screen() and self.shooting:
                bullet.reset_position(Vector({"x":self.image.position.x, "y":self.image.position.y})) 
                self.bullet_pool.append(bullet)
                
                