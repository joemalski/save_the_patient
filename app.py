# Filename: app.py
# Description: main module for the game.
# Date: April 23, 2020

import pygame

# initialize pygame module
pygame.init()

# title and icon
pygame.display.set_caption('Save the Patient!')
icon = pygame.image.load('assets/images/sprites/coronavirus_32.png')
pygame.display.set_icon(icon)

# background
background = pygame.image.load('assets/images/background/play.jpg')

# create the screen
screen = pygame.display.set_mode((800, 600))

# game loop
game_loop_flag = True

while game_loop_flag:
    # set screen background color
    screen.fill((0, 0, 0))
    
    # background image
    screen.blit(background, (0, 0))

    # check events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_loop_flag = False

    # updates the screen on every iteration of the game loop
    pygame.display.update()
