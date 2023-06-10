from kivymd.uix.screen import MDScreen
from kivy.lang import Builder
from kivy.properties import BooleanProperty

Builder.load_string(
'''
#:import BasicButton views.utils
#:import BasicLabel views.utils
#:import BasicTextInput views.utils
#:import BasicDropDownItem views.utils
#:import Background views.utils
#:import SelectImageButton views.utils
#:import BasicDropDownItem views.utils
            
<UserAccountConfigurationPage>:
    id: _screen
    username: 'username'
    Background:
    RelativeLayout:
        MDIconButton:
            pos_hint: {'right': 1, 'top': 1}
            icon: "close"
            on_press:
                app.root.current = 'follow_estabs_page'
        SelectImageButton:
            pos_hint: {'center_x': .5 if not _screen.client else 10, 'center_y': .8}
            size_hint: .4, .2
            icon_size: '125sp'
        MDIconButton:
            pos_hint: {'center_x': .5 if _screen.client else 10, 'center_y': .8}
            size_hint: .4, .2
            icon_size: '125sp'
            icon: 'image'
            on_press:
                app.root.current = 'image_selection_page'
        BasicLabel:
            id: name
            text: _screen.username
            pos_hint: {'center_x': .5, 'center_y': .65}
            font_size: '25sp'
        BasicLabel:
            text: 'Bio'
            pos_hint: {'center_x': .5, 'center_y': .56}
            font_size: '18sp'
        BasicTextInput:
            pos_hint: {'center_x': .5, 'center_y': .51 if not _screen.client else .375}
            size_hint_y: .06 + (.25 if _screen.client else 0)
            hint_text: 'Crie uma bio'
            multiline: _screen.client
        BasicLabel:
            text: 'Número'
            pos_hint: {'center_x': .5 if not _screen.client else 10, 'center_y': .44}
            font_size: '18sp'
        BasicTextInput:
            pos_hint: {'center_x': .5 if not _screen.client else 10, 'center_y': .39}
        BasicLabel:
            text: 'Tipo de serviço'
            pos_hint: {'center_x': .5 if not _screen.client else 10, 'center_y': .31}
            font_size: '18sp'
        BasicDropDownItem:
            size_hint_x: .8
            pos_hint: {'center_x': .5 if not _screen.client else 10, 'center_y': .24}
        BasicButton:
            text: 'Definir'
            size_hint_x: .8
            pos_hint: {'center_x': .5, 'center_y': .15}
            on_press:
                app.root.current = 'follow_estabs_page'
'''
)

class UserAccountConfigurationPage(MDScreen):
    name = 'user_account_configuration_page'
    client = BooleanProperty()