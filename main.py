import random
import pygame

pygame.init()
#window settings/general settings
w_width, w_height = 800, 600
window = pygame.display.set_mode((w_width, w_height))
pygame.display.set_caption("funi snek game")
#clock
clock = pygame.time.Clock()
#font
font = pygame.font.SysFont("arial", 25, bold=True)

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
    "x": random.choice([109, 242, 375, 508, 641]),
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

    #movement logic and cube collision
    for cube in cubes[:]:
        cube["y"] += cube["vel_y"]
        cube_rect = pygame.Rect(cube["x"], cube["y"], 50, 50)

        if player_rect.colliderect(cube_rect):
            if score > personal_best:
                personal_best = score
            attempts += 1
            reset_game()
            break

        if cube["y"] > w_height:
            cube.update(spawn_cubes())
            score += 1
            if score % 10 == 0:
                wave += 1
                cubes.append(spawn_cubes())

#window drawing
#this needs to be first bc its the background
    window.fill((0, 0, 0))

#player draw
    window.blit(player_surface, (player_x, player_y))
#cubes draw
    for cube in cubes:
        window.blit(cube_surface, (cube["x"], cube["y"]))

#HUD
    text_score = font.render(f"Score: {score}", True, (255, 255, 255))
    text_wave = font.render(f"Wave: {wave}", True, (255, 255, 255))
    text_stats = font.render(f"PB: {personal_best} | attempts: {attempts}", True, (255, 255, 0))

    window.blit(text_score, (10, 10))
    window.blit(text_wave, (10, 35))
    window.blit(text_stats, (w_width - text_stats.get_width() - 10, 10))


    pygame.display.flip()
    clock.tick(240)