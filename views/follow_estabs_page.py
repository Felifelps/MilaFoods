from kivymd.uix.screen import MDScreen
from kivy.lang import Builder

Builder.load_string(
'''
#:import BasicListItem views.utils
#:import BasicLabel views.utils
#:import Background views.utils
#:import join os.path.join
#:import colors kivymd.color_definitions.colors
#:import EstabAccount views.utils

<BottomAnimalBar@RelativeLayout>:
    canvas:
        Color:
            rgba: app.theme_cls.primary_dark
        Rectangle:
            size: self.size
            pos: self.pos
    Image:
        source: join('views', 'data', 'animal.png')
        size_hint: 1.5, 1.5
        allow_stretch: True
        pos_hint: {'center_x': .85, 'center_y': .75}
    BasicLabel:
        text: 'Vem lanchar'
        font_size: '20sp'
        pos_hint: {'center_x': .25, 'center_y': .5}

<FollowEstabsPage>:
    Background:
    BasicLabel:
        text: 'Siga a empresas!'
        font_size: '20sp'
        pos_hint: {'center_x': .5, 'center_y': .96}
    MDIconButton:
        pos_hint: {'right': 1, 'top': 1}
        icon: "close"
    ScrollView:
        size_hint: .9, .78
        pos_hint: {'center_x': .5, 'top': .93}
        bar_color: 0, 0, 0, 0
        MDList:
            id: estabs
            EstabAccount:
            EstabAccount:
            EstabAccount:
            EstabAccount:
            EstabAccount:
            EstabAccount:
            EstabAccount:
            EstabAccount:
            EstabAccount:
    BottomAnimalBar:
        size_hint: 1, .15
        pos_hint: {'center_x': .5, 'y': 0} 

'''
)

class FollowEstabsPage(MDScreen):
    name = 'follow_estabs_page'