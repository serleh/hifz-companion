from src.alignment.tokenizer import tokenize_ayah
from src.alignment.edit_distance import build_table, backtrack


def align_recitation(expected_text, recited_text):
    expected = tokenize_ayah(expected_text)
    recited = tokenize_ayah(recited_text)

    table = build_table(expected, recited)

    return backtrack(expected, recited, table)