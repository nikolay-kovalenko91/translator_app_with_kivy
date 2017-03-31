from requests import Session

from core.translators.yandex_translator import YandexTranslator


class TranslatorEngine:
    _ya_translator = None

    def __init__(self):
        self._ya_translator = YandexTranslator()

    def translate_text(self, text, original_lang, expected_lang):
        res = self._ya_translator.translate_text(text, original_lang, expected_lang)
        return res
