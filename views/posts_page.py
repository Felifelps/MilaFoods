from kivymd.uix.screen import MDScreen
from kivy.lang import Builder

Builder.load_string(
'''
#:import TopSearchBar views.utils
#:import BottomBar views.utils
#:import BasicLabel views.utils
#:import Background views.utils
#:import LateralMenu views.utils
#:import Post views.utils
    
<PostsPage>:
    Background:
    FloatLayout:
        TopCentralSearchBar:
            id: bar
            lm: _lm
        RecycleView:
            id: _rv
            viewclass: 'Post'
            pos_hint: {'center_x': .5, 'top': .875}
            size_hint: .98, .8
            RecycleBoxLayout:
                id: _stack
                adaptive_height: True
                spacing: 10, 20
        BottomBar:
        LateralMenu:
            id: _lm
'''
)

class PostsPage(MDScreen):
    name = 'posts_page'
    def on_enter(self, *args):
        self.ids._rv.data = [{'text': f'jorginho lanches {x}'} for x in range(25)]
        return super().on_enter(*args)