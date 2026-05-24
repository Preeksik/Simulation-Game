import pygame
import sys
import random
from World import World
from Turn import Turn
from Position import Position
from Organisms.Grass import Grass
from Organisms.Sheep import Sheep
from Organisms.Antelope import Antelope
from Organisms.Lynx import Lynx
from Organisms.Alien import Alien

CELL_SIZE = 64
BOARD_WIDTH = 5
BOARD_HEIGHT = 5
UI_HEIGHT = 80  
WINDOW_WIDTH = CELL_SIZE * BOARD_WIDTH
WINDOW_HEIGHT = (CELL_SIZE * BOARD_HEIGHT) + UI_HEIGHT 

def load_image(name):
    try:
        img = pygame.image.load(f"assets/{name}.png").convert_alpha()
        return pygame.transform.scale(img, (CELL_SIZE, CELL_SIZE))
    except FileNotFoundError:
        print(f"BŁĄD: Nie znaleziono pliku assets/{name}.png!")
        sys.exit()

if __name__ == '__main__':
    pygame.init()
    pygame.font.init()
    screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
    pygame.display.set_caption("Symulator Ekosystemu + Alien")

    
    font = pygame.font.SysFont('arial', 16, bold=True)

    img_bg = load_image("grass_bg")
    sprites = {
        "Grass": load_image("grass"),
        "Sheep": load_image("sheep"),
        "Antelope": load_image("antelope"),
        "Lynx": load_image("lynx"),
        "Alien": load_image("alien")
    }

    pyWorld = World(BOARD_WIDTH, BOARD_HEIGHT)
    turn_manager = Turn(pyWorld)

    pyWorld.addOrganism(Sheep(position=Position(xPosition=1, yPosition=1), world=pyWorld))
    pyWorld.addOrganism(Antelope(position=Position(xPosition=3, yPosition=3), world=pyWorld))
    pyWorld.addOrganism(Lynx(position=Position(xPosition=4, yPosition=0), world=pyWorld))
    pyWorld.addOrganism(Grass(position=Position(xPosition=2, yPosition=2), world=pyWorld))

    plague_overlay = pygame.Surface((WINDOW_WIDTH, BOARD_HEIGHT * CELL_SIZE), pygame.SRCALPHA)
    plague_overlay.fill((255, 0, 0, 64)) 

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ENTER:
                    turn_manager.makeTurn()
                elif event.key == pygame.K_p:
                    pyWorld.plague_turns = 2
            
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1: 
                    mx, my = pygame.mouse.get_pos()
                    if my >= UI_HEIGHT:
                        grid_x = mx // CELL_SIZE
                        grid_y = (my - UI_HEIGHT) // CELL_SIZE
                        pos = Position(xPosition=grid_x, yPosition=grid_y)
                        
                        
                        if pyWorld.getOrganismFromPosition(pos) is None:
                            NowyGatunek = random.choice([Sheep, Antelope, Lynx, Grass])
                            pyWorld.addOrganism(NowyGatunek(position=pos, world=pyWorld))

        pygame.draw.rect(screen, (40, 40, 40), (0, 0, WINDOW_WIDTH, UI_HEIGHT)) 
        tekst_tura = font.render("SPACJA - Następna tura", True, (255, 255, 255))
        tekst_plaga = font.render("P - Wywołaj Plagę", True, (255, 100, 100))
        tekst_dodaj = font.render("Lewy Klik na planszę - Dodaj losowy byt", True, (150, 255, 150))
        
        screen.blit(tekst_tura, (10, 10))
        screen.blit(tekst_plaga, (10, 32))
        screen.blit(tekst_dodaj, (10, 54))

        for x in range(BOARD_WIDTH):
            for y in range(BOARD_HEIGHT):
                px = x * CELL_SIZE
                py = y * CELL_SIZE + UI_HEIGHT
                screen.blit(img_bg, (px, py))
                
                rect = pygame.Rect(px, py, CELL_SIZE, CELL_SIZE)
                pygame.draw.rect(screen, (0, 0, 0), rect, 2) 

        frozen_positions = set()
        for org in pyWorld.organisms:
            if isinstance(org, Alien):
                frozen_positions.update(org.getFrozenPositions())
                
        for fx, fy in frozen_positions:
            ice_surface = pygame.Surface((CELL_SIZE, CELL_SIZE), pygame.SRCALPHA)
            ice_surface.fill((0, 150, 255, 128)) 
            screen.blit(ice_surface, (fx * CELL_SIZE, fy * CELL_SIZE + UI_HEIGHT))

        for org in pyWorld.organisms:
            x_px = org.position.x * CELL_SIZE
            y_px = org.position.y * CELL_SIZE + UI_HEIGHT 
            species_name = type(org).__name__
            
            if species_name in sprites:
                screen.blit(sprites[species_name], (x_px, y_px))
                
            max_bar_width = CELL_SIZE - 6
            power_width = min(org.power * 4, max_bar_width) 
            
            pygame.draw.rect(screen, (0, 0, 0), (x_px + 2, y_px + 2, power_width + 2, 8))
            pygame.draw.rect(screen, (255, 40, 40), (x_px + 3, y_px + 3, power_width, 6))

        if pyWorld.plague_turns > 0:
            screen.blit(plague_overlay, (0, UI_HEIGHT))

        pygame.display.flip()

    pygame.quit()