# Filename: app.py
# Description: main module for the game.
# Date: April 23, 2020

import pygame, sys

from core.screen import Screen
from core.sprite import Sprite

# pygame initialization
pygame.init()

# main screen initialization
main_screen = Screen(pygame)
main_screen.set_size((800, 600))
main_screen.set_icon_path('assets/images/sprites/coronavirus_32.png')
main_screen.set_caption('Save the Patient! A Covid-19 Game...')


# player screen initialization
# initial position of player, bottom center
player = Sprite(pygame, Screen.object)
player.set_x(336)
player.set_y(472)
player.set_image_path('assets/images/sprites/doctor_128.png')

# wave counter
wave = 1

def set_menu_header(ammo_value, virus_killed):
    # ammo image
    ammo_image = Sprite(pygame, Screen.object)
    ammo_image.set_x(5)
    ammo_image.set_y(5)
    ammo_image.set_image_path('assets/images/sprites/vaccine_16.png')
    ammo_image.draw()

    # ammo value
    font = pygame.font.Font('freesansbold.ttf', 16)
    ammo_text = font.render('(left) x ' + str(ammo_value),
        True, (0, 255, 0))
    Screen.object.blit(ammo_text, (25, 5))

    # virus image
    virus_image = Sprite(pygame, Screen.object)
    virus_image.set_x(5)
    virus_image.set_y(30)
    virus_image.set_image_path('assets/images/sprites/virus_16.png')
    virus_image.draw()

    # virus killed
    font = pygame.font.Font('freesansbold.ttf', 16)
    virus_text = font.render('(killed) x ' + str(virus_killed),
        True, (0, 255, 0))
    Screen.object.blit(virus_text, (25, 30))

# quit the game
def game_quit():
    # quits pygame
    pygame.quit()
    print('\nThanks for playing... Stay Home, Stay Safe!\n')
    sys.exit()

# show's the wave page screen
def show_wave_page_screen():
    flag = True
    font = pygame.font.Font('freesansbold.ttf', 32)
    wave_text = font.render('Wave ' + str(wave), True, (255, 0, 0))
    Screen.object.blit(wave_text, (350, 250))

    # updates the screen on every iteration of the game loop
    pygame.display.update()

    while flag:
        # check events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                flag = False
                game_quit()

            # check keystrokes
            if event.type == pygame.KEYDOWN:
                flag = False

# game loop
def game_loop():
    # set_repeat(), for smoother keypress responses
    pygame.key.set_repeat(10,10)

    game_loop_flag = True
    player_x_change = 0

    while game_loop_flag:
        # set screen background
        main_screen.set_background_color((192, 192, 192))
        main_screen.set_background_image(
            'assets/images/background/background_2.jpg',
            (0, 0))

        # set header
        set_menu_header(10, 0)

        # draw player
        player.draw()

        # check events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_loop_flag = False  

            # check keystrokes
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    player_x_change = -15
                if event.key == pygame.K_RIGHT:
                    player_x_change = 15

            if event.type == pygame.KEYUP:
                if (event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT):
                    player_x_change = 0

        player.set_x(player.get_x() + player_x_change)

        # check player left and right boundaries
        # x: 800, sprite: 128x128
        # left boundary: 0
        # right boundary: 672 (800-128)
        if player.get_x() <= 0:
            player.set_x(0)
        elif player.get_x() >= 672:
            player.set_x(672)

        player.draw()

        # updates the screen on every iteration of the game loop
        pygame.display.update()

    game_quit()


# show wave text
show_wave_page_screen()

# run game loop
game_loop()



