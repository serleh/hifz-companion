import numpy as np

class AudioConsumer:
    def __init__(self, buffer):
        self.buffer = buffer

    def get_audio(self):
        return self.buffer.get()

    def get_combined_audio(self):
        chunks = self.buffer.get()

        if not chunks:
            return np.array([])

        return np.concatenate(chunks, axis=0)

    def get_recent_audio(self, window_size):
        chunks = self.buffer.get()

        recent_chunks = chunks[-window_size:]

        if not recent_chunks:
            return np.array([])

        return np.concatenate(recent_chunks, axis=0)