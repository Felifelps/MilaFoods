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
    pos_hint: {'top': .5}
    scroll_view_blur: 0
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
                pos_hint: {'center_x': .2, 'center_y': .75}
            Label:
                text: f"[b]{app.user['username']}[/b]"
                font_size: '25sp'
                markup: True
                size_hint: None, None
                size: self.texture_size
                pos_hint: {'x': .4, 'center_y': .75}
            Label:
                text: app.user['description']
                font_size: '14sp'
                size_hint: None, None
                size: self.texture_size
                pos_hint: {'x': .05, 'top': .65}
            BasicButton:
                text: 'Editar Perfil'
                md_bg_color: app.theme_cls.primary_dark
                pos_hint: {'x': .025, 'y': .48}
            SavedArea:
            
        BottomBar:
        LateralMenu:
            id: _lm

'''
)

class ClientProfilePage(MDScreen):
    name = 'client_profile_page'

class SavedArea(MDRelativeLayout):
    up_anim = Animation(pos_hint={'top': .9}, duration=0.1, scroll_view_blur=0.5)
    down_anim =  Animation(pos_hint={'top': .4}, duration=0.1, scroll_view_blur=0)
    def on_touch_down(self, touch):
        if self.collide_point(*touch.pos) and touch.spos[1] > .8 and self.pos_hint['top'] == .9:
            self.down_anim.start(self)
        elif self.collide_point(*touch.pos) and self.pos_hint['top'] == .4:
            self.up_anim.start(self)
        return super().on_touch_down(touch)
