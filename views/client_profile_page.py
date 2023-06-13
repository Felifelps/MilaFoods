from kivymd.uix.screen import MDScreen
from kivymd.uix.relativelayout import MDRelativeLayout
from kivy.animation import Animation
from kivy.lang import Builder
from kivy.properties import ListProperty
from control.control import get_post, get_user

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
    screen: None
    pos_hint: {'center_x': .4 if self.screen != None and self.screen.username == app.user['username'] else 10, 'top': .5}
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
    image_code: 0
    sa: _sa
    Background:
        id: _bg
    RelativeLayout:
        TopImageBar:
            lm: _lm
        MDFloatLayout:
            id: _estab
            MDIconButton:
                icon: 'account-circle' if _screen.image_code == 0 else join('views', 'data', 'profile_images', f'{_screen.image_code}.png')
                icon_size: '112.5sp'
                pos_hint: {'center_x': .2, 'center_y': .75}
            Label:
                text: f"[b]{_screen.username}[/b]"
                font_size: '25sp'
                markup: True
                size_hint: None, None
                size: self.texture_size
                pos_hint: {'x': .4, 'center_y': .75}
            Label:
                text: _screen.description
                font_size: '14sp'
                size_hint: None, None
                size: self.texture_size
                pos_hint: {'x': .05, 'top': .65}
            BasicButton:
                text: 'Editar Perfil'
                md_bg_color: app.theme_cls.primary_dark
                pos_hint: {'x': .025, 'y': .48}
            SavedArea:
                id: _sa
                screen: _screen
            
        BottomBar:
        LateralMenu:
            id: _lm
'''
)

class ClientProfilePage(MDScreen):
    name = 'client_profile_page'
    saved = ListProperty([])
    def on_saved(self, a, b):
        data = []
        n = 0
        for saved in get_user(self.manager.app.user['username'])['saved']:
            if n == 3: break
            saved_data = get_post(saved)
            saved_data['id'] = str(saved_data['id'])
            saved_data['width'] = 130
            saved_data['height'] = 130
            data.append(saved_data)
            n += 1
        self.sa.rv.data = data

class SavedArea(MDRelativeLayout):
    def on_touch_down(self, touch):
        if self.collide_point(*touch.pos):
            self.parent.parent.parent.manager.current = 'saved_page'
            return True
        return super().on_touch_down(touch)
