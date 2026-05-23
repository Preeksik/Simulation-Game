import random
from ActionEnum import ActionEnum
from Position import Position
from Organisms.Alien import Alien

class Turn:
    def __init__(self, world):
         self.world = world

    def makeTurn(self):
        actions = []

        frozen_positions = set()
        for org in self.world.organisms:
            if isinstance(org, Alien):
                frozen_positions.update(org.getFrozenPositions())

        species_counts = {}
        for org in self.world.organisms:
            if not isinstance(org, Alien) and self.world.positionOnBoard(org.position):
                species_name = type(org).__name__
                species_counts[species_name] = species_counts.get(species_name, 0) + 1

        for org in self.world.organisms:
            if not isinstance(org, Alien) and self.world.positionOnBoard(org.position):
                species_name = type(org).__name__
                if species_counts.get(species_name, 0) <= 2:
                    org.power += 2 

        for org in self.world.organisms:
            if (org.position.x, org.position.y) in frozen_positions:
                continue 

            if self.world.positionOnBoard(org.position):
                actions = org.move()
                for a in actions:
                    self.makeMove(a)
                actions = []
                if self.world.positionOnBoard(org.position):
                    actions = org.action()
                    for a in actions:
                        self.makeMove(a)
                    actions = []

        self.world.organisms = [o for o in self.world.organisms if self.world.positionOnBoard(o.position)]
        
        for o in self.world.organisms:
            if (o.position.x, o.position.y) in frozen_positions:
                continue

            o.liveLength -= 1
            o.power += 1 
            
            if self.world.plague_turns > 0:
                o.liveLength = o.liveLength // 2

            if o.liveLength < 1:
                print(str(o.__class__.__name__) + ': died of old age at: ' + str(o.position))

        if self.world.plague_turns > 0:
            self.world.plague_turns -= 1
            print(f"Plague is active! Turns left: {self.world.plague_turns}")

        self.world.organisms = [o for o in self.world.organisms if o.liveLength > 0]

        self.world.newOrganisms = [o for o in self.world.newOrganisms if self.world.positionOnBoard(o.position)]
        self.world.organisms.extend(self.world.newOrganisms)
        
        self.world.organisms.sort(key=lambda o: o.initiative, reverse=True)
        self.world.newOrganisms = []

        self.world.turn += 1

        if self.world.turn % 7 == 0:
            free_positions = []
            for x in range(self.world.worldX):
                for y in range(self.world.worldY):
                    pos = Position(xPosition=x, yPosition=y)
                    if self.world.getOrganismFromPosition(pos) is None:
                        free_positions.append(pos)
            
            if free_positions:
                spawn_pos = random.choice(free_positions)
                new_alien = Alien(position=spawn_pos, world=self.world)
                self.world.addOrganism(new_alien)
                print(f"Alien (K) landed at ({spawn_pos.x}, {spawn_pos.y}) and froze time!")

    def makeMove(self, action):
        if action.action == ActionEnum.A_ADD:
            self.world.newOrganisms.append(action.organism) 
        elif action.action == ActionEnum.A_INCREASEPOWER:
            action.organism.power += action.value
        elif action.action == ActionEnum.A_MOVE:
            action.organism.position = action.position
        elif action.action == ActionEnum.A_REMOVE:
            action.organism.position = Position(xPosition=-1, yPosition=-1)