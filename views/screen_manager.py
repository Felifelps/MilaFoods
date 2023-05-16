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
from kivymd.uix.screenmanager import MDScreenManager

class ScreenManager(MDScreenManager):
    def on_kv_post(self, base_widget):
        for i in [
            EstabLoginPage(),
            EstabSignUpPage(),
            FollowEstabsPage(),
            EstabAccountConfigurationPage(),
            EstabAccountEditPage(),
            SavedPage(),
            ThemeConfigPage(),
            PostsPage(),
            ClientSignUpPage(),
            ClientOrEstabPage(),
            ClientLoginPage(),
        ]: 
            self.add_widget(i)
            
        return super().on_kv_post(base_widget)
    
#briefcase dev
    