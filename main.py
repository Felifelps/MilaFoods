from views.screen_manager import ScreenManager
from kivymd.app import MDApp
from kivy.core.window import Window
from kivy.properties import DictProperty
from control.firebase_to_local import get_user_data, get_client, get_estab
Window.size = (340, 600)

class MilaFoods(MDApp):
    user = DictProperty({})
    def build(self):
        self.theme_cls.theme_style = 'Dark'
        self.theme_cls.primary_palette = 'Red'
        return ScreenManager()

    def on_start(self):
        data = get_user_data()
        if data[0] != '===++UserDefault++===': 
            self.user = (get_client(data[0]) if data[2] == 'client' else get_estab(data[0]))
            self.user['type'] = data[2]
        self.root.load_client_pages()
        return super().on_start()

if __name__ == '__main__':
    MilaFoods().run()