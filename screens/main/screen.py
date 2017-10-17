from kivy.lang import Builder

from core.translator_engine import TranslatorEngine
from screens.base.screen import BaseScreen


from utils.store import save_translation


Builder.load_file('screens/main/main.kv')


class MainScreen(BaseScreen):
    original_lang = ['eng', 'Английский']
    expected_transl = ['rus', 'Русский']
    tr_engine = None

    def __init__(self, *args, **kwargs):
        super(MainScreen, self).__init__()
        self.tr_engine = TranslatorEngine()

    def on_language_choice(self):
        """
        Updates translation direction
        :return:
        """
        self.original_lang, self.expected_transl = self.expected_transl, self.original_lang
        self.ids.output_view.text = ''

    def translate_text(self):
        text = self.ids.input.text
        translation = self.tr_engine.translate_text(text, self.original_lang[0], self.expected_transl[0])
        output_view = self.ids.output_view
        output_view.text = translation

    def on_save_translation(self):
        text = self.ids.input.text
        translation = self.ids.output_view.text
        save_translation(
            text=text,
            original_lang=self.original_lang[0],
            translation=translation,
            expected_transl=self.expected_transl[0])
