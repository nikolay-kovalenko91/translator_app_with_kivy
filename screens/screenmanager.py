from kivy.uix.screenmanager import ScreenManager, SlideTransition

from screens.main.screen import MainScreen
from screens.about.screen import AboutScreen
from screens.favourites.screen import FavouritesScreen


sm = ScreenManager(transition=SlideTransition())
screens = {
    'main': MainScreen,
    'about': AboutScreen,
    'favourites': FavouritesScreen,
}
