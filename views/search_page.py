from kivymd.uix.screen import MDScreen
from kivy.lang import Builder

Builder.load_string('''
#:import BasicLabel views.utils
#:import Background views.utils
#:import EstabAccount views.utils
#:import TopImageBar views.utils
#:import BottomBar views.utils
#:import TopActiveSearchBar views.utils

<SearchPage>:
    Background:
        id: _bg
    RelativeLayout:
        TopActiveSearchBar:
        ScrollView:
            size_hint: .9, .8
            pos_hint: {'center_x': .5, 'top': .875}
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
        BottomBar:
'''
)

class SearchPage(MDScreen):
    name = 'search_page'