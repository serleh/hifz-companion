class TranscriptStabilizer:
    def __init__(self):
        self.previous_words = []
        self.committed_count = 0

    def update(self, words):
        stable_words = []

        for i in range(self.committed_count, len(words)):
            if i < len(self.previous_words):
                if words[i] == self.previous_words[i]:
                    stable_words.append(words[i])

        self.committed_count += len(stable_words)

        self.previous_words = words

        return stable_words