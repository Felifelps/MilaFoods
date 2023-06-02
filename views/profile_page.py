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

<SavedArea>:
    size_hint: 1, .4
    pos_hint: {'top': .4}
    scroll_view_blur: 0
    BasicLabel:
        text: 'Salvos'
        font_size: '25sp'
        pos_hint: {'center_x': .5, 'top': .9}
        canvas:
            Color:
                rgba: 1, 1, 1, 1
            Line:
                points: 0, self.y - dp(10), root.width, self.y - dp(10)
    MDIconButton:
        icon: 'star'
        icon_size: '40sp'
        pos_hint: {'right': 1, 'top': .975}
    MDIconButton:
        icon: 'star'
        icon_size: '40sp'
        pos_hint: {'x': 0, 'top': .975}
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
    id: _screen
    Background:
        id: _bg
    RelativeLayout:
        TopImageBar:
            lm: _lm
        MDFloatLayout:
            id: _estab
            MDIconButton:
                icon: 'account-circle' if app.user['image_code'] == "0" else join('views', 'data', 'profile_images', f'{app.user["image_code"]}.png')
                icon_size: '112.5sp'
                center_x: root.width*0.2
                center_y: root.height - dp(175)
            Label:
                text: app.user['username']
                font_size: '25sp'
                size_hint: None, None
                size: self.texture_size
                pos_hint: {'x': .4, 'center_y': .7}
            Label:
                text: app.user['description']
                font_size: '14sp'
                size_hint: None, None
                size: self.texture_size
                pos: dp(10), root.height - dp(275)
            BasicButton:
                text: 'Editar Perfil'
                font_size: '15sp'
                size_hint: .2, .025
                pos_hint: {'x': .01, 'center_y': .425}
            SavedArea:
            
        BottomBar:
        LateralMenu:
            id: _lm

'''
)

class ProfilePage(MDScreen):
    name = 'profile_page'
    
    username = StringProperty('username')
    bio = StringProperty('bio')
    img_src = StringProperty('logo.png')
    n_followers = NumericProperty(1)
    n_publications = NumericProperty(1)
    publications_data = [] #{'username': username, 'img_src': img_src, 'title': title, 'description': description}

    def set_profile_page(self, username):
        self.username = username
        print('get the user by the database')
        #self.bio = 'Bio'
        #self.img_src = 'logo.png' 
        #self.n_followers = 1
        #self.n_publications = 1

class SavedArea(MDRelativeLayout):
    up_anim = Animation(pos_hint={'top': .9}, duration=0.1, scroll_view_blur=0.5)
    down_anim =  Animation(pos_hint={'top': .4}, duration=0.1, scroll_view_blur=0)
    def on_touch_down(self, touch):
        if self.collide_point(*touch.pos) and touch.spos[1] > .8 and self.pos_hint['top'] == .9:
            self.down_anim.start(self)
        elif self.collide_point(*touch.pos) and self.pos_hint['top'] == .4:
            self.up_anim.start(self)
        return super().on_touch_down(touch)
