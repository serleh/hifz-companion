from src.alignment.progress import track_progress


def test_detects_repeated_word():
    expected = [
        "الحمد",
        "لله",
        "رب",
        "العالمين",
    ]

    recited = [
        "الحمد",
        "لله",
        "لله",
        "رب",
        "العالمين",
    ]

    result = track_progress(expected, recited)

    assert result == {
        "position": 4,
        "matched": ["الحمد", "لله", "رب", "العالمين"],
        "possible_skips": [],
        "possible_repeats": ["لله"],
        "possible_extras":[]
    }