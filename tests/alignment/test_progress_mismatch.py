from src.alignment.progress import track_progress


def test_detects_progress_after_middle_skip():
    expected = [
        "الحمد",
        "لله",
        "رب",
        "العالمين",
    ]

    recited = [
        "الحمد",
        "لله",
        "العالمين",
    ]

    result = track_progress(expected, recited)

    assert result == {
        "position": 4,
        "matched": ["الحمد", "لله", "العالمين"],
        "possible_skips": ["رب"],
        "possible_repeats": [],
        "possible_extras": []
    }