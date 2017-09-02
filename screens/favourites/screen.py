from kivy.lang import Builder
from kivy.uix.gridlayout import GridLayout
from kivy.properties import ObjectProperty

from screens.base.screen import BaseScreen

from utils.store import get_favorives


Builder.load_file('screens/favourites/favourites.kv')


class Translation(GridLayout):
    text = ObjectProperty()
    translation = ObjectProperty()


class FavouritesScreen(BaseScreen):
    translations_wrapper = ObjectProperty(None)

    def __init__(self, *args, **kwargs):
        super(FavouritesScreen, self).__init__()
        self.translations_wrapper.bind(minimum_height=self.translations_wrapper.setter('height'))
        self.on_get_saved_translations()

    def on_get_saved_translations(self):
        translations_list = get_favorives()
        translations_wrapper = self.ids.translations_wrapper
        for tr_description in translations_list:
            text = tr_description[1]['text']
            translation = tr_description[1]['translation']
            translation_view = Translation(text=text, translation=translation)
            translation_view.bind(minimum_height=translation_view.setter('height'))
            translations_wrapper.add_widget(translation_view)
