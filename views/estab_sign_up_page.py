from kivymd.uix.screen import MDScreen
from kivy.lang import Builder
from kivy.clock import Clock
from kivymd.uix.snackbar import Snackbar
from kivymd.uix.dialog import MDDialog
from control.control import check_estab_sign_up_inputs, send_email_code, send_validate_cpf_or_cnpj_email, sign_up_estab
import asyncio

Builder.load_string('''
#:import BasicButton views.utils
#:import BasicLabel views.utils
#:import BasicTextInput views.utils
#:import Background views.utils
#:import CodeConfirmMenu views.utils
#:import BasicSpinner views.utils
            
<EstabSignUpPage>:
    id: _screen
    textinputs: [_username, _email, _cpf_cnpj.ids._cpf, _cpf_cnpj.ids._cnpj, _password]
    BackgroundLogo:
    RelativeLayout:
        MDIconButton:
            pos_hint: {'center_x': .1, 'center_y': .65}
            theme_icon_color: 'Custom'
            icon_color: .9, .9, .9, 1
            icon: "arrow-left"
            disabled: _spinner.active
            on_press:
                app.root.current = 'client_or_estab_page'
        BasicLabel:
            text: 'Criar conta de \\nempresa'
            halign: 'center'
            pos_hint: {'center_x': .5, 'center_y': .6275}
            font_size: '23sp'
        BasicLabel:
            text: 'Email'
            pos_hint: {'center_x': .175, 'center_y': .6}
        BasicTextInput:
            id: _email
            hint_text: 'exemplo@email.com'
            pos_hint: {'center_x': .5, 'center_y': .55}
            disabled: _spinner.active
        BasicLabel:
            text: 'Senha'
            pos_hint: {'center_x': .175, 'center_y': .5}
        BasicTextInput:
            id: _password
            password: True
            password_mask: '*'
            pos_hint: {'center_x': .5, 'center_y': .45}
            disabled: _spinner.active
        MDIconButton:
            size_hint: 0.06, 0.06
            pos_hint: {'right': .875, 'center_y': .45}
            icon: "eye"
            theme_icon_color: "Custom"
            icon_color: .05, .05, .05, 1
            disabled: _spinner.active
            on_release:
                _password.password = not _password.password
                self.icon = 'eye' if _password.password else 'eye-off'
        BasicLabel:
            text: 'Username'
            pos_hint: {'x': .1, 'center_y': .4}
        BasicTextInput:
            id: _username
            pos_hint: {'center_x': .5, 'center_y': .35}
            disabled: _spinner.active
        CpfCnpjTextInput:
            id: _cpf_cnpj
            pos_hint: {'center_x': .5, 'center_y': .215}
            size_hint: 1, .2
            disabled: _spinner.active
        BasicButton:
            text: 'Criar conta'
            size_hint_x: .8
            pos_hint: {'center_x': .5, 'center_y': .075}
            disabled: _spinner.active
            on_press:
                root.check_inputs(_username.text, _email.text, _password.text, _cpf_cnpj)
        CodeConfirmMenu:
            id: _ccm
            screen: _screen
    BasicSpinner:
        id: _spinner
'''
)

class EstabSignUpPage(MDScreen):
    name = 'estab_sign_up_page'
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fail_connection_dialog = MDDialog(text='Falha de conexão, tente novamente :(')
        self.validating_advice_dialog = MDDialog(text='Agora validaremos seus dados.\nEm até um dia útil validaremos sua conta.\nApós esse período, faça login com seus dados no aplicativo.\nObrigado por se inscrever!')
        
    def on_pre_enter(self, *args):
        for i in self.textinputs: i.text, i.date = '', 'Selecione sua data de nascimento'
        return super().on_pre_enter(*args)
    
    async def _check_inputs(self, username, email, password, cpf_cnpj_input):
        valid = await check_estab_sign_up_inputs(username, email, password, None if cpf_cnpj_input.cpf else cpf_cnpj_input.text, None if not cpf_cnpj_input.cpf else cpf_cnpj_input.text, None if not cpf_cnpj_input.cpf else cpf_cnpj_input.date)
        if isinstance(valid, str): 
            return Snackbar(text=valid).open()
        self.data = [username, email, password, None if cpf_cnpj_input.cpf else cpf_cnpj_input.text, None if not cpf_cnpj_input.cpf else cpf_cnpj_input.text, None if not cpf_cnpj_input.cpf else cpf_cnpj_input.date]
        self.ids._spinner.active = True
        Snackbar(text='Enviando o código...').open()
        self.send_code()
        
    def check_inputs(self, username, email, password, cpf_cnpj_input):
        asyncio.ensure_future(self._check_inputs(username, email, password, cpf_cnpj_input))
    
    def resend_code(self):
        self.check_inputs(self.data[0], self.data[1], self.data[2], self.ids._cpf_cnpj)
    
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
        
    def check_code(self, code):
        asyncio.ensure_future(self._check_code(code))
        
    async def _check_code(self, code):
        if str(self.code.result()) == code:
            self.ids._spinner.active = True
            send = await send_validate_cpf_or_cnpj_email(*self.data[3:])
            if not send:
                return self.fail_connection_dialog.open()
            await sign_up_estab(*self.data)
            self.manager.current = 'client_or_estab_page'
            self.ids._spinner.active = False
            return self.validating_advice_dialog.open()
        Snackbar(text='Código errado').open()
        
        