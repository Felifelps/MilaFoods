from kivy.core.window import Window
Window.size = (340, 600)

import asyncio
from views.screen_manager import ScreenManager
from kivymd.app import MDApp
from kivy.properties import StringProperty, DictProperty
from control.control import get_username, get_user, get_theme, get_user_posts

class MilaFoods(MDApp):
    username = StringProperty(get_username())
    theme = StringProperty(get_theme())
    user = DictProperty()
    following = []
    lateral_menu_is_active = False
    posts = []
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        
    def build(self):
        self.theme_cls.theme_style = 'Dark'
        self.theme_cls.primary_palette = self.theme
        return ScreenManager(self)

    def on_start(self):
        self.root.load_screens()
        return super().on_start()

    async def async_run(self, async_lib=None):
        await self.update_user(self.username)
        await self.update_posts()
        return await super().async_run(async_lib)
    
    async def update_user(self, username):
        self.username = username
        user = await get_user(self.username)
        if user:
            self.user = user
            self.user['tel'] = str(self.user['tel'])
            return 
        self.user = {}
        
        
    async def update_posts(self):
        self.posts = await get_user_posts(self.username)
        for post in self.posts:
            post['id'] = str(post['id'])
            post['height'] = 300
            post['liked'] = f"{post['username']}-{post['id']}" in self.user['liked']
            post['saved'] = f"{post['username']}-{post['id']}" in self.user['saved']

if __name__ == '__main__':
    asyncio.run(MilaFoods().async_run())


