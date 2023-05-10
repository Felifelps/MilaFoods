from kivymd.uix.screen import MDScreen
from kivy.lang import Builder

Builder.load_string(
'''
#:import BasicButton views.utils
#:import BasicLabel views.utils
#:import BasicTextInput views.utils
#:import Background views.utils

<ClientLoginPage>:
    BackgroundLogo:
    RelativeLayout:
        BasicLabel:
            text: 'Login de cliente'
            pos_hint: {'center_x': .5, 'center_y': .6}
            font_size: '25sp'
        BasicLabel:
            text: 'Email'
            pos_hint: {'center_x': .175, 'center_y': .525}
        BasicTextInput:
            hint_text: 'exemplo@email.com'
            pos_hint: {'center_x': .5, 'center_y': .475}
        BasicLabel:
            text: 'Senha'
            pos_hint: {'center_x': .175, 'center_y': .41}
        BasicTextInput:
            id: password
            hint_text: "minhaSenha1!"
            password: True
            password_mask: '*'
            pos_hint: {'center_x': .5, 'center_y': .36}
        MDIconButton:
            size_hint: 0.06, 0.06
            pos_hint: {'right': .875, 'center_y': .36}
            icon: "eye"
            theme_icon_color: "Custom"
            icon_color: .05, .05, .05, 1
            on_release:
                password.password = not password.password
                self.icon = 'eye' if password.password else 'eye-off'
        BasicButton:
            text: 'Entrar'
            size_hint_x: .8
            pos_hint: {'center_x': .5, 'center_y': .26}
        BasicLabel:
            text: 'Ou use suas redes sociais'
            pos_hint: {'center_x': .5, 'center_y': .21}
        BasicButton:
            text: 'Instagram'
            size_hint_x: .3
            pos_hint: {'right': .9, 'center_y': .145}
        BasicButton:
            text: 'Facebook'
            size_hint_x: .3
            pos_hint: {'x': .1, 'center_y': .145}
        BasicLabel:
            text: 'Esqueceu a senha?'
            pos_hint: {'center_x': .5, 'center_y': .075}
        BasicLabel:
            text: 'Não tem uma conta? Crie aqui!!'
            pos_hint: {'center_x': .5, 'center_y': .025}
'''
)

class ClientLoginPage(MDScreen):
    name = 'client_login_page'