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
WIDTH = 450
HEIGHT = 300
floor_y = 220

#game variables
score = 0
high_score = 0
player_x = 50
player_y = floor_y - 10
player_width = 20
player_height = 20
x_change = 0
y_change = 0
gravity = 1
active = False
obstacles_speed = 2
## obstacle [x position, width, height, speed]
mtd_start_pos = WIDTH - (WIDTH / 2) + 100
snowman_start_pos = WIDTH
pl_logo_start_pos = WIDTH + (WIDTH / 2)
mtd_obstacle = [mtd_start_pos, 7 * player_width, 3 * player_height, 1.5 * obstacles_speed]
snowman_obstacle = [snowman_start_pos, player_width, 5 * player_height, 0.5 * obstacles_speed]
pl_logo_obstacle = [pl_logo_start_pos, player_width, player_height, 2 * obstacles_speed]
obstacles = [mtd_obstacle, snowman_obstacle, pl_logo_obstacle]


screen = pygame.display.set_mode([WIDTH, HEIGHT])
pygame.display.set_caption("The Runs")
background = black 
fps = 60
font = pygame.font.Font('freesansbold.ttf', 16)
timer = pygame.time.Clock()

IMAGE = pygame.image.load('game\\think.jpeg').convert()
# Create a rect with the size of the image.
IMAGE = pygame.transform.scale(IMAGE, (player_width, player_height))

running = True
while running:
    timer.tick(fps)
    screen.fill(background)
    if not active:
        welcome_text = font.render(f'The Runs', True, red, black)
        screen.blit(welcome_text, ((WIDTH / 2) - 40, HEIGHT - 250))
        instruction_text = font.render(f'Press [SPACE] to start', True, white, black)
        screen.blit(instruction_text, ((WIDTH / 2) - 80, HEIGHT - 200))
    score_text = font.render(f'Score: {score}', True, white, black)
    screen.blit(score_text, ((WIDTH / 2) - 130, HEIGHT - 50))
    high_score_text = font.render(f'High Score: {high_score}', True, white, black)
    screen.blit(high_score_text, ((WIDTH / 2) + 40, HEIGHT - 50))
    floor = pygame.draw.rect(screen, white, [0, floor_y, WIDTH, 5])
    player = IMAGE.get_rect()
    player.center = (player_x, player_y)
    screen.blit(IMAGE, (player_x, player_y)) #updates player position
    obstacle0 = pygame.draw.rect(screen, red, [obstacles[0][0], floor_y - obstacles[0][2], obstacles[0][1], obstacles[0][2]])
    obstacle1 = pygame.draw.rect(screen, orange, [obstacles[1][0], floor_y - obstacles[1][2], obstacles[1][1], obstacles[1][2]])
    obstacle2 = pygame.draw.rect(screen, yellow, [obstacles[2][0], floor_y - obstacles[2][2], obstacles[2][1], obstacles[2][2]])
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN and not active:
            if event.key == pygame.K_SPACE:
                obstacles[0][0] = mtd_start_pos
                obstacles[1][0] = snowman_start_pos
                obstacles[2][0] = pl_logo_start_pos
                player_x = 50
                score = 0
                active = True
        if event.type == pygame.KEYDOWN and active:
            if event.key == pygame.K_SPACE and y_change == 0:
                y_change = 18
            if event.key == pygame.K_RIGHT:
                x_change = 5
            if event.key == pygame.K_LEFT:
                x_change = -5
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
                obstacles[2][0] = pl_logo_start_pos
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
