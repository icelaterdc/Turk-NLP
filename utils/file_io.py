import os
import shutil

def load_json(path):
    """JSON dosyasını yükler ve dict döner."""
    import json
    with open(path, 'r', encoding='utf-8') as f:
        return json.load(f)

def clear_cache():
    """~/.cache/turknlp dizinini temizler."""
    cache_dir = os.path.expanduser('~/.cache/turknlp')
    if os.path.exists(cache_dir):
        shutil.rmtree(cache_dir)
        print(f'Cache temizlendi: {cache_dir}')
    else:
        print('Cache dizini bulunamadı.')
