import unittest
from Position import Position
from World import World
from Organisms.Alien import Alien

class TestAlien(unittest.TestCase):

    def test_alien_is_stationary(self):
        world = World(3, 3)
        alien = Alien(position=Position(xPosition=1, yPosition=1), world=world)
        world.addOrganism(alien)

        move_actions = alien.move()
        action_actions = alien.action()

        self.assertEqual(len(move_actions), 0)
        self.assertEqual(len(action_actions), 0)

    def test_alien_freezes_neighborhood(self):
        world = World(3, 3)
        alien = Alien(position=Position(xPosition=0, yPosition=0), world=world)
        world.addOrganism(alien)

        frozen = alien.getFrozenPositions()

        expected_frozen = {(0, 1), (1, 0), (1, 1)}
        self.assertEqual(frozen, expected_frozen)

if __name__ == '__main__':
    unittest.main()