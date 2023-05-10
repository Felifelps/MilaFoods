from kivymd.uix.list import TwoLineAvatarListItem, ImageLeftWidget
from kivy.properties import StringProperty
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
    
<Background@Image>:
    source: join('views', 'data', 'background_Red.png')

<BackgroundLogo@Image>:
    source: join('views', 'data', 'background_logo_Red.png')

''')

class BasicListItem(TwoLineAvatarListItem):
    src = StringProperty('')
    def on_src(self, a, b):
        if self.src != "": self.add_widget(ImageLeftWidget(source=self.src))
