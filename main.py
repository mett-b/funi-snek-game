import pygame
import random

pygame.init()
#window settings/general settings
w_width, w_height = 800, 600
window = pygame.display.set_mode((w_width, w_height))
pygame.display.set_caption("funi snek game")
#clock
clock = pygame.time.Clock()
#font
pygame.font.SysFont("arial", 50, bold=True)

#player variables
player_size = 50
player_x = 375
player_y = 520
player_surface = pygame.Surface((player_size, player_size))
player_surface.fill((0, 255, 0))

#waves and cubes
cube_surface = pygame.Surface((50, 50))
cube_surface.fill((255, 0, 0))

wave = 1#even if an array should start in 0, I want it to start in 1, also vscode tab is scary, it predicts very well...

destroyed_cubes = 0

def spawn_cubes():
    return {
    "x": random.randint(0, w_width - 50),
    "y": random.randint(-150, -50),
    "vel_y": random.randint(1, 5)#fall velocity
    }

#spawn first wave of cubes
cubes = [spawn_cubes() for _ in range(6)]

personal_best = 0
attempts = 0
score = 0

def reset_game():
    global player_x, score, wave, cubes
    player_x = 375
    score = 0
    wave = 1
    cubes = [spawn_cubes() for _ in range(6)]

#  /-------------------------------------------/
# /             ACTUAL GAME LOGIC             /
#/-------------------------------------------/
while True:
#quit logic(do not remove, if removed will cause error)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit(0)
    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_LEFT:
            player_x -= 133
        elif event.key == pygame.K_RIGHT:
            player_x += 133
    #player contraints
    player_x = max(0, min(w_width - player_size, player_x))
    #player collision
    player_rect = pygame.Rect(player_x, player_y, player_size, player_size)

    #movement logic
    for cube in cubes:
        cube["y"] += cube["vel_y"]
        cube_rect = pygame.Rect(cube["x"], cube["y"], 50, 50)

#this needs to be first bc its the background
    window.fill((0, 0, 0, 0))

    pygame.display.flip()
    clock.tick(30)

    #move player by 133 pixels in X(either minus or plus) when pressing left or right arrow keys
    #also add colission to the cubes
    #also make that if the cubes get destroyed, they will respawn at the top of the screen with a random velocity
    #waves!!11!1!1
    #personal best and trys record 