import googletrans

translator = googletrans.Translator()
lang_dict = googletrans.LANGUAGES
lang_code_dict = googletrans.LANGCODES
lang_list = list(googletrans.LANGUAGES.keys())


def translate(text: str, lang_name=None, lang_code=None):
    if lang_name:
        to_lang = lang_code_dict.get(lang_name)
    elif lang_code:
        to_lang = lang_code
    else:
        to_lang = "en"
    return_text = translator.translate(text=text, src="en", dest=to_lang)
    return return_text.text
