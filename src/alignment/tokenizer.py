from src.alignment.arabic import normalize_arabic

def tokenize_ayah(text):
    normalized = normalize_arabic(text)
    return normalized.split()