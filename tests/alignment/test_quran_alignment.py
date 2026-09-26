from src.alignment.quran import load_ayah
from src.alignment.tokenizer import tokenize_ayah
from src.alignment.edit_distance import build_table, backtrack


def test_detects_skipped_quran_word():
    ayah = load_ayah("data/quran/al_fatiha.json")

    expected = tokenize_ayah(ayah["text"])
    recited = ["الحمد", "لله", "العالمين"]

    table = build_table(expected, recited)
    result = backtrack(expected, recited, table)

    assert result == [
        ("match", "الحمد"),
        ("match", "لله"),
        ("skip", "رب"),
        ("match", "العالمين"),
    ]