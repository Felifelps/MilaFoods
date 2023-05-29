from kivymd.uix.screen import MDScreen
from kivy.lang import Builder

Builder.load_string(
'''
#:import BasicButton views.utils
#:import BasicLabel views.utils
#:import BasicTextInput views.utils
#:import Background views.utils
#:import CodeConfirmMenu views.utils

<ClientSignUpPage>:
    BackgroundLogo:
    RelativeLayout:
        BasicLabel:
            text: 'Criar conta de cliente'
            pos_hint: {'center_x': .5, 'center_y': .6}
            font_size: '25sp'
        BasicLabel:
            text: 'Nome'
            pos_hint: {'center_x': .175, 'center_y': .55}
        BasicTextInput:
            hint_text: 'Digite seu nome'
            pos_hint: {'center_x': .5, 'center_y': .5}
        BasicLabel:
            text: 'Email'
            pos_hint: {'center_x': .175, 'center_y': .45}
        BasicTextInput:
            hint_text: 'exemplo@email.com'
            pos_hint: {'center_x': .5, 'center_y': .4}
        BasicLabel:
            text: 'Senha'
            pos_hint: {'center_x': .175, 'center_y': .35}
        BasicTextInput:
            id: password
            hint_text: "minhaSenha1!"
            password: True
            password_mask: '*'
            pos_hint: {'center_x': .5, 'center_y': .3}
        MDIconButton:
            size_hint: 0.06, 0.06
            pos_hint: {'right': .875, 'center_y': .3}
            icon: "eye"
            theme_icon_color: "Custom"
            icon_color: .05, .05, .05, 1
            on_release:
                password.password = not password.password
                self.icon = 'eye' if password.password else 'eye-off'
        BasicButton:
            text: 'Criar conta'
            size_hint_x: .8
            pos_hint: {'center_x': .5, 'center_y': .2175}
            on_press:
                root.open()
        BasicLabel:
            text: 'Ou use suas redes sociais'
            pos_hint: {'center_x': .5, 'center_y': .16}
        BasicButton:
            text: 'Instagram'
            size_hint_x: .3
            pos_hint: {'right': .9, 'center_y': .1}
        BasicButton:
            text: 'Facebook'
            size_hint_x: .3
            pos_hint: {'x': .1, 'center_y': .1}
        CodeConfirmMenu:
            id: _ccm
'''
)

class ClientSignUpPage(MDScreen):
    name = 'client_sign_up_page'
    def open(self):
        self.ids._ccm.open()