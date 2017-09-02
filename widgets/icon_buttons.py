from kivy.lang import Builder
from kivy.uix.button import Button


Builder.load_file('widgets/kv/icon_buttons.kv')


class IconButton(Button):
    pass


class FooterMenuButton(IconButton):
    pass


class PanelButton(IconButton):
    pass
