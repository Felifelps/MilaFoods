from kivymd.uix.screen import MDScreen
from kivy.lang import Builder

Builder.load_string(
'''
#:import BasicButton views.utils
#:import BasicLabel views.utils
#:import BasicTextInput views.utils
#:import Background views.utils
            
<EstabAccountConfigurationPage>:
    Background:
    RelativeLayout:
        MDIconButton:
            pos_hint: {'right': 1, 'top': 1}
            icon: "close"
        BasicLabel:
            text: 'Criar conta de empresa'
            pos_hint: {'center_x': .5, 'center_y': .6}
            font_size: '23sp'
        BasicLabel:
            text: 'Nome da empresa'
            pos_hint: {'center_x': .275, 'center_y': .35}
        BasicTextInput:
            pos_hint: {'center_x': .5, 'center_y': .3}
        BasicLabel:
            text: 'CPF ou CNPJ'
            pos_hint: {'center_x': .225, 'center_y': .25}
        BasicTextInput:
            pos_hint: {'center_x': .5, 'center_y': .2}
        BasicButton:
            text: 'Criar conta'
            size_hint_x: .8
            pos_hint: {'center_x': .5, 'center_y': .1}
'''
)

class EstabAccountConfigurationPage(MDScreen):
    name = 'estab_account_configuration_page'