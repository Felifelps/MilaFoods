from kivymd.uix.screen import MDScreen
from kivy.lang import Builder
from kivymd.uix.snackbar import Snackbar
from kivy.clock import Clock
from control.firebase_to_local import check_username_and_password

Builder.load_string(
'''
#:import BasicButton views.utils
#:import BasicLabel views.utils
#:import BasicTextInput views.utils
#:import Background views.utils

<ClientLoginPage>:
    id: _screen
    textinputs: [_username, _password]
    BackgroundLogo:
    RelativeLayout:
        id: _rel
        MDIconButton:
            pos_hint: {'center_x': .1, 'center_y': .6}
            theme_icon_color: 'Custom'
            icon_color: .9, .9, .9, 1
            icon: "arrow-left"
            on_press:
                app.root.current = 'client_or_estab_page'
        BasicLabel:
            text: 'Login de cliente'
            pos_hint: {'center_x': .525, 'center_y': .6}
            font_size: '25sp'
        BasicLabel:
            text: 'Username'
            pos_hint: {'x': .1, 'center_y': .525}
        BasicTextInput:
            id: _username
            hint_text: 'Digite seu username'
            pos_hint: {'center_x': .5, 'center_y': .475}
        BasicLabel:
            text: 'Senha'
            pos_hint: {'center_x': .175, 'center_y': .41}
        BasicTextInput:
            id: _password
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
                _password.password = not _password.password
                self.icon = 'eye' if _password.password else 'eye-off'
        BasicButton:
            text: 'Entrar'
            size_hint_x: .8
            pos_hint: {'center_x': .5, 'center_y': .26}
            on_press:
                _screen.login_client(_username.text, _password.text)
                _username.text = ''
                _password.text = ''
        BasicLabel:
            text: 'Esqueceu a senha?'
            pos_hint: {'center_x': .5, 'center_y': .075}
        BasicLabel:
            text: 'Não tem uma conta? [color=#0000ff][ref=create_account]Crie aqui!![/ref][/color]'
            pos_hint: {'center_x': .5, 'center_y': .025}
            markup: True
            on_ref_press:
                app.root.current = 'client_sign_up_page'
'''
)
class ClientLoginPage(MDScreen):
    name = 'client_login_page'
    def on_pre_enter(self, *args):
        for i in self.textinputs: i.text = ''
        return super().on_pre_enter(*args)
    def login_client(self, username, password):
        client = check_username_and_password(username, password)
        if isinstance(client, str): return Snackbar(text=client).open()
        self.manager.app.update_user()
        Snackbar(text='Logado com sucesso').open()
        self.manager.load_client_pages()
        self.manager.current = 'posts_page'
    