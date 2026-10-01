from src.alignment.progress import track_progress


def test_tracks_current_position():
    expected = [
        "الحمد",
        "لله",
        "رب",
        "العالمين",
    ]

    recited = [
        "الحمد",
        "لله",
    ]

    result = track_progress(expected, recited)

    assert result == {
        "position": 2,
        "matched": ["الحمد", "لله"],
        "possible_skips": [],
        "possible_repeats": [],
        "possible_extras": [],
    }