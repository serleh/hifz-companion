import time

from src.speech.audio_buffer import AudioBuffer
from src.speech.microphone_stream import MicrophoneStream


buffer = AudioBuffer(max_chunks=30)
microphone = MicrophoneStream(buffer)

print("Recording for 5 seconds...")

microphone.start()

time.sleep(5)

microphone.stop()

print(f"Captured {len(buffer.get())} chunks")