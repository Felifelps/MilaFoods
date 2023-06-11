from kivymd.uix.screenmanager import MDScreenManager
from kivy.clock import Clock
from control.control import logout, get_post, get_user, get_saved_data, get_user_data
from .posts_page import PostsPage
from .search_page import SearchPage
from .theme_config_page import ThemeConfigPage
from .client_profile_page import ClientProfilePage
from .comment_page import CommentPage
from .client_login_page import ClientLoginPage
from .client_or_estab_page import ClientOrEstabPage
from .client_sign_up_page import ClientSignUpPage
from .estab_login_page import EstabLoginPage
from .estab_sign_up_page import EstabSignUpPage
from .user_account_configuration_page import UserAccountConfigurationPage
from .follow_estabs_page import FollowEstabsPage
from .image_selection_page import ImageSelectionPage

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
            CommentPage()
        ]: 
            self.add_widget(i)

    def load_client_pages(self):
        if not self.client_pages:
            self.load_user_pages()
            for i in [
                ClientProfilePage(),
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
            for i in [
                ClientOrEstabPage(),
                EstabLoginPage(),
                ClientSignUpPage(),
                ClientLoginPage(),
                EstabSignUpPage(),
                FollowEstabsPage(),
                ImageSelectionPage(),
                UserAccountConfigurationPage(),
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
    
    def load_user_config_page(self, client):
        page = self.get_screen('user_account_configuration_page')
        page.client = client
        page.username = self.app.user['username']
        self.current = 'user_account_configuration_page'
        
    def load_comment_page(self, id, username, image, text):
        page = self.get_screen('comment_page')
        page.code = f'{username}-{id}'
        post = get_post(page.code)
        page.username = username
        page.user_image = image
        page.text = text
        page.likes = post['likes']
        page.comments = post['comments']
        page.liked = page.code in get_user(self.app.user['username'])['liked']
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
        client = get_user(username)
        if isinstance(client, dict):
            self.load_client_profile_page(client)
        else:
            self.load_estab_profile_page(get_user(username))

    def load_client_profile_page(self, data):
        page = self.get_screen('client_profile_page')
        page.username = data['username']
        page.image_code = data['image_code']
        page.description = data['description']
        page.saved = data['saved']
        self.current = 'client_profile_page'
        
    def load_estab_profile_page(self, username):
        pass
    