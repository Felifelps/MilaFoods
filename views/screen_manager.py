from kivymd.uix.screenmanager import MDScreenManager
from kivy.clock import Clock
from control.control import logout, get_post, get_saved_data
from .posts_page import PostsPage
from .search_page import SearchPage
from .theme_config_page import ThemeConfigPage
from .client_profile_page import ClientProfilePage
from .comment_page import ViewPostPage

class ScreenManager(MDScreenManager):
    client_pages = False
    login_pages = False
    estab_pages = False
    logged_user_is_client = False
    def __init__(self, app, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.app = app
        
    def logout(self):
        self.load_login_pages()
        logout()
        def change_current(dt): self.current = 'client_or_estab_page'
        Clock.schedule_once(change_current, 2)
    
    def load_user_pages(self):
        for i in [
            PostsPage(),
            SearchPage(),
            ThemeConfigPage(),
            ClientProfilePage(),
            ViewPostPage()
        ]: 
            self.add_widget(i)

    def load_client_pages(self):
        if not self.client_pages:
            self.load_user_pages()
            for i in [
                ClientProfilePage()
            ]: 
                self.add_widget(i)
            self.client_pages = True
    
    def load_estab_pages(self):
        if not self.estab_pages:
            self.load_user_pages()
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
        if user['username'] == '===++UserDefault++===':
            self.load_login_pages()
        elif not user['can_post']:
            self.load_client_pages()
            self.logged_user_is_client = True
        elif user['can_post'] :
            self.load_estab_pages()
            self.logged_user_is_client = False
        
    def load_view_post_page(self, id, username, image, text, comments):
        page = self.get_screen('comment_page')
        page.code = f'{username}-{id}'
        page.username = username
        page.user_image = image
        page.text = text
        print(f'{username}-{id}')
        page.comments = get_post(f'{username}-{id}')['comments']
        self.current = 'comment_page'
    
    def load_profile_page(self, username=False):
        if username == False:
            if self.logged_user_is_client:
                page = self.get_screen('client_profile_page')
                page.username = self.app.user['username']
                page.image_code = self.app.user['image_code']
                page.description = self.app.user['description']
                page.saved = get_saved_data()
                self.current = 'client_profile_page'
                return True
            else:
                pass
        client = get_client(username)
        if isinstance(client, dict):
            self.load_client_profile_page(client)
        else:
            self.load_estab_profile_page(get_estab(username))

    def load_client_profile_page(self, data):
        page = self.get_screen('client_profile_page')
        page.username = data['username']
        page.image_code = data['image_code']
        page.description = data['description']
        page.saved = data['saved']
        self.current = 'client_profile_page'
        
    def load_estab_profile_page(self, username):
        pass
    