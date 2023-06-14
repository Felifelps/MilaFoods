from kaki.app import App
from main import ScreenManager, MilaFoods

class Live(App, MilaFoods):
    CLASSES = {
        "ScreenManager": "main.ScreenManager"
    }
    AUTORELOADER_PATHS = [
        (".", {"recursive": True}),
    ]
    def build_app(self):
        return ScreenManager(self)

Live().run()