from kivymd.uix.list import TwoLineAvatarListItem, ImageLeftWidget
from kivymd.uix.menu import MDDropdownMenu
from kivy.animation import Animation
from kivy.uix.textinput import TextInput
from kivy.uix.image import Image
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.button import MDFillRoundFlatIconButton, MDIconButton, MDFlatButton
from kivymd.uix.relativelayout import MDRelativeLayout
from kivymd.uix.floatlayout import MDFloatLayout
from kivymd.uix.filemanager import MDFileManager
from kivymd.uix.snackbar import Snackbar
from kivymd.uix.dialog import MDDialog 
from kivymd.uix.pickers import MDDatePicker
from kivy.properties import StringProperty, ListProperty, BooleanProperty
from kivy.metrics import dp
from kivy.lang import Builder
from kivy.clock import Clock
from kivy.core.window import Window
from PIL import Image as PILImage
import os

Builder.load_string('''
#:import join os.path.join
#:import colors kivymd.color_definitions.colors
#:import user_image_was_loaded firebase.utils.user_image_was_loaded

<BasicSpinner@MDSpinner>:
    size_hint: None, None
    size: dp(46), dp(46)
    pos_hint: {'center_x': .5, 'center_y': .5}
    color: .5, .5, .5, 1
    active: False

<BasicLabel@Label>:
    font_name: join('views', 'data', 'Graduate-Regular.ttf')
    font_size: '12.5sp'
    size_hint: None, None
    size: self.texture_size

<BasicIconButton@MDRectangleFlatIconButton>:
    font_name: join('views', 'data', 'Graduate-Regular.ttf')
    line_color: 0, 0, 0, 0
    theme_text_color: "Custom"
    text_color: "black"
    theme_icon_color: "Custom"
    icon_color: "black"
    halign: 'left'

<FollowButton>:
    username: 'username'
    image_code: ''
    image: ''
    spacing: 2
    followed: False
    app: app
    DynamicSourceImage:
        pos_hint: {'x': 0, 'center_y': .5}
        size_hint: None, None
        size: dp(35), dp(35)
        pattern: '@'
        key: root.image
    MDLabel:
        id: _label
        text: root.username
        size_hint: .32 if root.followed else .38, 1
        color: 0, 0, 0, 1
        halign: 'left'
    BasicButton:
        text: 'Seguindo' if root.followed else 'Seguir'
        pos_hint: {'right': .95, 'center_y': .5}
        size_hint: .1, None
        
<MenuIconButton@MDIconButton>:
    editable: False
    theme_icon_color: 'Custom'
    icon_color: app.theme_cls.primary_color
    icon_size: '50sp'
    size_hint: None, None
    size: dp(80), dp(80)
    md_bg_color: 'white'
    MDFloatLayout:
        size: root.size
        pos: root.pos
        MDIconButton:
            icon: 'close'
            theme_icon_color: 'Custom'
            icon_color: 1, 1, 1, 1
            size_hint: .5, .5
            pos: (self.parent.right - dp(10), self.parent.top - dp(10)) if self.parent.parent.editable else (-100, -100) 
            icon_size: '15sp'
            md_bg_color: app.theme_cls.primary_color
            on_press:
                print('Close')
    
<BasicButton@MDRaisedButton>:
    font_name: join('views', 'data', 'Graduate-Regular.ttf')
    md_bg_color: app.theme_cls.primary_color
    theme_text_color: "Custom"
    text_color: .9, .9, .9, 1
    elevation: 0

<BasicTextInput>:
    type: ''
    background_color: .9, .9, .9, 1
    size_hint: .8, 0.06
    multiline: False
    font_size: '18sp'

<BasicListItem>:
    canvas:
        Color:
            rgba: .9, .9, .9, 1
        Line:
            rounded_rectangle: (self.x + dp(4), self.y + dp(4), self.width - dp(8), self.height - dp(8), 10)
            width: 2
    font_name: join('views', 'data', 'Graduate-Regular.ttf')
    secondary_theme_text_color: 'Custom'
    secondary_text_color: colors['Amber']['300']
    
<Background>:
    theme: app.theme_cls.primary_palette
    allow_stretch: True
    keep_ratio: False
    source: join('views', 'data', f'background_{self.theme}.png')

<BackgroundLogo@FloatLayout>:
    size_hint: 1, 1
    Background:
        size_hint: 1, 1
    Image:
        source: join('views', 'data', 'logo.png')
        pos_hint: {'center_x': .5, 'center_y': .8}
        size_hint: None, None
        size: dp(250), dp(250)

<EstabAccount@BasicListItem>:
    size_hint: 1, None
    height: dp(80)
    source: join('views', 'data', 'background_Red.png')
    estab_name: 'Username'
    estab_place: 'Rua do seu andré'
    text: root.estab_name
    secondary_text: root.estab_place
    src: root.source

<BasicDropDownItem>:
    items: []
    text: ""
    font_size: "18sp"
    icon: 'menu-swap'
    theme_text_color: 'Custom'
    line_color: 0, 0, 0, 0
    text_color: 'black'
    md_bg_color: .75, .75, .75, 0
    icon_color: 0, 0, 0, 1
    radius: [5, 5, 5, 5]

<BasicTextField@MDTextField>:
    color_mode: 'custom'
    line_color_focus: .8, .8, .8, 1
    text_color_normal: .8, .8, .8, 1
    text_color_focus: .8, .8, .8, 1
    font_size: "15sp"
    hint_text_color_focus: 0, 0, 0, 0
    hint_text_color_normal: 0, 0, 0, 0

<BottomMenu>:
    base_height: .6
    md_bg_color: .95, .95, .95, 1
    size_hint: 1, self.base_height
    pos_hint: {'y': -self.base_height}
    bg_opacity: 0
    canvas.before:
        Color:
            rgba: 0, 0, 0, self.bg_opacity
        Rectangle:
            pos: 0, 0
            size: self.width, self.height*(10*self.base_height)

<ShowImage>:
    bg_opacity: 0
    canvas.before:
        Color:
            rgba: 0, 0, 0, self.bg_opacity
        Rectangle:
            pos: 0, 0
            size: app.root.size

<CodeConfirmMenu@BottomMenu>:
    base_height: .5
    screen: None
    MDLabel:
        size_hint: .95, .35
        pos_hint: {'center_x': .5, 'top': 1}
        text: 'Olá\\nObrigado por se inscrever em nosso app!\\nPrecisamos apenas confirmar seu email.\\nInsira o código aqui.'
        theme_text_color: 'Custom'
        text_color: .3, .3, .3, 1
        font_size: '17.5sp'
    BasicTextInput:
        id: _code
        canvas.before:
            Color:
                rgba: .4, .4, .4, 1
            Line:
                rounded_rectangle: self.x, self.y, self.width, self.height, 10, 10, 10, 10
                width: 1.25
        size_hint: .95, .2
        pos_hint: {'center_x': .5, 'top': .65}
        background_color: 0, 0, 0, 0
        hint_text_color: .95, .95, .95, 1
        hint_text: 'Insira o código de confirmação'
        font_size: '18sp'
        padding_x: dp(15)
        padding_y: dp(18)
        input_filter: 'int'
        multiline: False
        type: 'code'
    Label:
        size_hint: .8, .125
        pos_hint: {'center_x': .5, 'top': .45}
        text: 'Pode demorar alguns minutos para você receber \\nseu código!'
        color: .6, .6, .6, 1
        font_size: '12.5sp'
        halign: 'justify'
    BasicButton:
        text: 'Verificar'
        size_hint: .5, .15
        pos_hint: {'center_x': .5, 'top': .315}
        font_size: '20sp'
        destiny: True
        on_release: root.screen.check_code(_code.text)
    Label:
        size_hint: .8, .125
        pos_hint: {'center_x': .5, 'top': .45}
        text: 'Pode demorar alguns minutos para você receber \\nseu código!'
        color: .6, .6, .6, 1
        font_size: '12.5sp'
        halign: 'justify'
    Label:
        size_hint: .8, .05
        pos_hint: {'center_x': .5, 'top': .1}
        text: 'Não recebeu seu código? [ref=reenviar][color=0000ff]Reenviar[/color][/ref]'
        markup: True
        color: .6, .6, .6, 1
        font_size: '12.5sp'
        on_ref_press: 
            root.screen.resend_code()

<LateralMenuBase>:
    id: _lm
    orientation: 'vertical'
    size_hint: .8, 1
    pos_hint: {'x': -2, 'top': 1}
    bg_opacity: 0
    canvas.before:
        Rectangle:
            pos: self.pos
            size: self.size
        Color:
            rgba: 0, 0, 0, self.bg_opacity
        Rectangle:
            pos: 0, 0
            size: self.width*1.25, self.height
            
<LateralMenu@LateralMenuBase>:
    id: lm
    app: app
    MDRelativeLayout:  
        md_bg_color: app.theme_cls.primary_dark
        size_hint: 1, .3
        pos_hint: {'top': 1}
        Image:
            source: join('views', 'data', 'label.png')
            pos_hint: {'x': 0, 'top': 1}
            size_hint: .4, .2
        MDIconButton:
            pos_hint: {'right': 1, 'top': 1}
            icon: "close"
            on_press: 
                lm.close()
        DynamicSourceImage:
            pos_hint: {'center_x': .5, 'center_y': .55}
            size_hint: None, None
            size: sp(75), sp(75)
            pattern: '@'
            key: join('views', 'data', 'user_images', app.user_image)
            on_press:
                app.root.load_profile_page()
        Label: 
            text: app.user['username']
            font_size: '20sp'
            pos_hint: {'center_x': .5, 'center_y': .25}
            size_hint: None, None
            size: self.texture_size
    MDStackLayout:  
        md_bg_color: 'white'
        size_hint: 1, .7
        pos_hint: {'top': .7}
        on_touch_down: root.close()
        BasicIconButton:
            text: "Background"            
            icon: "selection-multiple"
            size_hint: 1, .1
            on_press: 
                app.root.current = 'theme_config_page'
        BasicIconButton:
            text: "Editar perfil"            
            icon: "account"
            size_hint: 1, .1
            on_press: 
                app.root.load_user_edit_page('posts_page')
        BasicIconButton:
            text: "Salvos"            
            icon: "star"
            size_hint: 1, .1
            on_press: 
                app.root.current = 'saved_page'
        MDLabel:
            canvas: 
                Color:
                    rgb: 0, 0, 0
                Line:
                    points: 0, self.top, self.x + self.width, self.top
                    width: 1
            text: '  Outros'
            size_hint: 1, .1
            color: 0, 0, 0, 1
            font_name: join('views', 'data', 'Graduate-Regular.ttf')
        BasicIconButton:
            text: "Trocar de conta"            
            icon: "account-convert"
            size_hint: 1, .1
            on_press: 
                self.parent.parent.dialog.open()
        BasicIconButton:
            text: "Compartilhar"            
            icon: "share-variant"
            size_hint: 1, .1
        BasicIconButton:
            text: "Avalie-nos"            
            icon: "open-in-new"
            size_hint: 1, .1

<BarMenuButton@MDIconButton>:
    lm: None
    pos_hint: {'right': .975, 'center_y': .5}
    icon_size: '25sp'
    icon: "menu"
    on_press:
        self.lm.open()

<SelectImageButton>:
    on_press: self.file_manager.show(os.path.expanduser('~'))

<TopTitleBar@MDRelativeLayout>:
    title: ''
    lm: None
    canvas.before:
        Color: 
            rgba: 0, 0, 0, .4
        RoundedRectangle: 
            size: self.width, self.height + dp(4)
            pos: 0, -dp(4)
        Color: 
            rgba: 0, 0, 0, .2
        RoundedRectangle: 
            size: self.width, self.height + dp(7)
            pos: 0, -dp(7)
    pos_hint: {'top': 1}
    size_hint: 1, .1
    md_bg_color: app.theme_cls.primary_dark
    DynamicSourceImage:
        pos_hint: {'x': .035, 'center_y': .5}
        size_hint: None, None
        size: sp(40), sp(40)
        pattern: '@'
        key: join('views', 'data', 'user_images', app.user_image)
        on_press:
            app.root.load_profile_page()
    Label:
        text: root.title
        markup: True
        size_hint: None, None
        size: self.texture_size
        pos_hint: {'x': .2, 'center_y': .5}
        font_size: '25sp'   
    BarMenuButton:
        lm: root.lm

<TopImageBar@MDRelativeLayout>:
    lm: None
    np: None
    pa: None
    new_post: False
    canvas.before:
        Color: 
            rgba: 0, 0, 0, .4
        RoundedRectangle: 
            size: self.width, self.height + dp(4)
            pos: 0, -dp(4)
        Color: 
            rgba: 0, 0, 0, .2
        RoundedRectangle: 
            size: self.width, self.height + dp(7)
            pos: 0, -dp(7)
    pos_hint: {'top': 1}
    size_hint: 1, .1
    md_bg_color: app.theme_cls.primary_dark
    Image:
        source: join('views', 'data', 'label.png')
        pos_hint: {'center_x': .3, 'center_y': .5}
    MDIconButton:
        pos_hint: {'right': .85 if root.new_post else 0, 'center_y': .5}
        icon_size: '25sp'
        icon: "plus"
        on_press:
            root.np.open()
            root.pa.close()
    BarMenuButton:
        lm: root.lm

<DynamicSourceImage>:
    background: False
    canvas.before:
        Color:
            rgba: .5, .5, .5, 1 if self.background else 0
        Rectangle:
            size: self.size
            pos: self.pos

<TopImageAndStarBar@MDRelativeLayout>:
    screen: None
    saved: False
    canvas.before:
        Color: 
            rgba: 0, 0, 0, .4
        RoundedRectangle: 
            size: self.width, self.height + dp(4)
            pos: 0, -dp(4)
        Color: 
            rgba: 0, 0, 0, .2
        RoundedRectangle: 
            size: self.width, self.height + dp(7)
            pos: 0, -dp(7)
    pos_hint: {'top': 1}
    size_hint: 1, .1
    md_bg_color: app.theme_cls.primary_dark
    Image:
        source: join('views', 'data', 'label.png')
        pos_hint: {'center_x': .3, 'center_y': .5}
    MDIconButton:
        pos_hint: {'right': 1, 'center_y': .5}
        icon_size: '25sp'
        theme_icon_color: 'Custom'
        icon_color: (.75, .75, .75, 1) if not root.saved else (.85, .68, .21, 1)
        icon: "star"
        on_press:
            root.screen.save_post()
    
<BottomBar@MDRelativeLayout>:
    canvas.before:
        Color: 
            rgba: 0, 0, 0, .4
        RoundedRectangle: 
            size: self.width, self.height + dp(4)
            pos: 0, 0
        Color: 
            rgba: 0, 0, 0, .2
        RoundedRectangle: 
            size: self.width, self.height + dp(7)
            pos: 0, 0
    pos_hint: {'y': 0}
    size_hint: 1, .1
    md_bg_color: app.theme_cls.primary_dark
    MDIconButton:
        pos_hint: {'center_x': .25, 'center_y': .65}
        icon_size: '25sp'
        icon: "home-account"
        on_press:
            self.parent.parent.parent.manager.current = 'posts_page'
    Label:
        text: 'Início'
        pos_hint: {'center_x': .25, 'center_y': .3}
        font_size: '15sp'
    MDIconButton:
        pos_hint: {'center_x': .75, 'center_y': .65}
        icon_size: '25sp'
        icon: "star"
        on_press:
            self.parent.parent.parent.manager.current = 'saved_page'
    Label:
        text: 'Salvos'
        pos_hint: {'center_x': .75, 'center_y': .3}
        font_size: '15sp'

<Post>:
    username: 'Username'
    text: 'description'
    image: 'image.png'
    user_image: 'account-circle.png'
    timestamp: ''
    liked: False
    saved: False
    likes: 0
    size_hint: 1, None
    app: app
    canvas.before:
        Color:
            rgba: .98, .98, .98, 1
        Rectangle:
            size: self.width, self.height
            pos: 0, 0
    DynamicSourceImage:
        pos_hint: {'center_x': .085, 'center_y': .925}
        size_hint: None, None
        size: sp(32.5), sp(32.5)
        pattern: join('views', 'data', 'user_images', '@')
        key: root.user_image
    Label:
        text: root.username
        color: .1, .1, .1, 1
        size_hint: None, None
        size: self.texture_size
        font_size: '12sp'
        pos_hint: {'x': .16, 'center_y': .915}
    DynamicSourceImage:
        id: _img
        pos_hint: {'top': .85}
        size_hint: 1, .55
        background: True
        pattern: join('views', 'data', 'post_images', '@')
        key: root.image
    MDIconButton:
        pos_hint: {'center_x': .08, 'center_y': .78}
        theme_icon_color: 'Custom'
        icon_color: (.75, .75, .75, 1) if not root.saved else (.85, .68, .21, 1)
        icon: "star"
    MDIconButton:
        pos_hint: {'right': 1, 'top': .33}
        theme_icon_color: 'Custom'
        icon: "heart"
        icon_color: (.75, .75, .75, 1) if not root.liked else (1, 0, .2, 1)
    Label:
        text: str(root.likes)
        color: .1, .1, .1, 1
        size_hint: None, None
        size: self.texture_size
        font_size: '13sp'
        pos_hint: {'right': .85, 'center_y': .255}
    Label:
        text: root.text if len(root.text) < 41 else root.text[:40] + '...'
        halign: 'justify'
        color: .1, .1, .1, 1
        size_hint: None, None
        size: self.texture_size
        font_size: '14sp'
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

<SavedPost>:
    image: "image.png"
    username: ''
    text: ''
    id: '0'
    size_hint: None, None
    size: dp(130), dp(150)
    app: app
    canvas.before:
        Color:
            rgba: .9, .9, .9, 1
        Rectangle:
            size: self.width, self.height
            pos: 0, 0
    DynamicSourceImage:
        id: _img
        pos_hint: {'top': 1}
        size_hint: 1, .75
        background: True
        pattern: join('views', 'data', 'post_images', '@')
        key: root.image
        a: self.change_source()
    Label:
        text: root.username
        color: .1, .1, .1, 1
        size_hint: None, None
        size: self.texture_size
        font_size: '12sp'
        markup: True
        pos_hint: {'x': .05, 'center_y': .175}
    Label:
        text: root.text if len(root.text) < 22 else root.text[:22] + '...'
        color: .1, .1, .1, 1
        size_hint: None, None
        size: self.texture_size
        font_size: '10sp'
        pos_hint: {'x': .05, 'center_y': .075}

<CpfCnpjTextInput>:
    cpf: True
    text: ''
    date: 'Selecione sua data de nascimento'
    allow_date: True
    disabled: False
    BasicLabel:
        text: 'Digite seu CPF ou CNPJ'
        pos_hint: {'x': .12, 'center_y': .9}
        font_size: '12.5sp'
    BasicTextInput:
        id: _cpf 
        type: 'cpf'
        disabled: root.disabled
        on_text:
            root.text = self.text
        hint_text: 'Digite seu CPF'
        size_hint: .8, .3
        pos_hint: {'x': .1, 'center_y': (.65 if root.cpf else 10)}
    BasicTextInput:
        id: _cnpj
        type: 'cnpj'
        disabled: root.disabled
        on_text:
            root.text = self.text
            root.date = 'Selecione sua data de nascimento'
        hint_text: 'Digite seu CNPJ'
        size_hint: .8, .3
        pos_hint: {'x': .1, 'center_y': (.65 if not root.cpf else 10)}
    MDRaisedButton:
        id: _date
        text: root.date
        size_hint: .8, .3
        disabled: not root.cpf or root.disabled
        pos_hint: {'x': .1, 'center_y': (.25 if root.allow_date else 10)}
        on_release: root.date_picker()
    BasicDropDownItem:
        size_hint: .2, .1
        text: 'CPF'
        font_size: '12.5sp'
        pos_hint: {'right': .9, 'center_y': .65}
        items: ['CPF','CNPJ']
        disabled: root.disabled
        on_text:
            root.cpf = not root.cpf
''')

class DynamicSourceImage(Image):
    key = StringProperty('')
    pattern = '@.png'
    press = BooleanProperty(False)
    def on_key(self, a, b):
        self.change_source()
        
    def change_source(self):
        self.source = self.pattern.replace('@', self.key)
        self.reload()
    
    def on_touch_down(self, touch):
        if self.collide_point(*touch.pos): self.press = not self.press
        return super().on_touch_down(touch)
    
class BasicListItem(TwoLineAvatarListItem):
    src = StringProperty('')
    def on_src(self, a, b):
        if self.src != "": self.add_widget(ImageLeftWidget(source=self.src))
    
class Background(DynamicSourceImage):
    key = 'Red'
    pattern = 'background_@.png'

class BasicDropDownItem(MDFillRoundFlatIconButton):
    items = ListProperty([])
    def on_items(self, a, b):
        def set_text(text): self.text = text
        self.menu = MDDropdownMenu(
            caller=self,
            items=[
                {'viewclass': 'OneLineListItem', 'text': t, 'on_release': lambda text=t: set_text(text) == self.menu.dismiss(), 'text_color': (0, 0, 0, 1), 'theme_text_color': 'Custom'} for t in self.items
            ],
            ver_growth='down',
            position='auto',
            width_mult=4,
            max_height=dp(112),
            background_color=(0.75, 0.75, 0.75, 1)
        )
        
    def on_release(self):
        self.menu.open()

class BasicTextInput(TextInput):
    def insert_text(self, substring, from_undo=False):
        text = self.text + substring
        text_len = len(text)
        if self.type == 'cpf' and (text_len > 11 or not substring.isdigit()): 
            return False
        elif self.type == 'cnpj' and (text_len > 14 or not substring.isdigit()): 
            return False
        elif self.type == 'description' and (text_len > 300 or text.count('\n') > 7):
            return False
        elif self.type == 'code' and text_len > 5:
            return False
        elif self.type == 'number':
            if text_len > 15 or not substring.isdigit():
                return False
            elif text_len == 2:
                self.text = f'({text}) '
                return True
            elif text_len >= 9:
                text_list = list(text)
                if text_len <= 14 and '-' not in text:
                    text_list.insert(9, '-')
                elif text_len == 15:
                    text_list.pop(text_list.index('-'))
                    text_list.insert(10, '-')
                self.text = ''.join(text_list)
                return True
        return super().insert_text(substring, from_undo)
    
    def do_backspace(self, from_undo=False, mode='bkspc'):
        if self.text == '': return False
        if self.type == 'number':
            if self.text[-1] == ' ':
                self.text = self.text.replace('(', '').replace(') ', '')
            elif len(self.text) == 15:
                self.text = self.text.replace('-', '')
                text_list = list(self.text)
                text_list.insert(9, '-')
                self.text = ''.join(text_list)
            elif len(self.text) > 2 and self.text[-2] == '-':
                self.text = self.text.replace('-', '')
        return super().do_backspace(from_undo, mode)

class LateralMenuBase(MDBoxLayout):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.dialog = MDDialog(
            text='Quer mesmo trocar de conta?',
            buttons=[
                MDFlatButton(text='Cancelar', on_press=lambda: self.dialog.dismiss()),
                MDFlatButton(text='Sair', on_press=self.change_account)
            ]
        )
        self.open_animation = Animation(
            pos_hint={'x': 0}, 
            bg_opacity=0.5, 
            duration=0.1
        )
        self.close_animation = Animation(
            pos_hint={'x': -2}, 
            bg_opacity=0, 
            duration=0.1
        )

    def app_state(self, state):
        self.app.lateral_menu_is_active = state

    def change_account(self, *args):
        self.parent.parent.manager.logout()
        self.dialog.dismiss()
    
    def open(self): 
        self.open_animation.start(self)
        Clock.schedule_once(lambda dt: self.app_state(True), 0.1) 

    def close(self): 
        self.close_animation.start(self)
        Clock.schedule_once(lambda dt: self.app_state(False), 0.1)    

    def on_touch_down(self, touch):
        if not self.collide_point(*touch.pos) and self.app.lateral_menu_is_active: 
            self.close()
        return super().on_touch_down(touch)

class BottomMenu(MDRelativeLayout):
    def on_kv_post(self, base_widget):
        self.open_anim = Animation(pos_hint={'y': 0}, bg_opacity=0.75, duration=0.1)
        self.close_anim = Animation(pos_hint={'y': -self.base_height}, bg_opacity=0, duration=0.1)
    def open(self):
        self.open_anim.start(self)
    def close(self):
        self.close_anim.start(self)
    def on_touch_down(self, touch):
        if not self.collide_point(touch.x, touch.y):
            self.close()
        return super().on_touch_down(touch)
           
class SelectImageButton(DynamicSourceImage):
    pattern = '@'
    key = os.path.join(os.getcwd(), 'views', 'data', 'user_images', 'account-circle.png')
    def __init__(self, *args, **kwargs):
        self.file_manager = MDFileManager(
            exit_manager=self.exit_file_manager,
            select_path=self.select_path
        )
        super().__init__(*args, **kwargs)
    
    def select_path(self, path):
        try:
            a = PILImage.open(path)
            print(PILImage.isImageType(path))
            self.key = os.path.join(path)
            self.change_source()
            return self.file_manager.close()
        except Exception as e:
            print(e)
            Snackbar(text='Escolha uma imagem').open()
    
    def exit_file_manager(self, *args): 
        self.file_manager.close()
        
class Post(MDRelativeLayout):
    def on_touch_down(self, touch):
        if self.collide_point(*touch.pos) and not self.app.lateral_menu_is_active:
            if self.to_local(*touch.pos)[1] <= 255:
                self.app.root.load_comment_page(self.id, self.username, self.image, self.text, self.user_image)
            else:
                self.app.root.load_profile_page(self.username)
        return super().on_touch_down(touch)

class CpfCnpjTextInput(MDFloatLayout):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.picker = MDDatePicker()
        self.picker.bind(on_cancel=lambda a, b: self.picker.dismiss(), on_save=self.save_date)

    def date_picker(self):
        self.picker.open()
        
    def save_date(self, instance, value, date_range):
        self.date = value.strftime('%d/%m/%Y')
        self.picker.dismiss()
        
class SavedPost(MDRelativeLayout):
    def on_touch_down(self, touch):
        if self.collide_point(*touch.pos):
            self.app.root.load_comment_page(self.id, self.username, self.image, self.text, None)
        return super().on_touch_down(touch)

class FollowButton(MDBoxLayout):
    def on_touch_down(self, touch):
        if self.collide_point(*touch.pos):
            self.app.root.load_profile_page(self.username)
        return super().on_touch_down(touch)