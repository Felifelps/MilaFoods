from kivymd.uix.screenmanager import MDScreenManager

class ScreenManager(MDScreenManager):
    def load_client_pages(self):
        from .posts_page import PostsPage
        for i in [
            PostsPage()
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
    
    def load_screens(self, user):
        if user == {}:
            self.load_login_pages()
        elif user['type'] == 'client':
            self.load_client_pages()
        elif user['type'] == 'estab':
            self.load_estab_pages()
        

    
    