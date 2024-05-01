# Wrtite a simple pong game using pygame

import pygame
import sys

# Constaints
HALF = 2

# General setup
pygame.init()
clock = pygame.time.Clock()

# Setting up the main window
screen_width = 1280
screen_height = 960
screen_vertical_center = screen_width / HALF
screen_horizaontal_center = screen_height / HALF
background_color = pygame.Color('grey12')
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

# Game while loop
while True:
    # Handle input
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quite()
            pygame.exit()

    # Moving Visuals
    screen.fill(background_color)
    pygame.draw.aaline(screen, light_grey, (screen_vertical_center, 0), (screen_vertical_center, screen_height))
    pygame.draw.rect(screen, light_grey, player)
    pygame.draw.rect(screen, light_grey, opponent)
    pygame.draw.ellipse(screen, yellow, ball)
    
    # Update window
    pygame.display.flip()
    clock.tick(60)