import soundfile as sf

from src.speech.transcribe import create_transcriber
from src.speech.whisper_processor import WhisperProcessor


audio, sample_rate = sf.read("samples/ayah-002.wav")

transcriber = create_transcriber()
processor = WhisperProcessor(transcriber)

result = processor.transcribe(audio)

print("Sample rate:", sample_rate)
print("Transcription:")
print(result)