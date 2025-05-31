import pytest
from turknlp.core.lemmatizer import TurkishLemmatizer

def test_lemmatize_exception(tmp_path):
    # Create temporary exception dict
    data = {"koşuyorum": "koş"}
    file_path = tmp_path / "exceptions.json"
    file_path.write_text(str(data))

    lemmatizer = TurkishLemmatizer(mode="rule", exception_dict=str(file_path))
    assert lemmatizer.lemmatize("koşuyorum") == "koş"

def test_lemmatize_suffix():
    lemmatizer = TurkishLemmatizer(mode="rule")
    assert lemmatizer.lemmatize("kitaplar") == "kitap"
    assert lemmatizer.lemmatize("sevci") == "sev"
