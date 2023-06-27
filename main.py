from kivy.core.window import Window
Window.size = (340, 600)

import asyncio
from views.screen_manager import ScreenManager
from kivymd.app import MDApp
from kivy.properties import StringProperty, DictProperty
from control.control import get_username, get_user, get_theme, post,list_users, update_user

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
        #asyncio.ensure_future(self.test_post())
        return super().on_start()
    
    async def test_post(self):
        for user in await list_users(True):
            await update_user(
                user['username'], 
                {
                    'liked': [],
                    'saved': [],
                    'following': ['MilaFoods'],
                    'n_of_posts': 0 if user['can_post'] else None,
                    'n_of_followers': 0 if user['can_post'] else None,
                }
            )
            print(user['username'])
        print('done')

    async def async_run(self, async_lib=None):
        await self.update_user(self.username)
        return await super().async_run(async_lib)
    
    async def update_user(self, username):
        self.username = username
        user = await get_user(self.username)
        if user != False:
            user.update({'tel': str(user['tel'])})
            self.user = user
            return 
        self.user = {}

if __name__ == '__main__':
    asyncio.run(MilaFoods().async_run())


