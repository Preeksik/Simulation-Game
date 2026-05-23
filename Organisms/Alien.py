from .Organism import Organism
from Position import Position

class Alien(Organism):

    INITIAL_POWER = 0
    INITIAL_INITIATIVE = 10
    INITIAL_LIVE_LENGTH = 999
    SIGN = 'K'

    def __init__(self, alien=None, position=None, world=None):
        super(Alien, self).__init__(alien, position, world)

    def clone(self):
        return Alien(self, None, None)

    def initParams(self):
        self.power = self.INITIAL_POWER
        self.initiative = self.INITIAL_INITIATIVE
        self.liveLength = self.INITIAL_LIVE_LENGTH
        self.sign = self.SIGN
    
    def move(self):
        return []

    def action(self):
        return []

    def getFrozenPositions(self):
        frozen_positions = set()
        
        for dx in [-1, 0, 1]:
            for dy in [-1, 0, 1]:
                if dx == 0 and dy == 0:
                    continue 
                
                check_x = self.position.x + dx
                check_y = self.position.y + dy
                pos_to_check = Position(xPosition=check_x, yPosition=check_y)
                
                if self.world.positionOnBoard(pos_to_check):
                    frozen_positions.add((check_x, check_y))
                    
        return frozen_positions