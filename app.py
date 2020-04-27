# Filename: app.py
# Description: main module for the game.
# Date: April 23, 2020

import pygame, sys, math, random

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
wave = 25
viruses = []

def random_x_start():
    result = random.randint(1, 12)

    if result == 1:
        return 16
    elif result == 2:
        return 80
    elif result == 3:
        return 144
    elif result == 4:
        return 208
    elif result == 5:
        return 272
    elif result == 6:
        return 336
    elif result == 7:
        return 400
    elif result == 8:
        return 464
    elif result == 9:
        return 528
    elif result == 10:
        return 592
    elif result == 11:
        return 656
    elif result == 12:
        return 720

def random_y_start():
    result = random.randint(1, 8)

    if result == 1:
        return -62
    elif result == 2:
        return -126
    elif result == 3:
        return -190
    elif result == 4:
        return -254
    elif result == 5:
        return -318
    elif result == 6:
        return -382
    elif result == 7:
        return -446
    elif result == 8:
        return -510

def create_viruses(waves):
    viruses_created = []
    while waves >= 1:
        virus = Sprite(pygame, Screen.object)
        virus.set_x(random_x_start())
        virus.set_y(random_y_start())
        virus.set_image_path('assets/images/sprites/virus_64.png')
        viruses_created.append(virus)
        waves -= 1

    return viruses_created


def is_collision(enemy_x, enemy_y, bullet_x, bullet_y):
    distance = math.sqrt(math.pow(enemy_x-bullet_x, 2) + math.pow(enemy_y-bullet_y, 2))
    if distance < 27:
        return True
    else:
        return False

def set_menu_header(ammo_value, virus_killed, wave):
    # add
    font = pygame.font.Font('freesansbold.ttf', 16)
    wave_text = font.render('Wave ' + str(wave),
        True, (0, 255, 0))
    Screen.object.blit(wave_text, (380, 5))

    # ammo image
    ammo_image = Sprite(pygame, Screen.object)
    ammo_image.set_x(5)
    ammo_image.set_y(5)
    ammo_image.set_image_path('assets/images/sprites/vaccine_16.png')
    ammo_image.draw()

    # ammo value    
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
    wave_page_flag = True
    font = pygame.font.Font('freesansbold.ttf', 32)
    wave_text = font.render('Wave ' + str(wave), True, (255, 0, 0))
    Screen.object.blit(wave_text, (350, 250))

    # updates the screen on every iteration of the game loop
    pygame.display.update()

    while wave_page_flag:
        # check events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                wave_page_flag = False
                game_quit()

            # check keystrokes
            if event.type == pygame.KEYDOWN:
                wave_page_flag = False

# game loop
def game_loop():

    # set_repeat(), for smoother keypress responses
    pygame.key.set_repeat(10,10)

    game_loop_flag = True
    player_x_change = 0
    viruses = create_viruses(wave)

    while game_loop_flag:
        # set screen background
        main_screen.set_background_color((192, 192, 192))
        main_screen.set_background_image(
            'assets/images/background/background_2.jpg',
            (0, 0))

        # set header
        set_menu_header(10, 0, 1)

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
        if player.get_x() <= -20:
            player.set_x(-20)
        elif player.get_x() >= 692:
            player.set_x(692)

        player.draw()

        for i in range(wave):
            viruses[i].draw()
            viruses[i].set_y(viruses[i].get_y() + 1)

         # updates the screen on every iteration of the game loop
        pygame.display.update()

    game_quit()

# show wave text
show_wave_page_screen()

# run game loop
game_loop()



