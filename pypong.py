# Wrtite a simple pong game using pygame

import pygame
import sys
import random

# adding in random commit to try out git

# Constaints
HALF = 2

def ball_animation():
    global ball_speed_x, ball_speed_y

    # Ball motion
    ball.x += ball_speed_x
    ball.y += ball_speed_y

    # Tells the ball to switch directions when it hits the max window screen
    if ball.top <= 0 or ball.bottom >= screen_height:
        ball_speed_y *= -1
    if ball.left <= 0 or ball.right >= screen_width:
        ball_restart()
    
    # This stops the ball on the paddel instead of the window 
    if ball.colliderect(player) or ball.colliderect(opponent):
        ball_speed_x *= -1

def player_animation():
    player.y += player_speed
    if player.top <= 0:
        player.top = 0
    if player.bottom >= screen_height:
        player.bottom = screen_height

def oppnent_ai():
    if opponent.top < ball.y:
        opponent.top += opponent_speed
    if opponent.bottom > ball.y:
        opponent.bottom -= opponent_speed
    if player.top <= 0:
        player.top = 0
    if player.bottom >= screen_height:
        player.bottom = screen_height

def ball_restart():
    global ball_speed_y, ball_speed_x
    ball.center = (screen_width/2, screen_height/2)
    ball_speed_y = random_polarity(7)
    ball_speed_x = random_polarity(7)

def random_polarity(input_number):
    randomized_polarity = random.choice((1,-1))
    return input_number * randomized_polarity

# General setup
pygame.init()
clock = pygame.time.Clock()

# Setting up the main window
screen_width = 1280
screen_height = 960
screen_vertical_center = screen_width / HALF
screen_horizaontal_center = screen_height / HALF
background_color = pygame.Color('steelblue')
light_grey = (200,200,200)
yellow = (255,255,102)
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('PyPong')

# Create Game objects
# Create a ball placed at center
ball_size = 30
ball_center = ball_size / HALF
ball = pygame.Rect(screen_vertical_center - ball_center, screen_horizaontal_center - ball_center, ball_size, ball_size)

# Create Paddels for the players and place at center
paddel_padding = 20
paddel_width = 10
paddel_length = 140
paddel_horizaonal_center = paddel_length / HALF
player = pygame.Rect(screen_width - 20, screen_height / 2 - 70, 10, 140)
opponent = pygame.Rect(10, screen_height/2 -70, 10, 140)

# Ball speed
ball_speed_x = random_polarity(7)
ball_speed_y = random_polarity(7)

#Player and oppent speeds
player_speed = 0
opponent_speed = 5

# Game while loop
while True:
    # Handle input
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_DOWN:
                player_speed += 7
            if event.key == pygame.K_UP:
                player_speed -= 7
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_DOWN:
                player_speed -= 7
            if event.key == pygame.K_UP:
                player_speed += 7
    
    ball_animation()
    player_animation()
    oppnent_ai()

    # Moving Visuals
    screen.fill(background_color)
    pygame.draw.aaline(screen, light_grey, (screen_vertical_center, 0), (screen_vertical_center, screen_height))
    pygame.draw.rect(screen, light_grey, player)
    pygame.draw.rect(screen, light_grey, opponent)
    pygame.draw.ellipse(screen, yellow, ball)
    
    # Update window
    pygame.display.flip()
    clock.tick(60)