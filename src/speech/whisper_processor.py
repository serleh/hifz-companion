class WhisperProcessor:
    def __init__(self, transcriber):
        self.transcriber = transcriber

    def transcribe(self, audio):
        result = self.transcriber(audio)
        return result["text"]