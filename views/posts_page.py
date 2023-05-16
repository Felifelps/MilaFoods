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
    username: 'Username'
    post_title: 'title'
    description: 'description'
    image: _img
    size_hint: 1, None
    height: dp(275)
    canvas.before:
        Color:
            rgba: .98, .98, .7, 1
        Rectangle:
            size: self.width, self.height
            pos: 0, 0
    MDIconButton:
        pos_hint: {'center_x': .085, 'center_y': .925}
        icon_size: '35sp'
        theme_icon_color: 'Custom'
        icon_color: .1, .1, .1, 1
        icon: "account-circle"
    MDIconButton:
        pos_hint: {'right': 1, 'center_y': .925}
        icon_size: '30sp'
        theme_icon_color: 'Custom'
        icon_color: .1, .1, .1, 1
        icon: "dots-horizontal"
    Label:
        text: root.username
        color: .1, .1, .1, 1
        size_hint: None, None
        size: self.texture_size
        font_size: '12sp'
        pos_hint: {'x': .16, 'center_y': .915}
    Image:
        id: _img
        pos_hint: {'top': .85}
        size_hint: 1, .55
    MDIconButton:
        pos_hint: {'center_x': .08255, 'center_y': .78}
        icon_size: '35sp'
        theme_icon_color: 'Custom'
        icon_color: .75, .75, .75, 1
        icon: "star"
        clicked: False
        on_release:
            self.icon_color = (.75, .75, .75, 1) if self.clicked else (.2, .2, .2, 1)
            self.clicked = not self.clicked
    Label:
        text: root.post_title
        color: .1, .1, .1, 1
        size_hint: None, None
        size: self.texture_size
        font_size: '14sp'
        markup: True
        pos_hint: {'x': .025, 'top': .28}
    Label:
        text: root.description
        color: .1, .1, .1, 1
        size_hint: None, None
        size: self.texture_size
        font_size: '11sp'
        markup: True
        pos_hint: {'x': .025, 'top': .19}
    
            
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
                    post_title: "Jorginho lanches"
                Post:
                Post:
                Post:
                Post:
            
        BottomBar:
        
        
'''
)

class PostsPage(MDScreen):
    name = 'posts_page'
    