from kivymd.uix.screenmanager import MDScreenManager
from kivy.clock import Clock
from control.firebase_to_local import logout, get_post, get_saved_data, get_client

class ScreenManager(MDScreenManager):
    client_pages = False
    login_pages = False
    estab_pages = False
    client = False
    def __init__(self, app, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.app = app
        
    def logout(self):
        self.load_login_pages()
        logout()
        def change_current(dt): self.current = 'client_or_estab_page'
        Clock.schedule_once(change_current, 2)
    
    def load_client_pages(self):
        if not self.client_pages:
            from .posts_page import PostsPage
            from .search_page import SearchPage
            from .theme_config_page import ThemeConfigPage
            from .client_profile_page import ClientProfilePage
            from .view_post_page import ViewPostPage
            for i in [
                PostsPage(),
                SearchPage(),
                ThemeConfigPage(),
                ClientProfilePage(),
                ViewPostPage()
            ]: 
                self.add_widget(i)
            self.client_pages = True
    
    def load_estab_pages(self):
        if not self.estab_pages:
            for i in [
            ]: 
                self.add_widget(i)
            self.estab_pages = True
    
    def load_login_pages(self):
        if not self.login_pages:
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
            self.login_pages = True
    
    def load_screens(self, user):
        client = user['image'] == None
        estab = user['image_code'] == None
        if user['username'] == '===++UserDefault++===':
            self.load_login_pages()
        elif client and not estab:
            self.load_client_pages()
            self.client = True
        elif estab and not client:
            self.load_estab_pages()
            self.client = False
        
    def load_view_post_page(self, id, username, image, text, comments):
        page = self.get_screen('view_post_page')
        page.username = username
        page.image = image
        page.text = text
        page.comments = get_post(f'{username}-{id}')['comments']
        self.current = 'view_post_page'
    
    def load_client_profile_page(self, username=False):
        page = self.get_screen('client_profile_page')
        if username == False:
            page.username = self.app.user['username']
            page.image_code = self.app.user['image_code']
            page.description = self.app.user['description']
            page.saved = get_saved_data()
        else:
            client = get_client(username)
            if client == False: return 
            page.username = username
            page.image_code = client['image_code']
            page.description = client['description']
            page.saved = client['saved']
        self.current = 'client_profile_page'
        
    def load_estab_profile_page(self, username):
        pass
    
    def client_user(self, username):
        client = get_client(username)
        print(client, not isinstance(client, dict))
        if not isinstance(client, dict):
            return False
        return True