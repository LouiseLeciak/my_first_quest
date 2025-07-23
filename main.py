import pygame
from utils import load_map, draw_map, draw_player, find_player

TILE_SIZE = 40
map_data = load_map("map.txt")
MAP_HEIGHT = len(map_data)
MAP_WIDTH = len(map_data[0])
SCREEN_WIDTH = TILE_SIZE * MAP_WIDTH
SCREEN_HEIGHT = TILE_SIZE * MAP_HEIGHT
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

COLORS = {
    '#': (34, 139, 34),     # Arbre
    '.': (220, 220, 220),   # Sol
    'P': (255, 255, 0),     # Joueur
    'N': (0, 128, 255),     # PNJ
    'O': (255, 105, 180),   # Objet
    'E': (255, 0, 0),       # Ennemi
}

pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("My first quest")
clock = pygame.time.Clock()

map_data = load_map("map.txt")
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
        if map_data[new_y][new_x] in ['.', 'O', 'N']:
            player_x, player_y = new_x, new_y

    draw_map(screen, map_data, COLORS, TILE_SIZE)
    draw_player(screen, (player_x, player_y), TILE_SIZE, COLORS['P'])

    pygame.display.flip()
    clock.tick(10)

pygame.quit()
