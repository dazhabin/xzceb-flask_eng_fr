"""
Functions for English to French and French to English translation
"""

from deep_translator import MyMemoryTranslator

def english_to_french(english_text):
    """
    This function returns string translated from English to French
    """
    french_text = MyMemoryTranslator(source='english', target='french').translate(english_text)
    return french_text

def french_to_english(french_text):
    """
    This function returns string translated from French to English
    """
    english_text = MyMemoryTranslator(source='french', target='english').translate(french_text)
    return english_text
