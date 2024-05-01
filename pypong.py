# Wrtite a simple pong game using pygame

import pygame
import sys

# General setup
pygame.init()
clock = pygame.time.Clock()

# Setting up the main window
screen_width = 1280
screen_height = 960
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('PyPong')

# Game while loop
while True:
    # Handle input
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quite()
            pygame.exit()
    
    # Update window
    pygame.display.flip()
    clock.tick(60)