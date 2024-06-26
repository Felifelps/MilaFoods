from kivymd.uix.screen import MDScreen
from kivymd.uix.relativelayout import MDRelativeLayout
from kivy.animation import Animation
from kivy.lang import Builder
from control.control import get_user_posts, get_user, user_follow, user_un_follow, post
from kivymd.uix.dialog import MDDialog
from views.utils import DynamicSourceImage
from kivymd.uix.snackbar import Snackbar
from kivy.metrics import dp
import webbrowser, asyncio, os, json

Builder.load_string('''
#:import BasicLabel views.utils
#:import Background views.utils
#:import BasicButton views.utils
#:import BasicTextField views.utils
#:import BasicTextInput views.utils
#:import TopImageBar views.utils
#:import BottomBar views.utils
#:import LateralMenu views.utils
#:import Post views.utils
#:import BottomMenu views.utils
#:import SelectImageButton views.utils
#:import BasicSpinner views.utils
#:import join os.path.join

<NewPost@BottomMenu>:
    screen: None
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
        id: _image_button
        size_hint: 1.5, .4
        pos_hint: {'center_x': .5, 'top': .85}
        pattern: '@'
        key: join('views', 'data', 'post_images', 'image.png')
        a: self.change_source()
    BasicTextInput:
        id: _textinput
        type: 'description'
        size_hint: 1, .2
        pos_hint: {'center_x': .5, 'top': .45}
        font_size: '18.25sp'
        hint_text: 'Escreva uma legenda'
        multiline: True
    BasicButton:
        size_hint: .8, .2
        pos_hint: {'center_x': .5, 'center_y': .125}
        text: 'Publicar'
        font_size: '15sp'
        on_press:
            root.screen.check_new_post(_textinput.text, _image_button.source)

<PostsArea>:
    rv: _rv
    loading: _loading
    screen: None
    size_hint: 1, .4
    pos_hint: {'top': .4}
    scroll_view_blur: 0
    username: ''
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
        elevation: 0
        on_press: 
            app.root.current = 'menu_page'
    MDScrollViewRefreshLayout:
        id: _refresh_layout
        size_hint: 1, 2
        pos_hint: {'top': .675}
        refresh_callback: lambda *args: root.screen.refresh_user_posts() == self.refresh_done()
        root_layout: root
        canvas.before:
            Color:
                rgba: 0, 0, 0, root.scroll_view_blur
            Rectangle:
                size: self.width, self.height*2
                pos: self.x, self.y
        RecycleView:
            id: _rv
            viewclass: 'Post'
            RecycleBoxLayout:
                orientation: 'vertical'
                default_size: None, dp(56)
                default_size_hint: 1, None
                size_hint_y: None
                height: self.minimum_height
                spacing: dp(10)
    BasicLabel:
        text: f'{"Sua" if root.username == app.username else "Esta"} conta não tem publicações\\nainda :('
        font_size: '15sp'
        pos_hint: {'center_x': .5 if _loading.active == False and _rv.data == [] else 10, 'center_y': .5} 
    BasicSpinner:
        id: _loading

<EstabProfilePage>:
    id: _screen
    username: app.user['username']
    description: app.user['description']
    image: app.user_image
    n_of_followers: app.user['n_of_followers']
    n_of_posts: app.user['n_of_posts']
    tel: str(app.user['tel'])
    following: False
    app: app
    pa: _pa
    np: _np
    show: False
    on_username:
        self.get_loaded_posts()
    Background:
        id: _bg
    RelativeLayout:
        TopImageBar:
            lm: _lm
            np: _np
            pa: _pa
            new_post: _screen.username == app.user['username']
        MDFloatLayout:
            pa: _pa
            Label:
                text: _screen.username
                font_size: '25sp'
                size_hint: None, None
                size: self.texture_size
                pos_hint: {'x': .05, 'center_y': .625}
            Label:
                text: _screen.format_description(_screen.description)
                font_size: '14sp'
                size_hint: None, None
                size: self.texture_size
                pos_hint: {'x': .05, 'top': .575}
            BasicButton:
                size_hint_x: .275
                pos_hint: {'center_x': .5, 'center_y': .69 if _screen.username == app.user['username'] else .7}
                text: 'Editar\\nperfil' if _screen.username == app.user['username'] else ('Seguindo' if _screen.following else 'Seguir')
                a: list(map(lambda x: x - 0.2 if x != 1 else 1, app.theme_cls.primary_dark))
                md_bg_color: list(map(lambda x: x - 0.2 if x != 1 else 1, app.theme_cls.primary_dark)) if _screen.following else app.theme_cls.primary_dark
                on_press:
                    _screen.left_button_action()
            BasicButton:
                size_hint_x: .275
                pos_hint: {'right': .98, 'center_y': .7}
                text: 'Whatsapp'
                md_bg_color: app.theme_cls.primary_dark
                on_press:
                    _screen.open_zap()
            Label:
                text: f'[size=20sp]{_screen.n_of_posts}[/size]\\nPublicações'
                halign: 'center'
                markup: True
                font_size: '12.5sp'
                size_hint: None, None
                size: self.texture_size
                pos_hint: {'center_x': .5, 'center_y': .775}
            Label:
                text: f'[size=20sp]{_screen.n_of_followers}[/size]\\nSeguidores'
                halign: 'center'
                markup: True
                font_size: '12.5sp'
                size_hint: None, None
                size: self.texture_size
                pos_hint: {'center_x': .82, 'center_y': .775}
            ShowImage:
                id: _image
                pos_hint: {'x': .04, 'center_y': .75}
                size_hint: None, None
                size: sp(85), sp(85)
                pattern: '@'
                key: root.image
                screen: _screen
            PostsArea:
                id: _pa
                username: _screen.username
                screen: _screen
        BottomBar:
        LateralMenu:
            id: _lm
        NewPost:
            id: _np
            screen: _screen
    BasicSpinner:
        id: _spinner
'''
)

class EstabProfilePage(MDScreen):
    name = 'estab_profile_page'
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.unregistered_dialog = MDDialog(text='Esta conta não tem número cadastrado')
        self.loaded_posts = {}

    def format_description(self, description):
        text = description
        lines = []
        for i in range(len(description)//48):
            if (i + 1)*48 < len(description):
                lines.append(text[i*48: (i + 1)*48 ])
            else:
                lines.append(text[i*48:])
        if len(description) > 48:
            last_space_index = text[:48].rfind(' ')
            if last_space_index == -1:
                text = description[:48] + '\n' + description[48:]
            else:
                text = text[:last_space_index] + '\n' + text[last_space_index + 1:]
        return text
        
    def refresh_user_posts(self):
        self.loaded_posts.pop(self.username)
        self.load_posts()
        self.pa.ids._refresh_layout.refresh_done()
        
    def get_loaded_posts(self):
        self.pa.ids._loading.active = True
        if self.username not in self.loaded_posts.keys():
            self.load_posts()
        else:
            self.pa.rv.data = self.loaded_posts[self.username]
        self.pa.ids._loading.active = False
        
    def on_enter(self, *args):
        if self.loaded_posts == {}:
            self.loaded_posts[self.manager.app.username] = self.manager.app.posts
        self.get_loaded_posts()
        self.pa.loading.active = False
        return super().on_pre_enter(*args)

    def on_leave(self, *args):
        self.pa.close()
        self.np.close()
        self.ids._image.close()
        return super().on_leave(*args)
    
    def left_button_action(self):
        if self.username == self.app.username:
            self.manager.load_user_edit_page('posts_page')
        else:
            self.follow()
    
    def follow(self):
        self.ids._spinner.active = True
        asyncio.ensure_future(self._follow())
        
    async def _follow(self):
        if self.following:
            await user_un_follow(self.app.username, self.username)
        else:
            await user_follow(self.app.username, self.username)
        self.following = not self.following
        self.n_of_followers += 1 if self.following else -1
        self.ids._spinner.active = False
    
    def load_posts(self):
        self.pa.loading.active = True
        asyncio.ensure_future(self._load_posts())
        self.pa.loading.active = False
        
    async def _load_posts(self):
        user_data = await get_user(self.username)
        self.pa.rv.data = []
        if user_data['posts'] == []: return
        data = []
        for post in await get_user_posts(self.username):
            post.update({
                'height': 300,
                'liked': f'{post["username"]}-{post["id"]}' in user_data['liked'],
                'saved': f'{post["username"]}-{post["id"]}' in user_data['saved']
            })
            data.append(post)
        self.pa.rv.data = data
        self.show = not self.pa.rv.data == []
        self.loaded_posts[self.username] = self.pa.rv.data
    
    def check_new_post(self, text, image_path):
        asyncio.ensure_future(self._check_new_post(text, image_path))
        
    async def _check_new_post(self, text, image_path):
        self.ids._spinner.active = True
        try:
            await post(self.manager.app.username, text, image_path)
            Snackbar(text='Post publicado com sucesso!').open()
            self.np.ids._textinput.text = ''
            self.np.ids._image_button.key = os.path.join('views', 'data', 'post_images', 'image.png')
            self.np.ids._image_button.change_source()
            self.np.close()
            await self.manager.app.update_user(self.manager.app.user['username'])
            self.loaded_posts[self.manager.app.username] = self.manager.app.posts
        except:
            Snackbar(text='Um erro ocorreu! Tente novamente').open()
        self.ids._spinner.active = False
    
    def open_zap(self):
        if len(self.tel) < 10:
            return self.unregistered_dialog.open()
        webbrowser.open('https://wa.me/55' + "".join(filter(lambda x: x.isdigit(), self.tel)))
        
class ShowImage(DynamicSourceImage):
    opened = False
    def on_kv_post(self, base_widget):
        self.parent_obj = self.parent
        self.starter_size = self.size[0]
        self.starter_hint = self.pos_hint
        self.open_anim = Animation(size=(dp(310), dp(310)), pos_hint={'center_y': .5}, bg_opacity=0.75, duration=0.1)
        self.close_anim = Animation(size=(self.starter_size, self.starter_size), pos_hint=self.starter_hint, bg_opacity=0, duration=0.1)
    def open(self):
        self.parent_obj.remove_widget(self)
        self.parent_obj.add_widget(self)
        self.open_anim.start(self)
        self.opened = True
    def close(self):
        pa = self.parent_obj.pa
        self.parent_obj.remove_widget(pa)
        self.parent_obj.add_widget(pa)
        self.close_anim.start(self)
        self.opened = False
    def on_touch_down(self, touch):
        if not self.collide_point(touch.x, touch.y) or self.opened:
            self.close()
        else:
            self.open()
        return super().on_touch_down(touch)
    
class PostsArea(MDRelativeLayout):
    up_anim = Animation(pos_hint={'top': .9}, duration=0.1, scroll_view_blur=0.75)
    down_anim =  Animation(pos_hint={'top': .4}, duration=0.1, scroll_view_blur=0)
    def open(self):
        self.up_anim.start(self)

    def close(self):
        self.down_anim.start(self)

    def on_touch_down(self, touch):
        if self.collide_point(*touch.pos) and touch.spos[1] > .8 and self.pos_hint['top'] == .9 and not self.ids.menu_button.collide_point(*touch.pos):
            self.close()
        elif self.collide_point(*touch.pos) and self.pos_hint['top'] == .4 and not self.ids.menu_button.collide_point(*touch.pos):
            self.open()
        return super().on_touch_down(touch)
