from kivymd.uix.screen import MDScreen
from kivy.lang import Builder
from kivy.properties import BooleanProperty
from kivymd.uix.snackbar import Snackbar
from kivymd.uix.button import MDIconButton
from control.control import update_user, upload_image
import asyncio

Builder.load_string('''
#:import BasicButton views.utils
#:import BasicLabel views.utils
#:import BasicTextInput views.utils
#:import BasicDropDownItem views.utils
#:import Background views.utils
#:import SelectImageButton views.utils
#:import BasicDropDownItem views.utils
#:import join os.path.join
#:import BasicSpinner views.utils
            
<UserAccountConfigurationPage>:
    id: _screen
    username: 'username'
    selected_image: 'image'
    bio: 'Sou novo no app!'
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
            icon_size: '125sp'
        ChangeableIcon:
            pos_hint: {'center_x': .5 if _screen.client else 10, 'center_y': .8}
            icon_size: '125sp'
            source: _screen.selected_image if not _screen.selected_image.isdigit() else join('views', 'data', 'profile_images', f'{int(_screen.selected_image)}.png')
            screen: _screen
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
            text: _screen.bio
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
    BasicSpinner:
        id: _spinner
'''
)

class ChangeableIcon(MDIconButton):
    def on_touch_down(self, touch):
        if self.collide_point(*touch.pos):
            self.screen.manager.get_screen('image_selection_page').back_to = self.screen.name
            self.screen.manager.current = 'image_selection_page'
        return super().on_touch_down(touch)

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
        if self.client:
            await update_user(
                self.manager.app.user['username'], 
                {
                    'image_code': self.selected_image, 
                    'description': self.ids._bio.text
                }
            )
        else:
            tel = ''
            for n in self.ids._number.text:
                if n.isdigit():
                    tel += n
            await upload_image(self.manager.app.user['username'], self.ids._image_button.icon if self.ids._image_button.icon not in ['account', 'image'] else None)
            await update_user(
                self.manager.app.user['username'], 
                {
                    'tel': tel, 
                    'description': self.ids._bio.text
                }
            )
        await self.manager.app.update_user(self.manager.app.user['username'])
        self.ids._spinner.active = False
        Snackbar(text='Alterações salvas com sucesso').open()
        self.manager.current = self.back_to
        
            