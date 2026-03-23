from transformers import pipeline

class ASRModel:
    def __init__(self):
        self.model = pipeline(
            "automatic-speech-recognition",
            model="openai/whisper-small"
        )

    def transcribe(self, audio_path):
        return self.model(audio_path)["text"]