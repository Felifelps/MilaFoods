from kivymd.uix.screen import MDScreen
from kivy.lang import Builder
from kivy.properties import StringProperty, ListProperty, BooleanProperty, NumericProperty
from control.control import user_like, user_un_like, user_comment, save_post, un_save_post
from kivymd.uix.dialog import MDDialog
from kivymd.uix.snackbar import Snackbar
import asyncio

Builder.load_string('''
#:import TopImageAndStarBar views.utils
#:import BottomBar views.utils
#:import BasicLabel views.utils
#:import Background views.utils
#:import LateralMenu views.utils
#:import Post views.utils
#:import ProfileButton views.utils
#:import BasicSpinner views.utils
#:import join os.path.join

<EmojiButton@MDIconButton>:
    screen: self.parent.screen
    code: 1
    pos_hint: {'center_x': .2 + (0.1 * (self.code - 1)), 'center_y': .375}
    icon: join('views', 'data', 'emojis', f'{int(self.code)}.png')
    on_press:
        self.screen.comment(self.code)

<Comment@BoxLayout>:
    username: 'username'
    code: 1
    spacing: dp(10)
    MDIconButton:
        icon_size: '35sp'
        size_hint_y: 1 
        icon: 'account-circle' #if app.user['image_code'] == "0" else join('views', 'data', 'profile_images', f"{app.user['image_code']}.png")
        theme_icon_color: "Custom"
        icon_color: 'black'
        on_press:
            app.root.load_profile_page(root.username)
    Label:
        id: _label
        text: root.username
        size_hint: None, 1
        size: self.texture_size
        color: 0, 0, 0, 1
    MDIcon:
        icon_size: '40sp'
        source: join('views', 'data', 'emojis', f'{int(root.code)}.png')
        size_hint_y: 1

    
<CommentBar@MDRelativeLayout>:
    md_bg_color: .3, .3, .3, 1
    screen: None
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
    
<CommentPage>:
    id: _screen
    rv: _rv
    Background:
    FloatLayout:
        TopImageAndStarBar:
            screen: _screen
            saved: _screen.saved
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
                icon: 'account-circle'
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
                source: join('views', 'data', 'logo.png') 
            MDIconButton:
                pos_hint: {'right': 1, 'top': .6}
                theme_icon_color: 'Custom'
                icon: "heart"
                icon_color: (.75, .75, .75, 1) if not _screen.liked else (1, 0, .2, 1)
                on_release:
                    _screen.like_or_un_like()
            Label:
                text: str(_screen.likes)
                color: .1, .1, .1, 1
                size_hint: None, None
                size: self.texture_size
                font_size: '13sp'
                pos_hint: {'right': .85, 'center_y': .555}
            Label:
                text: f"[ref='name']{_screen.text if len(_screen.text) < 22 else _screen.text[:20] + '...'}[/ref]"
                color: .1, .1, .1, 1
                size_hint: None, None
                size: self.texture_size
                font_size: '14sp'
                markup: True
                pos_hint: {'x': .03, 'top': .575}
                on_ref_press:
                    _screen.open_text(_screen.text)
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
                screen: _screen
                pos_hint: {'y': 0}
                size_hint: 1, .125
        BottomBar:
    BasicSpinner:
        id: _spinner
'''
)

class CommentPage(MDScreen):
    name = 'comment_page'
    username = StringProperty('') 
    user_image = StringProperty('') 
    text = StringProperty('') 
    code = StringProperty('') 
    comments = ListProperty([])
    liked = BooleanProperty()
    saved = BooleanProperty()
    likes = NumericProperty()
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.text_dialog = MDDialog(text="")
        self.snackbar = Snackbar(text="")
    
    def open_text(self, text):
        self.text_dialog.text = text
        self.text_dialog.open()
    
    async def _save_post(self):
        if self.saved: await un_save_post(self.code)
        else: await save_post(self.code) 
        self.saved = not self.saved
        self.manager.get_screen('posts_page').user_like_or_save_update(self.likes)
        self.snackbar.text = 'Post salvo'
        self.snackbar.open()
        self.ids._spinner.active = False
        
    def save_post(self):
        self.ids._spinner.active = True
        asyncio.ensure_future(self._save_post())
        
    def on_comments(self, a, b):
        self.rv.data = [{'username': x.split('-')[0], 'code': x.split('-')[1], 'size_hint_x': 1} for x in self.comments]
    
    def like_or_un_like(self):
        self.ids._spinner.active = True
        asyncio.ensure_future(self._like_or_un_like())
    
    async def _like_or_un_like(self):
        if self.liked:
            await user_un_like(self.parent.app.user['username'], self.code)
        else:
            await user_like(self.parent.app.user['username'], self.code)
        self.likes += -1 if self.liked else 1
        self.liked = not self.liked
        self.manager.get_screen('posts_page').user_like_or_save_update(self.likes)
        self.ids._spinner.active = False
    
    def comment(self, image_code):
        self.ids._spinner.active = True
        asyncio.ensure_future(self._comment(image_code))
        
    async def _comment(self, image_code):  
        await user_comment(self.parent.app.user['username'], self.code, image_code)
        self.comments = self.comments + [f"{self.parent.app.user['username']}-{image_code}"]
        self.ids._spinner.active = False
        
        
