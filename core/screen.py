# Filename: screen.py
# Description: Screen Class
# Date: April 24, 2020

class Screen:

    # Screen Object, an object from pygame.display.set_mode()
    object = None

    def __init__(self, pygame):
        self.pygame = pygame
        self.size = None
        self.caption = None
        self.icon_path = None
        self.background_color = None
        self.background_image_path = None
        self.background_point = None

    def show_details(self):
        print('\nScreen Details')
        print('--------------')
        print('size:', self.size)
        print('caption:', self.caption)
        print('icon path:', self.icon_path)
        print('background color:', self.background_color)
        print('background image path:', self.background_image_path)
        print('background image point(x,y):', self.background_point)

    def set_size(self, size):
        self.size = size
        Screen.object = self.pygame.display.set_mode(self.size)

    def get_size(self):
        return self.size

    def set_caption(self, caption):
        self.caption = caption
        self.pygame.display.set_caption(self.caption)

    def get_caption(self):
        return self.caption

    def set_icon_path(self, icon_path):
        self.icon_path = icon_path
        icon = self.pygame.image.load(self.icon_path)
        self.pygame.display.set_icon(icon)

    def get_icon_path(self):
        return self.icon_path

    def set_background_color(self, background_color):
        self.background_color = background_color
        Screen.object.fill(self.background_color)

    def get_background_color(self):
        return self.background_color

    def set_background_image(self, background_path, background_point):
        self.background_image_path = background_path
        self.background_point = background_point
        background = self.pygame.image.load(self.background_image_path)
        Screen.object.blit(background, self.background_point)