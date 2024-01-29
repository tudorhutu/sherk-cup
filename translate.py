from deep_translator import GoogleTranslator
import random
langs_list = GoogleTranslator().get_supported_languages()
def translate_to_greek(text):    
    random_lang = random.sample(sorted(set(langs_list)), 1)    
    translated_text = GoogleTranslator(source='auto', target = str(random_lang[0])).translate(text)
    return translated_text
