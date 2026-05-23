from .Animal import Animal
from Action import Action
from ActionEnum import ActionEnum
from Organisms.Lynx import Lynx
from Position import Position

class Antelope(Animal):

    INITIAL_POWER = 4
    INITIAL_INITIATIVE = 3
    INITIAL_LIVE_LENGTH = 11
    INITIAL_POWER_TO_REPRODUCE = 5
    SIGN = 'A'

    def __init__(self, antelope=None, position=None, world=None):
        super(Antelope, self).__init__(antelope, position, world)

    def clone(self):
        return Antelope(self, None, None)

    def initParams(self):
        self.power = self.INITIAL_POWER
        self.initiative = self.INITIAL_INITIATIVE
        self.liveLength = self.INITIAL_LIVE_LENGTH
        self.powerToReproduce = self.INITIAL_POWER_TO_REPRODUCE
        self.sign = self.SIGN

    def getNeighboringPosition(self):
        return self.world.filterPositionsWithoutAnimals(self.world.getNeighboringPositions(self.position))
    
    def move(self):
        neighbors = self.world.getNeighboringPositions(self.position)
        lynx_position = None
        
        for pos in neighbors:
            org = self.world.getOrganismFromPosition(pos) 
            if isinstance(org, Lynx):
                lynx_position = pos 
                break 

        if lynx_position is None:
            return super(Antelope, self).move()
        else:
            dx = self.position.x - lynx_position.x
            dy = self.position.y - lynx_position.y
            
            escape_x = self.position.x + (dx * 2)
            escape_y = self.position.y + (dy * 2)
            escape_pos = Position(xPosition=escape_x, yPosition=escape_y)
            
            if self.world.positionOnBoard(escape_pos):
                org_at_escape = self.world.getOrganismFromPosition(escape_pos)
                
                if org_at_escape is None:
                    result = []
                    result.append(Action(ActionEnum.A_MOVE, escape_pos, 0, self))
                    self.lastPosition = self.position
                    return result
            
            result = []
            result.append(Action(ActionEnum.A_MOVE, lynx_position, 0, self))
            self.lastPosition = self.position
            
            lynx_org = self.world.getOrganismFromPosition(lynx_position)
            result.extend(lynx_org.consequences(self)) 
            
            return result