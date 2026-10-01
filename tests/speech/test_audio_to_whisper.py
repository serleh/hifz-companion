import numpy as np

from src.speech.audio_buffer import AudioBuffer
from src.speech.audio_consumer import AudioConsumer
from src.speech.whisper_processor import WhisperProcessor


class FakeTranscriber:
    def __call__(self, audio):
        self.received_audio = audio
        return {"text": "الحمد لله"}


def test_audio_consumer_output_can_be_processed_by_whisper():
    buffer = AudioBuffer(max_chunks=3)

    buffer.add(np.array([[0.1], [0.2]]))
    buffer.add(np.array([[0.3], [0.4]]))

    consumer = AudioConsumer(buffer)

    audio = consumer.get_combined_audio()

    transcriber = FakeTranscriber()
    processor = WhisperProcessor(transcriber)

    result = processor.transcribe(audio)

    expected_audio = np.array([
        [0.1],
        [0.2],
        [0.3],
        [0.4],
    ])

    assert np.array_equal(transcriber.received_audio, expected_audio)
    assert result == "الحمد لله"