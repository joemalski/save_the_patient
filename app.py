# Filename: app.py
# Description: main module for the game.
# Date: April 23, 2020

import pygame, sys

from core.screen import Screen
from core.player import Player

# pygame initialization
pygame.init()

# main screen initialization
main_screen = Screen(pygame)
main_screen.set_size((800, 600))
main_screen.set_icon_path('assets/images/sprites/coronavirus_32.png')
main_screen.set_caption('Save the Patient! A Covid-19 Game...')


# player screen initialization
# initial position of player, bottom center
player = Player(pygame, Screen.object)
player.set_x(336)
player.set_y(472)
player.set_image_path('assets/images/sprites/doctor_128.png')

# game loop
game_loop_flag = True
player_x_change = 0

while game_loop_flag:
    # set screen background
    main_screen.set_background_color((192, 192, 192))
    main_screen.set_background_image('assets/images/background/play.jpg',
        (0, 0))

    # draw player
    player.draw()

    # check events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_loop_flag = False  

        # check keystrokes
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                player_x_change = -10
            if event.key == pygame.K_RIGHT:
                player_x_change = 10

        if event.type == pygame.KEYUP:
            if (event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT):
                player_x_change = 0

    player.set_x(player.get_x() + player_x_change)
    player.draw()

    # updates the screen on every iteration of the game loop
    pygame.display.update()

# quits pygame
pygame.quit()
print('\nThanks for playing... Stay Home, Stay Safe!\n')
sys.exit()
