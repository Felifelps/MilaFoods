from kivymd.uix.list import TwoLineAvatarListItem, ImageLeftWidget
from kivymd.uix.menu import MDDropdownMenu
from kivy.uix.image import Image
from kivymd.uix.button import MDFillRoundFlatIconButton
from kivy.properties import StringProperty
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

<BasicTextInput@TextInput>:
    background_color: .9, .9, .9, 1
    size_hint: .8, 0.06
    multiline: False
    font_size: '18sp'

<BasicListItem>:
    canvas:
        Color:
            rgba: .9, .9, .9, 1
        Line:
            rounded_rectangle: (self.x + dp(1.5), self.y + dp(1.5), self.width - dp(3), self.height - dp(3), 10)
            width: 2
    font_name: join('views', 'data', 'Graduate-Regular.ttf')
    secondary_theme_text_color: 'Custom'
    secondary_text_color: colors['Amber']['300']
    
<Background>:
    allow_stretch: True
    keep_ratio: False
    source: join('views', 'data', f'background_{self.theme}.png')

<BackgroundLogo@Image>:
    Background:
    Image:
        source: join('views', 'data', 'logo.png')
        pos: root.pos[0] + root.width*0.5 - dp(137.5), root.pos[1] + root.height*0.775 - dp(137.5)
        size: dp(275), dp(275)
    
<BasicDropDownItem>:
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
    types = [
        'Lanches',
        'Salgados',
        'Pizzaria'
    ]
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        def set_text(text): self.text = text
        self.menu = MDDropdownMenu(
            caller=self,
            items=[
                {'viewclass': 'OneLineListItem', 'text': t, 'on_release': lambda text=t: set_text(text) == self.menu.dismiss(), 'text_color': (0, 0, 0, 1), 'theme_text_color': 'Custom'} for t in self.types
            ],
            ver_growth='down',
            position='auto',
            width_mult=4,
            max_height=dp(112),
            background_color=(0.75, 0.75, 0.75, 1)
        )
        
    def on_release(self):
        self.menu.open()