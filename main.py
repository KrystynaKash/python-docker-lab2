from googletrans import Translator, LANGUAGES

def CodeLang(lang):
    lang = lang.lower()
    if lang in LANGUAGES: # якщо ввели код (en)
        return LANGUAGES[lang].capitalize()
    for code, name in LANGUAGES.items(): # якщо ввели назву (english)
        if name.lower() == lang:
            return code
    return "Error: Language not found"

def LangDetect(txt):
    translator = Translator()
    result = translator.detect(txt)
    return f"Language: {result.lang}, Confidence: {result.confidence}"

def TransLate(text, lang):
    translator = Translator()
    try:
        # Визначаємо код мови, якщо ввели назву
        dest_code = CodeLang(lang) if len(lang) > 3 else lang
        result = translator.translate(text, dest=dest_code)
        return result.text
    except Exception as e:
        return f"Error: {str(e)}"

if __name__ == "__main__":
    text_to_translate = "Привіт, як справи?"
    target_language = "English" # Можна міняти на 'en' або 'English'
    
    print(LangDetect(text_to_translate))
    print(f"Code/Name: {CodeLang(target_language)}")
    print(f"Translation: {TransLate(text_to_translate, target_language)}")