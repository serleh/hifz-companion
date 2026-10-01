import numpy as np

from src.speech.whisper_processor import WhisperProcessor


class FakeTranscriber:
    def __call__(self, audio):
        self.received_audio = audio
        return {"text": "الحمد لله رب العالمين"}


def test_processor_transcribes_audio():
    transcriber = FakeTranscriber()
    processor = WhisperProcessor(transcriber)

    audio = np.array([0.1, 0.2, 0.3])

    result = processor.transcribe(audio)

    assert result == "الحمد لله رب العالمين"


def test_processor_passes_audio_waveform_to_transcriber():
    transcriber = FakeTranscriber()
    processor = WhisperProcessor(transcriber)

    audio = np.array([0.1, 0.2, 0.3])

    processor.transcribe(audio)

    assert np.array_equal(transcriber.received_audio, audio)