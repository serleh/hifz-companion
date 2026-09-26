from src.alignment.service import align_recitation


def test_align_recitation_detects_skipped_word():
    expected = "الْحَمْدُ لِلَّهِ رَبِّ الْعَالَمِينَ"
    recited = "الْحَمْدُ لِلَّهِ الْعَالَمِينَ"

    result = align_recitation(expected, recited)

    assert result == [
        ("match", "الحمد"),
        ("match", "لله"),
        ("skip", "رب"),
        ("match", "العالمين"),
    ]