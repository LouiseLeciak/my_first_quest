import pygame
from utils import load_map, draw_map, draw_player, find_player
from utils import show_menu, show_options, draw_butto

def start_battle(screen, font):
    BATTLE_WIDTH = 640
    BATTLE_HEIGHT = 480
    screen = pygame.display.set_mode((BATTLE_WIDTH, BATTLE_HEIGHT))

    player_hp = 10
    enemy_hp = 10
    dialogue = "Un ennemi apparaît !"

    attack_buttons = [
        ("Baffe", -3, 0),
        ("Croche-patte", -2, 0),
        ("Coup de boule", -4, -1),
        ("Excuses", 0, 0)
    ]

    button_width = 260
    button_height = 40
    h_spacing = 40
    v_spacing = 20

    MAX_BAR_WIDTH = 200
    BAR_HEIGHT = 20
    enemy_bar_x = BATTLE_WIDTH - MAX_BAR_WIDTH - 50
    enemy_bar_y = 50
    player_bar_x = 50
    player_bar_y = 50

    box_height = 120
    box_rect = pygame.Rect(30, BATTLE_HEIGHT - box_height - 20, BATTLE_WIDTH - 60, box_height)
    box_padding = 10

    # Calcul des positions des boutons (centrés dans box_rect)
    total_width = 2 * button_width + h_spacing
    start_x = box_rect.x + (box_rect.width - total_width) // 2
    start_y = box_rect.y + 10
    button_rects = []
    for i in range(4):
        row = i // 2
        col = i % 2
        rect = pygame.Rect(
            start_x + col * (button_width + h_spacing),
            start_y + row * (button_height + v_spacing),
            button_width,
            button_height
        )
        button_rects.append(rect)

    state = "dialogue"
    running = True
    mouse_clicked = False

    while player_hp > 0 and enemy_hp > 0 and running:
        screen.fill((0, 0, 0))

        # Barres de vie
        enemy_bar_width = max(0, enemy_hp * 20)
        player_bar_width = max(0, player_hp * 20)
        pygame.draw.rect(screen, (255, 0, 0), (enemy_bar_x, enemy_bar_y, enemy_bar_width, BAR_HEIGHT))
        pygame.draw.rect(screen, (0, 255, 0), (player_bar_x, player_bar_y, player_bar_width, BAR_HEIGHT))

        # Encadré
        pygame.draw.rect(screen, (50, 50, 50), box_rect, border_radius=10)
        pygame.draw.rect(screen, (200, 200, 200), box_rect, 3, border_radius=10)

        if state == "dialogue":
            wrapped_text = []
            words = dialogue.split(' ')
            line = ''
            for word in words:
                test_line = line + word + ' '
                if font.size(test_line)[0] > box_rect.width - 20:
                    wrapped_text.append(line)
                    line = word + ' '
                else:
                    line = test_line
            wrapped_text.append(line)

            i = 0
            for line in wrapped_text:
                txt_surf = font.render(line.strip(), True, (255, 255, 255))
                screen.blit(txt_surf, (box_rect.x + 10, box_rect.y + 10 + i * 35))
                i += 1


        elif state == "combat":
            i = 0
            for rect in button_rects:
                pygame.draw.rect(screen, (100, 100, 200), rect)
                txt_surf = font.render(attack_buttons[i][0], True, (255, 255, 255))
                txt_rect = txt_surf.get_rect(center=rect.center)
                screen.blit(txt_surf, txt_rect)
                i += 1


        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

            if event.type == pygame.KEYDOWN:
                if state == "dialogue" and event.key == pygame.K_SPACE:
                    state = "combat"
                    pygame.event.clear()
                elif state == "combat" and event.key == pygame.K_ESCAPE:
                    pass

        if state == "combat":
            if pygame.mouse.get_pressed()[0]:
                if not mouse_clicked:
                    mouse_clicked = True
                    i = 0
                    for rect in button_rects:
                        if rect.collidepoint(pygame.mouse.get_pos()):
                            if attack_buttons[i][0] == "Excuses":
                                dialogue = "L'ennemi est touché par tes excuses..."
                                state = "dialogue"
                                pygame.time.wait(1000)
                                dialogue = "Il décide de te laisser partir."
                                pygame.time.wait(1000)
                                return "peace"
                            else:
                                effect, self_damage = attack_buttons[i][1], attack_buttons[i][2]
                                enemy_hp += effect
                                player_hp += self_damage
                                dialogue = f"Tu as utilisé {attack_buttons[i][0]} !"
                                state = "dialogue"
                                pygame.time.wait(500)
                                if enemy_hp > 0:
                                    player_hp -= 2
                                    dialogue += " L'ennemi riposte !"
                        i += 1

            else:
                mouse_clicked = False

        pygame.time.wait(60)

    return "victory" if player_hp > 0 else "defeat"
