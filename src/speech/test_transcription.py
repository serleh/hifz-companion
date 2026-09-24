from transcribe import create_transcriber, transcribe


audio_path = "samples/ayah-002.wav"


transcriber = create_transcriber()
text = transcribe(transcriber, audio_path)

print("Transcription: ")
print(text)