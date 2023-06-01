from kivymd.uix.screenmanager import MDScreenManager
from control.firebase_to_local import logout

class ScreenManager(MDScreenManager):
    def logout(self):
        logout()
    
    def load_client_pages(self):
        from .posts_page import PostsPage
        from .search_page import SearchPage
        for i in [
            PostsPage(),
            SearchPage()
        ]: 
            self.add_widget(i)
    
    def load_estab_pages(self):
        for i in [
        ]: 
            self.add_widget(i)
    
    def load_login_pages(self):
        from .client_login_page import ClientLoginPage
        from .client_or_estab_page import ClientOrEstabPage
        from .client_sign_up_page import ClientSignUpPage
        from .estab_login_page import EstabLoginPage
        from .estab_sign_up_page import EstabSignUpPage
        for i in [
            ClientOrEstabPage(),
            EstabLoginPage(),
            ClientSignUpPage(),
            ClientLoginPage(),
            EstabSignUpPage()
        ]: 
            self.add_widget(i)
    
    def load_screens(self, user, default_user):
        client = user['image'] == None
        estab = user['image_code'] == None
        print(user['username'], default_user)
        if user['username'] == default_user:
            self.load_login_pages()
        elif client and not estab:
            self.load_client_pages()
        elif estab and not client:
            self.load_estab_pages()
        

    
    