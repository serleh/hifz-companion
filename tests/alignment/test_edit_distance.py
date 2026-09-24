from src.alignment.edit_distance import build_table, backtrack


#  Skipped word test
def test_detects_skipped_word():
    expected = ['A', 'B', 'C']
    recited = ['A','C']

    table = build_table(expected,recited)
    result = backtrack(expected,recited,table)

    assert result == [
        ("match", "A"),
        ("skip", "B"),
        ("match", "C"),
    ]



# Extra word test
def test_detects_extra_word():
    expected = ["A", "B", "C"]
    recited = ["A", "B", "B", "C"]

    table = build_table(expected, recited)
    result = backtrack(expected, recited, table)

    assert result == [
        ("match", "A"),
        ("extra", "B"),
        ("match", "B"),
        ("match", "C"),
    ]



# Substitute word test
def test_detects_substitution():
    expected = ["A", "B", "C"]
    recited = ["A", "X", "C"]

    table = build_table(expected, recited)
    result = backtrack(expected, recited, table)

    assert result == [
        ("match", "A"),
        ("substitute", "B", "X"),
        ("match", "C"),
    ]