from .client_login_page import ClientLoginPage
from .client_or_estab_page import ClientOrEstabPage
from .client_sign_up_page import ClientSignUpPage
from .estab_account_configuration_page import EstabAccountConfigurationPage
from .estab_account_edit_page import EstabAccountEditPage
from .estab_login_page import EstabLoginPage
from .estab_sign_up_page import EstabSignUpPage
from .follow_estabs_page import FollowEstabsPage
from .posts_page import PostsPage
from .theme_config_page import ThemeConfigPage
from .saved_page import SavedPage
from .search_page import SearchPage
from .profile_page import ProfilePage
from .menu_page import MenuPage
from kivymd.uix.screenmanager import MDScreenManager
from kivy.lang import Builder

class ScreenManager(MDScreenManager):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for i in [
            ClientOrEstabPage(),
            MenuPage(),
            ProfilePage(),
            PostsPage(),
            SearchPage(),
            EstabAccountEditPage(),
            EstabLoginPage(),
            EstabSignUpPage(),
            FollowEstabsPage(),
            EstabAccountConfigurationPage(),
            SavedPage(),
            ThemeConfigPage(),
            ClientSignUpPage(),
            ClientLoginPage(),
        ]: 
            self.add_widget(i)
        for screen in self.screens:
            screen.add_widget(Builder.load_string('''
Button:
    text: 'Next'
    size: 10, 10
    pos: 0, 0
    size_hint: .1, .1
    on_press: self.parent.manager.current = self.parent.manager.next()
                                                  
'''))
    
    
    