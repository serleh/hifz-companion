from src.alignment.transcript_stabilizer import TranscriptStabilizer


def test_commits_words_that_remain_stable():
    stabilizer = TranscriptStabilizer()

    first = stabilizer.update(
        ["الحمد", "لله"]
    )

    assert first == []


    second = stabilizer.update(
        ["الحمد", "لله"]
    )

    assert second == ["الحمد", "لله"]


def test_does_not_commit_word_that_changes():
    stabilizer = TranscriptStabilizer()

    first = stabilizer.update(
        ["الحمد", "لله", "ربي"]
    )

    assert first == []

    second = stabilizer.update(
        ["الحمد", "لله", "رب"]
    )

    assert second == ["الحمد", "لله"]


def test_committed_words_remain_locked():
    stabilizer = TranscriptStabilizer()

    stabilizer.update(
        ["الحمد", "لله"]
    )

    committed = stabilizer.update(
        ["الحمد", "لله"]
    )

    assert committed == ["الحمد", "لله"]

    revised = stabilizer.update(
        ["الحمد", "ربي"]
    )

    assert revised == []




def test_commits_repeated_words_at_different_positions():
    stabilizer = TranscriptStabilizer()

    first = stabilizer.update(
        ["الحمد", "لله", "رب"]
    )

    assert first == []

    second = stabilizer.update(
        ["الحمد", "لله", "رب"]
    )

    assert second == ["الحمد", "لله", "رب"]

    third = stabilizer.update(
        ["الحمد", "لله", "رب", "لله"]
    )

    assert third == []

    fourth = stabilizer.update(
        ["الحمد", "لله", "رب", "لله"]
    )

    assert fourth == ["لله"]










def test_commits_words_as_transcript_grows():
    stabilizer = TranscriptStabilizer()

    assert stabilizer.update(
        ["الحمد"]
    ) == []

    assert stabilizer.update(
        ["الحمد", "لله"]
    ) == ["الحمد"]

    assert stabilizer.update(
        ["الحمد", "لله", "رب"]
    ) == ["لله"]

    assert stabilizer.update(
        ["الحمد", "لله", "رب", "العالمين"]
    ) == ["رب"]