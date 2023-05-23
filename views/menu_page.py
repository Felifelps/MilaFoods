from kivymd.uix.screen import MDScreen
from kivymd.uix.relativelayout import MDRelativeLayout
from kivy.animation import Animation
from kivy.properties import StringProperty
from kivy.lang import Builder

Builder.load_string(
'''
#:import MenuIconButton views.utils
#:import BasicLabel views.utils
#:import BasicTextField views.utils
#:import LateralMenu views.utils
#:import TopImageBar views.utils
#:import Background views.utils
#:import join os.path.join

<MenuItemData>:
    md_bg_color: .9, .9, .9, 1
    title: 'title'
    img: 'star'
    description: 'description'
    price: 35
    quantity: 1
    size_hint: 1, .6
    pos_hint: {'x': 0, 'y': -0.6}
    bg_opacity: 0
    canvas.before:
        Color:
            rgba: 0, 0, 0, self.bg_opacity
        Rectangle:
            pos: 0, 0
            size: self.width, self.height*1.75
    BasicLabel:
        text: root.title
        color: .2, .2, .2, 1
        font_size: '17.5sp'
        pos_hint: {'center_x': .5, 'top': .975}
    MDIconButton:
        id: _img
        icon_size: '90sp'
        md_bg_color: 'red'
        icon: root.img
        pos_hint: {'center_x': .5, 'center_y': .65}
    BasicLabel:
        text: root.description
        color: .2, .2, .2, 1
        font_size: '15sp'
        pos_hint: {'x': .025, 'center_y': .45}
    RelativeLayout:
        pos_hint: {'center_x': .5, 'center_y': .125}
        size_hint: .96, .2
        canvas.before:
            Color:
                rgba: .2, .2, .2, 1
            Line:
                rounded_rectangle: 0, 0, self.width, self.height, 20, 20, 20, 20
                width: 2
        BasicLabel:
            text: f'R${root.price*root.quantity}'
            color: .2, .2, .2, 1
            font_size: '25sp'
            pos_hint: {'x': .05, 'center_y': .5}
        BasicLabel:
            text: str(root.quantity)
            color: .2, .2, .2, 1
            font_size: '17.5sp'
            pos_hint: {'center_x': .77, 'center_y': .5}
        MDIconButton:
            icon: 'minus'
            theme_icon_color: 'Custom'
            icon_color: 0, 0, 0, 1
            pos_hint: {'x': .6, 'center_y': .5}
            on_press:
                root.quantity -= 0 if root.quantity == 1 else 1
        MDIconButton:
            icon: 'plus'
            theme_icon_color: 'Custom'
            icon_color: 0, 0, 0, 1
            pos_hint: {'x': .8, 'center_y': .5}
            on_press:
                root.quantity += 1
    BasicButton:
        text: '+Carrinho'
        pos_hint: {'right': .98, 'center_y': .85}
        size_hint: .15, .1

<MenuItem@RelativeLayout>:
    size_hint: .98, None
    height: dp(52.5)
    pos_hint: {'center_x': .5}
    title: 'alimento'
    img: 'star'
    description: 'Description'
    price: 35
    canvas.before:
        Color:
            rgba: 1, 1, 1, 1
        RoundedRectangle:
            size: self.width, self.height
            pos: 0, 0
            radius: [20]
    MDIconButton:
        icon: root.img
        md_bg_color: 'red'
        pos_hint: {'x': .025, 'center_y': .5}
    BasicLabel:
        text: root.title
        font_size: '17.5sp'
        color: .2, .2, .2, 1
        pos_hint: {'x': .2, 'top': .95}
    BasicLabel:
        text: root.description
        font_size: '10sp'
        color: .2, .2, .2, 1
        pos_hint: {'x': .2, 'top': .525}
    BasicButton:
        text: f'R${root.price}'
        pos_hint: {'right': .95, 'center_y': .5}
        size_hint: .2, .6
        on_press:
            self.parent.parent.mid.open(root.title, root.img, root.description, root.price)
        
<MenuPage>:
    Background:
    FloatLayout:
        TopImageBar:
            lm: _lm
        BasicLabel:
            text: '  Lanches'
            pos_hint: {'x': 0, 'center_y': .85}
            font_size: '20sp'
        BasicIconButton:
            text: 'Carrinho'
            icon: 'cart'
            icon_size: '20sp'
            font_size: '20sp'
            text_color: 'white'
            icon_color: 'white'
            size_hint: .3, .1
            pos_hint: {'right': 1, 'center_y': .85}
        MDRelativeLayout:
            pos_hint: {'x': 0, 'top': .79}
            size_hint: 1, .1
            MenuIconButton:
                icon: 'hamburger'
                pos_hint: {'x': .025}
            MenuIconButton:
                icon: 'french-fries'
                pos_hint: {'x': .275}
            MenuIconButton:
                icon: 'bottle-soda-classic-outline'
                pos_hint: {'x': .525}
            MenuIconButton:
                icon: 'ice-cream'
                pos_hint: {'x': .775}
        MDLabel:
            canvas: 
                Color:
                    rgb: 1, 1, 1
                Line:
                    points: 0, self.y, self.x + self.width, self.y
                    width: 1
            text: '  [b]Cardápio[/b]'
            size_hint: 1, .075
            markup: True
            font_size: '20sp'
            pos_hint: {'x': 0, 'center_y': .65}
            font_name: join('views', 'data', 'Graduate-Regular.ttf')
        ScrollView:
            pos_hint: {'center_x': .5, 'top': .6}
            size_hint: 1, .5
            MDStackLayout:
                mid: _mid
                spacing: 0, 10
                padding: 10
                adaptive_height: True
                MenuItem:
                    title: 'Hamburguer'
                    price: 10
                MenuItem:
                MenuItem:
                MenuItem:
                MenuItem:
                MenuItem:
        BottomBar:
        LateralMenu:
            id: _lm
        MenuItemData:
            id: _mid
'''
)

class MenuPage(MDScreen):
    name = 'menu_page'
    
class MenuItemData(MDRelativeLayout):
    description = StringProperty('description')
    open_animation = Animation(pos_hint={'y': 0}, bg_opacity=0.5, duration=0.1)
    close_animation = Animation(pos_hint={'y': -0.6}, bg_opacity=0, duration=0.1)
    def open(self, title, img, description, price):
        self.title = title
        self.img = img
        self.description = description 
        self.price = price
        self.quantity = 1
        self.open_animation.start(self)
    def close(self):
        self.close_animation.start(self)
    def on_touch_down(self, touch):
        if not self.collide_point(touch.x, touch.y):
            self.close()
        return super().on_touch_down(touch)