from kivy.app import App
from kivy.uix.widget import Widget
from kivy.graphics import Color, Rectangle, Line
from kivy.config import Config

import random

class MySquareApp(App):
    def build(self):
        # set the window title
        # self.title = 'Loop & Squares'
        self.title = 'Loop & Lines'
    

        parent = Widget()
        with parent.canvas:
            #color RGB:
            # 0 = minimum
            # 1 = maximum (255)
            #
            # (1, 0, 0) -> red
            # (0, 1, 0) -> green
            # (0, 0, 1) -> blue
            # (1, 1, 0) -> yellow ...
            number_lines = 0
            while number_lines <= 800:
                Color(1, 1, 1)
                Line(points=[200, 400, 800, 800])
                number_lines += 100
            # number_rectangles = 0
            # while number_rectangles <= 800:
                # my_color_red = random.randrange(0, 10)/10
                # my_color_green = random.randrange(0, 10)/10
                # my_color_blue = random.randrange(0, 10)/10
                # Color(my_color_red, my_color_green, my_color_blue)
                # Rectangle(size=(100, 100), pos=(number_rectangles,0))
                # Line(points=[400, 400, 800, 400], width=5)
                # number_rectangles += 100
                
        return parent

if __name__ == '__main__':
    # set the window size
    Config.set('graphics', 'width', '800')
    Config.set('graphics', 'height', '800')
    MySquareApp().run()

