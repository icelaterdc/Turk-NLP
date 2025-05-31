import re

class TurkishTokenizer:
    """Türkçe metin için basit regex tabanlı tokenizasyon"""

    def __init__(self):
        # Kelime ayırıcı regex: boşluk ve noktalama
        self.pattern = re.compile(r"\w+|[^\w\s]", re.UNICODE)

    def tokenize(self, text: str):
        """Verilen metni token'lara böler."""
        if not isinstance(text, str):
            raise TypeError("text must be a string")
        tokens = self.pattern.findall(text)
        return tokens
