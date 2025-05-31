# Bu dosya temel bir BERT wrapper'ı içerecek
class TrBertBase:
    """Türkçe BERT temel modeli wrapper"""

    def __init__(self, model_name='dbmdz/bert-base-turkish-cased'):
        self.model_name = model_name

    def load_model(self):
        raise NotImplementedError("Model yüklenmesi uygulanmadı.")
