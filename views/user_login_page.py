from kivymd.uix.screen import MDScreen
from kivy.lang import Builder
from os.path import join

Builder.load_string(
'''
#:import join os.path.join
<BasicLabel@Label>:
    font_name: join('views', 'data', 'Graduate-Regular.ttf')
    font_size: '12.5sp'
    
<BasicButton@MDRaisedButton>:
    font_name: join('views', 'data', 'Graduate-Regular.ttf')
    
<UserLoginPage>:
    Image:
        source: join('views', 'data', 'background.png')
    RelativeLayout:
        BasicLabel:
            text: 'Login de cliente'
            pos_hint: {'center_x': .5, 'center_y': .6}
            font_size: '25sp'
        BasicLabel:
            text: 'Email'
            pos_hint: {'center_x': .175, 'center_y': .525}
        TextInput:
            hint_text: 'exemplo@email.com'
            background_color: .9, .9, .9, 1
            size_hint: .8, 0.06
            pos_hint: {'center_x': .5, 'center_y': .475}
            multiline: False
        BasicLabel:
            text: 'Senha'
            pos_hint: {'center_x': .175, 'center_y': .41}
        TextInput:
            background_color: .9, .9, .9, 1
            password: True
            password_mask: '*'
            size_hint: .8, 0.06
            pos_hint: {'center_x': .5, 'center_y': .36}
            multiline: False
        MDIconButton:
            size_hint: 0.06, 0.06
            pos_hint: {'right': .875, 'center_y': .36}
            icon: "eye"
            theme_icon_color: "Custom"
            icon_color: .05, .05, .05, 1
        BasicButton:
            text: 'Inscreva-se aqui!'
            size_hint_x: .8
            on_press: print(self.height)
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

class UserLoginPage(MDScreen):
    name = 'user_login_page'