## https://youtu.be/ZV8TNrwqG1Y
import pygame 
import random 

pygame.init()

#game constants 
white = (255, 255, 255)
black = (0,0,0)
green = (0,255, 0)
red = (255, 0, 0)
orange = (255, 165, 0)
yellow = (255, 255, 0)
sky_blue = (0, 255, 255)
grass_green = (106, 168, 79)
#450, 300
WIDTH = 900
HEIGHT = 600
floor_y = 510

#game variables
score = 0
high_score = 0
player_x = 50
player_y = floor_y - 10
player_width = 60
player_height = 100
x_change = 0
y_change = 0
gravity = 1
active = False
obstacles_speed = 2
## obstacle [x position, width, height, speed]
mtd_start_pos = random.randint(WIDTH + 50, WIDTH + 200)
snowman_start_pos = random.randint(WIDTH + 50, WIDTH + 200)
squirrel_start_pos = random.randint(WIDTH + 50, WIDTH + 200)
mtd_obstacle = [mtd_start_pos, 3 * player_width, player_height, 1.25 * obstacles_speed]
snowman_obstacle = [snowman_start_pos, player_width, 2 * player_height, 0.5 * obstacles_speed]
squirrel_obstacle = [squirrel_start_pos, 0.5 * player_width, 0.5* player_height, 2 * obstacles_speed]
obstacles = [mtd_obstacle, snowman_obstacle, squirrel_obstacle]


screen = pygame.display.set_mode([WIDTH, HEIGHT])
pygame.display.set_caption("The Runs")
fps = 60
font = pygame.font.Font('freesansbold.ttf', 24)
title_font = pygame.font.Font('freesansbold.ttf', 64)
timer = pygame.time.Clock()

BACKGROUND_IMAGE = pygame.image.load("RunsWorking\game\\background.jpg")
PLAYER_IMAGE = pygame.image.load('RunsWorking\pyxelate\modified_char_dude.png').convert()
MTD_IMAGE = pygame.image.load('RunsWorking\game\mtd.png').convert()
SNOWMAN_IMAGE = pygame.image.load('RunsWorking\game\snowman.png').convert()
SQUIRREL_IMAGE = pygame.image.load('RunsWorking\game\squirrel.png').convert()

BACKGROUND_IMAGE = pygame.transform.scale(BACKGROUND_IMAGE, (WIDTH, HEIGHT))
PLAYER_IMAGE = pygame.transform.scale(PLAYER_IMAGE, (player_width, player_height))
MTD_IMAGE = pygame.transform.scale(MTD_IMAGE, (mtd_obstacle[1], mtd_obstacle[2]))
SNOWMAN_IMAGE = pygame.transform.scale(SNOWMAN_IMAGE, (snowman_obstacle[1], snowman_obstacle[2]))
SQUIRREL_IMAGE = pygame.transform.scale(SQUIRREL_IMAGE, (squirrel_obstacle[1], squirrel_obstacle[2]))

running = True
while running:
    timer.tick(fps)
    screen.blit(BACKGROUND_IMAGE, (0, 0))
    if not active:
        welcome_text = title_font.render(f'The Runs', True, black, sky_blue)
        screen.blit(welcome_text, ((WIDTH / 2) - 165, HEIGHT - 550))
        instruction_text = font.render(f'Press [SPACE] to start', True, black, sky_blue)
        screen.blit(instruction_text, ((WIDTH / 2) - 150, HEIGHT - 400))
    score_text = font.render(f'Score: {score}', True, white, grass_green)
    screen.blit(score_text, ((WIDTH / 2) - 130, HEIGHT - 30))
    high_score_text = font.render(f'High Score: {high_score}', True, white, grass_green)
    screen.blit(high_score_text, ((WIDTH / 2) + 40, HEIGHT - 30))
    floor = pygame.draw.rect(screen, grass_green, [0, floor_y, WIDTH, 5])
    player = PLAYER_IMAGE.get_rect()
    player.center = (player_x, player_y)
    obstacle0 = MTD_IMAGE.get_rect()
    obstacle0.center = (obstacles[0][0], floor_y - obstacles[0][2])

    obstacle1 = SNOWMAN_IMAGE.get_rect()
    obstacle1.center = (obstacles[1][0], floor_y - obstacles[1][2])
    obstacle2 = SQUIRREL_IMAGE.get_rect()
    obstacle2.center = (obstacles[2][0], floor_y - obstacles[2][2])
    screen.blit(PLAYER_IMAGE, (player_x, player_y)) 
    screen.blit(MTD_IMAGE, (obstacles[0][0], floor_y - obstacles[0][2])) 
    screen.blit(SNOWMAN_IMAGE, (obstacles[1][0], floor_y - obstacles[1][2])) 
    screen.blit(SQUIRREL_IMAGE, (obstacles[2][0], floor_y - obstacles[2][2])) 

    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN and not active:
            if event.key == pygame.K_SPACE:
                obstacles[0][0] = mtd_start_pos
                obstacles[1][0] = snowman_start_pos
                obstacles[2][0] = squirrel_start_pos
                player_x = 50
                score = 0
                active = True
        if event.type == pygame.KEYDOWN and active:
            if event.key == pygame.K_SPACE and y_change == 0:
                y_change = 20
            if event.key == pygame.K_RIGHT:
                x_change = 10
            if event.key == pygame.K_LEFT:
                x_change = -10
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT:
                x_change = 0
            if event.key == pygame.K_LEFT:
                x_change = 0
    
    for i in range(len(obstacles)):
        if active:
            obstacles[i][0] -= obstacles[i][3] # obstacle speed
            if obstacles[i][0] < -(obstacles[i][1]): # pos is off screen
                obstacles[i][0] = random.randint(WIDTH + 20, WIDTH + 120)
                score += 1
            
            if player.colliderect(obstacle0) or player.colliderect(obstacle1) or player.colliderect(obstacle2):
                if score > high_score:
                    high_score = score
                obstacles[0][0] = mtd_start_pos
                obstacles[1][0] = snowman_start_pos
                obstacles[2][0] = squirrel_start_pos
                player_x = 50
                score = 0
                active = False

    if 0 <= player_x <= WIDTH - player_width:
        player_x += x_change
    if player_x < 0:
        player_x = 0
    if player_x > WIDTH - player_width:
        player_x = WIDTH - player_width

    if y_change > 0 or player_y < floor_y - player_height:
        player_y -= y_change
        y_change -= gravity 
    if player_y > floor_y - player_height: ## below floor
        player_y = floor_y - player_height
    if player_y == floor_y - player_height and y_change < 0:
        y_change = 0
    
    pygame.display.flip()
pygame.quit()
