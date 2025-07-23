import pygame
from utils import load_map, draw_map, draw_player, find_player
from utils import show_menu, show_options, draw_button
from battle import start_battle

TILE_SIZE = 40
SCREEN_WIDTH = 500
SCREEN_HEIGHT = 400
COLORS = {
    '#': (34, 139, 34),
    '.': (220, 220, 220),
    'P': (255, 255, 0),
    'N': (0, 128, 255),
    'O': (255, 105, 180),
    'E': (255, 0, 0),
}

pygame.init()
font = pygame.font.SysFont(None, 40)

### Jeu principal ###
def run_game():
    map_data = load_map("map.txt")
    MAP_HEIGHT = len(map_data)
    MAP_WIDTH = len(map_data[0])
    SCREEN_WIDTH_GAME = TILE_SIZE * MAP_WIDTH
    SCREEN_HEIGHT_GAME = TILE_SIZE * MAP_HEIGHT

    screen = pygame.display.set_mode((SCREEN_WIDTH_GAME, SCREEN_HEIGHT_GAME))
    pygame.display.set_caption("My first quest")
    clock = pygame.time.Clock()

    player_x, player_y = find_player(map_data)
    map_data[player_y][player_x] = '.'

    running = True
    while running:
        screen.fill((0, 0, 0))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        keys = pygame.key.get_pressed()
        dx, dy = 0, 0
        if keys[pygame.K_LEFT]: dx = -1
        elif keys[pygame.K_RIGHT]: dx = 1
        elif keys[pygame.K_UP]: dy = -1
        elif keys[pygame.K_DOWN]: dy = 1

        new_x, new_y = player_x + dx, player_y + dy
        if 0 <= new_x < MAP_WIDTH and 0 <= new_y < MAP_HEIGHT:
            tile = map_data[new_y][new_x]
            if tile in ['.', 'O', 'N']:
                player_x, player_y = new_x, new_y
            elif tile == 'E':
                result = start_battle(screen,font)
                screen = pygame.display.set_mode((SCREEN_WIDTH_GAME, SCREEN_HEIGHT_GAME))
                if result in ["victory", "peace"]:
                    map_data[new_y][new_x] = '.'
                    player_x, player_y = new_x, new_y
                elif result == "defeat":
                    print("Tu as perdu !")
                    pygame.time.wait(2000)
                    return

        draw_map(screen, map_data, COLORS, TILE_SIZE)
        draw_player(screen, (player_x, player_y), TILE_SIZE, COLORS['P'])

        pygame.display.flip()
        clock.tick(10)

# Main

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
action = show_menu(screen, font)

if action == "play":
    run_game()

pygame.quit()
