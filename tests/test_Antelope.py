import unittest
from Position import Position
from World import World
from Organisms.Lynx import Lynx
from Organisms.Antelope import Antelope
from ActionEnum import ActionEnum

class TestAntelope(unittest.TestCase):

    def test_antelope_escapes_from_lynx(self):
        world = World(5, 5)
        antelope = Antelope(position=Position(xPosition=2, yPosition=2), world=world)
        lynx = Lynx(position=Position(xPosition=2, yPosition=1), world=world)
        
        world.addOrganism(antelope)
        world.addOrganism(lynx)

        actions = antelope.move()

        self.assertTrue(len(actions) > 0)
        action = actions[0]
        self.assertEqual(action.action, ActionEnum.A_MOVE)
        self.assertEqual(action.position.x, 2)
        self.assertEqual(action.position.y, 4)

    def test_antelope_attacks_when_cornered(self):
        world = World(3, 3)
        antelope = Antelope(position=Position(xPosition=0, yPosition=0), world=world)
        lynx = Lynx(position=Position(xPosition=0, yPosition=1), world=world)
        
        world.addOrganism(antelope)
        world.addOrganism(lynx)

        actions = antelope.move()

        action = actions[0]
        self.assertEqual(action.action, ActionEnum.A_MOVE)
        self.assertEqual(action.position.x, 0)
        self.assertEqual(action.position.y, 1)

if __name__ == '__main__':
    unittest.main()