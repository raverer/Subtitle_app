from indic_transliteration import sanscript
from indic_transliteration.sanscript import transliterate

SUPPORTED = {
    "hi": sanscript.DEVANAGARI,
    "mr": sanscript.DEVANAGARI,
    "bn": sanscript.BENGALI,
    "ta": sanscript.TAMIL,
    "te": sanscript.TELUGU,
    "gu": sanscript.GUJARATI,
    "pa": sanscript.GURMUKHI,
}

def romanize_text(text, lang):
    if lang not in SUPPORTED:
        return text  # fallback

    return transliterate(
        text,
        SUPPORTED[lang],
        sanscript.ITRANS
    )
