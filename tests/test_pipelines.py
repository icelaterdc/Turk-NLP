import pytest
from turknlp.pipelines.basic_pipeline import BasicPipeline

def test_basic_pipeline_structure():
    pipeline = BasicPipeline()
    result = pipeline.process("Merhaba dünya")
    assert "tokens" in result
    assert "lemmas" in result
    assert "pos_tags" in result
