
from kivy.core.window import Window
Window.size = (340, 600)

import asyncio
from views.screen_manager import ScreenManager
from kivymd.app import MDApp
from kivy.properties import StringProperty, DictProperty
from control.control import get_username, get_user, get_theme

class MilaFoods(MDApp):
    username = StringProperty(get_username())
    theme = StringProperty(get_theme())
    user = DictProperty()
    posts = []
    following = []
    lateral_menu_is_active = False
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        
    def build(self):
        self.theme_cls.theme_style = 'Dark'
        self.theme_cls.primary_palette = self.theme
        return ScreenManager(self)

    def on_start(self):
        self.root.load_screens()
        return super().on_start() 
    
    def update_user(self, username):
        print(username)
        self.username = username
        user = get_user(self.username)
        self.user = {} if user == False else user

if __name__ == '__main__':
    asyncio.run(MilaFoods().async_run())


