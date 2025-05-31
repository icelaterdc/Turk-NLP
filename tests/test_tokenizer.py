import pytest
from turknlp.core.tokenizer import TurkishTokenizer

def test_tokenize_simple():
    tokenizer = TurkishTokenizer()
    text = "Merhaba dünya!"
    tokens = tokenizer.tokenize(text)
    assert tokens == ["Merhaba", "dünya", "!"]

def test_tokenize_empty():
    tokenizer = TurkishTokenizer()
    tokens = tokenizer.tokenize("")
    assert tokens == []
