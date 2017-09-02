import hashlib

from kivy.storage.jsonstore import JsonStore


def save_translation(text='', original_lang='eng', translation='', expected_transl='rus'):

    store = JsonStore('kivy_translator.json')
    key = '{}{}'.format(text, translation).encode('utf-8')
    key_hash_object = hashlib.md5(key)
    uuid = key_hash_object.hexdigest()
    direction = '{}-{}'.format(original_lang, expected_transl)

    store.put(uuid, direction=direction, text=text, translation=translation)


def get_favorives():
    store = JsonStore('kivy_translator.json')
    entries = list((x for x in store.find()))
    return entries
