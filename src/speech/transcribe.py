from transformers import pipeline

MODEL_NAME =  "tarteel-ai/whisper-base-ar-quran"


def create_transcriber():
    return pipeline('automatic-speech-recognition',MODEL_NAME)


def transcribe(transcriber,audio_path):
    result = transcriber(audio_path)

    return result['text']