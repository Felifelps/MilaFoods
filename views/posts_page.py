from kivymd.uix.screen import MDScreen
from kivy.lang import Builder
from kivy.metrics import dp

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
                id: _box
                orientation: 'vertical'
                default_size: None, dp(56)
                default_size_hint: 1, None
                size_hint_y: None
                height: self.minimum_height
                orientation: 'vertical'
                spacing: dp(10)
        BottomBar:
        LateralMenu:
            id: _lm
'''
)

class PostsPage(MDScreen):
    name = 'posts_page'
    def on_enter(self, *args):
        self.ids._rv.data = [{'description': f'jorginho lanches {x}', 'height': dp(300)} for x in range(200)]
        return super().on_enter(*args)