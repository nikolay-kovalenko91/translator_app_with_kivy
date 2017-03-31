from kivy.uix.screenmanager import ScreenManager, SlideTransition

from screens.main.screen import MainScreen
from screens.about.screen import AboutScreen


sm = ScreenManager(transition=SlideTransition())
screens = {
    'main': MainScreen,
    'about': AboutScreen,
}
