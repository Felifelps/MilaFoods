import asyncio, platform

if 'Windows' in platform.system():
    from kivy.core.window import Window
    Window.size = (340, 600)

from views.screen_manager import ScreenManager
from kivymd.app import MDApp 
from kivymd.uix.dialog import MDDialog
from kivy.properties import StringProperty, DictProperty
from control.control import get_username, list_users, get_theme, update_user, get_user_posts, get_user, user_image_was_loaded

class MilaFoods(MDApp):
    username = StringProperty(get_username())
    theme = StringProperty(get_theme())
    user_image = StringProperty('account-circle.png')
    user = DictProperty()
    following = []
    lateral_menu_is_active = False
    posts = []
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
                    'n_of_followers': 0
                }
            )
            print(user['username'])
        #print(json.dumps(a, indent=4))

    async def async_run(self, async_lib=None):
        await self.update_user(self.username)
        return await super().async_run(async_lib)
    
    async def update_user(self, username):
        if username != self.username: self.username = username
        user = await get_user(self.username)
        if user != False:
            self.user_image = user_image_was_loaded(username)
            self.user = user
            self.posts = await get_user_posts(username)
            for post in self.posts:
                post.update({
                    'height': 300
                })
            return 
        self.user = {}

try:
    if __name__ == '__main__':
        loop = asyncio.new_event_loop()
        loop.run_until_complete(MilaFoods().async_run())
except Exception as e:
    input(e)


