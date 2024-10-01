import random
from sprites.sprites import sprites
from .sprite_class import Sprite
from .vector_class import Vector

class Enemy:
    def __init__(self, img_src, position, size):
        self.image = Sprite(img_src, position, size, 0)
        self.position = Vector(position)
        self.velocity = 5

    def draw(self, screen):
        self.image.draw(screen)

    def update(self):
        self.image.position.x += self.velocity    

class EnemyGrid:
    def __init__(self):
        self.enemy_grid = []
        self.direction = 1  
        self.speed = 2 
        self.downward_speed = 1  
        self.width = 0
        self.height = 0
        self.counter = 0
        self.position=Vector({"x":0,"y":0})
        self.generate_enemies()
       
    def draw(self, screen):
        for grid in self.enemy_grid:
            self.position=Vector({"x":grid[0].image.position.x,"y":grid[0].image.position.y})
            for enemy in grid:
                enemy.draw(screen)
    

    def update(self, screen):
        max_width=self.position.x + self.width
        if max_width>=screen.get_width():
            for grid in self.enemy_grid:
                for enemy in grid:
                    enemy.image.position.y+=self.height
                    enemy.image.position.x=0
        for grid in self.enemy_grid:
            for enemy in grid:
                enemy.update()
        
     

    def populate_enemy_grid(self):
        row = random.randint(1, 10)
        col = random.randint(1, 10)
        self.height = col * 40
        self.width = row * 40
        for i in range(row):
            new_arr = []
            for j in range(col):
                enemy = Enemy(sprites["enemy1"], {"x": 40 * i, "y": 40 * j}, {"width": 40, "height": 40})
                new_arr.append(enemy)
            self.enemy_grid.append(new_arr)  

    def generate_enemies(self):
        self.populate_enemy_grid()
