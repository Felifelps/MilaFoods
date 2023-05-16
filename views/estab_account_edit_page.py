from kivymd.uix.screen import MDScreen
from kivy.lang import Builder

Builder.load_string(
'''
#:import BasicButton views.utils
#:import BasicLabel views.utils
#:import BasicTextField views.utils
#:import BasicDropDownItem views.utils
#:import TopBar views.utils
#:import Background views.utils
#:import join os.path.join
            
<EstabAccountEditPage>:
    Background:
    FloatLayout:
        MDTopAppBar:
            title: ""
            pos_hint: {'top': 1}
            font_name: join('views', 'data', 'Graduate-Regular.ttf')
            right_action_items: [['close', lambda x: print('opa')]]
        Image:
            source: join('views', 'data', 'label.png')
            pos_hint: {'x': .03, 'center_y': .9425}
            size_hint: .4, .3
        BasicButton:
            text: 'Editar\\nCardápio'
            font_size: '12sp'
            size_hint: .1, .05
            pos_hint: {'right': .975, 'center_y': .835}
        MDIconButton:
            pos_hint: {'center_x': .5, 'center_y': .7}
            icon: "account-circle"
            icon_size: '125sp'
        BasicLabel:
            text: 'Alterar Imagem'
            pos_hint: {'center_x': .5, 'center_y': .56}
            font_size: '25sp'
        BasicLabel:
            text: 'Nome'
            pos_hint: {'center_x': .09, 'center_y': .48}
            font_size: '17.5sp'
        BasicTextField:
            size_hint: .96, .12 
            pos_hint: {'center_x': .5, 'center_y': .42} 
        BasicLabel:
            text: 'Biografia'
            pos_hint: {'center_x': .15, 'center_y': .35}
            font_size: '17.5sp'
        BasicTextField:
            size_hint: .96, .12 
            pos_hint: {'center_x': .5, 'center_y': .29} 
        BasicLabel:
            text: 'Número'
            pos_hint: {'center_x': .125, 'center_y': .22}
            font_size: '17.5sp'
        BasicTextField:
            size_hint: .96, .12 
            pos_hint: {'center_x': .5, 'center_y': .16} 
        

'''
)

class EstabAccountEditPage(MDScreen):
    name = 'estab_account_edit_page'