from kivymd.uix.screen import MDScreen
from kivy.lang import Builder

Builder.load_string(
'''
#:import BasicButton views.utils
#:import BasicLabel views.utils
#:import BasicTextInput views.utils
#:import BasicDropDownItem views.utils
#:import Background views.utils
            
<EstabAccountConfigurationPage>:
    Background:
    RelativeLayout:
        MDIconButton:
            pos_hint: {'right': 1, 'top': 1}
            icon: "close"
        MDIconButton:
            pos_hint: {'center_x': .5, 'center_y': .8}
            icon: "account-circle"
            icon_size: '125sp'
        BasicLabel:
            id: name
            text: '[Name]'
            pos_hint: {'center_x': .5, 'center_y': .65}
            font_size: '25sp'
        BasicLabel:
            text: 'Localização'
            pos_hint: {'center_x': .5, 'center_y': .56}
            font_size: '18sp'
        BasicTextInput:
            pos_hint: {'center_x': .5, 'center_y': .51}
        BasicLabel:
            text: 'Número'
            pos_hint: {'center_x': .5, 'center_y': .44}
            font_size: '18sp'
        BasicTextInput:
            pos_hint: {'center_x': .5, 'center_y': .39}
        BasicLabel:
            text: 'Tipo de serviço'
            pos_hint: {'center_x': .5, 'center_y': .31}
            font_size: '18sp'
        BasicDropDownItem:
            size_hint_x: .8
            pos_hint: {'center_x': .5, 'center_y': .24}
        BasicButton:
            text: 'Definir'
            size_hint_x: .8
            pos_hint: {'center_x': .5, 'center_y': .15}
'''
)

class EstabAccountConfigurationPage(MDScreen):
    name = 'estab_account_configuration_page'