from kaki.app import App
from kivymd.factory_registers import Factory

class Live(App):
    CLASSES = {
        "ClientProfilePage": "views.client_profile_page"
    }
    AUTORELOADER_PATHS = [
        (".", {"recursive": True}),
    ]
    def build_app(self):
        return Factory.ScreenManager()

Live().run()