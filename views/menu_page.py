from kivymd.uix.screen import MDScreen
from kivy.lang import Builder
from kivy.properties import StringProperty, BooleanProperty, NumericProperty
from views.utils import BottomMenu

Builder.load_string('''
#:import MenuIconButton views.utils
#:import BasicLabel views.utils
#:import BasicButton views.utils
#:import BasicTextField views.utils
#:import LateralMenu views.utils
#:import TopImageBar views.utils
#:import Background views.utils
#:import SelectImageButton views.utils
#:import LateralMenuBase views.utils
#:import join os.path.join

<ShoppingCart@LateralMenuBase>:


<MenuItemData>:
    BasicLabel:
        text: root.title
        color: .2, .2, .2, 1
        font_size: '17.5sp'
        pos_hint: {'center_x': .5, 'top': .975}
    MDIconButton:
        id: _img
        icon_size: '90sp'
        md_bg_color: app.theme_cls.primary_color
        icon: root.img
        pos_hint: {'center_x': .5, 'center_y': .65}
    BasicButton:
        text: '+Carrinho'
        pos_hint: {'right': .975, 'top': .9}
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

<MenuItemEditable>:
    BasicTextInput:
        hint_text: "Digite o nome do produto"
        font_size: '17.5sp'
        pos_hint: {'center_x': .5, 'top': .975}
        size_hint: .96, .1 
    SelectImageButton:
        pos_hint: {'center_x': .5, 'center_y': .7}
        avatar: False
        size_hint: .3, .3
    BasicButton:
        text: 'Salvar'
        pos_hint: {'right': .975, 'top': .85}
    BasicTextInput:
        hint_text: 'Dê uma descrição ao produto'
        font_size: '15sp'
        pos_hint: {'x': .025, 'center_y': .4}
        size_hint: .96, .25
        multiline: True
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
            text: 'R$'
            color: 0, 0, 0, 1
            font_size: '20sp'
            pos_hint: {'x': .05, 'center_y': .5}
        BasicTextInput:
            id: _price
            text: '0'
            price: float(0 if self.text == '' else self.text)
            font_size: '20sp'
            background_color: 0, 0, 0, 0
            pos_hint: {'x': .15, 'center_y': .5}
            size_hint: .96, .5
            input_filter: 'float'
        MDIconButton:
            icon: 'minus'
            theme_icon_color: 'Custom'
            icon_color: 0, 0, 0, 1
            pos_hint: {'x': .7, 'center_y': .5}
            on_press:
                _price.text = str(_price.price - (0 if _price.price <= 0 else 1)) 
        MDIconButton:
            icon: 'plus'
            theme_icon_color: 'Custom'
            icon_color: 0, 0, 0, 1
            pos_hint: {'x': .8, 'center_y': .5}
            on_press:
                _price.text = str(_price.price + 1)
        
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
        md_bg_color: app.theme_cls.primary_color
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
            self.parent.parent.menu.open(root.title, root.img, root.description, root.price)
        
<MenuPage>:
    id: _screen
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
            on_press:
                _sp.open()
        MDRelativeLayout:
            pos_hint: {'x': 0, 'top': .79}
            size_hint: 1, .1
            MenuIconButton:
                editable: _screen.editable
                icon: 'hamburger'
                pos_hint: {'x': .025}
            MenuIconButton:
                editable: _screen.editable
                icon: 'french-fries'
                pos_hint: {'x': .275}
            MenuIconButton:
                editable: _screen.editable
                icon: 'bottle-soda-classic-outline'
                pos_hint: {'x': .525}
            MenuIconButton:
                editable: _screen.editable
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
                menu: _mie if _screen.editable else _mid
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
        MenuItemEditable:
            id: _mie
        ShoppingCart:
            id: _sp
'''
)

class MenuPage(MDScreen):
    name = 'menu_page'
    editable = BooleanProperty(False)
    
class MenuItemData(BottomMenu):
    title = StringProperty('title')
    img = StringProperty('img')
    description = StringProperty('description')
    price = NumericProperty(35)
    quantity = NumericProperty(1)

    def open(self, title, img, description, price):
        self.title = title
        self.img = img
        self.description = description
        self.price = price
        self.quantity = 1
        super().open()

class MenuItemEditable(BottomMenu):
    def open(self, *args):
        for child in self.children: 
            if 'TextInput' in str(child): child.text = ''
        super().open()
    
    