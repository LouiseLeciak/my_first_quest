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

### Menu principal ###
def draw_button(surface, text, rect, color, font):
    pygame.draw.rect(surface, color, rect)
    txt_surf = font.render(text, True, (255, 255, 255))
    txt_rect = txt_surf.get_rect(center=rect.center)
    surface.blit(txt_surf, txt_rect)

def show_menu(screen, font):
    button_play = pygame.Rect(150, 150, 200, 50)
    button_options = pygame.Rect(150, 220, 200, 50)
    button_quit = pygame.Rect(150, 290, 200, 50)
    while True:
        screen.fill((20, 20, 20))
        draw_button(screen, "Jouer", button_play, (70, 130, 180), font)
        draw_button(screen, "Options", button_options, (120, 120, 200), font)
        draw_button(screen, "Quitter", button_quit, (180, 70, 70), font)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return "quit"
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                if button_play.collidepoint(event.pos):
                    return "play"
                elif button_options.collidepoint(event.pos):
                    show_options(screen, font)
                elif button_quit.collidepoint(event.pos):
                    return "quit"

        pygame.display.flip()

def show_options(screen, font):
    back_button = pygame.Rect(150, 300, 200, 50)

    while True:
        screen.fill((50, 50, 50))
        title = font.render("Options", True, (255, 255, 255))
        screen.blit(title, (500 // 2 - title.get_width() // 2, 50)) # 500 pour scren width

        option_txt = font.render("Pas d'option dispo pour le moment", True, (200, 200, 200))
        screen.blit(option_txt, (500 // 2 - option_txt.get_width() // 2, 150))

        draw_button(screen, "Retour", back_button, (120, 120, 200), font)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                if back_button.collidepoint(event.pos):
                    return

        pygame.display.flip()