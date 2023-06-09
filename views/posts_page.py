from kivymd.uix.screen import MDScreen
from kivy.lang import Builder
from kivy.metrics import dp
from kivy.properties import ListProperty, BooleanProperty
from kivymd.uix.dialog import MDDialog
from control.control import get_posts_from_server

Builder.load_string('''
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
                spacing: dp(10)
        BottomBar:
        LateralMenu:
            id: _lm
'''
)

class PostsPage(MDScreen):
    name = 'posts_page'
    data = ListProperty()
    updated = BooleanProperty(False)
    def get_posts(self, random=True):
        if not self.updated: self.updated = True
        self.dialog.dismiss()
        self.ids._rv.data = get_posts_from_server()
    
    def on_pre_enter(self, *args):
        self.ids._rv.data = get_posts_from_server()
        return super().on_pre_enter(*args)

    def on_data(self, a, b):
        self.ids._rv.data = self.data
    
    def on_enter(self, *args):
        if not self.updated:
            self.dialog = MDDialog(
                text='Atualizando posts...',
                on_open=lambda x: self.get_posts()
            )
            self.dialog.open()
        return super().on_enter(*args)