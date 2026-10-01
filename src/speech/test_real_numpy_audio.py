import soundfile as sf


audio, sample_rate = sf.read("samples/ayah-002.wav")

print("Sample rate:", sample_rate)
print("Audio shape:", audio.shape)
print("Audio dtype:", audio.dtype)
print("First samples:", audio[:5])