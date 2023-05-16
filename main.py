from views.screen_manager import ScreenManager
from kivymd.app import MDApp
from kivy.core.window import Window
Window.size = (340, 600)

class MilaFoods(MDApp):
    def build(self):
        self.theme_cls.theme_style = 'Dark'
        self.theme_cls.primary_palette = 'Red'
        return ScreenManager()

if __name__ == '__main__':
    MilaFoods().run()