import torch
from transformers import pipeline, DistilBertTokenizer, DistilBertForSequenceClassification

class EmailClassifier:
    def __init__(self):
        model_name = "distilbert-base-uncased-finetuned-sst-2-english"
        self.tokenizer = DistilBertTokenizer.from_pretrained("distilbert-base-uncased-finetuned-sst-2-english")
        self.model = DistilBertForSequenceClassification.from_pretrained(model_name)

    def classify(self, text: str):
        """
        Classifies an email into predefined categories.

        Args:
            text (str): The email text to classify.

        Returns:
            dict: The classification label and confidence score.
        """
        inputs = self.tokenizer(text, return_tensors="pt", truncation=True, padding=True)
        with torch.no_grad():
            logits = self.model(**inputs).logits
            predicted_class_id = logits.argmax().item()
            confidence = torch.softmax(logits, dim=1)[0, predicted_class_id].item()
        
        return {"label": self.model.config.id2label[predicted_class_id], "confidence": confidence}

# Create an instance of EmailClassifier
email_classifier = EmailClassifier()