import asyncio
from views.screen_manager import ScreenManager
from kivymd.app import MDApp
from kivy.core.window import Window
from kivy.properties import DictProperty
from control.firebase_to_local import get_user_data, estab_un_like, estab_comment
Window.size = (340, 600)

class MilaFoods(MDApp):
    user = DictProperty(get_user_data())
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def build(self):
        self.theme_cls.theme_style = 'Dark'
        self.theme_cls.primary_palette = self.user['theme']
        return ScreenManager(self)

    def on_start(self):
        print(self.user)
        self.root.load_screens(self.user)
        return super().on_start()

    def update_user(self): self.user = get_user_data()    

if __name__ == '__main__':
    asyncio.run(MilaFoods().async_run())
