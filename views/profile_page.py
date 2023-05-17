from kivymd.uix.screen import MDScreen
from kivy.lang import Builder

Builder.load_string('''
#:import BasicLabel views.utils
#:import Background views.utils
#:import BasicButton views.utils
#:import TopImageBar views.utils
#:import BottomBar views.utils
#:import Post views.utils

<ProfilePage>:
    Background:
        id: _bg
    RelativeLayout:
        TopImageBar:
        Image:
            size_hint: None, None
            size: dp(100), dp(100)
            pos_hint: {'x': .05, 'center_y': .75}
        Label:
            text: 'Username'
            font_size: '20sp'
            size_hint: None, None
            size: self.texture_size
            pos_hint: {'x': .05, 'center_y': .625}
        Label:
            text: 'Description\\nCavalo'
            font_size: '12.5sp'
            size_hint: None, None
            size: self.texture_size
            pos_hint: {'x': .05, 'top': .6}
        BasicButton:
            size_hint_x: .275
            pos_hint: {'x': .375, 'y': .675}
            text: 'Seguir'
            md_bg_color: app.theme_cls.primary_dark
        BasicButton:
            size_hint_x: .275
            pos_hint: {'x': .675, 'y': .675}
            text: 'Whatsapp'
            md_bg_color: app.theme_cls.primary_dark
        Label:
            text: '{}'
            font_size: '20sp'
            size_hint: None, None
            size: self.texture_size
            pos_hint: {'center_x': .5, 'center_y': .8}
        Label:
            text: 'Publicações'
            font_size: '12.5sp'
            size_hint: None, None
            size: self.texture_size
            pos_hint: {'center_x': .5, 'center_y': .76}
        Label:
            text: '{}'
            font_size: '20sp'
            size_hint: None, None
            size: self.texture_size
            pos_hint: {'center_x': .83, 'center_y': .8}
        Label:
            text: 'Seguidores'
            font_size: '12.5sp'
            size_hint: None, None
            size: self.texture_size
            pos_hint: {'center_x': .83, 'center_y': .76}
        BasicLabel:
            text: 'Publicações'
            font_size: '25sp'
            pos_hint: {'x': .05, 'center_y': .46}
            canvas:
                Color:
                    rgba: 1, 1, 1, 1
                Line:
                    points: 0, self.y - dp(10), 10000, self.y - dp(10)
        BasicButton:
            size_hint_x: .275
            pos_hint: {'right': .95, 'center_y': .46}
            text: 'Cardápio'
            md_bg_color: app.theme_cls.primary_dark
        ScrollView:
            pos_hint: {'center_x': .5, 'top': .4}
            size_hint: .98, .3
            MDStackLayout:
                id: _stack
                adaptive_height: True
                spacing: 10, 20
                Post:
                    post_title: "Jorginho lanches"
                Post:
                Post:
                Post:
                Post:
        BottomBar:
'''
)

class ProfilePage(MDScreen):
    name = 'profile_page'