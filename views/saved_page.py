from kivymd.uix.screen import MDScreen
from kivy.lang import Builder

Builder.load_string(
'''
#:import TopBar views.utils
#:import BottomBar views.utils
#:import BasicLabel views.utils
#:import Background views.utils
#:import join os.path.join

<Post@RelativeLayout>:
    image: _img
    size_hint: None, None
    size: dp(130), dp(150)
    canvas.before:
        Color:
            rgba: .9, .9, .9, 1
        Rectangle:
            size: self.width, self.height
            pos: 0, 0
    Image:
        id: _img
        pos_hint: {'top': 1}
        size_hint: 1, .75
    Label:
        text: '[b][Título do post][/b]'
        color: .1, .1, .1, 1
        size_hint: None, None
        size: self.texture_size
        font_size: '12sp'
        markup: True
        pos_hint: {'x': .05, 'center_y': .175}
    Label:
        text: '[Nome estab]'
        color: .1, .1, .1, 1
        size_hint: None, None
        size: self.texture_size
        font_size: '10sp'
        pos_hint: {'x': .05, 'center_y': .075}
            
<SavedPage>:
    Background:
    FloatLayout:
        TopBar:
            id: bar
            title: "[Username]"
            right_action_items: [['menu', lambda x: print('opa')]]
            left_action_items: [['account-circle', lambda x: print('opa')]]
            icon_size: '25sp'
        MDIconButton:
            icon: 'star'
            icon_size: '50sp'
            pos_hint: {'center_x': .125, 'center_y': .8}
        BasicLabel:
            text: 'Salvos'
            font_size: '30sp'
            pos_hint: {'center_x': .375, 'center_y': .8}
        BasicLabel:
            id: number
            text: 'Você tem {} imagens salvas'
            #font_size: '30sp'
            pos_hint: {'center_x': .375, 'center_y': .73}
        ScrollView:
            pos_hint: {'center_x': .5, 'top': .7}
            size_hint: .8, .55
            MDStackLayout:
                id: _stack
                adaptive_height: True
                spacing: 10, 20
                Post:
                Post:
                Post:
                Post:
                Post:
                Post:
                Post:
                Post:
            
        BottomBar:
        
        
'''
)

class SavedPage(MDScreen):
    name = 'saved_page'
    