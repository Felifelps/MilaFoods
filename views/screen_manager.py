from kivymd.uix.screenmanager import MDScreenManager
from kivy.clock import Clock
from control.control import logout, get_post, get_user
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
from .saved_page import SavedPage
from .estab_profile_page import EstabProfilePage
from .estab_account_edit_page import EstabAccountEditPage

class ScreenManager(MDScreenManager):
    login_pages = False
    user_pages = False
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
        if not self.user_pages:
            for i in [
                EstabAccountEditPage(),
                PostsPage(),
                SearchPage(),
                ThemeConfigPage(),
                CommentPage(),
                SavedPage(),
                ClientProfilePage(),
                EstabProfilePage(),
            ]: 
                self.add_widget(i)
            self.user_pages = True
    
    def load_login_pages(self):
        if not self.login_pages:
            for i in [
                ClientOrEstabPage(),
                UserAccountConfigurationPage(),
                ImageSelectionPage(),
                EstabLoginPage(),
                ClientSignUpPage(),
                ClientLoginPage(),
                EstabSignUpPage(),
                FollowEstabsPage(),
            ]: 
                self.add_widget(i)
            self.login_pages = True
    
    def load_screens(self):
        if self.app.username == '===NoUser===':
            return self.load_login_pages()
        self.app.update_user(self.app.username)
        self.logged_user_is_client = not self.app.user['can_post']
        self.load_user_pages()
    
    def load_user_config_page(self, client):
        page = self.get_screen('user_account_configuration_page')
        page.client = client
        page.username = self.app.username
        self.current = 'user_account_configuration_page' if self.app.user['description'] == '' else 'posts_page'
        
    def load_comment_page(self, id, username, image, text):
        page = self.get_screen('comment_page')
        page.code = f'{username}-{id}'
        post = get_post(page.code)
        page.username = username
        page.user_image = image
        page.text = text
        page.likes = post['likes']
        page.comments = post['comments']
        user = get_user(self.app.username)
        page.liked = page.code in user['liked']
        page.saved = page.code in user['saved']
        self.current = 'comment_page'
    
    def load_profile_page(self, username=False):
        if username == False:
            if self.app.user['can_post']:
                return self.load_estab_profile_page(self.app.user)
            else:
                return self.load_client_profile_page(self.app.user, get_user(self.app.username)['saved'])
        user = get_user(username)
        if user['can_post']:
            return self.load_estab_profile_page(user)
        self.load_client_profile_page(user)

    def load_client_profile_page(self, data, saved=False):
        page = self.get_screen('client_profile_page')
        page.username = data['username']
        page.image_code = str(data['image_code'])
        page.description = data['description']
        page.saved = data['saved'] if saved == False else saved
        self.current = 'client_profile_page'
        
    def load_estab_profile_page(self, data):
        if isinstance(data, str): data = get_user(data)
        page = self.get_screen('estab_profile_page')
        page.username = data['username']
        page.image = str(data['image'])
        page.description = data['description']
        page.n_of_posts = data['n_of_posts']
        page.n_of_followers = data['n_of_followers']
        page.following = page.username in self.app.user['following']
        page.tel = str(data['tel'])
        if self.current == 'estab_profile_page':
            page.dialog.open()
        self.current = 'estab_profile_page'
        
    def load_user_edit_page(self, username):
        print('carregando', username)
    