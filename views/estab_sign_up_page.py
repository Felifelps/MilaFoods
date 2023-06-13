from kivymd.uix.screen import MDScreen
from kivy.lang import Builder
from kivymd.uix.snackbar import Snackbar
from kivymd.uix.dialog import MDDialog
from control.control import check_estab_sign_up_inputs, send_email_code, send_validate_cpf_or_cnpj_email, sign_up_estab

Builder.load_string('''
#:import BasicButton views.utils
#:import BasicLabel views.utils
#:import BasicTextInput views.utils
#:import Background views.utils
#:import CodeConfirmMenu views.utils
            
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
        BasicLabel:
            text: 'Senha'
            pos_hint: {'center_x': .175, 'center_y': .5}
        BasicTextInput:
            id: _password
            password: True
            password_mask: '*'
            pos_hint: {'center_x': .5, 'center_y': .45}
        MDIconButton:
            size_hint: 0.06, 0.06
            pos_hint: {'right': .875, 'center_y': .45}
            icon: "eye"
            theme_icon_color: "Custom"
            icon_color: .05, .05, .05, 1
            on_release:
                _password.password = not _password.password
                self.icon = 'eye' if _password.password else 'eye-off'
        BasicLabel:
            text: 'Username'
            pos_hint: {'x': .1, 'center_y': .4}
        BasicTextInput:
            id: _username
            pos_hint: {'center_x': .5, 'center_y': .35}
        CpfCnpjTextInput:
            id: _cpf_cnpj
            pos_hint: {'center_x': .5, 'center_y': .215}
            size_hint: 1, .2
        BasicButton:
            text: 'Criar conta'
            size_hint_x: .8
            pos_hint: {'center_x': .5, 'center_y': .075}
            on_press:
                root.check_inputs(_username.text, _email.text, _password.text, _cpf_cnpj)
        CodeConfirmMenu:
            id: _ccm
            screen: _screen
'''
)

class EstabSignUpPage(MDScreen):
    name = 'estab_sign_up_page'
    def open(self):
        self.ids._ccm.open(False)
        
    def on_pre_enter(self, *args):
        for i in self.textinputs: i.text, i.date = '', 'Selecione sua data de nascimento'
        return super().on_pre_enter(*args)
    
    def check_inputs(self, username, email, password, cpf_cnpj_input):
        valid = check_estab_sign_up_inputs(username, email, password, None if cpf_cnpj_input.cpf else cpf_cnpj_input.text, None if not cpf_cnpj_input.cpf else cpf_cnpj_input.text, None if not cpf_cnpj_input.cpf else cpf_cnpj_input.date)
        if isinstance(valid, str): 
            return Snackbar(text=valid).open()
        self.data = [username, email, password, None if cpf_cnpj_input.cpf else cpf_cnpj_input.text, None if not cpf_cnpj_input.cpf else cpf_cnpj_input.text, None if not cpf_cnpj_input.cpf else cpf_cnpj_input.date]
        self.dialog = MDDialog(
            text='Enviando código...',
            on_open=lambda x: self.send_code(email)
        )
        self.dialog.open()
    
    def resend_code(self):
        self.check_inputs(self.data[0], self.data[1], self.data[2], self.ids._cpf_cnpj)
        
    def send_code(self, email):
        self.dialog.dismiss()
        self.code = send_email_code(email)
        if not self.code:
            return MDDialog(
                text='Falha de conexão, tente novamente :('
            ).open()
        self.ids._ccm.open()
        
    def check_code(self, code):
        if str(self.code) == code:
            send = send_validate_cpf_or_cnpj_email(*self.data[3:])
            if not send:
                return MDDialog(
                    text='Falha de conexão, tente novamente :('
                ).open()
            sign_up_estab(*self.data)
            self.manager.current = 'client_or_estab_page'
            return MDDialog(
                text='Agora validaremos seus dados.\nEm até um dia útil validaremos sua conta.\nApós esse período, faça login com seus dados no aplicativo.\nObrigado por se inscrever!'
            ).open()
        Snackbar(text='Código errado').open()
        
        