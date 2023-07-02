from kivymd.uix.screen import MDScreen
from kivy.lang import Builder
from kivy.metrics import dp
from control.control import list_users, user_image_was_loaded
import asyncio, os

Builder.load_string('''
#:import BasicLabel views.utils
#:import Background views.utils
#:import EstabAccount views.utils
#:import BottomBar views.utils
#:import FollowButton views.utils

<SearchBar@MDRelativeLayout>:
    canvas.before:
        Color: 
            rgba: 0, 0, 0, .4
        RoundedRectangle: 
            size: self.width, self.height + dp(4)
            pos: 0, -dp(4)
        Color: 
            rgba: 0, 0, 0, .2
        RoundedRectangle: 
            size: self.width, self.height + dp(7)
            pos: 0, -dp(7)
    pos_hint: {'top': 1}
    size_hint: 1, .1
    md_bg_color: app.theme_cls.primary_dark
    screen: None
    search_box: _search_box
    MDTextField:
        id: _search_box
        color_mode: 'custom'
        line_color_focus: .8, .8, .8, 1
        text_color_normal: .8, .8, .8, 1
        text_color_focus: .8, .8, .8, 1
        font_size: "18sp"
        hint_text: "Pesquisar"
        hint_text_color_focus: .8, .8, .8, 0.5
        hint_text_color_normal: .8, .8, .8, 0.5
        size_hint: .5, 1.15
        pos_hint: {'x': .125, 'center_y': .5}
        on_text: 
            root.screen.search(self.text)
    MDIconButton:
        pos_hint: {'x': 0, 'center_y': .5}
        icon: "magnify"
    BasicButton:
        text: 'Cancelar'
        pos_hint: {'right': .975, 'center_y': .5}
        font_size: '10sp'
        md_bg_color: app.theme_cls.primary_dark
        elevation: 0
        on_press:
            app.root.current = 'posts_page'

<SearchPage>:
    id: _screen
    rv: _rv
    app: app
    sb: _sb
    Background:
        id: _bg
    RelativeLayout:
        SearchBar:
            id: _sb
            screen: _screen
        RecycleView:
            id: _rv
            viewclass: 'FollowButton'
            size_hint: .98, .8
            pos_hint: {'center_x': .5, 'top': .875}
            RecycleBoxLayout:
                orientation: 'vertical'
                default_size: None, dp(56)
                default_size_hint: 1, None
                size_hint_y: None
                height: self.minimum_height
                spacing: dp(1)
        BottomBar:
'''
)

class SearchPage(MDScreen):
    name = 'search_page'
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        asyncio.ensure_future(self._set_users())
        
    async def _set_users(self):
        data = []
        for user in await list_users(True):
            if user['username'] == self.app.username or not user['can_post']: continue
            user.update({
                'image': os.path.join('views', 'data', 'user_images', user_image_was_loaded(user['username'])),
                'image_code': str(user['image_code']),
                'size_hint': (1, None),
                'height': dp(60)
            })
            data.append(user)
        self.rv.data = data
        self.users = data
    
    def on_pre_enter(self):
        for user in self.users:
            user['following'] = user['username'] in self.app.user['following']
        self.rv.data = self.users
        self.sb.search_box.text = ''
            
    def search(self, text):
        data = []
        for user in self.users:
            if text.lower() in user['username'].lower():
                data.append(user)
        self.rv.data = data