# Filename: player.py
# Description: Player Class "player sprite"
# Date: April 24, 2020

class Player:

    # Screen Object, an object from pygame.display.set_mode()
    object = None

    def __init__(self, pygame, screen_object):
        Player.object = screen_object
        self.pygame = pygame
        self.x = None
        self.y = None
        self.image_path = None
        self.rendered = False

    # show player's object values
    def show_details(self):
        print('\nPlayer Details')
        print('--------------')
        print('x:', self.x)
        print('y:', self.y)
        print('image path:', self.image_path)
        print('rendered:', self.rendered)

    # set x coordinate, where "x" is an int
    def set_x(self, x):
        self.x = x

    def get_x(self):
        return self.x

    # set y coordinate, where "y" is an int
    def set_y(self, y):
        self.y = y

    def get_y(self):
        return self.y

    # set image path, where "image_path" is a str
    def set_image_path(self, image_path):
        self.image_path = image_path

    def get_image_path(self):
        return self.image_path

    # returns status of the sprite if rendered or not
    # returns True or False
    def is_rendered(self):
        if self.rendered:
            return True
        else:
            return False

    # draw player image on screen
    # image, x and y should be initialize first
    # it automatically sets the "self.rendered" to true
    def draw(self):
        image = self.pygame.image.load(self.image_path)
        Player.object.blit(image, (self.x, self.y))
        self.rendered = True