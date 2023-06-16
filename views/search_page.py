from kivymd.uix.screen import MDScreen
from kivy.lang import Builder
from kivy.metrics import dp
from control.control import list_users

Builder.load_string('''
#:import BasicLabel views.utils
#:import Background views.utils
#:import EstabAccount views.utils
#:import BottomBar views.utils
#:import TopActiveSearchBar views.utils
#:import FollowButton views.utils

<SearchPage>:
    rv: _rv
    app: app
    Background:
        id: _bg
    RelativeLayout:
        TopActiveSearchBar:
        RecycleView:
            id: _rv
            viewclass: 'FollowButton'
            size_hint: .9, .8
            pos_hint: {'center_x': .5, 'top': .875}
            RecycleBoxLayout:
                orientation: 'vertical'
                default_size: None, dp(56)
                default_size_hint: 1, None
                size_hint_y: None
                height: self.minimum_height
                spacing: dp(1)
        BottomBar:
'''
)

class SearchPage(MDScreen):
    name = 'search_page'
    users = list_users(True)
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        data = []
        for user in self.users:
            user['following'] = self.app.username in user['following']
            user['image'] = str(user['image'])
            user['image_code'] = str(user['image_code'])
            user['size_hint'] = (1, None)
            user['height'] = dp(60)
            data.append(user)
        self.rv.data = data