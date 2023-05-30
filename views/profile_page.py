from kivymd.uix.screen import MDScreen
from kivymd.uix.relativelayout import MDRelativeLayout
from kivy.animation import Animation
from kivy.lang import Builder
from kivy.properties import StringProperty, NumericProperty

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
#:import join os.path.join

<NewPost@BottomMenu>:
    canvas:
        Color:
            rgba: app.theme_cls.primary_color
        Rectangle:
            size: self.width, self.height*0.15
            pos: 0, self.height*0.85
        Color:
            rgba: 0, 0, 0, 1
        Line:
            rectangle: self.x, self.y + self.height*0.25, self.width, self.height*0.75
    MDIconButton:
        icon: 'arrow-left'
        pos_hint: {'x': 0, 'center_y': .925}
        on_press: root.close()
    BasicLabel:
        theme_text_color: 'Custom'
        text_color: 0, 0, 0, 1
        text: 'Nova Publicação'
        font_size: '22.5sp'
        halign: 'center'
        pos_hint: {'center_x': .5, 'top': .95}
    SelectImageButton:
        size_hint: 1.5, .4
        pos_hint: {'center_x': .5, 'top': .85}
        avatar: False
    TextInput:
        size_hint: 1, .2
        pos_hint: {'center_x': .5, 'top': .45}
        font_size: '18.25sp'
        hint_text: 'Escreva uma legenda'
    BasicButton:
        size_hint: .4, .15
        pos_hint: {'center_x': .5, 'center_y': .125}
        text: 'Publicar'
        font_size: '15sp'

<PostsArea>:
    size_hint: 1, .4
    pos_hint: {'top': .4}
    scroll_view_blur: 0
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
        id: menu_button
        size_hint: .275, .15
        pos_hint: {'right': .975, 'top': .95}
        text: 'Cardápio'
        md_bg_color: app.theme_cls.primary_dark
        on_press: 
            app.root.current = 'menu_page'
    ScrollView:
        size_hint: 1, 2
        pos_hint: {'top': .675}
        canvas.before:
            Color:
                rgba: 0, 0, 0, self.parent.scroll_view_blur
            Rectangle:
                size: self.width, self.height*2
                pos: self.x, self.y
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
            np: _np
        MDFloatLayout:
            MDIconButton:
                icon: join('views', 'data', 'logo.png')
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
        NewPost:
            id: _np

'''
)
4
class ProfilePage(MDScreen):
    name = 'profile_page'
    username = StringProperty('')
    bio = StringProperty('')
    img_src = StringProperty('')
    n_followers = NumericProperty(0)
    n_publications = NumericProperty(0)
    publications_data = [] #{'username': username, 'img_src': img_src, 'title': title, 'description': description}

    def set_profile_page(self, username, bio, img_src, n_followers, n_publications):
        self.username = username
        self.bio = bio
        self.img_src = img_src 
        self.n_followers = n_followers
        self.n_publications = n_publications

class PostsArea(MDRelativeLayout):
    up_anim = Animation(pos_hint={'top': .9}, duration=0.1, scroll_view_blur=0.5)
    down_anim =  Animation(pos_hint={'top': .4}, duration=0.1, scroll_view_blur=0)
    def on_touch_down(self, touch):
        if self.collide_point(*touch.pos) and touch.spos[1] > .8 and self.pos_hint['top'] == .9 and not self.ids.menu_button.collide_point(*touch.pos):
            self.down_anim.start(self)
        elif self.collide_point(*touch.pos) and self.pos_hint['top'] == .4 and not self.ids.menu_button.collide_point(*touch.pos):
            self.up_anim.start(self)
        return super().on_touch_down(touch)
