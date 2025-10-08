# Traduit les noms propres jopnais en anglais
import csv
import json
import pandas as pd

# Fonction pour charger le cache
def load_cache(cache_file):
    try:
        with open(cache_file, 'r', encoding='utf-8') as f:
            return json.load(f)
    except FileNotFoundError:
        return {}

# Fonction pour sauvegarder le cache
def save_cache(cache, cache_file):
    with open(cache_file, 'w', encoding='utf-8') as f:
        json.dump(cache, f, ensure_ascii=False, indent=4)

# Si la valeur n'est pas dans le cache, demande la traduction
def ask_translation(text):
    print(f"Traduction pour '{text}': ", end="")
    return input().strip()

def annotate_csv(input_file, output_file, cache_file='translation_cache.json'):
    cache = load_cache(cache_file)
    df = pd.read_csv(input_file)

    # Ne traiter que les 5 premières colonnes
    cols_to_check = df.columns[:5]

    for col in cols_to_check:
        for i, value in enumerate(df[col]):
            if pd.isna(value):
                continue
            # Vérifier si la valeur est du texte japonais et non déjà dans le cache
            if value not in cache and any('\u3040' <= char <= '\u30ff' or '\u4e00' <= char <= '\u9faf' for char in str(value)):
                translation = ask_translation(value)
                cache[value] = translation

    save_cache(cache, cache_file)

def replace_with_cache(df, cache):
    for col in df.columns[:5]:
        df[col] = df[col].apply(lambda x: cache.get(x, x) if pd.notna(x) else x)
    return df

input_file = "./clean_datasets/filtered_race_result.csv"
output_file = "./clean_datasets/translated_race_result.csv"
annotate_csv(input_file, output_file)
cache = load_cache('translation_cache.json')
df = pd.read_csv(input_file)
df = replace_with_cache(df, cache)
df.to_csv(output_file, index=False)

