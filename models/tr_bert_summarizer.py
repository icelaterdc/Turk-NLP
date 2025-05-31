# Özetleme için BERT/T5 wrapper
class TrBertSummarizer:
    """Türkçe özetleme modeli"""

    def __init__(self, model_name='deniz/transformer-summarizer-tr'):
        self.model_name = model_name

    def summarize(self, text):
        raise NotImplementedError("Özetleme uygulanmadı.")
