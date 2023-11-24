import pygame
import random

import pygame.draw

pygame.init()
PLAYER_SPEED = 9
X_SCREEN = 900
Y_SCREEN = 900
FPS = 60
HALF_X = 900//2
BALL_SPEED_x = 0
BALL_SPEED_y = 0
LEFT_XPOS = 100
RIGHT_XPOS = 800
LEFT_YPOS = 450
RIGHT_YPOS = 450
RANDOM = random.choice([1,-1])
UPORDOWN = random.choice(["UP", "DOWN"])
randomnum = random.randint(0,1)
BALL_X = random.randint(425,475)
if UPORDOWN=="UP":
    BALL_Y = random.randint(300, 330)
    if randomnum==0:
        BALL_SPEED_x = -5
        BALL_SPEED_y = -5
    else:
        BALL_SPEED_x = 5
        BALL_SPEED_y = -5
else:
    BALL_Y = random.randint(600, 630)
    if randomnum==0:
        BALL_SPEED_x = -5
        BALL_SPEED_y = 5
    else:
        BALL_SPEED_x = 5
        BALL_SPEED_y = 5
screen = pygame.display.set_mode((X_SCREEN,Y_SCREEN))
clock = pygame.time.Clock()
while True:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            pygame.quit()
            exit()
    screen.fill("black")
    KEYS = pygame.key.get_pressed()
    if KEYS[pygame.K_w]:
        LEFT_YPOS -= PLAYER_SPEED
    if KEYS[pygame.K_s]:
        LEFT_YPOS += PLAYER_SPEED
    if KEYS[pygame.K_UP]:
        RIGHT_YPOS -= PLAYER_SPEED
    if KEYS[pygame.K_DOWN]:
        RIGHT_YPOS += PLAYER_SPEED
    for i in range(0,900,30):
        pygame.draw.rect(screen,"white",[HALF_X, i + i*1, 2, 30])
    pygame.draw.rect(screen, "white",[BALL_X,BALL_Y,5,5])
    pygame.draw.rect(screen,"white", [LEFT_XPOS,LEFT_YPOS, 2, 50])
    pygame.draw.rect(screen,"white", [RIGHT_XPOS, RIGHT_YPOS, 2, 50])
    BALL_X += BALL_SPEED_x
    BALL_Y += BALL_SPEED_y
    if BALL_Y <= 0:
        BALL_SPEED_y *= -1
    if BALL_Y >= Y_SCREEN:
        BALL_SPEED_y *= -1
    pygame.display.update()
    clock.tick(FPS)