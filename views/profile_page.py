from kivymd.uix.screen import MDScreen
from kivy.uix.relativelayout import RelativeLayout
from kivy.animation import Animation
from kivy.lang import Builder
import math

Builder.load_string('''
#:import BasicLabel views.utils
#:import Background views.utils
#:import BasicButton views.utils
#:import TopImageBar views.utils
#:import BottomBar views.utils
#:import LateralMenu views.utils
#:import Post views.utils
#:import join os.path.join

<PostsArea>:
    size_hint: 1, .35
    pos_hint: {'top': .35}
    BasicLabel:
        text: 'Publicações'
        font_size: '25sp'
        pos_hint: {'x': .025, 'top': .9}
        halign: 'left'
        canvas:
            Color:
                rgba: 1, 1, 1, 1
            Line:
                points: 0, self.y - dp(10), root.width, self.y - dp(10)
    BasicButton:
        size_hint: .275, .2
        pos_hint: {'right': .975, 'top': .95}
        text: 'Cardápio'
        md_bg_color: app.theme_cls.primary_dark
    ScrollView:
        size_hint: 1, 2
        pos_hint: {'top': .65}
        MDStackLayout:
            adaptive_height: True
            top: root.height - root.height*0.6
            spacing: 10, 20
            Post:
                post_title: "Jorginho lanches"
            Post:
            Post:
            Post:
            Post:

<ProfilePage>:
    Background:
        id: _bg
    RelativeLayout:
        TopImageBar:
            lm: _lm
        MDFloatLayout:
            MDIconButton:
                icon: join('views', 'data', 'animal.png')
                icon_size: '75sp'
                x: dp(10)
                center_y: root.height - dp(175)
            Label:
                text: 'Username'
                font_size: '25sp'
                size_hint: None, None
                size: self.texture_size
                pos: dp(10), root.height - dp(250)
            Label:
                text: 'Description\\nCavalo'
                font_size: '14sp'
                size_hint: None, None
                size: self.texture_size
                pos: dp(10), root.height - dp(285)
            BasicButton:
                size_hint_x: .275
                center_x: root.width/2 - dp(5)
                center_y: root.height - dp(200)
                text: 'Seguir'
                md_bg_color: app.theme_cls.primary_dark
            BasicButton:
                size_hint_x: .275
                center_x: root.width - dp(60)
                center_y: root.height - dp(200)
                text: 'Whatsapp'
                md_bg_color: app.theme_cls.primary_dark
            Label:
                id: publications
                number: 300
                text: f'[size=20sp]{self.number}[/size]\\nPublicações'
                halign: 'center'
                markup: True
                font_size: '12.5sp'
                size_hint: None, None
                size: self.texture_size
                center_y: root.height - dp(155)
                center_x: root.width - dp(58)
            Label:
                id: followers
                number: 300
                text: f'[size=20sp]{self.number}[/size]\\nSeguidores'
                halign: 'center'
                markup: True
                font_size: '12.5sp'
                size_hint: None, None
                size: self.texture_size
                center_y: root.height - dp(155)
                center_x: root.width/2
            PostsArea:

        BottomBar:
        LateralMenu:
            id: _lm
'''
)

class ProfilePage(MDScreen):
    name = 'profile_page'
    print('ajeitar profile page')

class PostsArea(RelativeLayout):
    up_anim = Animation(pos_hint={'top': .9}, duration=0.1)
    down_anim =  Animation(pos_hint={'top': .35}, duration=0.1)
    def on_touch_down(self, touch):
        if self.collide_point(*touch.pos) and touch.spos[1] > .8 and self.pos_hint['top'] == .9:
            self.down_anim.start(self)
        elif self.collide_point(*touch.pos) and self.pos_hint['top'] == .35:
            self.up_anim.start(self)
        return super().on_touch_down(touch)
