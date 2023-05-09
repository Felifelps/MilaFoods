from kivy.uix import button, label, textinput
from kivy.lang import Builder

Builder.load_string('''
#:import join os.path.join
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

''')

