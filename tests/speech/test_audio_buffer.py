import numpy as np

from src.speech.audio_buffer import AudioBuffer


def test_buffer_keeps_recent_audio_chunks():
    buffer = AudioBuffer(max_chunks=3)

    chunk_1 = np.array([1, 2])
    chunk_2 = np.array([3, 4])
    chunk_3 = np.array([5, 6])

    buffer.add(chunk_1)
    buffer.add(chunk_2)
    buffer.add(chunk_3)

    result = buffer.get()

    assert len(result) == 3
    assert np.array_equal(result[0], chunk_1)
    assert np.array_equal(result[1], chunk_2)
    assert np.array_equal(result[2], chunk_3)


def test_buffer_discards_oldest_audio_chunk():
    buffer = AudioBuffer(max_chunks=3)

    chunk_1 = np.array([1, 2])
    chunk_2 = np.array([3, 4])
    chunk_3 = np.array([5, 6])
    chunk_4 = np.array([7, 8])

    buffer.add(chunk_1)
    buffer.add(chunk_2)
    buffer.add(chunk_3)
    buffer.add(chunk_4)

    result = buffer.get()

    assert len(result) == 3
    assert np.array_equal(result[0], chunk_2)
    assert np.array_equal(result[1], chunk_3)
    assert np.array_equal(result[2], chunk_4)




def test_get_returns_snapshot():
    buffer = AudioBuffer(max_chunks=3)

    chunk_1 = np.array([1, 2])

    buffer.add(chunk_1)

    snapshot = buffer.get()

    buffer.add(np.array([3, 4]))

    assert len(snapshot) == 1
    assert np.array_equal(snapshot[0], chunk_1)