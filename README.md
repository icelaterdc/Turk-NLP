# TurkNLP – Geniş Kapsamlı Türkçe Doğal Dil İşleme (NLP) Kütüphanesi

TurkNLP, Türkçe dili için sıfırdan geliştirilmiş, modüler yapıya sahip, genişletilebilir ve modern bir doğal dil işleme (NLP) kütüphanesidir. Amaç; hem akademik çalışmalarda hem de endüstriyel projelerde Türkçe NLP alanındaki ihtiyaçlara açık kaynaklı bir çözüm sunmaktır.

## Özellikler

* ✨ **Tokenizasyon**: Türkçeye uygun kelime ve cümle ayırma
* 🧠 **Morfolojik Çözümleme**: Ek ayrıştırma ve kök bulma
* 🔎 **POS Tagging**: Kelime türü etiketleme
* 🧾 **Ad Öbeği Çıkarımı (NER)**: Kişi, kurum, yer vs. tanıma
* ⚖️ **Duygu Analizi**: Türkçeye uygun olumlu/olumsuz duygu sınıflandırma
* 📚 **Leksik Analiz**: Sözlük tabanlı yapı ve anlamsal analiz
* 🤖 **Transformer Entegrasyonu**: Huggingface destekli modellerle çalışma
* ⚙️ **Modüler Mimari**: Her modül bağımsız ve entegre çalışabilir
* 🧪 **CLI ve API desteği**: Komut satırı ve REST API üzerinden kullanım

## Dizin Yapısı

```
TurkNLP/
├── turknlp/                # Ana Python modülü
│   ├── tokenization/       # Tokenizer sınıfları
│   ├── morphology/         # Morfolojik analiz
│   ├── pos/                # POS tagging
│   ├── ner/                # Named Entity Recognition
│   ├── sentiment/          # Duygu analizi modelleri
│   ├── transformers/       # Transformer modelleri entegrasyonu
│   └── utils/              # Yardımcı araçlar
├── tests/                  # Birim testleri
├── examples/               # Jupyter örnekleri
├── pyproject.toml          # Proje yapılandırması (Poetry tabanlı)
├── README.md
└── .github/workflows/      # Otomatik test/CI betikleri
```

## Kurulum

Bu proje [Poetry](https://python-poetry.org/) ile yapılandırılmıştır. Eğer Poetry yüklü değilse:

```bash
pip install poetry
```

Projeyi kurmak için:

```bash
git clone https://github.com/kullaniciadi/turknlp.git
cd turknlp
poetry install
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

## Transformer Destekli Modeller

```python
from turknlp.transformers import TurkishBERTNER
model = TurkishBERTNER()
result = model.predict("Mustafa Kemal Atatürk Türkiye Cumhuriyeti'nin kurucusudur.")
print(result)
```

## Testler

```bash
poetry run pytest tests/
```

## Yol Haritası

* [x] Tokenizer
* [x] Morfolojik analiz
* [x] POS tagging
* [x] NER
* [x] Sentiment
* [x] Transformer destek
* [ ] Bağlam bazlı anlambilim (WSD)
* [ ] Dil modeli destekli metin üretimi

## Katkı

Projeye katkı sağlamak için forkladıktan sonra PR gönderebilirsiniz:

```bash
git clone https://github.com/icelaterdc/Turk-NLP.git
cd Turk-NLP
git checkout -b yeni-ozellik
```

## Lisans

MIT Lisansı ile lisanslanmıştır.

---

> "TurkNLP, Türkçeye özel geliştirilen açık kaynak NLP araçları için güçlü bir temel sunmayı hedefler."
