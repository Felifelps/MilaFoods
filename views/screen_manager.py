from kivymd.uix.screenmanager import MDScreenManager
from .client_login_page import ClientLoginPage
from .client_or_estab_page import ClientOrEstabPage

class ScreenManager(MDScreenManager):
    def on_kv_post(self, base_widget):
        self.add_widget(ClientOrEstabPage())
        self.add_widget(ClientLoginPage())
        return super().on_kv_post(base_widget)
    
    