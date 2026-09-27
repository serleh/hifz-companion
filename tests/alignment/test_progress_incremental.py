from src.alignment.progress import ProgressTracker


def test_tracker_ignores_already_processed_words():
    expected = [
        "الحمد",
        "لله",
        "رب",
        "العالمين",
    ]

    tracker = ProgressTracker(expected)

    first_result = tracker.process(
        ["الحمد", "لله"]
    )

    assert first_result["position"] == 2

    second_result = tracker.process(
        ["الحمد", "لله", "رب"]
    )

    assert second_result == {
        "position": 3,
        "matched": ["رب"],
        "possible_skips": [],
        "possible_repeats": [],
        "possible_extras": [],
    }