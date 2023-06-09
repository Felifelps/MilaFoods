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
from kivy.properties import StringProperty, ListProperty
from kivy.metrics import dp
from kivy.lang import Builder
import os

Builder.load_string('''
#:import join os.path.join
#:import colors kivymd.color_definitions.colors

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

<ProfileButton@MDIconButton>:
    image: 'None'
    username: 'Username'
    icon: 'account-circle' if app.user['image_code'] == "0" else join('views', 'data', 'profile_images', f"{app.user['image_code']}.png")
    icon_size: '50sp'
    on_press:
        app.root.current = 'client_profile_page'
        
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
    items: ['Lanches','Salgados','Pizzaria']
    text: "Escolha seu serviço"
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
    TextInput:
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
            print('reenviar')

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
                _lm.close()
        MDIconButton:
            icon: 'account-circle' if app.user['image_code'] == "0" else join('views', 'data', 'profile_images', f"{app.user['image_code']}.png")
            icon_size: '75sp'
            on_press:
                app.root.load_profile_page()
            pos_hint: {'center_x': .5, 'center_y': .55}
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
                app.root.current = 'estab_account_edit_page'
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
            text: "Carrinho"            
            icon: "cart"
            size_hint: 1, .1
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
    avatar: True
    icon: 'account' if self.avatar else 'image'
    icon_theme_color: 'Primary' if self.avatar else 'Custom'
    md_bg_color: .3, .3, .3, 3
    on_press: self.file_manager.show('C://')

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
    MDIconButton:
        icon: 'account-circle' if app.user['image_code'] == "0" else join('views', 'data', 'profile_images', f"{app.user['image_code']}.png")
        on_press:
            app.root.load_profile_page()
        pos_hint: {'x': .025, 'center_y': .5}
        icon_size: '40sp'
    Label:
        text: f'[b]{root.title}[/b]'
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
        pos_hint: {'right': .85 if root.np != None else 0, 'center_y': .5}
        icon_size: '25sp'
        icon: "plus"
        on_press:
            root.np.open()
    BarMenuButton:
        lm: root.lm

<TopImageAndStarBar@MDRelativeLayout>:
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
        icon: "star"
        on_press:
            print('Save')

<TopCentralSearchBar@MDRelativeLayout>:
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
    MDIconButton:
        pos_hint: {'x': .025, 'center_y': .5}
        icon_size: '40sp'
        icon: 'account-circle' if app.user['image_code'] == "0" else join('views', 'data', 'profile_images', f"{app.user['image_code']}.png")
        on_press:
            app.root.load_profile_page()
    MDTextField:
        color_mode: 'custom'
        line_color_focus: .8, .8, .8, 1
        text_color_normal: .8, .8, .8, 1
        text_color_focus: .8, .8, .8, 1
        font_size: "13sp"
        hint_text: "Pesquisar"
        hint_text_color_focus: .8, .8, .8, 0.5
        hint_text_color_normal: .8, .8, .8, 0.5
        size_hint: .6, 1
        pos_hint: {'center_x': .5, 'center_y': .5}
        on_focus:
            app.root.current = 'search_page'
    MDIconButton:
        pos_hint: {'x': .7, 'center_y': .5}
        icon: "magnify" 
        on_press:
            app.root.current = 'search_page'
    BarMenuButton:
        lm: root.lm

<TopActiveSearchBar@MDRelativeLayout>:
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
    MDTextField:
        color_mode: 'custom'
        line_color_focus: .8, .8, .8, 1
        text_color_normal: .8, .8, .8, 1
        text_color_focus: .8, .8, .8, 1
        font_size: "13sp"
        hint_text: "Pesquisar"
        hint_text_color_focus: .8, .8, .8, 0.5
        hint_text_color_normal: .8, .8, .8, 0.5
        size_hint: .5, 1
        pos_hint: {'x': .125, 'center_y': .5}
    MDIconButton:
        pos_hint: {'x': 0, 'center_y': .5}
        icon: "magnify"
    BasicButton:
        text: 'Cancelar'
        size_hint: .1, .2
        pos_hint: {'right': .975, 'center_y': .5}
        font_size: '10sp'
        md_bg_color: app.theme_cls.primary_dark
        on_press:
            app.root.current = 'posts_page'
    
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
    image: join('views', 'data', 'logo.png')
    timestamp: ''
    id: 0
    liked: False
    likes: 0
    size_hint: 1, None
    manager: app.root
    canvas.before:
        Color:
            rgba: .98, .98, .98, 1
        Rectangle:
            size: self.width, self.height
            pos: 0, 0
    MDIconButton:
        pos_hint: {'center_x': .085, 'center_y': .925}
        icon_size: '35sp'
        theme_icon_color: 'Custom'
        icon_color: .1, .1, .1, 1
        icon: "account-circle" if root.image == 'None' else root.image
        on_press:
            root.manager.load_estab_profile_page(root.username)
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
        source: join('views', 'data', 'logo.png') if root.image == 'None' else root.image
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
        text: root.text
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

<SavedPost@RelativeLayout>:
    image: _img
    username: 'Username'
    size_hint: None, None
    size: dp(130), dp(150)
    canvas.before:
        Color:
            rgba: .9, .9, .9, 1
        Rectangle:
            size: self.width, self.height
            pos: 0, 0
    Image:
        id: _img
        pos_hint: {'top': 1}
        size_hint: 1, .75
    Label:
        text: root.username
        color: .1, .1, .1, 1
        size_hint: None, None
        size: self.texture_size
        font_size: '12sp'
        markup: True
        pos_hint: {'x': .05, 'center_y': .175}
    Label:
        text: '[Nome estab]'
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
    BasicLabel:
        text: 'Digite seu CPF ou CNPJ'
        pos_hint: {'x': .12, 'center_y': .9}
        font_size: '12.5sp'
    BasicTextInput:
        id: _cpf 
        type: 'cpf'
        on_text:
            root.text = self.text
        hint_text: 'Digite seu CPF'
        size_hint: .8, .3
        pos_hint: {'x': .1, 'center_y': (.65 if root.cpf else 10)}
    BasicTextInput:
        id: _cnpj
        type: 'cnpj'
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
        disabled: not root.cpf
        pos_hint: {'x': .1, 'center_y': (.25 if root.allow_date else 10)}
        on_release: root.date_picker()
    BasicDropDownItem:
        size_hint: .2, .1
        text: 'CPF'
        font_size: '12.5sp'
        pos_hint: {'right': .9, 'center_y': .65}
        items: ['CPF','CNPJ']
        on_text:
            root.cpf = not root.cpf
''')

class BasicListItem(TwoLineAvatarListItem):
    src = StringProperty('')
    def on_src(self, a, b):
        if self.src != "": self.add_widget(ImageLeftWidget(source=self.src))
    
class Background(Image):
    theme = StringProperty('Red')
    def on_theme(self, a, b):
        self.source = f'background_{self.theme}.png'
        self.reload()

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
        if self.type == 'cpf' and (len(self.text) + len(substring) > 11 or not substring.isdigit()): 
            return False
        elif self.type == 'cnpj' and (len(self.text) + len(substring) > 14 or not substring.isdigit()): 
            return False
        return super().insert_text(substring, from_undo)
    
    def paste(self):
        return super().paste()

class LateralMenuBase(MDBoxLayout):
    open_animation = Animation(pos_hint={'x': 0}, bg_opacity=0.5, duration=0.1)
    close_animation = Animation(pos_hint={'x': -2}, bg_opacity=0, duration=0.1)
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.dialog = MDDialog(
            text='Quer mesmo trocar de conta?',
            buttons=[
                MDFlatButton(text='Cancelar', on_press=lambda: self.dialog.dismiss()),
                MDFlatButton(text='Sair', on_press=self.change_account)
            ]
        )
        
    def change_account(self, *args):
        self.parent.parent.manager.logout()
        self.dialog.dismiss()
    
    def open(self): 
        self.open_animation.start(self)

    def close(self): 
        self.close_animation.start(self)

    def on_touch_down(self, touch):
        if not self.collide_point(*touch.pos): 
            self.close()
        return super().on_touch_down(touch)

class BottomMenu(MDRelativeLayout):
    def on_kv_post(self, base_widget):
        self.open_anim = Animation(pos_hint={'y': 0}, bg_opacity=0.5, duration=0.1)
        self.close_anim = Animation(pos_hint={'y': -self.base_height}, bg_opacity=0, duration=0.1)
    def open(self):
        self.open_anim.start(self)
    def close(self):
        self.close_anim.start(self)
    def on_touch_down(self, touch):
        if not self.collide_point(touch.x, touch.y):
            self.close()
        return super().on_touch_down(touch)
           
class SelectImageButton(MDIconButton):
    def __init__(self, *args, **kwargs):
        self.file_manager = MDFileManager(
            exit_manager=self.exit_file_manager,
            select_path=self.select_path
        )
        super().__init__(*args, **kwargs)
        
    def select_path(self, path):
        for extension in ['png', 'jpg']:
            if extension in path: 
                self.icon = os.path.join(path) 
                return self.file_manager.close()
        Snackbar(text='Escolha uma imagem').open()
    
    def exit_file_manager(self, *args): 
        self.file_manager.close()
        
class Post(MDRelativeLayout):
    def on_touch_down(self, touch):
        if self.collide_point(*touch.pos):
            self.manager.load_view_post_page(self.id, self.username, self.image, self.text, [])
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