from kivymd.uix.screen import MDScreen
from kivy.lang import Builder
from kivy.properties import BooleanProperty
from kivymd.uix.dialog import MDDialog
from kivymd.uix.snackbar import Snackbar
from control.control import get_user, save_user_data, update_user, upload_image

Builder.load_string('''
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
            id: _image_button
            pos_hint: {'center_x': .5 if not _screen.client else 10, 'center_y': .8}
            icon_size: '125sp'
        MDIconButton:
            pos_hint: {'center_x': .5 if _screen.client else 10, 'center_y': .8}
            icon_size: '125sp'
            icon: _screen.selected_image if not _screen.selected_image.isdigit() else join('views', 'data', 'profile_images', f'{int(_screen.selected_image)}.png')
            on_icon:
                self.icon = _screen.selected_image if not _screen.selected_image.isdigit() else join('views', 'data', 'profile_images', f'{int(_screen.selected_image)}.png')
                pos_hint: {'center_x': .5 if _screen.client else 10, 'center_y': .8}
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
            type: 'description'
            pos_hint: {'center_x': .5, 'center_y': .44 if not _screen.client else .375}
            size_hint_y: .16 + (.15 if _screen.client else 0)
            text: 'Sou novo no app!'
            hint_text: 'Crie uma bio'
            multiline: _screen.client
        BasicLabel:
            text: 'Número'
            pos_hint: {'center_x': .5 if not _screen.client else 10, 'center_y': .32}
            font_size: '18sp'
        BasicTextInput:
            id: _number
            pos_hint: {'center_x': .5 if not _screen.client else 10, 'center_y': .26}
            type: 'number'
            hint_text: '(XX) XXXXX-XXXX'
        BasicButton:
            text: 'Definir'
            size_hint_x: .8
            pos_hint: {'center_x': .5, 'center_y': .15}
            on_press:
                _screen.check_inputs()
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
    
    def check_inputs(self):
        if not self.client and self.ids._number.text != '' and len(self.ids._number.text) <= 14:
            return Snackbar(text='Número inválido!').open()
        self.dialog.open()
        
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
            upload_image(self.manager.app.user['username'], self.ids._image_button.icon if self.ids._image_button.icon not in ['account', 'image'] else None)
            update_user(
                self.manager.app.user['username'], 
                {
                    'tel': self.ids._number.text, 
                    'description': self.ids._bio.text
                }
            )
        save_user_data(get_user(self.manager.app.user['username']))
        self.dialog.dismiss()
        self.manager.app.update_user()
        self.manager.current = 'follow_estabs_page'
            