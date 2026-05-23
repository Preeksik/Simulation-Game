from .Animal import Animal

class Lynx(Animal):
    INITIAL_POWER = 6
    INITIAL_INITIATIVE = 5
    INITIAL_LIVE_LENGTH = 18
    INITIAL_POWER_TO_REPRODUCE = 14
    SIGN = 'R'

    def __init__(self, lynx=None, position=None, world=None):
        super(Lynx, self).__init__(lynx, position, world)

    def clone(self):
        return Lynx(self, None, None)
    
    def initParams(self):
        self.power = self.INITIAL_POWER
        self.initiative = self.INITIAL_INITIATIVE
        self.liveLength = self.INITIAL_LIVE_LENGTH
        self.powerToReproduce = self.INITIAL_POWER_TO_REPRODUCE
        self.sign = self.SIGN
    
    def getNeighboringPosition(self):
        all_neighbors = self.world.getNeighboringPositions(self.position)
        
        valid_positions = []

        for pos in all_neighbors:
            org = self.world.getOrganismFromPosition(pos)
            if org is None or not isinstance(org, Lynx):
                valid_positions.append(pos)
        
        return valid_positions