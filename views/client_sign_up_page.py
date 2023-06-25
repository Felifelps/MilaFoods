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
            text: 'cavalo'
            hint_text: 'Digite seu username'
            pos_hint: {'center_x': .5, 'center_y': .5}
            disabled: _spinner.active
        BasicLabel:
            text: 'Email'
            pos_hint: {'center_x': .175, 'center_y': .45}
        BasicTextInput:
            id: _email
            text: 'felipefelipe23456@gmail.com'
            hint_text: 'exemplo@email.com'
            pos_hint: {'center_x': .5, 'center_y': .4}
            disabled: _spinner.active
        BasicLabel:
            text: 'Senha'
            pos_hint: {'center_x': .175, 'center_y': .35}
        BasicTextInput:
            id: _password
            text: 'felipe'
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
    MDSpinner:
        id: _spinner
        size_hint: None, None
        size: dp(46), dp(46)
        pos_hint: {'center_x': .5, 'center_y': .5}
        color: .5, .5, .5, 1
        active: False
        elevation: 2
    
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
        def test_time():
            self.times += 1
            print(self.code)
            print(f'waiting: {self.times*5} seconds')
        self.code_function = lambda dt: test_time() if not isinstance(self.code, int) else Clock.unschedule(self.code_function) == self.code_send()
    
    def send_code(self):
        self.ids._spinner.active = True
        self.code = asyncio.ensure_future(send_email_code(self.data[1]))
        self.times = 0
        Clock.schedule_interval(self.code_function, 5)
        
    def code_send(self):
        self.ids._spinner.active = False
        Snackbar(text='Código enviado').open()
        if not self.code:
            return MDDialog(
                text='Falha de conexão, tente novamente :('
            ).open()
        self.ids._ccm.open()
        
    async def _check_inputs(self, username, email, password):
        valid = await check_client_sign_up_inputs(username, email, password)
        if isinstance(valid, str): 
            return Snackbar(text=valid).open()
        self.data = [username, email, password]
        Snackbar(text='Enviando código...').open()
        self.send_code()

    def check_inputs(self, username, email, password):
        asyncio.ensure_future(self._check_inputs(username, email, password))
    
    async def resend_code(self): 
        await self._check_inputs(*self.data)
        
    async def check_code(self, code):
        if str(self.code) == code:
            client = await sign_up_and_login_client(*self.data)
            if not client:
                return Snackbar(text='Credenciais inválidas').open()
            await self.manager.app.update_user(client['username'])
            self.manager.load_client_pages()
            self.manager.load_user_config_page(True)
            return Snackbar(text='Conta criada!').open()
        Snackbar(text='Código errado').open()
        
        