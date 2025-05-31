import re

def normalize_whitespace(text: str):
    """Metindeki fazla boşlukları birleştirir."""
    return ' '.join(text.split())
