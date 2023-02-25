https://youtu.be/ZV8TNrwqG1Y
import pygame 
import random 

pygame.init()

#game constants 
white = (255, 255, 255)
black = (0,0,0)
green = (0,255, 0)
Width = 450
Height = 300

#game variables
score = 0
player_first = 50
player_second = 200
y_change = 0
gravity = 1

screen = pygame.display.set_mode([Width, Height])
pygame.display.set_caption("Infinite Runner")
background = black 
fps = 60
font = pygame.font.Font('freesansbold.ttf', 16)
timer = pygame.time.Clock()

running = True;
while running:
    timer.tick(fps)
    screen.fill(background)
    floor = pygame.draw.rect(screen, white, [0, 220, Width, 5])
    player = pygame.draw.rect(screen, green, [player_first, player_second, 20, 20])

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE and y_change == 0:
                y_change = 18

    if y_change > 0 or player_second < 200:
        player_second -= y_change
        y_change -= gravity 

    
    pygame.display.flip()
pygame.quit()
