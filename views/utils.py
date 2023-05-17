from kivymd.uix.list import TwoLineAvatarListItem, ImageLeftWidget
from kivymd.uix.menu import MDDropdownMenu
from kivy.uix.textinput import TextInput
from kivy.uix.image import Image
from kivymd.uix.button import MDFillRoundFlatIconButton
from kivy.properties import StringProperty, ListProperty
from kivy.metrics import dp
from kivy.lang import Builder

Builder.load_string('''
#:import join os.path.join
#:import colors kivymd.color_definitions.colors

<BasicLabel@Label>:
    font_name: join('views', 'data', 'Graduate-Regular.ttf')
    font_size: '12.5sp'
    size_hint: None, None
    size: self.texture_size
    
<BasicButton@MDRaisedButton>:
    font_name: join('views', 'data', 'Graduate-Regular.ttf')

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
    
<BasicDropDownItem>:
    items: ['Lanches','Salgados','Pizzaria']
    text: "Escolha seu serviço"
    font_size: "18sp"
    icon: 'menu-swap'
    theme_text_color: 'Custom'
    line_color: 0, 0, 0, .8
    text_color: 'black'
    md_bg_color: .75, .75, .75, 1
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

<TopTitleBar@MDRelativeLayout>:
    title: ''
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
        icon: "account-circle"
    Label:
        text: f'[b]{root.title}[/b]'
        markup: True
        size_hint: None, None
        size: self.texture_size
        pos_hint: {'x': .2, 'center_y': .5}
        font_size: '25sp'
    MDIconButton:
        pos_hint: {'right': .975, 'center_y': .5}
        icon_size: '25sp'
        icon: "menu"

<TopImageBar@MDRelativeLayout>:
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
        pos_hint: {'right': .975, 'center_y': .5}
        icon_size: '25sp'
        icon: "menu"

<TopSearchBar@MDRelativeLayout>:
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
        icon: "account-circle"
    MDTextField:
        color_mode: 'custom'
        line_color_focus: .8, .8, .8, 1
        text_color_normal: .8, .8, .8, 1
        text_color_focus: .8, .8, .8, 1
        font_size: "13sp"
        hint_text_color_focus: 0, 0, 0, 0
        hint_text_color_normal: 0, 0, 0, 0
        size_hint: .6, 1
        pos_hint: {'center_x': .5, 'center_y': .5}
    MDIconButton:
        pos_hint: {'x': .7, 'center_y': .5}
        icon: "magnify"
    MDIconButton:
        pos_hint: {'right': .975, 'center_y': .5}
        icon_size: '25sp'
        icon: "menu"

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
    Label:
        text: 'Início'
        pos_hint: {'center_x': .25, 'center_y': .3}
        font_size: '15sp'
    MDIconButton:
        pos_hint: {'center_x': .75, 'center_y': .65}
        icon_size: '25sp'
        icon: "star"
    Label:
        text: 'Salvos'
        pos_hint: {'center_x': .75, 'center_y': .3}
        font_size: '15sp'

<Post@RelativeLayout>:
    username: 'Username'
    post_title: 'title'
    description: 'description'
    image: _img
    size_hint: 1, None
    height: dp(275)
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
        source: 'close'
    MDIconButton:
        pos_hint: {'center_x': .08, 'center_y': .78}
        theme_icon_color: 'Custom'
        icon_color: .75, .75, .75, 1
        icon: "star"
        clicked: False
        on_release:
            self.icon_color = (.75, .75, .75, 1) if self.clicked else (.2, .2, .2, 1)
            self.clicked = not self.clicked
    MDIconButton:
        pos_hint: {'right': .9, 'top': .28}
        theme_icon_color: 'Custom'
        icon: "heart"
        icon_color: .75, .75, .75, 1
        clicked: False
        on_release:
            self.icon_color = (.75, .75, .75, 1) if self.clicked else (.2, .2, .2, 1)
            self.clicked = not self.clicked
    MDIconButton:
        pos_hint: {'right': 1, 'top': .28}
        theme_icon_color: 'Custom'
        icon: "message-outline"
        icon_color: .1, .1, .1, 1
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
        pos_hint: {'x': .03, 'top': .19}
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
        if self.type == 'cpf' and (len(self.text) >= 11 or not substring.isdigit()): 
            return False
        elif self.type == 'cnpj' and (len(self.text) >= 14 or not substring.isdigit()): 
            return False
        return super().insert_text(substring, from_undo)