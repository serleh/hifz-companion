def track_progress(expected, recited):
    matched = []

    possible_skips = []

    possible_repeats = []

    possible_extras = []

    expected_index = 0

    for word in recited:

        # Normal match
        if expected_index < len(expected) and word == expected[expected_index]:
            matched.append(word)
            expected_index += 1
            continue

        # Repeated previous word
        if matched and word == matched[-1]:
            possible_repeats.append(word)
            continue

        # Look ahead for the recognized word
        try:
            next_index = expected.index(word, expected_index)
        except ValueError:
            possible_extras.append(word)
            continue

        # Words between the current position and the recognized word
        # were possibly skipped.
        possible_skips.extend(expected[expected_index:next_index])

        matched.append(word)
        expected_index = next_index + 1

    return {
        "position": expected_index,
        "matched": matched,
        "possible_skips": possible_skips,
        "possible_repeats": possible_repeats,
        "possible_extras": possible_extras,
    }


# PROGRESS TRACKER
class ProgressTracker:
    def __init__(self, expected):
        self.expected = expected
        self.position = 0
        self.processed_words =0

    def process(self, words):
        
        matched = []
        possible_skips = []
        possible_repeats = []
        possible_extras = []

        new_words = words[self.processed_words:]
        self.processed_words = len(words)

        for word in new_words:
            if (
                self.position < len(self.expected)
                and word == self.expected[self.position]
            ):
                matched.append(word)
                self.position += 1
                continue

            if matched and word == matched[-1]:
                possible_repeats.append(word)
                continue

            try:
                next_index = self.expected.index(
                    word,
                    self.position,
                )
            except ValueError:
                possible_extras.append(word)
                continue

            possible_skips.extend(
                self.expected[self.position:next_index]
            )

            matched.append(word)
            self.position = next_index + 1

        return {
            "position": self.position,
            "matched": matched,
            "possible_skips": possible_skips,
            "possible_repeats": possible_repeats,
            "possible_extras": possible_extras,
        }