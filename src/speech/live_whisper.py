class LiveWhisper:
    def __init__(self, audio_consumer, whisper_processor, window_size):
        self.audio_consumer = audio_consumer
        self.whisper_processor = whisper_processor
        self.window_size = window_size
        self.running = False

    def transcribe_latest(self):
        audio = self.audio_consumer.get_recent_audio(self.window_size)

        if audio.size == 0:
            return ""

        return self.whisper_processor.transcribe(audio)

    def process_once(self):
        return self.transcribe_latest()

    def start(self):
        self.running = True

    def stop(self):
        self.running = False

    def start_loop(self):
        self.start()

        while self.running:
            self.process_once()


