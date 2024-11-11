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
    def __init__(self, rows=2, cols=5, size=40):
        self.enemy_grid = []
        self.direction = 1  
        self.speed = 2 
        self.downward_speed = 50 
        self.size = size
        self.position = Vector({"x": 0, "y": 0})
        self.generate_enemies(rows, cols)

    def draw(self, screen):
        for grid in self.enemy_grid:
            for enemy in grid:
                enemy.draw(screen)

    def update(self, screen):
        max_width = self.enemy_grid[0][0].image.position.x + (len(self.enemy_grid) * self.size)
        if max_width >= 500:
            for grid in self.enemy_grid:
                for enemy in grid:
                    enemy.image.position.y += self.downward_speed
            for i, grid in enumerate(self.enemy_grid):
                for j, enemy in enumerate(grid):
                    enemy.image.position.x = self.size * j 
        for grid in self.enemy_grid:
            for enemy in grid:
                enemy.update()

    def populate_enemy_grid(self, rows, cols):
        for i in range(rows):
            new_arr = []
            for j in range(cols):
                enemy = Enemy(sprites["ufo"], {"x": self.size * j, "y": self.size * i}, {"width": self.size, "height": self.size})
                new_arr.append(enemy)
            self.enemy_grid.append(new_arr)

    def generate_enemies(self, rows, cols):
        self.populate_enemy_grid(rows, cols)
        print(len(self.enemy_grid))