WINDOW_WIDTH = 512
WINDOW_HEIGHT = 288

KIVY_FONTS = [
    {
        "name": "FontAwesome",
        "fn_regular": "assets/fonts/fontawesome.ttf"
    },
]

YANDEX_TRANSLATOR_API_KEY = ''

try:
    from local_settings import *
except ImportError:
    pass