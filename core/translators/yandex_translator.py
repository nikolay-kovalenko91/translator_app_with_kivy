import json
from requests import Session, exceptions

from kivy.logger import Logger

from settings import YANDEX_TRANSLATOR_API_KEY


YANDEX_TRANSLATOR_URL = 'https://translate.yandex.net/api/v1.5/tr.json/translate'


class YandexTranslator:
    _languages_codes = {
        'eng': 'en',
        'rus': 'ru'
    }

    def translate_text(self, text, original_lang, expected_lang):
        data = {
            'key': YANDEX_TRANSLATOR_API_KEY,
            'text': text,
            'lang': '{}-{}'.format(self._languages_codes[original_lang], self._languages_codes[expected_lang])
        }
        return self._send_data(data)

    def _send_data(self, data):
        session = Session()
        res = None
        try:
            res = session.post(YANDEX_TRANSLATOR_URL, data=data)
        except exceptions.ConnectionError as e:
            Logger.error('Internet connection error: {}'.format(e))
            return ''
        res_json_text = json.loads(res.text)
        res_text = ''
        if res.status_code is not 200:
            Logger.error('{} - Bad request'.format(res.status_code))
            return res_text
        if 'text' in res_json_text:
            res_text = res_json_text['text'][0]
        return res_text

