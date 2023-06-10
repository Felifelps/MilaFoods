from kivymd.uix.screen import MDScreen
from kivy.lang import Builder

Builder.load_string(
'''
#:import TopTitleBar views.utils
#:import BottomBar views.utils
#:import BasicLabel views.utils
#:import Background views.utils
#:import LateralMenu views.utils
#:import join os.path.join
#:import SavedPost views.utils

            
<SavedPage>:
    Background:
    FloatLayout:
        TopTitleBar:
            id: bar
            lm: _lm
            title: "[Username]"
            icon_size: '25sp'
        MDIconButton:
            icon: 'star'
            icon_size: '50sp'
            pos_hint: {'center_x': .125, 'center_y': .8}
        BasicLabel:
            text: 'Salvos'
            font_size: '30sp'
            pos_hint: {'center_x': .375, 'center_y': .8}
        BasicLabel:
            id: number
            text: 'Você tem {} imagens salvas'
            #font_size: '30sp'
            pos_hint: {'center_x': .375, 'center_y': .73}
        ScrollView:
            pos_hint: {'center_x': .5, 'top': .7}
            size_hint: .8, .55
            MDStackLayout:
                id: _stack
                adaptive_height: True
                spacing: 10, 20
                SavedPost:
                SavedPost:
                SavedPost:
                SavedPost:
                SavedPost:
                SavedPost:
                SavedPost:
                SavedPost:
        BottomBar:
        LateralMenu:
            id: _lm
'''
)

class SavedPage(MDScreen):
    name = 'saved_page'
    