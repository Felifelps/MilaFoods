from kivymd.uix.screen import MDScreen
from kivy.lang import Builder

Builder.load_string(
'''
#:import BasicButton views.utils
#:import BasicLabel views.utils
#:import BasicTextInput views.utils
#:import Background views.utils
#:import CodeConfirmMenu views.utils
            
<EstabSignUpPage>:
    BackgroundLogo:
    RelativeLayout:
        BasicLabel:
            text: 'Criar conta de empresa'
            pos_hint: {'center_x': .5, 'center_y': .6}
            font_size: '23sp'
        BasicLabel:
            text: 'Email'
            pos_hint: {'center_x': .175, 'center_y': .55}
        BasicTextInput:
            hint_text: 'exemplo@email.com'
            pos_hint: {'center_x': .5, 'center_y': .5}
        BasicLabel:
            text: 'Senha'
            pos_hint: {'center_x': .175, 'center_y': .45}
        BasicTextInput:
            id: password
            password: True
            password_mask: '*'
            pos_hint: {'center_x': .5, 'center_y': .4}
        MDIconButton:
            size_hint: 0.06, 0.06
            pos_hint: {'right': .875, 'center_y': .4}
            icon: "eye"
            theme_icon_color: "Custom"
            icon_color: .05, .05, .05, 1
            on_release:
                password.password = not password.password
                self.icon = 'eye' if password.password else 'eye-off'
        BasicLabel:
            text: 'Nome da empresa'
            pos_hint: {'center_x': .275, 'center_y': .35}
        BasicTextInput:
            pos_hint: {'center_x': .5, 'center_y': .3}
        BasicLabel:
            text: 'CPF ou CNPJ'
            pos_hint: {'center_x': .225, 'center_y': .25}
        BasicTextInput:
            type: 'cpf'
            pos_hint: {'center_x': .5, 'center_y': .2}
            max_text_length: 11
        BasicButton:
            text: 'Criar conta'
            size_hint_x: .8
            pos_hint: {'center_x': .5, 'center_y': .1}
            on_press:
                root.open()
        CodeConfirmMenu:
            id: _ccm
            posts: False
'''
)

class EstabSignUpPage(MDScreen):
    name = 'estab_sign_up_page'
    def open(self):
        self.ids._ccm.open()
    print('Ajeitar o cpf e cnpj pra escolher')