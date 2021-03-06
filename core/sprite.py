# Filename: sprite.py
# Description: Sprite Class, creates sprites
# Date: April 24, 2020

class Sprite:

    # Screen Object, an object from py.display.set_mode()
    object = None

    def __init__(self, py, screen_object):
        Sprite.object = screen_object
        self.py = py
        self.x = None
        self.y = None
        self.image_path = None
        self.rendered = True

    # show sprite's object values
    def show_details(self):
        print('\nSprite Details')
        print('--------------')
        print('x:', self.x)
        print('y:', self.y)
        print('speed:', self.speed)
        print('image path:', self.image_path)
        print('rendered:', self.rendered)

    # set x coordinate, where "x" is an int
    # "x" is the "row"
    def set_x(self, x):
        self.x = x

    def get_x(self):
        return self.x

    # set y coordinate, where "y" is an int
    # "y" is the "column"
    def set_y(self, y):
        self.y = y

    def get_y(self):
        return self.y

    # set sprite speed (optional)
    # "speed" is int
    def set_speed(self, speed):
        self.speed = speed

    def get_speed(self):
        return self.speed

    # set image path, where "image_path" is a str
    def set_image_path(self, image_path):
        self.image_path = image_path

    def get_image_path(self):
        return self.image_path

    # set rendered to True or False values
    def set_rendered(self, value):
        self.rendered = value

    def get_rendered(self):
        return self.rendered

    # draw sprite image on screen
    # self.image, self.x and self.y should be set or initialized first
    # it automatically sets the "self.rendered" to true
    def draw(self):
        image = self.py.image.load(self.image_path)
        Sprite.object.blit(image, (self.x, self.y))