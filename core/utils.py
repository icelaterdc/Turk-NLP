# Genel yardımcı fonksiyonlar ve sabitler

def load_stopwords(path):
    """Stop-word listesini dosyadan yükler."""
    with open(path, 'r', encoding='utf-8') as f:
        stopwords = [line.strip() for line in f if line.strip()]
    return set(stopwords)
