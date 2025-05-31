from turknlp.pipelines.basic_pipeline import BasicPipeline

class SentimentPipeline:
    """Duygu analizi pipeline (basit stub)"""

    def __init__(self):
        self.pipeline = BasicPipeline()
        # Duygu analizi model placeholder
        self.model = None

    def predict(self, text: str):
        data = self.pipeline.process(text)
        # Henüz duygu analizi uygulanmadı; sadece nötr döner
        return {
            'sentiment': 'neutral',
            'pipeline_output': data
        }
