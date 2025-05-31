from turknlp.pipelines.basic_pipeline import BasicPipeline

class SummarizePipeline:
    """Özetleme pipeline (basit stub)"""

    def __init__(self):
        self.pipeline = BasicPipeline()
        # Özetleyici model placeholder
        self.model = None

    def summarize(self, text: str):
        data = self.pipeline.process(text)
        # Henüz özetleme uygulanmadı; sadece ilk cümleyi döner
        sentences = text.split('.')
        summary = sentences[0] if sentences else ''
        return {
            'summary': summary,
            'pipeline_output': data
        }
