from kivymd.uix.screen import MDScreen
from kivy.lang import Builder
from kivy.properties import BooleanProperty
from kivymd.uix.snackbar import Snackbar
from kivy.uix.image import Image
from control.control import update_user, upload_image
import asyncio, os

Builder.load_string('''
#:import BasicButton views.utils
#:import BasicLabel views.utils
#:import BasicTextInput views.utils
#:import BasicDropDownItem views.utils
#:import Background views.utils
#:import SelectImageButton views.utils
#:import BasicDropDownItem views.utils
#:import join os.path.join
#:import getcwd os.getcwd
#:import BasicSpinner views.utils
#:import DynamicSourceImage views.utils
            
<UserAccountConfigurationPage>:
    id: _screen
    username: 'account-circle'
    selected_image: 'account-circle.png'
    Background:
    RelativeLayout:
        MDIconButton:
            pos_hint: {'right': 1, 'top': 1}
            icon: "close"
            on_press:
                app.root.current = _screen.back_to
        SelectImageButton:
            id: _image_button
            pos_hint: {'center_x': .5 if not _screen.client else 10, 'center_y': .8}
            size_hint: None, None
            size: sp(100), sp(100)
            pattern: '@'
            key: join(getcwd(), 'views', 'data', 'user_images', _screen.selected_image)
        DynamicSourceImage:
            pos_hint: {'center_x': .5 if _screen.client else 10, 'center_y': .8}
            size_hint: None, None
            size: sp(125), sp(125)
            pattern: '@'
            key: join(getcwd(), 'views', 'data', 'user_images', _screen.selected_image)
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
            multiline: True
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
    BasicSpinner:
        id: _spinner
'''
)

class UserAccountConfigurationPage(MDScreen):
    name = 'user_account_configuration_page'
    client = BooleanProperty(False)
    back_to = 'follow_estabs_page'
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
    
    def check_inputs(self):
        if not self.client and self.ids._number.text != '' and len(self.ids._number.text) <= 14:
            return Snackbar(text='Número inválido!').open()
        self.ids._spinner.active = True
        asyncio.ensure_future(self._save_definitions())
        
    async def _save_definitions(self):
        try:
            if self.client:
                await update_user(
                    self.manager.app.user['username'], 
                    {
                        'image': self.selected_image, 
                        'description': self.ids._bio.text
                    }
                )
            else:
                await upload_image(self.manager.app.user['username'], self.ids._image_button.key)
                await update_user(
                    self.manager.app.user['username'], 
                    {
                        'tel': self.ids._number.text, 
                        'description': self.ids._bio.text
                    }
                )
            await self.manager.app.update_user(self.manager.app.user['username'])
            Snackbar(text='Alterações salvas com sucesso').open()
            self.manager.current = self.back_to
        except Exception as e:
            print(e)
            Snackbar(text='Um erro ocorreu! Tente novamente mais tarde.').open()
        self.ids._spinner.active = False
            
        
            