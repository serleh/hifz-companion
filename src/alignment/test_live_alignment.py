from src.alignment.quran import load_ayah
from src.alignment.service import align_recitation
from src.speech.transcribe import create_transcriber, transcribe
from src.alignment.feedback import interpret_alignment


ayah = load_ayah("data/quran/al_fatiha.json")

transcriber = create_transcriber()

transcribed_text = transcribe(
    transcriber,
    "samples/ayah-002.wav",
)

result = align_recitation(
    ayah["text"],
    transcribed_text,
)


feedback = interpret_alignment(result)

print("Expected:")
print(ayah["text"])

print("\nTranscribed:")
print(transcribed_text)

print("\nAlignment:")

for operation in result:
    print(operation)


print("\nFeedback:")

for event in feedback:
    print(event)