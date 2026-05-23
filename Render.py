from Position import Position

class Renderer:
    def __init__(self, world):
        self.world = world

    def render(self):
        result = '\nturn: ' + str(self.world.turn) + '\n'
        for wY in range(0, self.world.worldY):
            for wX in range(0, self.world.worldX):
                org = self.world.getOrganismFromPosition(Position(xPosition=wX, yPosition=wY))
                if org:
                    result += str(org.sign)
                else:
                    result += self.world.separator
            result += '\n'
        return result