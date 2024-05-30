import requests
import json

def translate_text(text, target_lang):
    api_key = 'eff154b0-86c4-df24-76fe-4a2304a44b37:fx'
    url = 'https://api-free.deepl.com/v2/translate'

    params = {
        'auth_key': api_key,
        'text': text,
        'target_lang': target_lang  # The language into which the text should be translated
    }

    response = requests.post(url, data=params)
    translation = json.loads(response.content)

    return translation['translations'][0]['text']


