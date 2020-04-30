# Filename: app.py
# Description: main module for the game.
# Date: April 23, 2020

import pygame as py
import sys, math, random

from pygame import mixer
from core.screen import Screen
from core.sprite import Sprite

# pygame initialization
py.init()

# main screen initialization
app_main_screen = Screen(py)
app_main_screen.set_size((800, 600))
app_main_screen.set_icon_path('assets/images/sprites/coronavirus_32.png')
app_main_screen.set_caption('Save the Patient! A Covid-19 Game...')


# app_player screen initialization
# initial position of app_player, bottom center
app_player = Sprite(py, Screen.object)
app_player.set_x(336)
app_player.set_y(472)
app_player.set_image_path('assets/images/sprites/doctor_128.png')

# app variables
app_wave = 25
app_viruses = []
app_fired_vaccines = []

# randomize x starting position
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

# randomize y starting position
def random_y_start():
    if app_wave == 1:
        result = 1
    elif app_wave > 1 and app_wave <= 4:
        result = random.randint(1, 3)
    elif app_wave > 4 and app_wave <= 10:
        result = random.randint(1, 3)
    elif app_wave > 10:
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

# randomize sprite's speed
def random_speed():

    if app_wave <= 2:
        return 0.5

    if app_wave > 2 and app_wave <= 5:
        result = random.randint(1, 2)
        if result == 1:
            return 0.5
        else:
            return 1

    if app_wave > 5 and app_wave <= 10:
        result = random.randint(1, 3)
        if result == 1:
            return 1
        elif result == 2:
            return 1.5
        else:
            return 2

    if app_wave > 10:
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

# create viruses for the waves
def create_viruses(waves):
    viruses_created = []
    while waves >= 1:
        virus = Sprite(py, Screen.object)
        virus.set_x(random_x_start())
        virus.set_y(random_y_start())
        virus.set_speed(random_speed())
        virus.set_image_path('assets/images/sprites/virus_64.png')

        # check for any duplicates, change sprite imaged to virus mutated
        for i in range(len(viruses_created)):
            if (virus.get_x() == viruses_created[i].get_x() and
                virus.get_y() == viruses_created[i].get_y()):

                mutation = random.randint(1, 3)
                if mutation == 1:
                    virus.set_image_path(
                        'assets/images/sprites/mutated_64.png')
                    viruses_created[i].set_image_path('assets/images/sprites/mutated_64.png')
                elif mutation == 2:
                    virus.set_image_path(
                        'assets/images/sprites/mutated_64.png')
                    viruses_created[i].set_image_path('assets/images/sprites/mutated_64.png')
                else:
                    virus.set_image_path(
                        'assets/images/sprites/mers_64.png')
                    viruses_created[i].set_image_path('assets/images/sprites/mers_64.png')

                # 
                randomize_speed = random.randint(1,2)
                if randomize_speed == 1:
                    virus.set_speed(1)
                    viruses_created[i].set_speed(1)
                elif randomize_speed == 2:
                    virus.set_speed(2)
                    viruses_created[i].set_speed(2)

        viruses_created.append(virus)
        waves -= 1

    return viruses_created

# check if vaccine hits a virus
def is_collision(enemy_x, enemy_y, bullet_x, bullet_y):
    distance = math.sqrt(math.pow(enemy_x-bullet_x, 2) + math.pow(enemy_y-bullet_y, 2))
    if distance < 64:
        decapitation_sound = mixer.Sound('assets/sounds/decapitation.wav')
        decapitation_sound.play()
        return True
    else:
        return False

# create vaccines that are fired
def create_fired_vaccines(x, y):
        vaccine = Sprite(py, Screen.object)
        vaccine.set_x(x)
        vaccine.set_y(y)
        vaccine.set_speed(8)
        vaccine.set_image_path('assets/images/sprites/vaccine_64.png')

        laser_sound = mixer.Sound('assets/sounds/laser.wav')
        laser_sound.play()

        return vaccine

# menu header for the game window
def set_menu_header(ammo_value, virus_killed, app_wave):
    # add
    font = py.font.Font('freesansbold.ttf', 16)
    wave_text = font.render('Wave ' + str(app_wave),
        True, (0, 255, 0))
    Screen.object.blit(wave_text, (380, 5))

    # ammo image
    ammo_image = Sprite(py, Screen.object)
    ammo_image.set_x(5)
    ammo_image.set_y(5)
    ammo_image.set_image_path('assets/images/sprites/vaccine_16.png')
    ammo_image.draw()

    # ammo value    
    ammo_text = font.render('(Fired) x ' + str(ammo_value),
        True, (0, 255, 0))
    Screen.object.blit(ammo_text, (25, 5))

    # virus image
    virus_image = Sprite(py, Screen.object)
    virus_image.set_x(5)
    virus_image.set_y(30)
    virus_image.set_image_path('assets/images/sprites/virus_16.png')
    virus_image.draw()

    # virus killed
    virus_text = font.render('(Killed) x ' + str(virus_killed),
        True, (0, 255, 0))
    Screen.object.blit(virus_text, (25, 30))

# quit the game
def game_quit():
    # quits pygame
    py.quit()
    print('\nThanks for playing... Stay Home, Stay Safe!\n')
    sys.exit()

# show's the wave page screen
def show_wave_page_screen():

    # background sound
    mixer.music.stop() # stop previous music
    mixer.music.load('assets/sounds/background_1.wav')
    mixer.music.play() # -1, makes it infinite loop

    wave_page_flag = True
    font_1 = py.font.Font('freesansbold.ttf', 32)
    wave_text = font_1.render('Wave ' + str(app_wave), True, (255, 0, 0))
    Screen.object.blit(wave_text, (350, 250))

    
    font_2 = py.font.Font('freesansbold.ttf', 16)

    instruction_1_text = font_2.render('[SPACEBAR] - fire', True, (255, 0, 0))
    Screen.object.blit(instruction_1_text, (325, 330))

    instruction_2_text = font_2.render('[ARROW LEFT] - move left',
        True, (255, 0, 0))
    Screen.object.blit(instruction_2_text, (325, 350))

    instruction_3_text = font_2.render('[ARROW RIGHT] - move right',
        True, (255, 0, 0))
    Screen.object.blit(instruction_3_text, (325, 370))
  
    instruction_4_text = font_2.render(
        'Kill all SARS-COVID-2 viruses !!!',
        True, (255, 0, 0))
    Screen.object.blit(instruction_4_text, (325, 400))
    

    # updates the screen on every iteration of the game loop
    py.display.update()

    while wave_page_flag:
        # check events
        for event in py.event.get():
            if event.type == py.QUIT:
                wave_page_flag = False
                game_quit()

            # check keystrokes
            if event.type == py.KEYDOWN:
                wave_page_flag = False

# main game loop
def game_loop():

    # background sound
    mixer.music.stop() # stop previous music
    mixer.music.load('assets/sounds/background_2.wav')
    mixer.music.play(-1) # -1, makes it infinite loop

    # set_repeat(), for smoother keypress responses
    py.key.set_repeat(10,10)

    game_loop_flag = True
    player_x_change = 0
    app_viruses = create_viruses(app_wave)
    score = 0
    fired = 0
    while game_loop_flag:
        # set screen background
        app_main_screen.set_background_color((192, 192, 192))
        app_main_screen.set_background_image(
            'assets/images/background/background_2.jpg',
            (0, 0))

        # set header
        set_menu_header(fired, score, app_wave)

        # check events
        for event in py.event.get():
            if event.type == py.QUIT:
                game_loop_flag = False  

            # check keystrokes
            if event.type == py.KEYDOWN:
                if event.key == py.K_LEFT:
                    player_x_change = -20
                if event.key == py.K_RIGHT:
                    player_x_change = 20
                if event.key == py.K_SPACE:
                    py.key.set_repeat(0)
                    fired += 1
                    app_fired_vaccines.append(create_fired_vaccines(
                        app_player.get_x()+32, app_player.get_y()+64))

            if event.type == py.KEYUP:
                if (event.key == py.K_LEFT or event.key == py.K_RIGHT):
                    player_x_change = 0

        app_player.set_x(app_player.get_x() + player_x_change)

        # check app_player left and right boundaries
        # x: 800, sprite: 128x128
        # left boundary: 0
        # right boundary: 672 (800-128)
        if app_player.get_x() <= -20:
            app_player.set_x(-20)
        elif app_player.get_x() >= 692:
            app_player.set_x(692)

        app_player.draw()

        # app_viruses movement       
        for i, virus in enumerate(app_viruses):
            ''' For Testing Purposes:
            print('app_viruses[{}] y: {}'.format(i, virus.get_y()))
            print('app_viruses[{}] is rendered:{}'.format(i,
                virus.get_rendered()))
            '''

            virus.draw()
            if virus.get_rendered() == True:
                virus.set_y(virus.get_y() + virus.get_speed())

            # check if virus sprite is out of the screen 
            if virus.get_y() > 600:
                virus.set_rendered(False)
                app_viruses.pop(i) # remove list element

        # fire vaccine movement
        for i, fired_vaccine in enumerate(app_fired_vaccines):
            ''' For Testing Purposes:
            print('app_fired_vaccines[{}] y: {}'.format(i,
                fired_vaccine.get_y()))
            print('app_fired_vaccines[{}] is rendered:{}'.format(i,
                fired_vaccine.get_rendered()))
            '''

            fired_vaccine.draw()
            if fired_vaccine.get_rendered() == True:
                fired_vaccine.set_y(fired_vaccine.get_y() - 
                    fired_vaccine.get_speed())

            # check if fired vaccine sprite is out of the screen 
            if fired_vaccine.get_y() < -64:
                fired_vaccine.set_rendered(False)
                app_fired_vaccines.pop(i) # remove list element

        # collision detection
        for i, virus in enumerate(app_viruses):
            for j, fired_vaccine in enumerate(app_fired_vaccines):
                collision = is_collision(virus.get_x(),
                                virus.get_y(),
                                fired_vaccine.get_x(),
                                fired_vaccine.get_y())
                if collision:
                    virus.set_rendered(False)
                    virus.set_y(-64)
                    app_viruses.pop(i) # remove virus list element
                    fired_vaccine.set_rendered(False)
                    fired_vaccine.set_y(-64)
                    app_fired_vaccines.pop(j) # remove fired_vaccine list element
                    score += 1

                    # for testing
                    #print('SARS-COVID-2 Virus has been hit !!!')


        # updates the screen on every iteration of the game loop
        py.display.update()

    game_quit()



# ------------------------
# Program Execution Point
# -------------------------

# show wave text
show_wave_page_screen()

# run game loop
game_loop()



