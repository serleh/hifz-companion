from src.speech.transcribe import create_transcriber
from src.speech.whisper_processor import WhisperProcessor


audio_path = "samples/ayah-002.wav"

transcriber = create_transcriber()
processor = WhisperProcessor(transcriber)

result = processor.transcribe(audio_path)

print("Transcription:")
print(result)