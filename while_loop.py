from kivy.app import App
from kivy.uix.widget import Widget
from kivy.graphics import Color, Line
from kivy.config import Config

class MySquareApp(App):
    def build(self):

        self.title = 'Loop & Lines'

        parent = Widget()
        with parent.canvas:
            for x in range(500):
                for y in range(1, 800, 30):
                    Color(1, 1, 1)
                    Line(points=[x, y, 800, y], width=0.5)
                    Line(points=[y, x, y, 800], width=0.5)
                    # print(x, y)

        return parent

if __name__ == '__main__':
    # set the window size
    Config.set('graphics', 'width', '800')
    Config.set('graphics', 'height', '800')
    MySquareApp().run()
            