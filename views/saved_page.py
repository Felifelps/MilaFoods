from kivymd.uix.screen import MDScreen
from kivy.lang import Builder
from kivy.properties import ListProperty
from control.control import get_user, get_post

Builder.load_string(
'''
#:import TopTitleBar views.utils
#:import BottomBar views.utils
#:import BasicLabel views.utils
#:import Background views.utils
#:import LateralMenu views.utils
#:import join os.path.join
#:import SavedPost views.utils
            
<SavedPage>:
    id: _screen
    Background:
    FloatLayout:
        TopTitleBar:
            id: bar
            lm: _lm
            title: app.user['username']
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
            text: f'Você tem {len(_rv.data)} posts salvos'
            #font_size: '30sp'
            pos_hint: {'center_x': .375, 'center_y': .73}
        RecycleView:
            id: _rv
            viewclass: 'SavedPost'
            pos_hint: {'center_x': .5, 'top': .7}
            size_hint: .8, .55
            RecycleGridLayout:
                cols: 2
                default_col_width: dp(106)
                default_size: None, dp(56)
                default_size_hint: 1, None
                size_hint_y: None
                height: self.minimum_height
                padding: dp(5)
                spacing: dp(5)
        BottomBar:
        LateralMenu:
            id: _lm
'''
)

class SavedPage(MDScreen):
    name = 'saved_page'
    def on_pre_enter(self, *args):
        data = []
        for saved in get_user(self.manager.app.user['username'])['saved']:
            saved_data = get_post(saved)
            saved_data['id'] = str(saved_data['id'])
            saved_data['width'] = 130
            saved_data['height'] = 130
            data.append(saved_data)
        self.ids._rv.data = data
        return super().on_pre_enter(*args)
    