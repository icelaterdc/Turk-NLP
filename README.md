# TurkNLP – Geniş Kapsamlı Türkçe Doğal Dil İşleme (NLP) Kütüphanesi

TurkNLP, Türkçe dili için sıfırdan geliştirilmiş, modüler halinde organize edilmiş, genisletilebilir ve modern bir doğal dil işleme kütüphanesidir. Amaç; hem akademik çalışmalarda hem de endüstriyel projelerde Türkçe NLP çalışmalarını desteklemektir.

## Özellikler

* ✨ **Tokenizasyon**: Türkçe diline uygun noktalama ve ek ayrışması
* 🪤 **Morfolojik Çözümleme**: Ek ayrışması, kök bulma ve yapısal analiz
* 🔮 **POS Tagging**: Türkçe için özelleştirilmiş sözcük türü etiketleme
* 🧬 **Ad Öbeği Çıkarımı (NER)**: Küçük ve orta boyutlu Türkçe NER modelleri
* ⚖️ **Sentiment Analizi**: Türkçe duygu sınıflandırması için hazır modeller
* 🧬 **Leksik Analiz**: Sözcük özellikleri, kelime türevleri, anlam frekansları
* 🔢 **Makine Öğrenmesi ve Transformer Entegrasyonu**: Huggingface destekli modeller
* ⚙️ **Modüler Arası Bağlantı**: Her modül, diğerleriyle uyumlu çalışır
* 🔧 **API ve CLI Arayüzleri**: Kolay entegrasyon ve terminal üzerinden çalışma

## Dizin Yapısı

```
TurkNLP/
├── turknlp/                # Ana Python modülü
│   ├── tokenization/
│   ├── morphology/
│   ├── pos/
│   ├── ner/
│   ├── sentiment/
│   ├── lexicon/
│   ├── transformers/
│   ├── cli/
│   └── utils/
├── tests/                  # Birim testleri
├── examples/               # Kullanım örnekleri (notebook)
├── data/                   # Örnek veri setleri ve modeller
├── scripts/                # Model eğitimi ve işleme scriptleri
├── .github/workflows/      # Otomatik test/CI betikleri
├── requirements.txt
├── setup.py
└── README.md
```

## Kurulum

```bash
pip install -r requirements.txt
python setup.py install
```

## Temel Kullanım

```python
from turknlp.tokenization import TurkishTokenizer
from turknlp.morphology import MorphAnalyzer

text = "Ankara'da hava oldukça güzel."
tokens = TurkishTokenizer().tokenize(text)
morphs = MorphAnalyzer().analyze(tokens)

for token, morph in zip(tokens, morphs):
    print(token, morph)
```

## Çevrim İçi Modeller

TurkNLP, Huggingface modelleriyle entegredir. Ağaç yapısında `transformers/` dizinindeki betikleri kullanarak T5, BERT tabanlı önceden eğitilmiş modelleri çağırabilirsiniz.

```python
from turknlp.transformers import TurkishBERTNER
ner_model = TurkishBERTNER()
print(ner_model.predict("Mustafa Kemal Atatürk, Türkiye Cumhuriyeti'nin kurucusudur."))
```

## Testler

```bash
pytest tests/
```

## Yol Haritası

* [x] Tokenizer
* [x] Morfolojik analiz
* [x] POS tagging
* [x] NER
* [x] Sentiment
* [x] Transformer destek
* [ ] Bağlam bazlı anlambilim (Word Sense Disambiguation)
* [ ] Dil modeli destekli metin üretimi

## Katkı

Pull request'ler, hata bildirimleri ve yeni özellik önerileri açıktır.

```bash
git clone https://github.com/icelaterdc/Turk-NLP.git
cd Turk-NLP
git checkout -b yeni-ozellik
```

## Lisans

MIT Lisansı ile sunulmuştur.

---

> "TurkNLP, Türkçe NLP alanında açık kaynak, şeffaf ve gelişime açık bir altyapı sunmayı hedefler."
