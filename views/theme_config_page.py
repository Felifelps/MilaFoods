from kivymd.uix.screen import MDScreen
from kivy.lang import Builder

Builder.load_string(
'''
#:import BasicLabel views.utils
#:import Background views.utils
#:import join os.path.join

<ThemeButton@RelativeLayout>:
    color: 'Red'
    size_hint: .5, .25
    bg: None
    MDTextButton:
        theme_text_color: 'Custom'
        text_color: 0, 0, 0, 0
        size_hint: 1, 1
        on_press:
            app.theme_cls.primary_palette = root.color
            root.bg.theme = root.color
    Image:
        size_hint: .5, 1
        source: join('views', 'data', f'background_{root.color}.png')
        size_hint_x: .5
    BasicLabel:
        size_hint: .5, 1
        pos_hint: {'x': .5}
        text: {'Red': 'Vermelho', 'Purple': 'Roxo', 'Green': 'Verde', 'Gray': 'Preto'}[root.color]
        
<ThemeConfigPage>:
    Background:
        id: _bg
    RelativeLayout:
        MDTopAppBar:
            title: "Background"
            font_name: join('views', 'data', 'Graduate-Regular.ttf')
            left_action_items: [['arrow-left', lambda x: print('opa')]]
            pos_hint: {'top': 1}
        MDStackLayout:
            size_hint: .84, .88
            pos_hint: {'x': .1, 'y': 0}
            #md_bg_color: 'white'
            ThemeButton:
                bg: _bg
            ThemeButton:
                bg: _bg
                color: 'Green'
            ThemeButton:
                bg: _bg
                color: 'Purple'
            ThemeButton:
                bg: _bg
                color: 'Gray'
                
'''
)

class ThemeConfigPage(MDScreen):
    name = 'theme_config_page'