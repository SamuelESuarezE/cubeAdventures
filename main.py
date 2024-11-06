import pygame
import pygame.freetype
from modules.player import Player
from modules.tile import Tile
from modules.levels_config import level1, enemies1
from modules.constants import *

# Inicializar juego
pygame.init()
pygame.mixer.init()
pygame.font.init()

# Ventana
SCREEN = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT), pygame.SCALED, vsync=1)

icon = pygame.image.load('assets/player.png')
pygame.display.set_caption('Cube Adventures')
pygame.display.set_icon(icon)
my_font = pygame.freetype.SysFont('courier', 30)
pygame.mixer.music.load('assets/Eric Skiff - Underclocked.mp3')
winning_sound = pygame.mixer.Sound("assets/win.mp3")
pygame.mixer.music.play(-1)
pygame.mixer.music.set_volume(0.2)

def draw_rects():
    player.draw(SCREEN)
    level1.draw(SCREEN)

    for enemy in enemies:
        enemy.draw(SCREEN)
        enemy.move()

def show_menu():
    while True:
        SCREEN.fill(COLOR_BG)

        title = pygame.image.load('assets/title.png')
        SCREEN.blit(title, (SCREEN_WIDTH / 2 - title.get_width() / 2, SCREEN_HEIGHT / 4 - title.get_height() / 2))
        
        my_font.render_to(SCREEN, (350, 275), "Select a level", fgcolor=(255, 255, 255), size=20)

        level_buttons = [
            pygame.Rect(345, 320, 100, 50),
            pygame.Rect(465, 320, 100, 50),
            pygame.Rect(585, 320, 100, 50)
        ]

        for i, button in enumerate(level_buttons):
            pygame.draw.rect(SCREEN, COLOR_GRAY, button)
            my_font.render_to(SCREEN, (button.x + 10, button.y + 18), f"Level {i + 1}", fgcolor=(255, 255, 255), size=20)

        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return None
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                for i, button in enumerate(level_buttons):
                    if button.collidepoint(mouse_pos):
                        return i + 1 

levels = {
    1: {"level": level1, "enemies": enemies1}
}

selected_level = show_menu()

if selected_level:
    level = levels[selected_level]['level']
    enemies = levels[selected_level]['enemies']
    player = Player(level.spawn_point[0], level.spawn_point[1])

while True:
    CLOCK.tick(FPS)
    SCREEN.fill(COLOR_BG)

    draw_rects()

    # Eventos
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
        
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                player.moving_left = True
            if event.key == pygame.K_RIGHT:
                player.moving_right = True
            if event.key == pygame.K_UP:
                player.moving_up = True
            if event.key == pygame.K_DOWN:
                player.moving_down = True
            if event.key == pygame.K_r:
                player.reset()
            if event.key == pygame.K_ESCAPE:
                selected_level = show_menu()
                level = levels[selected_level]['level']
                enemies = levels[selected_level]['enemies']
                player.reset()
            

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                player.moving_left = False
            if event.key == pygame.K_RIGHT:
                player.moving_right = False
            if event.key == pygame.K_UP:
                player.moving_up = False
            if event.key == pygame.K_DOWN:
                player.moving_down = False

    if player.alive:
        player.move()

        for rect in level.map:
            if player.rect.colliderect(rect.rect) and rect.type == 2:
                player.dead()
                break
            if player.rect.colliderect(rect.rect) and rect.type == 1:
                if player.moving_up:
                    player.rect.y += 5
                if player.moving_down:
                    player.rect.y -= 5
                if player.moving_left:
                    player.rect.x += 5
                if player.moving_right:
                    player.rect.x -= 5
            if player.rect.colliderect(rect.rect) and rect.type == 3:
                winning_sound.play()
                selected_level = show_menu()
                if selected_level:
                    level = levels[selected_level]['level']
                    enemies = levels[selected_level]['enemies']
                    player.reset()
                break
            if player.rect.collidelist([enemy.rect for enemy in enemies]) != -1:
                player.dead()
                break
    


    if not player.alive:
        my_font.render_to(SCREEN, (SCREEN_WIDTH / 2 - 100, SCREEN_HEIGHT / 2 - 100), "GAME OVER", fgcolor=COLOR_WHITE, size=30)
        my_font.render_to(SCREEN, (SCREEN_WIDTH / 2 - 120, SCREEN_HEIGHT / 2 - 50), "Press R to restart", fgcolor=COLOR_WHITE, size=30)



    
    pygame.display.update()
