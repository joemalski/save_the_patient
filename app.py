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
wave = 5
viruses = []
fired_vaccines = []

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
    if wave == 1:
        result = 1
    elif wave > 1 and wave <= 4:
        result = random.randint(1, 3)
    elif wave > 4 and wave <= 10:
        result = random.randint(1, 3)
    elif wave > 10:
        result = random.randint(1, 4)

    # result values
    if result == 1:
        return -62

    elif result == 2:
        return -126

    elif result == 3:
        return -190

    elif result == 4:
        return -254

def random_speed():

    if wave <= 2:
        return 0.5

    if wave > 2 and wave <= 5:
        result = random.randint(1, 2)
        if result == 1:
            return 0.5
        else:
            return 1

    if wave > 5 and wave <= 10:
        result = random.randint(1, 3)
        if result == 1:
            return 1
        elif result == 2:
            return 1.5
        else:
            return 2

    if wave > 10:
        result = random.randint(1, 5)
        if result == 1:
            return 0.5
        elif result == 2:
            return 1
        elif result == 3:
            return 1.5
        elif result == 4:
            return 2
        elif result == 5:
            return 2.5

def create_viruses(waves):
    viruses_created = []
    while waves >= 1:
        virus = Sprite(pygame, Screen.object)
        virus.set_x(random_x_start())
        virus.set_y(random_y_start())
        virus.set_speed(random_speed())
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

def create_fired_vaccines(x, y):
        vaccine = Sprite(pygame, Screen.object)
        vaccine.set_x(x)
        vaccine.set_y(y)
        vaccine.set_speed(8)
        vaccine.set_image_path('assets/images/sprites/vaccine_64.png')
        return vaccine

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
        set_menu_header(wave + 5, 0, wave)

        # check events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_loop_flag = False  

            # check keystrokes
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    player_x_change = -20
                if event.key == pygame.K_RIGHT:
                    player_x_change = 20
                if event.key == pygame.K_SPACE:
                    pygame.key.set_repeat(0)
                    fired_vaccines.append(create_fired_vaccines(
                        player.get_x()+32, player.get_y()+64))

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

        # viruses movement       
        for i in range(len(viruses)):
            ''' For Testing Purposes:
            print('viruses[{}] y: {}'.format(i, viruses[i].get_y()))
            print('viruses[{}] is rendered:{}'.format(i,
                viruses[i].get_rendered()))
            '''

            viruses[i].draw()
            if viruses[i].get_rendered() == True:
                viruses[i].set_y(viruses[i].get_y() + viruses[i].get_speed())

            # check if virus sprite is out of bounds or is already
            # destroyed by vaccine            
            if viruses[i].get_y() > 600:
                viruses[i].set_rendered(False)

        # fire vaccine movement
        fired_vaccines_counter = len(fired_vaccines)
        for i in range(fired_vaccines_counter):
            ''' For Testing Purposes:
            print('fired_vaccines[{}] y: {}'.format(i,
                fired_vaccines[i].get_y()))
            print('fired_vaccines[{}] is rendered:{}'.format(i,
                fired_vaccines[i].get_rendered()))
            '''

            fired_vaccines[i].draw()
            if fired_vaccines[i].get_rendered() == True:
                fired_vaccines[i].set_y(fired_vaccines[i].get_y() - 
                    fired_vaccines[i].get_speed())

            # check if vaccine sprite is out of bounds or has already
            # destroyed a virus
            if fired_vaccines[i].get_y() < -64:
                fired_vaccines[i].set_rendered(False)

        # collision detection
        for i in range(len(viruses)):
            for j in range(len(fired_vaccines)):
                collision = is_collision(viruses[i].get_x(),
                                viruses[i].get_y(),
                                fired_vaccines[j].get_x(),
                                fired_vaccines[j].get_y())
                if collision:
                    viruses[i].rendered = False
                    viruses[i].set_y(-64)
                    fired_vaccines[j].rendered = False
                    fired_vaccines[j].set_y(-64)
                    print('Hit Virus Bitch!!! viruses[{}]'.format(i))


        # updates the screen on every iteration of the game loop
        pygame.display.update()

    game_quit()



# ------------------------
# Program Execution Point
# -------------------------
# show wave text
show_wave_page_screen()

# run game loop
game_loop()



