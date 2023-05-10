from kivymd.uix.screen import MDScreen
from kivy.lang import Builder

Builder.load_string(
'''
#:import BasicListItem views.utils

<FollowEstabsPage>:
    Image:
        source: join('views', 'data', 'background_Red.png')
    MDList:
        id: estabs
        size_hint: .8, .9
        pos_hint: {'center_x': .5, 'center_y': .5}
        BasicListItem:
            text: 'Teste'
            secondary_text: 'hehehe'
    
'''
)

class FollowEstabsPage(MDScreen):
    name = 'follow_estabs_page'