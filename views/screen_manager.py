from kivymd.uix.screenmanager import MDScreenManager
from .client_login_page import ClientLoginPage

class ScreenManager(MDScreenManager):
    def on_kv_post(self, base_widget):
        self.add_widget(ClientLoginPage())
        return super().on_kv_post(base_widget)
    
    