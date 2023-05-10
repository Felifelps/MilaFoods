from kivy.uix import button, label, textinput
from kivy.lang import Builder

Builder.load_string('''
#:import join os.path.join
#:import colors kivymd.color_definitions

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

<BasicListItem@TwoLineAvatarListItem>:
    canvas:
        Color:
            rgba: .9, .9, .9, 1
        Line:
            rounded_rectangle: (self.x, self.y, self.width, self.height, 10)
            width: 2
    font_name: join('views', 'data', 'Graduate-Regular.ttf')
    secondary_theme_text_color: 'Custom'
    secondary_text_color: colors['Amber']['300']

''')

