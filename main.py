import pygame
import os

pygame.init()

width = 900
height = 500
WIN = pygame.display.set_mode((width,height))
pygame.display.set_caption("Space Invaders")

WHITE = (255,255,255)
BLACK = (0,0,0)
RED = (255,0,0)
YELLOW = (255,255,0)

BORDER = pygame.Rect(width // 2 - 5, 0 ,10, height)

HEALTH_FONT = pygame.font.SysFont('cosmicsans', 40)
WINNER_FONT = pygame.font.SysFont('cosmicsans', 100)

FPS = 60 #fps is frames per second
VEL = 5 # player speed
BULLET_VEL = 7 # bullet speed
MAX_BULLETS = 3
SPACESHIP_WIDTH, SPACESHIP_HEIGHT = 55,40

#custom events

YELLOW_HIT = pygame.USEREVENT +1
RED_HIT = pygame.USEREVENT +2

YELLOW_SPACESHIP_IMAGE = pygame.image.load(os.path.join('assets', 'yellowspaceship.png'))
YELLOW_SPACESHIP = pygame.transform.rotate(pygame.transform.scale(YELLOW_SPACESHIP_IMAGE,(SPACESHIP_WIDTH, SPACESHIP_HEIGHT)), 90)

RED_SPACESHIP_IMAGE = pygame.image.load(os.path.join('assets', 'redspaceship.png'))
RED_SPACESHIP  = pygame.image.rotate(pygame.transform.scale(RED_SPACESHIP_IMAGE, (SPACESHIP_WIDTH, SPACESHIP_HEIGHT)), 270)

SPACE = pygame.transform.scale(pygame.image.load(os.path.join('assets', 'bgimg.png')), (width,height))

def draw_window(red,yellow, red_bullets, yellow_bullets, red_health, yellow_health):
    WIN.blit(SPACE, (0,0))
    pygame.draw.rect(WIN, BLACK, BORDER) #border rect in middle

    WIN.blit(RED_SPACESHIP, (red.x, red.y))

    red_health_text = HEALTH_FONT.render("Health: " + str(red_health), 1, WHITE)
    WIN.blit(red_health_text, (700,10))

    for bullet in red_bullets:
        pygame.draw.rect(WIN, RED, bullet)

    WIN.blit(YELLOW_SPACESHIP, (yellow.x, yellow.y))

    yellow_health_text = HEALTH_FONT.render("Health: " + str(yellow_health), 1, WHITE)
    WIN.blit(yellow_health_text, (700,10))

    for bullet in yellow_bullets:
        pygame.draw.rect(WIN,YELLOW, bullet)

    pygame.display.update()

# WASD KEYS
def yellow_handle_movement(keys_pressed, yellow):
    if keys_pressed[pygame.K_a] and yellow.x - VEL > 0:
        yellow.x -= VEL
    if keys_pressed[pygame.K_d] and yellow.x + VEL + yellow.width < BORDER.x:
        yellow.x += VEL
    if keys_pressed[pygame.K_w] and yellow.y - VEL > 0:
        yellow.y -= VEL
    if keys_pressed[pygame.K_s] and yellow.y + VEL + yellow.height < height - 15:
        yellow.y += VEL

def red_handle_movement(keys_pressed, red):
    if keys_pressed[pygame.K_LEFT] and red.x - VEL > BORDER.x + BORDER.width:
        red.x -= VEL
    if keys_pressed[pygame.K_RIGHT] and red.x + VEL + red.width < width:
        red.x += VEL
    if keys_pressed[pygame.K_UP] and red.y - VEL > 0:
        red.y -= VEL
    if keys_pressed[pygame.K_DOWN] and red.y + VEL + red.height < height - 15:
        red.y += VEL




