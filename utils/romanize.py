from indic_transliteration import sanscript
from indic_transliteration.sanscript import transliterate

# Supported Indian languages
LANG_MAP = {
    "hi": sanscript.DEVANAGARI,
    "mr": sanscript.DEVANAGARI,
    "bn": sanscript.BENGALI,
    "ta": sanscript.TAMIL,
    "te": sanscript.TELUGU,
    "gu": sanscript.GUJARATI,
    "pa": sanscript.GURMUKHI,
}

def romanize_text(text, lang):
    """
    Romanizes Indian language text.
    English words remain unchanged automatically.
    """
    if lang not in LANG_MAP:
        return text

    return transliterate(
        text,
        LANG_MAP[lang],
        sanscript.ITRANS
    )
