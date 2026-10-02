
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
        processing_interval=0.5,
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

    audio_consumer.get_recent_audio = (
        lambda window_size: np.array([])
    )

    live_whisper = LiveWhisper(
        audio_consumer,
        whisper_processor,
        window_size=3,
        processing_interval=0.5,
    )

    result = live_whisper.transcribe_latest()

    assert result == ""


def test_live_whisper_processes_one_cycle():

    audio_consumer = FakeAudioConsumer()
    whisper_processor = FakeWhisperProcessor()

    live_whisper = LiveWhisper(
        audio_consumer,
        whisper_processor,
        window_size=3,
        processing_interval=0.5,
    )

    result = live_whisper.process_once()

    assert result == "الحمد لله"
    assert audio_consumer.received_window_size == 3


def test_live_whisper_can_process_multiple_cycles():

    audio_consumer = FakeAudioConsumer()
    whisper_processor = FakeWhisperProcessor()

    live_whisper = LiveWhisper(
        audio_consumer,
        whisper_processor,
        window_size=3,
        processing_interval=0.5,
    )

    first_result = live_whisper.process_once()
    second_result = live_whisper.process_once()

    assert first_result == "الحمد لله"
    assert second_result == "الحمد لله"


def test_live_whisper_stops_when_requested():

    audio_consumer = FakeAudioConsumer()
    whisper_processor = FakeWhisperProcessor()

    live_whisper = LiveWhisper(
        audio_consumer,
        whisper_processor,
        window_size=3,
        processing_interval=0.5,
    )

    live_whisper.stop()

    assert live_whisper.running is False


def test_live_whisper_starts_when_requested():

    audio_consumer = FakeAudioConsumer()
    whisper_processor = FakeWhisperProcessor()

    live_whisper = LiveWhisper(
        audio_consumer,
        whisper_processor,
        window_size=3,
        processing_interval=0.5,
    )

    live_whisper.start()

    assert live_whisper.running is True


def test_live_whisper_runs_processing_loop():

    audio_consumer = FakeAudioConsumer()
    whisper_processor = FakeWhisperProcessor()

    live_whisper = LiveWhisper(
        audio_consumer,
        whisper_processor,
        window_size=3,
        processing_interval=0.5,
    )

    calls = []

    def fake_process_once():
        calls.append(1)

        if len(calls) == 3:
            live_whisper.stop()

    live_whisper.process_once = fake_process_once

    live_whisper.start_loop()

    assert len(calls) == 3


def test_live_whisper_accepts_processing_interval():

    audio_consumer = FakeAudioConsumer()
    whisper_processor = FakeWhisperProcessor()

    live_whisper = LiveWhisper(
        audio_consumer,
        whisper_processor,
        window_size=3,
        processing_interval=0.5,
    )

    assert live_whisper.processing_interval == 0.5



def test_live_whisper_waits_between_processing_cycles(monkeypatch):

    audio_consumer = FakeAudioConsumer()
    whisper_processor = FakeWhisperProcessor()

    live_whisper = LiveWhisper(
        audio_consumer,
        whisper_processor,
        window_size=3,
        processing_interval=0.5,
    )

    sleep_calls = []

    def fake_sleep(seconds):
        sleep_calls.append(seconds)

    monkeypatch.setattr(
        "time.sleep",
        fake_sleep,
    )

    calls = []

    def fake_process_once():
        calls.append(1)

        if len(calls) == 3:
            live_whisper.stop()

    live_whisper.process_once = fake_process_once

    live_whisper.start_loop()

    assert sleep_calls == [0.5, 0.5]