from src.alignment.progress import track_progress


def test_detects_unexpected_word():
    expected = [
        "الحمد",
        "لله",
        "رب",
        "العالمين",
    ]

    recited = [
        "الحمد",
        "لله",
        "محمد",
        "رب",
        "العالمين",
    ]

    result = track_progress(expected, recited)

    assert result == {
        "position": 4,
        "matched": ["الحمد", "لله", "رب", "العالمين"],
        "possible_skips": [],
        "possible_repeats": [],
        "possible_extras": ["محمد"],
    }