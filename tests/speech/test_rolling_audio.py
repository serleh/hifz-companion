import numpy as np

from src.speech.audio_buffer import AudioBuffer
from src.speech.audio_consumer import AudioConsumer


def test_consumer_returns_latest_audio_window():
    buffer = AudioBuffer(max_chunks=5)

    buffer.add(np.array([[1.0]]))
    buffer.add(np.array([[2.0]]))
    buffer.add(np.array([[3.0]]))
    buffer.add(np.array([[4.0]]))
    buffer.add(np.array([[5.0]]))

    consumer = AudioConsumer(buffer)

    audio = consumer.get_recent_audio(window_size=3)

    expected = np.array([
        [3.0],
        [4.0],
        [5.0],
    ])

    assert np.array_equal(audio, expected)


def test_consumer_returns_all_audio_when_window_is_larger_than_buffer():
    buffer = AudioBuffer(max_chunks=5)

    buffer.add(np.array([[1.0]]))
    buffer.add(np.array([[2.0]]))

    consumer = AudioConsumer(buffer)

    audio = consumer.get_recent_audio(window_size=5)

    expected = np.array([
        [1.0],
        [2.0],
    ])

    assert np.array_equal(audio, expected)



def test_consumer_returns_empty_audio_when_buffer_is_empty():
    buffer = AudioBuffer(max_chunks=5)

    consumer = AudioConsumer(buffer)

    audio = consumer.get_recent_audio(window_size=3)

    assert audio.size == 0



def test_recent_audio_does_not_remove_chunks_from_buffer():
    buffer = AudioBuffer(max_chunks=5)

    buffer.add(np.array([[1.0]]))
    buffer.add(np.array([[2.0]]))
    buffer.add(np.array([[3.0]]))

    consumer = AudioConsumer(buffer)

    consumer.get_recent_audio(window_size=2)

    audio = consumer.get_recent_audio(window_size=3)

    expected = np.array([
        [1.0],
        [2.0],
        [3.0],
    ])

    assert np.array_equal(audio, expected)