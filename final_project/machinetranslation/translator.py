import json
import os
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from dotenv import load_dotenv
load_dotenv()
apikey = os.environ.get("apikey")
url = os.environ.get("url")
authenticator = IAMAuthenticator(apikey)
language_translator = LanguageTranslatorV3(
    version='2018-05-01', authenticator=authenticator)
language_translator.set_service_url(url)


def english_to_french(text: str = "Enter translated text", source: str = "Enter Source Language", target: str = "Enter Target Language"):
    '''translate text from english to french'''
    source = "en"
    target = "fr"
    translation = language_translator.translate(
        text=text,
        source=source,
        target=target).get_result()
    print(json.dumps(translation, indent=2, ensure_ascii=False))


def french_to_english(text: str = "Enter translated text", source: str = "Enter Source Language", target: str = "Enter Target Language"):
    '''translate text from french to english'''
    source = "fr"
    target = "en"
    translation = language_translator.translate(
        text=text,
        source=source,
        target=target).get_result()
    if text == "":
        print("No value entered")
    else:
        print(json.dumps(translation, indent=2, ensure_ascii=False))
