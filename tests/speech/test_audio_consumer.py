import numpy as np

from src.speech.audio_buffer import AudioBuffer
from src.speech.audio_consumer import AudioConsumer


def test_consumer_gets_recent_audio():
    buffer = AudioBuffer(max_chunks=3)

    chunk_1 = np.array([[1], [2]])
    chunk_2 = np.array([[3], [4]])
    chunk_3 = np.array([[5], [6]])

    buffer.add(chunk_1)
    buffer.add(chunk_2)
    buffer.add(chunk_3)

    consumer = AudioConsumer(buffer)

    audio = consumer.get_audio()

    assert len(audio) == 3
    assert np.array_equal(audio[0], chunk_1)
    assert np.array_equal(audio[1], chunk_2)
    assert np.array_equal(audio[2], chunk_3)









def test_consumer_combines_audio_chunks():
    buffer = AudioBuffer(max_chunks=3)

    chunk_1 = np.array([[1], [2]])
    chunk_2 = np.array([[3], [4]])
    chunk_3 = np.array([[5], [6]])

    buffer.add(chunk_1)
    buffer.add(chunk_2)
    buffer.add(chunk_3)

    consumer = AudioConsumer(buffer)

    audio = consumer.get_combined_audio()

    expected = np.array([
        [1],
        [2],
        [3],
        [4],
        [5],
        [6],
    ])

    assert np.array_equal(audio, expected)



def test_consumer_returns_empty_array_when_buffer_is_empty():
    buffer = AudioBuffer(max_chunks=3)

    consumer = AudioConsumer(buffer)

    audio = consumer.get_combined_audio()

    assert audio.size == 0