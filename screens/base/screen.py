from kivy.lang import Builder
from kivy.uix.screenmanager import Screen


Builder.load_file('screens/base/base.kv')


class BaseScreen(Screen):

    def on_language_choice(self, *args):
        pass
    