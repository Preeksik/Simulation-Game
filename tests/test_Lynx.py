import unittest
from Position import Position
from World import World
from Organisms.Lynx import Lynx

class TestLynx(unittest.TestCase):

    def test_lynx_ignores_other_lynx(self):
        world = World(3, 3) # Tworzymy malutki świat testowy
        
        lynx1 = Lynx(position=Position(xPosition=1, yPosition=1), world=world)
        lynx2 = Lynx(position=Position(xPosition=1, yPosition=2), world=world)
        
        world.addOrganism(lynx1)
        world.addOrganism(lynx2)

        available_positions = lynx1.getNeighboringPosition()

        self.assertNotIn(lynx2.position, available_positions)

        
if __name__ == '__main__':
    unittest.main()