from kivymd.uix.screenmanager import MDScreenManager
from .user_login_page import UserLoginPage

class ScreenManager(MDScreenManager):
    def on_kv_post(self, base_widget):
        self.add_widget(UserLoginPage())
        return super().on_kv_post(base_widget)
    
    