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
app_main_screen.set_caption('Save the Patient! A COVID-19 Game...')


# app_player screen initialization
# initial position of app_player, bottom center
app_player = Sprite(py, Screen.object)
app_player.set_x(336)
app_player.set_y(472)
app_player.set_image_path('assets/images/sprites/doctor_128.png')

# app variables
app_wave = 1
app_main_loop_flag = True # This is global !

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
def random_y_start(wave):
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

# randomize sprite's speed
def random_speed(wave):

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

    if wave > 10 and wave <= 20:
        result = random.randint(1, 5)
        if result == 1:
            return 1
        elif result == 2:
            return 1.5
        elif result == 3:
            return 2
        elif result == 4:
            return 2.5
        else:
            return 3

    if wave > 20:
        result = random.randint(1, 7)
        if result == 1:
            return 1.5
        elif result == 2:
            return 2
        elif result == 3:
            return 2.5
        elif result == 4:
            return 3
        elif result == 5:
            return 3.5
        elif result == 6:
            return 4
        else:
            return 4.5

# create viruses for the waves
def create_viruses(waves):
    viruses_created = []
    while waves >= 1:
        virus = Sprite(py, Screen.object)
        virus.set_x(random_x_start())
        virus.set_y(random_y_start(waves))
        virus.set_speed(random_speed(waves))
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

                # randomize speed                
                randomize_speed = random.randint(1,2)
                if waves < 20:
                    if randomize_speed == 1:
                        virus.set_speed(1)
                        viruses_created[i].set_speed(1)
                    elif randomize_speed == 2:
                        virus.set_speed(2)
                        viruses_created[i].set_speed(2)
                elif waves > 20 and waves <= 30:
                    if randomize_speed == 1:
                        virus.set_speed(2)
                        viruses_created[i].set_speed(2)
                    elif randomize_speed == 2:
                        virus.set_speed(3)
                        viruses_created[i].set_speed(3)
                elif waves > 30:
                    if randomize_speed == 1:
                        virus.set_speed(2)
                        viruses_created[i].set_speed(2)
                    elif randomize_speed == 2:
                        virus.set_speed(3)
                        viruses_created[i].set_speed(3)
                    else:
                        virus.set_speed(4)
                        viruses_created[i].set_speed(4)

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
    vaccine.set_speed(15)
    vaccine.set_image_path('assets/images/sprites/vaccine_64.png')

    laser_sound = mixer.Sound('assets/sounds/laser.wav')
    laser_sound.play()

    return vaccine

# menu header for the game window
def set_menu_header(ammo_value, virus_killed, wave):
    font = py.font.Font('freesansbold.ttf', 16)
    wave_text = font.render('COVID-19 Wave ' + str(wave),
        True, (0, 255, 0))
    Screen.object.blit(wave_text, (340, 5))

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

# show's the first page screen
def show_first_page_screen(main_screen):
    # set_repeat() stop key repeat
    py.key.set_repeat()
    py.event.clear()

    # background sound
    mixer.music.stop() # stop previous music
    mixer.music.load('assets/sounds/background_1.wav')
    mixer.music.play() # -1, makes it infinite loop


    main_screen.set_background_image(
            'assets/images/background/background_1.jpg',
            (0, 0))

    wave_page_flag = True
    font_1 = py.font.Font('freesansbold.ttf', 18)
    title_text = font_1.render('Save the Patient! A COVID-19 Game...', 
        True, (0, 255, 0))
    Screen.object.blit(title_text, (250, 220))

    
    font_2 = py.font.Font('freesansbold.ttf', 16)

    instruction_1_text = font_2.render('[SPACEBAR] - fire', True, (0, 255, 0))
    Screen.object.blit(instruction_1_text, (300, 270))

    instruction_2_text = font_2.render('[ARROW LEFT] - move left',
        True, (0, 255, 0))
    Screen.object.blit(instruction_2_text, (300, 290))

    instruction_3_text = font_2.render('[ARROW RIGHT] - move right',
        True, (0, 255, 0))
    Screen.object.blit(instruction_3_text, (300, 310))
  
    instruction_4_text = font_2.render(
        'Press Enter to continue',
        True, (0, 255, 0))
    Screen.object.blit(instruction_4_text, (300, 350))

    pygame_logo = py.image.load('assets/images/sprites/pygame_logo.png')
    Sprite.object.blit(pygame_logo, (280, 100))

    python_logo = py.image.load('assets/images/sprites/python.png')
    Sprite.object.blit(python_logo, (280, 420))    

    # updates the screen on every iteration of the game loop
    py.display.update()
    py.event.clear()

    while wave_page_flag:
        # check events
        for event in py.event.get():
            if event.type == py.QUIT:
                wave_page_flag = False
                game_quit()

            # check keystrokes
            if event.type == py.KEYDOWN:
                if event.key == py.K_RETURN:
                    wave_page_flag = False
                    py.event.clear()

                if event.key == py.K_ESCAPE:
                    wave_page_flag = False
                    game_quit()

# main game loop
def game_loop(main_screen, player, wave):

    # background sound
    mixer.music.stop() # stop previous music
    mixer.music.load('assets/sounds/break_in.wav')
    mixer.music.play(-1) # -1, makes it infinite loop

    # set_repeat(), for smoother keypress responses
    py.key.set_repeat(10, 10)

    game_loop_flag = True
    player_x_change = 0
    viruses = create_viruses(wave)
    fired_vaccines = []
    score = 0
    fired = 0

    while game_loop_flag:
        # set screen background
        main_screen.set_background_image(
            'assets/images/background/background_2.jpg',
            (0, 0))

        # set header
        set_menu_header(fired, score, wave)

        # check events
        for event in py.event.get():
            if event.type == py.QUIT:
                game_loop_flag = False
                py.event.clear()
                game_quit()

            # check keystrokes
            if event.type == py.KEYDOWN:
                if event.key == py.K_LEFT:
                    player_x_change = -20
                if event.key == py.K_RIGHT:
                    player_x_change = 20
                if event.key == py.K_SPACE:
                    # check if there is still a virus
                    # then allow to fire
                    if len(viruses) > 0:
                        py.key.set_repeat(0)                    
                        fired += 1
                        fired_vaccines.append(create_fired_vaccines(
                            player.get_x()+32, player.get_y()+64))
                        py.key.set_repeat(10,10)
                if event.key == py.K_ESCAPE:
                    game_loop_flag = False
                    py.event.clear()
                    result = False

            if event.type == py.KEYUP:
                if (event.key == py.K_LEFT or event.key == py.K_RIGHT):
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
        for i, virus in enumerate(viruses):
            ''' For Testing Purposes:
            print('viruses[{}] y: {}'.format(i, virus.get_y()))
            print('viruses[{}] is rendered:{}'.format(i,
                virus.get_rendered()))
            '''
            virus.draw()
            if virus.get_rendered() == True:
                virus.set_y(virus.get_y() + virus.get_speed())

            # check if virus entered the patient !!!
            if virus.get_y() > 600:
                virus.set_rendered(False)                
                viruses.clear()

        # fire vaccine movement
        for i, fired_vaccine in enumerate(fired_vaccines):
            ''' For Testing Purposes:
            print('fired_vaccines[{}] y: {}'.format(i,
                fired_vaccine.get_y()))
            print('fired_vaccines[{}] is rendered:{}'.format(i,
                fired_vaccine.get_rendered()))
            '''

            fired_vaccine.draw()
            if fired_vaccine.get_rendered() == True:
                fired_vaccine.set_y(fired_vaccine.get_y() - 
                    fired_vaccine.get_speed())

            # check if fired vaccine sprite is out of the screen 
            if fired_vaccine.get_y() < -64:
                fired_vaccine.set_rendered(False)
                fired_vaccines.pop(i) # remove list element

        # collision detection
        for i, virus in enumerate(viruses):
            for j, fired_vaccine in enumerate(fired_vaccines):
                collision = is_collision(virus.get_x(),
                                virus.get_y(),
                                fired_vaccine.get_x(),
                                fired_vaccine.get_y())
                if collision:
                    virus.set_rendered(False)
                    virus.set_y(-64)
                    viruses.pop(i) # remove virus element
                    fired_vaccine.set_rendered(False)
                    fired_vaccine.set_y(-64)
                    fired_vaccines.pop(j) # remove fired_vaccine element
                    score += 1

                    # for testing
                    #print('SARS-COVID-2 Virus has been hit !!!')

        # updates the screen on every iteration of the game loop
        py.display.update()

        # check if game is over
        if len(viruses) == 0:
            # delay 100ms for better effect
            py.time.delay(100)

            # change background
            main_screen.set_background_image(
                'assets/images/background/background_1.jpg',
                (0, 0))

            result = None
            font_1 = py.font.Font('freesansbold.ttf', 32)
            font_2 = py.font.Font('freesansbold.ttf', 16)
            if score < wave:

                # background sound
                mixer.music.stop() # stop previous music
                mixer.music.load('assets/sounds/astronomia.wav')
                mixer.music.play(-1) # -1, makes it infinite loop

                # coffin meme starz! super!
                coffin_meme_starz = py.image.load(
                    'assets/images/sprites/coffin_meme.png')
                Sprite.object.blit(coffin_meme_starz, (200, 95))    

                game_over_text = font_1.render(
                'Game Over (Wave '+str(wave)+')', True, (255, 0, 0))
                Screen.object.blit(game_over_text, (260, 220))

                message_text = font_2.render(
                'SARS-COVID-2 entered patient !', True, (255, 0, 0))
                Screen.object.blit(message_text, (285, 270))

                score_text = font_1.render(
                'Virus Killed: ' + str(score), True, (255, 0, 0))
                Screen.object.blit(score_text, (300, 300))
                result = False

                press_enter_text = font_2.render(
                'Press Enter to continue', True, (255, 0, 0))
                Screen.object.blit(press_enter_text, (325, 340))

            else:

                # background sound
                mixer.music.stop() # stop previous music
                mixer.music.load('assets/sounds/background_1.wav')
                mixer.music.play(-1) # -1, makes it infinite loop

                next_wave_text = font_1.render(
                'Next Virus Wave: ' + str(wave + 1), True, (0, 255, 0))
                Screen.object.blit(next_wave_text, (270, 250))

                score_text = font_1.render(
                'Virus Killed: ' + str(score), True, (0, 255, 0))
                Screen.object.blit(score_text, (300, 290))
                result = True

                press_enter_text = font_2.render(
                'Press Enter to continue', True, (0, 255, 0))
                Screen.object.blit(press_enter_text, (325, 340))

            py.display.update()

            while True:
                # check events
                for event in py.event.get():
                    if event.type == py.QUIT:
                        game_loop_flag = False
                        game_quit()

                    # check keystrokes
                    if event.type == py.KEYDOWN:
                        if event.key == py.K_RETURN:
                            game_loop_flag = False
                            return result
                        if event.key == py.K_ESCAPE:
                            py.event.clear()
                            game_loop_flag = False
                            return False
          
# quit the game
def game_quit():
    global app_main_loop_flag

    # quits pygame
    app_main_loop_flag = False
    py.quit()
    print('\nThanks for playing... Stay Home, Stay Safe!\n')
    print('Game Version: 0.1')
    print('Developed by: Joel F. Malinao')
    print('https://github.com/joemalski/save_the_patient\n')
    sys.exit()


# ------------------------
# Program Execution Point
# -------------------------

while app_main_loop_flag:

    # show wave text
    if app_wave == 1:
        show_first_page_screen(app_main_screen)

    # run game loop
    result = game_loop(app_main_screen, app_player, app_wave)

    if result:
        app_wave += 1
    else:
        app_wave = 1


