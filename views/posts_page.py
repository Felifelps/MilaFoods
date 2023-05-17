from kivymd.uix.screen import MDScreen
from kivy.lang import Builder

Builder.load_string(
'''
#:import TopSearchBar views.utils
#:import BottomBar views.utils
#:import BasicLabel views.utils
#:import Background views.utils
#:import Post views.utils
    
<PostsPage>:
    Background:
    FloatLayout:
        TopSearchBar:
            id: bar
        ScrollView:
            pos_hint: {'center_x': .5, 'top': .875}
            size_hint: .98, .8
            MDStackLayout:
                id: _stack
                adaptive_height: True
                spacing: 10, 20
                Post:
                    post_title: "Jorginho lanches"
            
        BottomBar:
        
        
'''
)

class PostsPage(MDScreen):
    name = 'posts_page'
    