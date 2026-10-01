import sounddevice as sd


class MicrophoneStream:
    def __init__(self, buffer):
        self.buffer = buffer

    def handle_audio(self, audio_chunk):
        self.buffer.add(audio_chunk)

    def start(self, sample_rate=16000, block_duration=0.1):
        block_size = int(sample_rate * block_duration)

        self.stream = sd.InputStream(
            samplerate=sample_rate,
            channels=1,
            blocksize=block_size,
            dtype="float32",
            callback=self._callback,
        )

        self.stream.start()

    def _callback(self, indata, frames, time, status):
        if status:
            print(status)

        self.handle_audio(indata.copy())

    def stop(self):
        self.stream.stop()
        self.stream.close()