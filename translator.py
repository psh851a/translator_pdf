from googletrans import Translator

def translate_to_chinese(text):
    if not isinstance(text, str) or not text:
        raise ValueError("Invalid input text for translation")
        
    translator = Translator()
    try:
        translation = translator.translate(text, src='en', dest='zh-cn')
    except Exception as e:
        raise ValueError(f"Translation service error: {str(e)}")
    
    if not translation or not hasattr(translation, 'text') or translation.text is None:
        raise ValueError("Translation service returned malformed response")
    
    return str(translation.text)
