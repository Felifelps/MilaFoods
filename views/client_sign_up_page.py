from kivymd.uix.screen import MDScreen
from kivymd.uix.snackbar import Snackbar
from control.control import sign_up_and_login_client, send_email_code, check_client_sign_up_inputs
from kivy.lang import Builder
from kivy.clock import Clock
from kivymd.uix.dialog import MDDialog
import asyncio

Builder.load_string('''
#:import BasicButton views.utils
#:import BasicLabel views.utils
#:import BasicTextInput views.utils
#:import Background views.utils
#:import CodeConfirmMenu views.utils
#:import BasicSpinner views.utils

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
            disabled: _spinner.active
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
            disabled: _spinner.active
        BasicLabel:
            text: 'Email'
            pos_hint: {'center_x': .175, 'center_y': .45}
        BasicTextInput:
            id: _email
            hint_text: 'exemplo@email.com'
            pos_hint: {'center_x': .5, 'center_y': .4}
            disabled: _spinner.active
        BasicLabel:
            text: 'Senha'
            pos_hint: {'center_x': .175, 'center_y': .35}
        BasicTextInput:
            id: _password
            hint_text: "minhaSenha1!"
            password: True
            password_mask: '*'
            pos_hint: {'center_x': .5, 'center_y': .3}
            disabled: _spinner.active
        MDIconButton:
            size_hint: 0.06, 0.06
            pos_hint: {'right': .875, 'center_y': .3}
            icon: "eye"
            theme_icon_color: "Custom"
            icon_color: .05, .05, .05, 1
            disabled: _spinner.active
            on_release:
                _password.password = not _password.password
                self.icon = 'eye' if _password.password else 'eye-off'
        BasicButton:
            text: 'Criar conta'
            size_hint_x: .8
            pos_hint: {'center_x': .5, 'center_y': .2175}
            disabled: _spinner.active
            on_press:
                _screen.check_inputs(_username.text, _email.text, _password.text)
        CodeConfirmMenu:
            id: _ccm
            screen: _screen
    BasicSpinner:
        id: _spinner
'''
)

class ClientSignUpPage(MDScreen):
    name = 'client_sign_up_page'
    times = 0
    def on_pre_enter(self, *args):
        for i in self.textinputs: i.text = ''
        return super().on_pre_enter(*args)
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fail_connection_dialog = MDDialog(text='Falha de conexão, tente novamente :(')
        
    def check_if_code_is_done(self):
        self.ids._spinner.active = False
        if not self.code.done():
            return self.fail_connection_dialog.open()
        Snackbar(text='Código enviado').open()
        self.ids._ccm.open()
    
    def send_code(self):
        self.ids._spinner.active = True
        self.code = asyncio.ensure_future(send_email_code(self.data[1]))
        self.code.add_done_callback(lambda a: self.check_if_code_is_done())
        Clock.schedule_once(lambda a: self.check_if_code_is_done(), 300)
        
    async def _check_inputs(self, username, email, password):
        valid = await check_client_sign_up_inputs(username, email, password)
        if isinstance(valid, str): 
            return Snackbar(text=valid).open()
        self.data = [username, email, password]
        Snackbar(text='Enviando código...').open()
        self.send_code()

    def check_inputs(self, username, email, password):
        asyncio.ensure_future(self._check_inputs(username, email, password))
    
    def resend_code(self):
        self.check_inputs(*self.data)
    
    def check_code(self, code):
        asyncio.ensure_future(self._check_code(code))
        
    async def _check_code(self, code):
        if str(self.code.result()) == code:
            self.ids._spinner.active = True
            client = await sign_up_and_login_client(*self.data)
            if not client:
                return Snackbar(text='Credenciais inválidas').open()
            await self.manager.app.update_user(client['username'])
            self.manager.load_client_pages()
            self.manager.load_user_config_page('follow_estabs_page')
            self.ids._spinner.active = False
            return Snackbar(text='Conta criada!').open()
        Snackbar(text='Código errado').open()
        
        