from src.alignment.feedback import interpret_alignment


def test_interprets_skipped_word():
    operations = [
        ("match", "الحمد"),
        ("match", "لله"),
        ("skip", "رب"),
        ("match", "العالمين"),
    ]

    result = interpret_alignment(operations)

    assert result == [
        {
            "type": "possible_skip",
            "expected_word": "رب",
        }
    ]




def test_interprets_substitution():
    operations = [
        ("match", "الحمد"),
        ("match", "لله"),
        ("match", "رب"),
        ("substitute", "العالمين", "لاعلمين"),
    ]

    result = interpret_alignment(operations)

    assert result == [
        {
            "type": "possible_substitution",
            "expected_word": "العالمين",
            "recognized_word": "لاعلمين",
        }
    ]