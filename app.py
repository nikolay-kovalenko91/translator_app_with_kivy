from kivy.app import App

from settings import WINDOW_HEIGHT, WINDOW_WIDTH, KIVY_FONTS

from kivy.config import Config
Config.set('graphics', 'width', WINDOW_HEIGHT)
Config.set('graphics', 'height', WINDOW_WIDTH)

from screens.screenmanager import sm, screens
from kivy.uix.screenmanager import ScreenManagerException
from kivy.core.text import LabelBase


class TranslatorApp(App):
    title = 'Translator'
    screen_manager = None

    def initialize_app(self):
        self.screen_manager = sm
        self.switch_screen('main')
        for font in KIVY_FONTS:
            LabelBase.register(**font)

    def switch_screen(self, screen_name):
        if screen_name in screens.keys():
            screen = screens[screen_name](name=screen_name)
            self.screen_manager.switch_to(screen)
            return
        else:
            raise ScreenManagerException('Screen {} not found'.format(screen_name))

    def build(self):
        self.initialize_app()
        return self.screen_manager


TranslatorApp().run()

