from keybert import KeyBERT

class InsightAgent:
    def __init__(self):
        self.model = KeyBERT()

    def run(self, text):
        keywords = self.model.extract_keywords(text, keyphrase_ngram_range=(1, 2), top_n=5)
        return [kw[0] for kw in keywords]