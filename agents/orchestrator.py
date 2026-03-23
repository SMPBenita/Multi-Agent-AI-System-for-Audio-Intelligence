from agents.transcription_agent import TranscriptionAgent
from agents.summarization_agent import SummarizationAgent
from agents.insight_agent import InsightAgent

class AudioAIOrchestrator:
    def __init__(self):
        self.transcriber = TranscriptionAgent()
        self.summarizer = SummarizationAgent()
        self.insight = InsightAgent()

    def run_pipeline(self, audio_path):
        # Step 1: Transcription
        text = self.transcriber.run(audio_path)

        # Step 2: Summarization
        summary = self.summarizer.run(text)

        # Step 3: Insights
        keywords = self.insight.run(text)

        return {
            "transcription": text,
            "summary": summary,
            "keywords": keywords
        }