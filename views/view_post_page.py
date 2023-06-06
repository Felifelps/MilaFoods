from kivymd.uix.screen import MDScreen
from kivy.lang import Builder
from kivy.properties import StringProperty, ListProperty
from control.firebase_to_local import estab_like, estab_un_like, client_like, client_un_like, add_liked_data, remove_liked_data

Builder.load_string('''
#:import TopImageAndStarBar views.utils
#:import BottomBar views.utils
#:import BasicLabel views.utils
#:import Background views.utils
#:import LateralMenu views.utils
#:import Post views.utils
#:import ProfileButton views.utils
#:import join os.path.join
<EmojiButton@MDIconButton>:
    code: 1
    pos_hint: {'center_x': .2 + (0.075 * (self.code - 1)), 'center_y': .375}
    icon: join('views', 'data', 'emojis', f'{self.code}.png')

<Comment@RelativeLayout>:
    size_hint: .35, .1
    username: 'username'
    code: 1
    MDIconButton:
        pos_hint: {'x': 0, 'center_y': .5}
        icon_size: '35sp'
        icon: 'account-circle' if app.user['image_code'] == "0" else join('views', 'data', 'profile_images', f"{app.user['image_code']}.png")
        theme_icon_color: "Custom"
        icon_color: 'black'
        on_press:
            app.root.load_profile_page(root.username)
    Label:
        text: root.username
        pos_hint: {'x': .2, 'center_y': .825}
        color: 0, 0, 0, 1
    MDIconButton:
        pos_hint: {'center_x': .65, 'center_y': .375}
        size_hint: .3, .5
        icon: join('views', 'data', 'profile_images', f'{root.code}.png')
    
<CommentBar@MDRelativeLayout>:
    md_bg_color: .3, .3, .3, 1
    MDIconButton:
        pos_hint: {'x': .02, 'center_y': .5}
        icon: join('views', 'data', 'profile_images', '1.png')
    Label:
        text: app.user['username']
        size_hint: None, None
        size: self.texture_size
        pos_hint: {'x': .15, 'center_y': .825}
    EmojiButton:
    EmojiButton:
        code: 2
    EmojiButton:
        code: 3
    EmojiButton:
        code: 4
    EmojiButton:
        code: 5
    EmojiButton:
        code: 6
    EmojiButton:
        code: 7
    EmojiButton:
        code: 8
    
<ViewPostPage>:
    id: _screen
    rv: _rv
    Background:
    FloatLayout:
        TopImageAndStarBar:
        RelativeLayout:
            pos_hint: {'x': 0, 'top': .9}
            size_hint: 1, .8
            canvas.before:
                Color:
                    rgba: .95, .95, .95, 1
                Rectangle:
                    size: self.width, self.height
                    pos: 0, 0
            MDIconButton:
                pos_hint: {'x': 0, 'center_y': .95}
                icon_size: '35sp'
                theme_icon_color: 'Custom'
                icon_color: 0, 0, 0, 1
                icon: 'account-circle' if _screen.user_image == 'None' else _screen.user_image
                on_press:
                    app.root.load_estab_profile_page(_screen.username)
            Label:
                text: _screen.username
                color: .1, .1, .1, 1
                size_hint: None, None
                size: self.texture_size
                font_size: '15sp'
                pos_hint: {'x': .16, 'center_y': .95}
            Image:
                pos_hint: {'top': .9}
                size_hint: 1, .3
                source: join('views', 'data', 'logo.png') #_screen.image
            MDIconButton:
                pos_hint: {'right': 1, 'top': .6}
                theme_icon_color: 'Custom'
                icon: "heart"
                icon_color: .75, .75, .75, 1
                clicked: _screen.code in app.liked
                on_release:
                    _screen.like_or_un_like(self.clicked, app.root.logged_user_is_client)
                    self.icon_color = (.75, .75, .75, 1) if self.clicked else (1, 0, .2, 1)
                    self.clicked = not self.clicked
            Label:
                text: _screen.text
                color: .1, .1, .1, 1
                size_hint: None, None
                size: self.texture_size
                font_size: '14sp'
                markup: True
                pos_hint: {'x': .03, 'top': .575}
            RecycleView:
                id: _rv
                viewclass: 'Comment'
                pos_hint: {'center_x': .5, 'top': .475}
                size_hint: .98, .35
                RecycleBoxLayout:
                    orientation: 'vertical'
                    default_size: None, dp(56)
                    default_size_hint: 1, None
                    size_hint_y: None
                    height: self.minimum_height
                    spacing: dp(10)
            CommentBar:
                pos_hint: {'y': 0}
                size_hint: 1, .125
        BottomBar:
'''
)

class ViewPostPage(MDScreen):
    name = 'view_post_page'
    username = StringProperty('') 
    user_image = StringProperty('') 
    text = StringProperty('') 
    code = StringProperty('') 
    comments = ListProperty([]) 
    def on_comments(self, a, b):
        self.rv.data = [{'username': x.split('-')[0], 'code': x.split('-')[1], 'size_hint_x': .35} for x in self.comments]
    
    def like_or_un_like(self, liked, is_client):
        if is_client:
            client_un_like(self.parent.app.user['username'], self.code) if liked else client_like(self.parent.app.user['username'], self.code)
            add_liked_data(self.code)
        else:
            estab_un_like(self.parent.app.user['username'], self.code) if liked else estab_like(self.parent.app.user['username'], self.code)
            remove_liked_data(self.code)
        self.manager.current_screen.get_posts(False)
