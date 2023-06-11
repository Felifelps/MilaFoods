from kivymd.uix.screen import MDScreen
from kivy.lang import Builder
from kivy.properties import BooleanProperty
from kivymd.uix.dialog import MDDialog
from control.control import get_user, save_user_data, update_user, upload_image

Builder.load_string(
'''
#:import BasicButton views.utils
#:import BasicLabel views.utils
#:import BasicTextInput views.utils
#:import BasicDropDownItem views.utils
#:import Background views.utils
#:import SelectImageButton views.utils
#:import BasicDropDownItem views.utils
#:import join os.path.join
            
<UserAccountConfigurationPage>:
    id: _screen
    username: 'username'
    selected_image: 'image'
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
            icon_size: '125sp'
            icon: _screen.selected_image if not _screen.selected_image.isdigit() else join('views', 'data', 'profile_images', f'{int(_screen.selected_image)}.png')
            on_press:
                app.root.get_screen('image_selection_page').back_to = _screen.name
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
            id: _bio
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
                _screen.dialog.open()
'''
)

class UserAccountConfigurationPage(MDScreen):
    name = 'user_account_configuration_page'
    client = BooleanProperty(False)
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.dialog = MDDialog(
            text='Salvando suas definições...',
            on_open=lambda a: self.save_definitions()
        )
    
    def save_definitions(self):
        if self.client:
            update_user(
                self.manager.app.user['username'], 
                {
                    'image_code': self.selected_image, 
                    'description': self.ids._bio.text
                }
            )
        else:
            upload_image(self.manager.app.user['username'], self.icon if self.icon not in ['account', 'image'] else None)
        save_user_data(get_user(self.manager.app.user['username']))
        self.dialog.dismiss()
        self.manager.app.update_user()
        self.manager.current = 'follow_estabs'
            