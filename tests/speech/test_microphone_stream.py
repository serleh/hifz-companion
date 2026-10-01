import numpy as np

from src.speech.audio_buffer import AudioBuffer
from src.speech.microphone_stream import MicrophoneStream


def test_microphone_callback_adds_audio_to_buffer():
    buffer = AudioBuffer(max_chunks=3)
    stream = MicrophoneStream(buffer)

    audio_chunk = np.array([[0.1], [0.2], [0.3]])

    stream.handle_audio(audio_chunk)

    result = buffer.get()

    assert len(result) == 1
    assert np.array_equal(result[0], audio_chunk)