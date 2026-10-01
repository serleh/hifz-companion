import sounddevice as sd
import soundfile as sf

SAMPLE_RATE = 16000
DURATION = 5
OUTPUT_PATH = "samples/microphone-test.wav"

print("Recording...")

audio = sd.rec(
    int(DURATION * SAMPLE_RATE),
    samplerate=SAMPLE_RATE,
    channels=1,
    dtype="float32",
)

sd.wait()

sf.write(
    OUTPUT_PATH,
    audio,
    SAMPLE_RATE,
)

print(f"Recording saved to {OUTPUT_PATH}")