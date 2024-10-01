from .background_class import Background
from .player_class import Player
from sprites.sprites import sprites
from .player_events_class import Events
from .enemy_class import EnemyGrid
class Game:
    def __init__(self,screen):
        self.screen=screen
        self.background=Background(sprites["background"],{"x":0,"y":0},{"width":screen.get_width(),"height":screen.get_height()},0)
        self.player=Player(sprites["player"],{"x":screen.get_width()/2,"y":screen.get_height()-50},{"width":50,"height":50},0)
        self.screen=screen
        self.events=Events()
        self.enemy=EnemyGrid()
    def draw(self):
        self.background.draw(self.screen)       
        self.player.draw(self.screen)
        self.enemy.draw(self.screen)
    def update(self,event):
        self.events.update(event,self.player,screen=self.screen)
        self.enemy.update(self.screen)