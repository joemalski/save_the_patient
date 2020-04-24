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
main_screen.set_background_color((192, 192, 192))
main_screen.set_background_image('assets/images/background/play.jpg', (0, 0))
main_screen.show_details()

# player screen initialization
player = Player(pygame, Screen.object)
player.set_x(100)
player.set_y(250)
player.set_image_path('assets/images/sprites/doctor_64.png')
player.draw()
player.show_details()

# game loop
game_loop_flag = True

while game_loop_flag:
    # check events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_loop_flag = False

    # updates the screen on every iteration of the game loop
    pygame.display.update()

# quits pygame
pygame.quit()
print('\nThanks for playing... Stay Home, Stay Safe!\n')
sys.exit()
