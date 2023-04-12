from kivy.app import App
from kivy.uix.widget import Widget
from kivy.graphics import Color, Rectangle, Line
from kivy.config import Config

class MySquareApp(App):
    def build(self):

        self.title = 'Loop & Lines'

        parent = Widget()
        with parent.canvas:
            for x in range(15):
                for y in range(25):
                    Color(1, 1, 1)
                    Line(points=[x, y, 800, y], width=2)
                    print(x,y)

        return parent

if __name__ == '__main__':
    # set the window size
    Config.set('graphics', 'width', '800')
    Config.set('graphics', 'height', '800')
    MySquareApp().run()
            