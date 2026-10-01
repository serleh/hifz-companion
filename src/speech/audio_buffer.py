class AudioBuffer:
    def __init__(self, max_chunks):
        self.max_chunks = max_chunks
        self.chunks = []

    def add(self, chunk):
        self.chunks.append(chunk)

        if len(self.chunks) > self.max_chunks:
            self.chunks.pop(0)

    def get(self):
        return self.chunks.copy()