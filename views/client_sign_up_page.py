from kivymd.uix.screen import MDScreen
from kivymd.uix.snackbar import Snackbar
from control.firebase_to_local import check_username_email_and_password, send_email_code, sign_up_and_login_new_client
from kivy.lang import Builder
from kivymd.uix.dialog import MDDialog

Builder.load_string(
'''
#:import BasicButton views.utils
#:import BasicLabel views.utils
#:import BasicTextInput views.utils
#:import Background views.utils
#:import CodeConfirmMenu views.utils

<ClientSignUpPage>:
    id: _screen
    textinputs: [_username, _email, _password]
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
            text: 'Criar conta de\\ncliente'
            halign: 'center'
            pos_hint: {'center_x': .5, 'center_y': .6}
            font_size: '25sp'
        BasicLabel:
            text: 'Username'
            pos_hint: {'x': .1, 'center_y': .55}
        BasicTextInput:
            id: _username
            hint_text: 'Digite seu username'
            pos_hint: {'center_x': .5, 'center_y': .5}
        BasicLabel:
            text: 'Email'
            pos_hint: {'center_x': .175, 'center_y': .45}
        BasicTextInput:
            id: _email
            hint_text: 'exemplo@email.com'
            pos_hint: {'center_x': .5, 'center_y': .4}
        BasicLabel:
            text: 'Senha'
            pos_hint: {'center_x': .175, 'center_y': .35}
        BasicTextInput:
            id: _password
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
                _password.password = not _password.password
                self.icon = 'eye' if _password.password else 'eye-off'
        BasicButton:
            text: 'Criar conta'
            size_hint_x: .8
            pos_hint: {'center_x': .5, 'center_y': .2175}
            on_press:
                _screen.check_inputs(_username.text, _email.text, _password.text)
        CodeConfirmMenu:
            id: _ccm
            screen: _screen
'''
)

class ClientSignUpPage(MDScreen):
    name = 'client_sign_up_page'
    def on_pre_enter(self, *args):
        for i in self.textinputs: i.text = ''
        return super().on_pre_enter(*args)
    
    def send_code(self):
        self.dialog.dismiss()
        self.code = send_email_code(self.data[1])
        if not self.code:
            return MDDialog(
                text='Falha de conexão, tente novamente :('
            ).open()
        self.ids._ccm.open()
        
    def check_inputs(self, username, email, password):
        valid = check_username_email_and_password(username, email, password)
        if isinstance(valid, str): 
            return Snackbar(text=valid).open()
        self.data = [username, email, password]
        self.dialog = MDDialog(
            text='Enviando código...',
            on_open=lambda x: self.send_code()
        )
        self.dialog.open()
        
    def check_code(self, code):
        if str(self.code) == code:
            client = sign_up_and_login_new_client(*self.data)
            if not client:
                return Snackbar(text='Credenciais inválidas').open()
            self.manager.app.update_user()
            self.manager.load_client_pages()
            self.manager.current = 'posts_page'
            return Snackbar(text='Logado com sucesso').open()
        Snackbar(text='Código errado').open()
        
        