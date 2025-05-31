from turknlp.core.tokenizer import TurkishTokenizer
from turknlp.core.normalizer import TurkishNormalizer
from turknlp.core.lemmatizer import TurkishLemmatizer
from turknlp.core.pos_tagger import TurkishPosTagger

class BasicPipeline:
    """Basit pipeline: normalize → tokenize → lemmatize → pos tagger"""

    def __init__(self):
        self.normalizer = TurkishNormalizer()
        self.tokenizer = TurkishTokenizer()
        self.lemmatizer = TurkishLemmatizer()
        self.pos_tagger = TurkishPosTagger()

    def process(self, text: str):
        text = self.normalizer.normalize(text)
        tokens = self.tokenizer.tokenize(text)
        lemmas = [self.lemmatizer.lemmatize(tok) for tok in tokens]
        pos_tags = self.pos_tagger.tag(tokens)
        return {
            'normalized_text': text,
            'tokens': tokens,
            'lemmas': lemmas,
            'pos_tags': pos_tags
        }
