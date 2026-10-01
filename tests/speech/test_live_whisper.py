import numpy as np

from src.speech.live_whisper import LiveWhisper


class FakeAudioConsumer:
    def get_recent_audio(self, window_size):
        self.received_window_size = window_size

        return np.array([
            [1.0],
            [2.0],
            [3.0],
        ])


class FakeWhisperProcessor:
    def transcribe(self, audio):
        self.received_audio = audio

        return "الحمد لله"


def test_live_whisper_transcribes_recent_audio():
    audio_consumer = FakeAudioConsumer()
    whisper_processor = FakeWhisperProcessor()

    live_whisper = LiveWhisper(
        audio_consumer,
        whisper_processor,
        window_size=3,
    )

    result = live_whisper.transcribe_latest()

    assert result == "الحمد لله"
    assert audio_consumer.received_window_size == 3

    expected_audio = np.array([
        [1.0],
        [2.0],
        [3.0],
    ])

    assert np.array_equal(
        whisper_processor.received_audio,
        expected_audio,
    )



def test_live_whisper_handles_empty_audio():
    audio_consumer = FakeAudioConsumer()
    whisper_processor = FakeWhisperProcessor()

    audio_consumer.get_recent_audio = lambda window_size: np.array([])

    live_whisper = LiveWhisper(
        audio_consumer,
        whisper_processor,
        window_size=3,
    )

    result = live_whisper.transcribe_latest()

    assert result == ""