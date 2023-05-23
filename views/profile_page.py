from kivymd.uix.screen import MDScreen
from kivy.lang import Builder

Builder.load_string('''
#:import BasicLabel views.utils
#:import Background views.utils
#:import BasicButton views.utils
#:import TopImageBar views.utils
#:import BottomBar views.utils
#:import LateralMenu views.utils
#:import Post views.utils
#:import join os.path.join

<ProfilePage>:
    Background:
        id: _bg
    RelativeLayout:
        TopImageBar:
            lm: _lm
        ScrollView:
            size_hint: 1, .8
            pos_hint: {'top': .85}
            MDFloatLayout:
                MDIconButton:
                    icon: join('views', 'data', 'animal.png')
                    icon_size: '75sp'
                    x: dp(10)
                    center_y: root.height - dp(175)
                Label:
                    text: 'Username'
                    font_size: '25sp'
                    size_hint: None, None
                    size: self.texture_size
                    pos: dp(10), root.height - dp(250)
                Label:
                    text: 'Description\\nCavalo'
                    font_size: '14sp'
                    size_hint: None, None
                    size: self.texture_size
                    pos: dp(10), root.height - dp(285)
                BasicButton:
                    size_hint_x: .275
                    center_x: root.width/2 - dp(5)
                    center_y: root.height - dp(200)
                    text: 'Seguir'
                    md_bg_color: app.theme_cls.primary_dark
                BasicButton:
                    size_hint_x: .275
                    center_x: root.width - dp(60)
                    center_y: root.height - dp(200)
                    text: 'Whatsapp'
                    md_bg_color: app.theme_cls.primary_dark
                Label:
                    id: publications
                    number: 300
                    text: f'[size=20sp]{self.number}[/size]\\nPublicações'
                    halign: 'center'
                    markup: True
                    font_size: '12.5sp'
                    size_hint: None, None
                    size: self.texture_size
                    center_y: root.height - dp(155)
                    center_x: root.width - dp(58)
                Label:
                    id: followers
                    number: 300
                    text: f'[size=20sp]{self.number}[/size]\\nSeguidores'
                    halign: 'center'
                    markup: True
                    font_size: '12.5sp'
                    size_hint: None, None
                    size: self.texture_size
                    center_y: root.height - dp(155)
                    center_x: root.width/2
                BasicLabel:
                    text: 'Publicações'
                    font_size: '25sp'
                    center_y: root.height - root.height*0.6
                    center_x: dp(7.5)
                    halign: 'left'
                    canvas:
                        Color:
                            rgba: 1, 1, 1, 1
                        Line:
                            points: 0, self.y - dp(10), root.width, self.y - dp(10)
                BasicButton:
                    size_hint_x: .275
                    center_y: root.height - root.height*0.6
                    right: root.width - dp(7.5)
                    text: 'Cardápio'
                    md_bg_color: app.theme_cls.primary_dark
                MDStackLayout:
                    top: root.height - root.height*0.7
                    spacing: 10, 20
                    Post:
                        post_title: "Jorginho lanches"
                    Post:
                    Post:
                    Post:
                    Post:
        BottomBar:
        LateralMenu:
            id: _lm
'''
)

class ProfilePage(MDScreen):
    name = 'profile_page'
    print('ajeitar profile page')