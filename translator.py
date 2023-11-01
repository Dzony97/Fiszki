import requests
import json

def translate_text(text, target_lang):
    api_key = 'TRANSLATOR_KEY'
    url = 'https://api-free.deepl.com/v2/translate'

    params = {
        'auth_key': api_key,
        'text': text,
        'target_lang': target_lang
    }

    response = requests.post(url, data=params)
    translation = json.loads(response.content)

    return translation['translations'][0]['text']


