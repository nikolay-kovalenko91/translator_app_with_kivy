from kivy.lang import Builder
from kivy.uix.screenmanager import Screen


Builder.load_file('screens/base/base.kv')


class BaseScreen(Screen):
    def __init__(self, *args, **kwargs):
        super(BaseScreen, self).__init__()
        header = self.ids.header
        header_label = header.ids.label
        header_label.on_ref_press = self.on_title_press

    def on_title_press(self, *args):
        pass