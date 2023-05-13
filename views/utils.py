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