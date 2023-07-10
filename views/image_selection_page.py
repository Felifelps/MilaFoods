from kivymd.uix.screen import MDScreen
from kivy.lang import Builder

Builder.load_string('''
#:import BasicLabel views.utils
#:import Background views.utils
#:import join os.path.join

<ProfileImageButton@MDIconButton>:
    code: '1'
    icon_size: '115sp'
    icon: join('views', 'data', 'user_images', f'{self.code}.png')
    on_press:
        self.parent.screen.back(self.code)

<ImageSelectionPage>:
    id: _screen
    back_to: 'user_account_configuration_page'
    Background:
        id: _bg
    RelativeLayout:
        MDTopAppBar:
            title: "Escolha uma foto de perfil"
            font_name: join('views', 'data', 'Graduate-Regular.ttf')
            left_action_items: [['arrow-left', lambda x: self.parent.parent.back()]]
            pos_hint: {'top': 1}
            icon_color: .9, .9, .9, 1
            headline_text_color: .9, .9, .9, 1
        ScrollView:
            pos_hint: {'center_x': .5, 'top': .85}
            size_hint: .9, .9
            MDStackLayout:
                id: _stack
                adaptive_height: True
                spacing: 10, 20
                screen: _screen
                ProfileImageButton:
                ProfileImageButton:
                    code: '2'
                ProfileImageButton:
                    code: '3'
                ProfileImageButton:
                    code: '4'
                ProfileImageButton:
                    code: '5'
                ProfileImageButton:
                    code: '6'
                ProfileImageButton:
                    code: '7'
                ProfileImageButton:
                    code: '8'
                ProfileImageButton:
                    code: '9'
                ProfileImageButton:
                    code: '10'
                ProfileImageButton:
                    code: '11'
                ProfileImageButton:
                    code: '12'
                ProfileImageButton:
                    code: '13'
                ProfileImageButton:
                    code: '14'
                ProfileImageButton:
                    code: '15'
'''
)
class ImageSelectionPage(MDScreen):
    name = 'image_selection_page'  
    def back(self, icon='account-circle'):
        self.manager.get_screen(self.back_to).selected_image = f'{icon}.png'
        self.manager.current = self.back_to