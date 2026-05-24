from Turn import Turn
from Organisms.Lynx import Lynx
from Render import Renderer
from World import World
from Position import Position
from Organisms.Grass import Grass
from Organisms.Sheep import Sheep
from Organisms.Antelope import Antelope
from Organisms.Alien import Alien
import os

if __name__ == '__main__':
    pyWorld = World(5, 5)
    renderer = Renderer(pyWorld)
    turn_manager = Turn(pyWorld)

    newOrg = Grass(position=Position(xPosition=2, yPosition=2), world=pyWorld)
    pyWorld.addOrganism(newOrg)

    newOrg = Grass(position=Position(xPosition=2, yPosition=4), world=pyWorld)
    pyWorld.addOrganism(newOrg)

    newOrg = Sheep(position=Position(xPosition=2, yPosition=3), world=pyWorld)
    pyWorld.addOrganism(newOrg)

    newOrg = Lynx(position=Position(xPosition=3, yPosition=2), world=pyWorld)
    pyWorld.addOrganism(newOrg)

    newOrg = Antelope(position=Position(xPosition=2, yPosition=2), world=pyWorld)
    pyWorld.addOrganism(newOrg)

    print(renderer.render())    

    for _ in range(0, 30):
        user_input = input('Enter - new turn | "p" - Plaga | "a" - add organism: ').lower()
        
        if user_input == 'p':
            pyWorld.plague_turns = 2
            print("PLAGUE HAS STARTED")
            input("Press ENTER to continue")
            
        elif user_input == 'd':
            try:
                gatunek = input("Input letter (L - Lynx, A - Antelope, S - Sheep, G - Grass): ").upper()
                x = int(input("Input position X: "))
                y = int(input("Input position Y: "))
                
                nowy_org = None
                pos = Position(xPosition=x, yPosition=y)
                
                if gatunek == 'L':
                    nowy_org = Lynx(position=pos, world=pyWorld)
                elif gatunek == 'A':
                    nowy_org = Antelope(position=pos, world=pyWorld)
                elif gatunek == 'S':
                    nowy_org = Sheep(position=pos, world=pyWorld)
                elif gatunek == 'G':
                    nowy_org = Grass(position=pos, world=pyWorld)
                else:
                    print("Nieznany gatunek!")
                    
                if nowy_org:
                    pyWorld.addOrganism(nowy_org)
                    print(f"Successfully dropped organism {gatunek} from the sky at position ({x}, {y})!")
            except ValueError:
                print("ERROR: X and Y are supposed to be numbers")
            
            input("Press ENTER to continue")
        
        os.system('cls')
        turn_manager.makeTurn()
        print(renderer.render())