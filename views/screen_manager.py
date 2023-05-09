from kivymd.uix.screenmanager import MDScreenManager
from .client_login_page import ClientLoginPage
from .client_or_estab_page import ClientOrEstabPage
from .client_sign_up_page import ClientSignUpPage
from .estab_login_page import EstabLoginPage

class ScreenManager(MDScreenManager):
    def on_kv_post(self, base_widget):
        self.add_widget(EstabLoginPage())
        self.add_widget(ClientSignUpPage())
        self.add_widget(ClientOrEstabPage())
        self.add_widget(ClientLoginPage())
        return super().on_kv_post(base_widget)
    
    