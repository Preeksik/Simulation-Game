import unittest
from Position import Position
from World import World
from Organisms.Sheep import Sheep
from Organisms.Antelope import Antelope
from Turn import Turn

class TestEvolution(unittest.TestCase):

    def test_evolution_buffs_endangered_species(self):
        world = World(5, 5)
        turn_manager = Turn(world)

        sheep1 = Sheep(position=Position(xPosition=0, yPosition=0), world=world)
        sheep2 = Sheep(position=Position(xPosition=4, yPosition=4), world=world)
        
        ant1 = Antelope(position=Position(xPosition=0, yPosition=4), world=world)
        ant2 = Antelope(position=Position(xPosition=4, yPosition=0), world=world)
        ant3 = Antelope(position=Position(xPosition=2, yPosition=2), world=world)
        
        for org in [sheep1, sheep2, ant1, ant2, ant3]:
            org.power = 1
            org.powerToReproduce = 999
            world.addOrganism(org)

        turn_manager.makeTurn()

        self.assertEqual(sheep1.power, 4)
        self.assertEqual(sheep2.power, 4)

        self.assertEqual(ant1.power, 2)
        self.assertEqual(ant2.power, 2)
        self.assertEqual(ant3.power, 2)

if __name__ == '__main__':
    unittest.main()