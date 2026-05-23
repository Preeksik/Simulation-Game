import unittest
from Position import Position
from World import World
from Organisms.Sheep import Sheep
from Turn import Turn
class TestPlague(unittest.TestCase):

    def test_plague_halves_life(self):
        world = World(3, 3)
        turn_manager = Turn(world)
        
        sheep = Sheep(position=Position(xPosition=1, yPosition=1), world=world)
        sheep.liveLength = 10 
        world.addOrganism(sheep)

        world.plague_turns = 1 

        turn_manager.makeTurn()

        self.assertEqual(sheep.liveLength, 4)

if __name__ == '__main__':
    unittest.main()