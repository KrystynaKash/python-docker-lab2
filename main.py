from googletrans import Translator, LANGUAGES
# Функція для конвертації назви мови в код
def CodeLang(lang):
    lang = lang.lower()
    if lang in LANGUAGES:  # Якщо введено код ('en'), функція повертає повну назву ('English')
        return LANGUAGES[lang].capitalize()
    for code, name in LANGUAGES.items(): # Якщо введено назву ('english'), функція шукає і повертає її код ('en')
        if name.lower() == lang:
            return code
    return "Error: Language not found"

# Функція для визначення мови вхідного тексту
def LangDetect(txt):
    translator = Translator()
    result = translator.detect(txt)
    return f"Language: {result.lang}, Confidence: {result.confidence}" # Повертає код мови та рівень впевненості алгоритму (від 0 до 1)

# Основна функція для перекладу
def TransLate(text, lang):
    translator = Translator()
    try:
        # Визначаємо цільовий код мови: 
        # Якщо назва довша за 3 символи, вважаємо її повною і конвертуємо в код
        dest_code = CodeLang(lang) if len(lang) > 3 else lang
        result = translator.translate(text, dest=dest_code)
        return result.text
    except Exception as e:
        return f"Error: {str(e)}"

if __name__ == "__main__":
    text_to_translate = "Привіт, як тебе звати?"
    target_language = "English" 
    
    print(f'Text to translate: {text_to_translate}')
    print(LangDetect(text_to_translate))
    print(f"Code/Name: {CodeLang(target_language)}")
    print(f"Translation: {TransLate(text_to_translate, target_language)}")