from kivymd.uix.screen import MDScreen
from kivy.lang import Builder
from os.path import join

Builder.load_string(
'''
#:import BasicButton views.utils
#:import BasicLabel views.utils
#:import Background views.utils

<ClientOrEstabPage>:
    BackgroundLogo:
    RelativeLayout:
        BasicLabel:
            text: 'Entrar como: '
            pos_hint: {'center_x': .5, 'center_y': .575}
            font_size: '25sp'
        BasicLabel:
            text: 'Empresa'
            pos_hint: {'center_x': .175, 'center_y': .5}
        BasicButton:
            text: 'Entrar como empresa'
            size_hint_x: .8
            pos_hint: {'center_x': .5, 'center_y': .425}
        BasicLabel:
            text: 'Cliente'
            pos_hint: {'center_x': .175, 'center_y': .35}
        BasicButton:
            text: 'Entrar como cliente'
            size_hint_x: .8
            pos_hint: {'center_x': .5, 'center_y': .275}
'''
)

class ClientOrEstabPage(MDScreen):
    name = 'clent_or_estab_page'