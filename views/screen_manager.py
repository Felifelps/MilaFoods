from .client_login_page import ClientLoginPage
from .client_or_estab_page import ClientOrEstabPage
from .client_sign_up_page import ClientSignUpPage
from .estab_account_configuration_page import EstabAccountConfigurationPage
from .estab_login_page import EstabLoginPage
from .estab_sign_up_page import EstabSignUpPage
from .follow_estabs_page import FollowEstabsPage
from .theme_config_page import ThemeConfigPage
from kivymd.uix.screenmanager import MDScreenManager

class ScreenManager(MDScreenManager):
    def on_kv_post(self, base_widget):
        self.add_widget(ThemeConfigPage())
        self.add_widget(EstabAccountConfigurationPage())
        self.add_widget(FollowEstabsPage())
        self.add_widget(EstabSignUpPage())
        self.add_widget(EstabLoginPage())
        self.add_widget(ClientSignUpPage())
        self.add_widget(ClientOrEstabPage())
        self.add_widget(ClientLoginPage())
        return super().on_kv_post(base_widget)
    
    