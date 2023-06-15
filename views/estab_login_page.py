from kivymd.uix.screen import MDScreen
from kivymd.uix.snackbar import Snackbar
from kivy.lang import Builder
from control.control import login_estab
from kivymd.uix.dialog import MDDialog

Builder.load_string('''
#:import join os.path.join
#:import BasicButton views.utils
#:import BasicLabel views.utils
#:import BasicTextInput views.utils
#:import BasicDropDownItem views.utils
#:import Background views.utils
#:import CpfCnpjTextInput views.utils
            
<EstabLoginPage>:
    id: _screen
    textinputs: [_cpf_cnpj.ids._cpf, _cpf_cnpj.ids._cnpj, _password]
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
            text: 'Login de Empresa'
            pos_hint: {'center_x': .55, 'center_y': .6}
            font_size: '25sp'
        CpfCnpjTextInput:
            id: _cpf_cnpj
            allow_date: False
            pos_hint: {'center_x': .5, 'center_y': .45}
            size_hint: 1, .2
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
                _screen.login_estab(_cpf_cnpj.text, _password.text)
        BasicLabel:
            text: 'Não tem uma conta? [color=#0000ff][ref=create_account]Crie aqui!![/ref][/color]'
            pos_hint: {'center_x': .5, 'center_y': .025}
            markup: True
            on_ref_press:
                app.root.current = 'estab_sign_up_page'
'''
)

class EstabLoginPage(MDScreen):
    name = 'estab_login_page'
    def on_pre_enter(self, *args):
        for i in self.textinputs: i.text, i.date = '', 'Selecione sua data de nascimento'
        return super().on_pre_enter(*args)
    
    def login_estab(self, cpf_cnpj, password):
        self.dialog = MDDialog(
            text='Checando os dados da conta...',
            on_open=lambda a: self.check_login_data(cpf_cnpj, password)
        )
        self.dialog.open()
        
    def check_login_data(self, cpf_cnpj, password):
        estab = login_estab(cpf_cnpj, password)
        self.dialog.dismiss()
        if isinstance(estab, str): return Snackbar(text=estab).open()
        self.manager.app.update_user(estab)
        Snackbar(text='Logado com sucesso').open()
        self.manager.load_user_pages()
        self.manager.load_user_config_page(False)