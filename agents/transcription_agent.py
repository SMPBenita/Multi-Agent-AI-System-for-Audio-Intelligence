from models.asr_model import ASRModel

class TranscriptionAgent:
    def __init__(self):
        self.asr = ASRModel()

    def run(self, audio_path):
        return self.asr.transcribe(audio_path)