import pygame

def load_map(filename):
    with open(filename, 'r') as f:
        return [list(line.strip()) for line in f.readlines()]

def draw_map(screen, map_data, colors, tile_size):
    for y in range(len(map_data)):
        row = map_data[y]
        for x in range(len(row)):
            tile = row[x]
            color = colors.get(tile, (100, 100, 100))
            rect = pygame.Rect(x * tile_size, y * tile_size, tile_size, tile_size)
            pygame.draw.rect(screen, color, rect)

def draw_player(screen, player_pos, tile_size, color):
    x, y = player_pos
    rect = pygame.Rect(x * tile_size, y * tile_size, tile_size, tile_size)
    pygame.draw.rect(screen, color, rect)

def find_player(map_data):
    for y in range(len(map_data)):
        row = map_data[y]
        for x in range(len(row)):
            if row[x] == 'P':
                return x, y
    return 1, 1 # fallback