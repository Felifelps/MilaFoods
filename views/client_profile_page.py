from kivymd.uix.screen import MDScreen
from kivymd.uix.relativelayout import MDRelativeLayout
from kivy.animation import Animation
from kivy.lang import Builder
from kivy.properties import ListProperty
from control.control import get_post, get_user
import asyncio

Builder.load_string('''
#:import BasicLabel views.utils
#:import Background views.utils
#:import BasicButton views.utils
#:import BasicTextField views.utils
#:import TopImageBar views.utils
#:import BottomBar views.utils
#:import LateralMenu views.utils
#:import Post views.utils
#:import BottomMenu views.utils
#:import SelectImageButton views.utils
#:import DynamicSourceImage views.utils
#:import join os.path.join

<SavedArea>:
    size_hint: 1, .4
    screen: None
    pos_hint: {'center_x': .5 if self.screen != None and self.screen.username == app.user['username'] else 10, 'top': .5}
    scroll_view_blur: 0
    rv: _rv
    BasicLabel:
        text: 'Salvos'
        font_size: '30sp'
        pos_hint: {'center_x': .5, 'top': .9}
        canvas:
            Color:
                rgba: 1, 1, 1, 1
            Line:
                points: 0, self.y - dp(5), root.width, self.y - dp(5)
    MDIconButton:
        icon: 'star'
        icon_size: '40sp'
        pos_hint: {'right': 1, 'top': .975}
    MDIconButton:
        icon: 'star'
        icon_size: '40sp'
        pos_hint: {'x': 0, 'top': .975}
    RecycleView:
        id: _rv
        viewclass: 'SavedPost'
        size_hint: 1, 2
        pos_hint: {'top': .675}
        RecycleGridLayout:
            cols: 3
            default_col_width: dp(106)
            default_size: None, dp(56)
            default_size_hint: 1, None
            size_hint_y: None
            height: self.minimum_height
            padding: dp(5)
            spacing: dp(5)

<ClientProfilePage>:
    id: _screen
    username: app.user['username']
    description: app.user['description']
    image: ''
    Background:
        id: _bg
    RelativeLayout:
        TopImageBar:
            lm: _lm
        MDFloatLayout:
            id: _estab
            DynamicSourceImage:
                pos_hint: {'center_x': .2, 'center_y': .75}
                size_hint: None, None
                size: sp(125), sp(125)
                pattern: join('views', 'data', 'user_images', '@')
                key: _screen.image
            Label:
                text: f"[b]{_screen.username}[/b]"
                font_size: '25sp'
                markup: True
                size_hint: None, None
                size: self.texture_size
                pos_hint: {'x': .425, 'center_y': .75}
            Label:
                text: _screen.description
                font_size: '14sp'
                size_hint: None, None
                size: self.texture_size
                pos_hint: {'x': .05, 'top': .625}
            
        BottomBar:
        LateralMenu:
            id: _lm
        
'''
)

class ClientProfilePage(MDScreen):
    name = 'client_profile_page'
    saved = ListProperty([])
