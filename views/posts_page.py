from kivymd.uix.screen import MDScreen
from kivy.lang import Builder
from kivy.metrics import dp
from kivy.properties import ListProperty
from kivymd.uix.dialog import MDDialog
from control.control import get_posts_from_server

Builder.load_string('''
#:import BottomBar views.utils
#:import BasicLabel views.utils
#:import Background views.utils
#:import LateralMenu views.utils
#:import Post views.utils

<PostsBar@MDRelativeLayout>:
    lm: None
    screen: None
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
    MDIconButton:
        pos_hint: {'x': .025, 'center_y': .5}
        icon_size: '40sp'
        icon: 'account-circle' #if app.user['image_code'] == "0" else join('views', 'data', 'profile_images', f"{app.user['image_code']}.png")
        on_press:
            app.root.load_profile_page()
    MDTextField:
        color_mode: 'custom'
        line_color_focus: .8, .8, .8, 1
        text_color_normal: .8, .8, .8, 1
        text_color_focus: .8, .8, .8, 1
        font_size: "13sp"
        hint_text: "Pesquisar"
        hint_text_color_focus: .8, .8, .8, 0.5
        hint_text_color_normal: .8, .8, .8, 0.5
        size_hint: .6, 1
        pos_hint: {'center_x': .5, 'center_y': .5}
        on_focus:
            if root.screen.loaded: app.root.current = 'search_page'
    MDIconButton:
        pos_hint: {'x': .7, 'center_y': .5}
        icon: "magnify" 
    BarMenuButton:
        lm: root.lm    

<PostsPage>:
    id: _screen
    Background:
    FloatLayout:
        PostsBar:
            id: bar
            lm: _lm
            screen: _screen
        RecycleView:
            id: _rv
            viewclass: 'Post'
            pos_hint: {'center_x': .5, 'top': .875}
            size_hint: .98, .8
            RecycleBoxLayout:
                id: _box
                orientation: 'vertical'
                default_size: None, dp(56)
                default_size_hint: 1, None
                size_hint_y: None
                height: self.minimum_height
                spacing: dp(10)
        BottomBar:
        LateralMenu:
            id: _lm
'''
)

class PostsPage(MDScreen):
    name = 'posts_page'
    data = ListProperty()
    updated = False
    loaded = False
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.dialog = MDDialog(
            text='Atualizando posts...',
            on_open=lambda x: self.get_posts(True)
        )
        
    def get_posts(self, random):
        self.dialog.dismiss()
        self.ids._rv.data = get_posts_from_server(random)
    
    def on_enter(self, *args):
        if not self.updated:
            self.dialog.open()
            self.updated = True
        self.loaded = True
        return super().on_enter(*args)

    def on_leave(self, *args):
        self.loaded = False
        return super().on_leave(*args)