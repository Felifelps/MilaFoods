from kivymd.uix.screen import MDScreen
from kivy.lang import Builder
from kivy.metrics import dp
from kivy.properties import ListProperty
from kivymd.uix.dialog import MDDialog
from control.firebase_to_local import update_posts, get_posts_from_db

Builder.load_string(
'''
#:import TopSearchBar views.utils
#:import BottomBar views.utils
#:import BasicLabel views.utils
#:import Background views.utils
#:import LateralMenu views.utils
#:import Post views.utils
    
<ViewPostPage>:
    Background:
    FloatLayout:
        canvas.before:
            Color:
                rgba: .98, .98, .98, 1
            Rectangle:
                size: self.width, self.height
                pos: 0, 0
        TopImageBar:
        MDIconButton:
            pos_hint: {'center_x': .085, 'center_y': .925}
            icon_size: '35sp'
            theme_icon_color: 'Custom'
            icon_color: .1, .1, .1, 1
            icon: "account-circle"
        Label:
            text: ""
            color: .1, .1, .1, 1
            size_hint: None, None
            size: self.texture_size
            font_size: '12sp'
            pos_hint: {'x': .16, 'center_y': .915}
        Image:
            id: _img
            pos_hint: {'top': .85}
            size_hint: 1, .55
            source: join('views', 'data', 'logo.png') 
        MDIconButton:
            pos_hint: {'center_x': .08, 'center_y': .78}
            theme_icon_color: 'Custom'
            icon_color: .75, .75, .75, 1
            icon: "star"
            clicked: False
            on_release:
                self.icon_color = (.75, .75, .75, 1) if self.clicked else (.85, .68, .21, 1)
                self.clicked = not self.clicked
        MDIconButton:
            pos_hint: {'right': .9, 'top': .28}
            theme_icon_color: 'Custom'
            icon: "heart"
            icon_color: .75, .75, .75, 1
            clicked: False
            on_release:
                self.icon_color = (.75, .75, .75, 1) if self.clicked else (1, 0, .2, 1)
                self.clicked = not self.clicked
        MDIconButton:
            pos_hint: {'right': 1, 'top': .28}
            theme_icon_color: 'Custom'
            icon: "message-outline"
            icon_color: .1, .1, .1, 1
        Label:
            text: ""
            color: .1, .1, .1, 1
            size_hint: None, None
            size: self.texture_size
            font_size: '14sp'
            markup: True
            pos_hint: {'x': .03, 'top': .28}
        MDRectangleFlatIconButton:
            text: "Comentar"
            halign: 'left'
            icon: "account-circle"
            line_color: 0, 0, 0, 0
            theme_text_color: 'Custom'
            text_color: .1, .1, .1, 1
            theme_icon_color: 'Custom'
            icon_color: .6, .6, .6, 1
            icon_size: '20sp'
            font_size: '11sp'
            size_hint: .05, .1
            pos_hint: {"center_x": .14, "center_y": .075}
        BottomBar:
'''
)

class ViewPostPage(MDScreen):
    name = 'view_post_page'
    data = ListProperty()
    def get_posts(self):
        update_posts()
        self.dialog.dismiss()
        data = get_posts_from_db()
        print(data)
        self.ids._rv.data = data