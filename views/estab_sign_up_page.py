from kivymd.uix.screen import MDScreen
from kivy.lang import Builder

Builder.load_string(
'''
#:import BasicButton views.utils
#:import BasicLabel views.utils
#:import BasicTextInput views.utils
#:import Background views.utils
#:import CodeConfirmMenu views.utils
            
<EstabSignUpPage>:
    BackgroundLogo:
    RelativeLayout:
        MDIconButton:
            pos_hint: {'center_x': .1, 'center_y': .6}
            theme_icon_color: 'Custom'
            icon_color: .9, .9, .9, 1
            icon: "arrow-left"
            on_press:
                app.root.current = 'client_or_estab_page'
        BasicLabel:
            text: 'Criar conta de empresa'
            pos_hint: {'center_x': .55, 'center_y': .6}
            font_size: '23sp'
        BasicLabel:
            text: 'Email'
            pos_hint: {'center_x': .175, 'center_y': .55}
        BasicTextInput:
            hint_text: 'exemplo@email.com'
            pos_hint: {'center_x': .5, 'center_y': .5}
        BasicLabel:
            text: 'Senha'
            pos_hint: {'center_x': .175, 'center_y': .45}
        BasicTextInput:
            id: password
            password: True
            password_mask: '*'
            pos_hint: {'center_x': .5, 'center_y': .4}
        MDIconButton:
            size_hint: 0.06, 0.06
            pos_hint: {'right': .875, 'center_y': .4}
            icon: "eye"
            theme_icon_color: "Custom"
            icon_color: .05, .05, .05, 1
            on_release:
                password.password = not password.password
                self.icon = 'eye' if password.password else 'eye-off'
        BasicLabel:
            text: 'Nome da empresa'
            pos_hint: {'center_x': .275, 'center_y': .35}
        BasicTextInput:
            pos_hint: {'center_x': .5, 'center_y': .3}
        CpfCnpjTextInput:
            pos_hint: {'center_x': .5, 'center_y': .225}
            size_hint: 1, .2
        BasicButton:
            text: 'Criar conta'
            size_hint_x: .8
            pos_hint: {'center_x': .5, 'center_y': .1}
            on_press:
                root.open()
        CodeConfirmMenu:
            id: _ccm
            posts: False
'''
)

class EstabSignUpPage(MDScreen):
    name = 'estab_sign_up_page'
    def open(self):
        self.ids._ccm.open(False)