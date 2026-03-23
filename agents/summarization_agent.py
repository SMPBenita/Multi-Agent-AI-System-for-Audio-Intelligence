from models.nlp_model import NLPModel

class SummarizationAgent:
    def __init__(self):
        self.nlp = NLPModel()

    def run(self, text):
        return self.nlp.summarize(text)