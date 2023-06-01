from kivymd.uix.screen import MDScreen
from kivymd.uix.snackbar import Snackbar
from kivy.lang import Builder

Builder.load_string('''
#:import join os.path.join
#:import BasicButton views.utils
#:import BasicLabel views.utils
#:import BasicTextInput views.utils
#:import BasicDropDownItem views.utils
#:import Background views.utils
#:import CpfCnpjTextInput views.utils
            
<EstabLoginPage>:
    BackgroundLogo:
    RelativeLayout:
        BasicLabel:
            text: 'Login de Empresa'
            pos_hint: {'center_x': .5, 'center_y': .6}
            font_size: '25sp'
        CpfCnpjTextInput:
            pos_hint: {'center_x': .5, 'center_y': .5}
            size_hint: 1, .2
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
            on_press: print(self.height)
            pos_hint: {'center_x': .5, 'center_y': .26}
            on_press:
                app.root.current = 'posts_page'
        BasicLabel:
            text: 'Ou use suas redes sociais'
            pos_hint: {'center_x': .5, 'center_y': .21}
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
    