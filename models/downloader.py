import os

class ModelDownloader:
    """Model indirme ve cache yönetimi"""

    def __init__(self, cache_dir=None):
        self.cache_dir = cache_dir or os.path.expanduser('~/.cache/turknlp/models')

    def download(self, model_name, version=None):
        """Belirtilen modeli indirir (henüz uygulanmadı)."""
        raise NotImplementedError("Model indirici henüz uygulanmadı.")
