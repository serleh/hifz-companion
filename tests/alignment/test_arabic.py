from src.alignment.arabic import normalize_arabic


def test_removes_arabic_diacritics():
    text = "الْعَالَمِينَ"

    result = normalize_arabic(text)

    assert result == "العالمين"


def test_preserves_arabic_letters():
    text = "الحمد لله"

    result = normalize_arabic(text)

    assert result == "الحمد لله"