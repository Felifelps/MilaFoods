from kivymd.uix.screen import MDScreen
from kivy.lang import Builder
from os.path import join

Builder.load_string(
'''
#:import join os.path.join
<BasicLabel@Label>:
    font_name: join('views', 'data', 'Graduate-Regular.ttf')
    font_size: '12.5sp'
    
<BasicButton@MDRaisedButton>:
    font_name: join('views', 'data', 'Graduate-Regular.ttf')

<ClientOrEstabPage>:
    Image:
        source: join('views', 'data', 'background.png')
    RelativeLayout:
        BasicLabel:
            text: 'Entrar como: '
            pos_hint: {'center_x': .5, 'center_y': .6}
            font_size: '25sp'
        BasicLabel:
            text: 'Empresa'
            pos_hint: {'center_x': .175, 'center_y': .525}
        BasicButton:
            text: 'Entrar como empresa'
            size_hint_x: .8
            pos_hint: {'center_x': .5, 'center_y': .5}
        BasicLabel:
            text: 'Cliente'
            pos_hint: {'center_x': .175, 'center_y': .41}
        BasicButton:
            text: 'Entrar como cliente'
            size_hint_x: .8
            pos_hint: {'center_x': .5, 'center_y': .38}
'''
)

class ClientOrEstabPage(MDScreen):
    name = 'clent_or_estab_page'