import sounddevice as sd
import soundfile as sf

SAMPLE_RATE = 16000
CHUNK_DURATION = 1
NUMBER_OF_CHUNKS = 3

for number in range(1, NUMBER_OF_CHUNKS + 1):
    print(f"Recording chunk {number}...")

    audio = sd.rec(
        int(CHUNK_DURATION * SAMPLE_RATE),
        samplerate=SAMPLE_RATE,
        channels=1,
        dtype="float32",
    )

    sd.wait()

    output_path = f"samples/chunk-{number}.wav"

    sf.write(
        output_path,
        audio,
        SAMPLE_RATE,
    )

    print(f"Saved {output_path}")