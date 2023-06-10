from kivymd.uix.screen import MDScreen
from kivy.lang import Builder

Builder.load_string('''
#:import BasicLabel views.utils
#:import Background views.utils
#:import join os.path.join

<EmojiButton@MDIconButton>:
    code: 1
    icon_size: '115sp'
    icon: join('views', 'data', 'profile_images', f'{int(self.code)}.png')
    on_press:
        self.parent.screen.save_profile_image(self.code)

<ImageSelectionPage>:
    id: _screen
    Background:
        id: _bg
    RelativeLayout:
        MDTopAppBar:
            title: "Escolha uma foto de perfil"
            font_name: join('views', 'data', 'Graduate-Regular.ttf')
            left_action_items: [['arrow-left', lambda x: self.parent.parent.back()]]
            pos_hint: {'top': 1}
            icon_color: .9, .9, .9, 1
            headline_text_color: .9, .9, .9, 1
        ScrollView:
            pos_hint: {'center_x': .5, 'top': .85}
            size_hint: .9, .9
            MDStackLayout:
                id: _stack
                adaptive_height: True
                spacing: 10, 20
                screen: _screen
                EmojiButton:
                EmojiButton:
                    code: 2
                EmojiButton:
                    code: 3
                EmojiButton:
                    code: 4
                EmojiButton:
                    code: 5
                EmojiButton:
                    code: 6
                EmojiButton:
                    code: 7
                EmojiButton:
                    code: 8
                EmojiButton:
                    code: 9
                EmojiButton:
                    code: 10
                EmojiButton:
                    code: 11
                EmojiButton:
                    code: 12
                EmojiButton:
                    code: 13
                EmojiButton:
                    code: 14
                EmojiButton:
                    code: 15
'''
)
class ImageSelectionPage(MDScreen):
    name = 'image_selection_page'
    def back(self): self.manager.current = 'posts_page'
    
    def save_profile_image(self, code):
        print(code)