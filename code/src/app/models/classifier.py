from transformers import pipeline

class EmailClassifier:
    def __init__(self):
        self.model = pipeline("text-classification", model="facebook/bart-large-mnli")

    def classify(self, text: str):
        labels = ["Adjustment", "Money Movement", "Fee Payment", "Commitment Change"]
        result = self.model(text, candidate_labels=labels)
        return {"label": result["labels"][0], "confidence": result["scores"][0]}
    
email_classifier = EmailClassifier()