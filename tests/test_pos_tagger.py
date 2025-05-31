import pytest
from turknlp.core.pos_tagger import TurkishPosTagger

def test_pos_tag_basic():
    tagger = TurkishPosTagger()
    tokens = ["Merhaba", "dünya"]
    tagged = tagger.tag(tokens)
    assert isinstance(tagged, list)
    assert tagged[0] == ("Merhaba", "NOUN")
