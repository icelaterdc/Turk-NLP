import json
import os

class TurkishLemmatizer:
    """Türkçe lemmatizer; kural tabanlı ve model tabanlı modlar."""

    def __init__(self, mode='rule', exception_dict=None):
        self.mode = mode
        if mode == 'rule':
            # Yorum: exception_dict, kendi JSON dosyanızı verebilirsiniz
            if exception_dict:
                with open(exception_dict, 'r', encoding='utf-8') as f:
                    self.exceptions = json.load(f)
            else:
                # Varsayılan boş dict
                self.exceptions = {}
        else:
            raise NotImplementedError("Model-based lemmatizer henüz uygulanmadı.")

    def lemmatize(self, word: str):
        """Kelimenin kökünü döner."""
        if not isinstance(word, str):
            raise TypeError("word must be a string")
        # Basit kural: exception dict kontrolü
        if word in self.exceptions:
            return self.exceptions[word]
        # Son eki kaldırma (örnek)
        for suffix in ['ler', 'lar', 'ci', 'cı', 'lik', 'lık', 'cular', 'cular']:
            if word.endswith(suffix):
                return word[: -len(suffix)]
        return word
