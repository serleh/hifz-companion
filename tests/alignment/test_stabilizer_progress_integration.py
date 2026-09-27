from src.alignment.progress import ProgressTracker
from src.alignment.transcript_stabilizer import TranscriptStabilizer


def test_stabilizer_feeds_only_committed_words_to_progress_tracker():
    expected = ["الحمد", "لله", "رب", "العالمين"]

    stabilizer = TranscriptStabilizer()
    tracker = ProgressTracker(expected)

    committed_transcript = []

    first = stabilizer.update(
        ["الحمد"]
    )

    assert first == []

    second = stabilizer.update(
        ["الحمد", "لله"]
    )

    assert second == ["الحمد"]

    committed_transcript.extend(second)

    result = tracker.process(committed_transcript)

    assert result["position"] == 1
    assert result["matched"] == ["الحمد"]

    third = stabilizer.update(
        ["الحمد", "لله", "رب"]
    )

    assert third == ["لله"]

    committed_transcript.extend(third)

    result = tracker.process(committed_transcript)

    assert result["position"] == 2
    assert result["matched"] == ["لله"]