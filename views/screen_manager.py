from .client_login_page import ClientLoginPage
from .client_or_estab_page import ClientOrEstabPage
from .client_sign_up_page import ClientSignUpPage
from .estab_login_page import EstabLoginPage
from .estab_sign_up_page import EstabSignUpPage
from .posts_page import PostsPage
from kivymd.uix.screenmanager import MDScreenManager
#from kivy.lang import Builder

class ScreenManager(MDScreenManager):
    def load_client_pages(self):
        for i in [
            PostsPage()
        ]: 
            self.add_widget(i)
            
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for i in [
            ClientOrEstabPage(),
            EstabLoginPage(),
            ClientSignUpPage(),
            ClientLoginPage(),
            EstabSignUpPage()
        ]: 
            self.add_widget(i)

    
    