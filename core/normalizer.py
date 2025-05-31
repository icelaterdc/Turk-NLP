import unicodedata

class TurkishNormalizer:
    """Türkçe metin normalizasyonu (lowercase, unicode normalization, temizleme)"""

    def __init__(self):
        pass

    def normalize(self, text: str):
        """Normalize edilmiş metni döner."""
        if not isinstance(text, str):
            raise TypeError("text must be a string")
        text = unicodedata.normalize('NFC', text)
        text = text.lower()
        text = ' '.join(text.split())
        return text
