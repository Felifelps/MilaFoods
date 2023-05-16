from kivymd.uix.screen import MDScreen
from kivy.lang import Builder

Builder.load_string(
'''
#:import TopSearchBar views.utils
#:import BottomBar views.utils
#:import BasicLabel views.utils
#:import Background views.utils
#:import join os.path.join

<Post@RelativeLayout>:
    username: ''
    image: _img
    size_hint: 1, None
    height: dp(250)
    canvas.before:
        Color:
            rgba: .9, .9, .9, 1
        Rectangle:
            size: self.width, self.height
            pos: 0, 0
    MDIconButton:
        pos_hint: {'center_x': .085, 'center_y': .9}
        icon_size: '40sp'
        theme_icon_color: 'Custom'
        icon_color: .1, .1, .1, 1
        icon: "account-circle"
    MDIconButton:
        pos_hint: {'right': 1, 'center_y': .9}
        icon_size: '30sp'
        theme_icon_color: 'Custom'
        icon_color: .1, .1, .1, 1
        icon: "dots-horizontal"
    MDIconButton:
        pos_hint: {'x': 0, 'center_y': .9}
        icon_size: '30sp'
        theme_icon_color: 'Custom'
        icon_color: .9, .9, .9, 1
        icon: "star"
        on_release:
            self.icon_color = (.1, .1, .1, 1) if self.icon_color == (.9, .9, .9, 1) else (.9, .9, .9, 1)
    Label:
        text: f'{root.username}'
        color: .1, .1, .1, 1
        size_hint: None, None
        size: self.texture_size
        font_size: '12sp'
        pos_hint: {'x': .16, 'center_y': .9}
    Label:
        text: ''
        color: .1, .1, .1, 1
        size_hint: None, None
        size: self.texture_size
        font_size: '12sp'
        markup: True
        pos_hint: {'x': .15, 'center_y': .95}
    Image:
        id: _img
        pos_hint: {'top': .8}
        size_hint: 1, .55
    
            
<PostsPage>:
    Background:
    FloatLayout:
        TopSearchBar:
            id: bar
        ScrollView:
            pos_hint: {'center_x': .5, 'top': .875}
            size_hint: .98, .8
            MDStackLayout:
                id: _stack
                adaptive_height: True
                spacing: 10, 20
                Post:
                    username: "Jorginho lanches"
                Post:
                Post:
                Post:
                Post:
            
        BottomBar:
        
        
'''
)

class PostsPage(MDScreen):
    name = 'posts_page'
    