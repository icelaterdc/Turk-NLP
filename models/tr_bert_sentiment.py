# Duygu analizi için BERT wrapper
class TrBertSentiment:
    """Türkçe duygu analizi modeli"""

    def __init__(self, model_name='saglamyigit/bert-base-turkish-sentiment-cased'):
        self.model_name = model_name

    def predict(self, text):
        raise NotImplementedError("Duygu analizi tahmini uygulanmadı.")
