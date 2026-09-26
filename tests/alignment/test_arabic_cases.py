from src.alignment.tokenizer import tokenize_ayah


def test_normalized_quran_words():
    text = "الْحَمْدُ لِلَّهِ رَبِّ الْعَالَمِينَ"

    result = tokenize_ayah(text)

    assert result == [
        "الحمد",
        "لله",
        "رب",
        "العالمين",
    ]


def test_asr_output_is_tokenized():
    text = "الْحَمْدُ لِلَّهِ رَبِّ لَاعْلَمِينَ"

    result = tokenize_ayah(text)

    assert result == [
        "الحمد",
        "لله",
        "رب",
        "لاعلمين",
    ]