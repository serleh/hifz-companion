class LiveWhisper:
    def __init__(self, audio_consumer, whisper_processor, window_size):
        self.audio_consumer = audio_consumer
        self.whisper_processor = whisper_processor
        self.window_size = window_size

    def transcribe_latest(self):
        audio = self.audio_consumer.get_recent_audio(self.window_size)

        if audio.size == 0:
            return ""

        return self.whisper_processor.transcribe(audio)