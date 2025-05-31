import re

class TurkishSentenceSplitter:
    """Türkçe cümle bölücü; noktalama bazlı basit yaklaşım"""

    def __init__(self):
        self.pattern = re.compile(r'(?<=[.!?])\s+')

    def split(self, text: str):
        """Metni cümlelere böler."""
        if not isinstance(text, str):
            raise TypeError("text must be a string")
        sentences = self.pattern.split(text.strip())
        return [s for s in sentences if s]
