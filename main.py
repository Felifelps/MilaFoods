from views.screen_manager import ScreenManager
from kivymd.app import MDApp
from kivy.core.window import Window
from kivy.properties import DictProperty
from control.firebase_to_local import get_user_data
Window.size = (340, 600)

class MilaFoods(MDApp):
    user = DictProperty({})
    default_user = '===++UserDefault++==='
    def build(self):
        self.theme_cls.theme_style = 'Dark'
        self.theme_cls.primary_palette = 'Red'
        return ScreenManager()

    def on_start(self):
        self.user = get_user_data()
        self.root.load_screens(self.user, self.default_user)
        return super().on_start()

if __name__ == '__main__':
    MilaFoods().run()