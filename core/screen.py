# Filename: screen.py
# Description: Screen Class
# Date: April 24, 2020

class Screen:

    # Screen Object, an object from py.display.set_mode()
    object = None

    def __init__(self, py):
        self.py = py
        self.size = None
        self.caption = None
        self.icon_path = None
        self.background_color = None
        self.background_image_path = None
        self.background_point = None

    # show screen's object values
    def show_details(self):
        print('\nScreen Details')
        print('--------------')
        print('size:', self.size)
        print('caption:', self.caption)
        print('icon path:', self.icon_path)
        print('background color:', self.background_color)
        print('background image path:', self.background_image_path)
        print('background image point(x,y):', self.background_point)

    # sets screen size where "size" is a tuple
    def set_size(self, size):
        self.size = size
        Screen.object = self.py.display.set_mode(self.size)

    def get_size(self):
        return self.size

    # sets screen caption where "caption" is a str
    def set_caption(self, caption):
        self.caption = caption
        self.py.display.set_caption(self.caption)

    def get_caption(self):
        return self.caption

    # sets screen icon, where "icon_path" is a str
    def set_icon_path(self, icon_path):
        self.icon_path = icon_path
        icon = self.py.image.load(self.icon_path)
        self.py.display.set_icon(icon)

    def get_icon_path(self):
        return self.icon_path

    # sets screen background color, where "background_color" is a tuple
    def set_background_color(self, background_color):
        self.background_color = background_color
        Screen.object.fill(self.background_color)

    def get_background_color(self):
        return self.background_color

    # sets screen images, where "background_path" is a str
    # and "background_point" is a tuple
    def set_background_image(self, background_path, background_point):
        self.background_image_path = background_path
        self.background_point = background_point
        background = self.py.image.load(self.background_image_path)
        Screen.object.blit(background, self.background_point)