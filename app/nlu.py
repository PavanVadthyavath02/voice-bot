
from transformers import pipeline

# Load a pre-trained text classification model (fine-tune later for custom intents)
classifier = pipeline("text-classification", model="distilbert-base-uncased-finetuned-sst-2-english")

def detect_intent(text):
    result = classifier(text)[0]  # Get the top classification result
    intent = result['label']  # Extract intent (e.g., "POSITIVE" / "NEGATIVE" in default SST-2)
    
    # Map Hugging Face labels to bot intents
    intent_mapping = {
        "POSITIVE": "Check Account Balance",
        "NEGATIVE": "Unknown"
    }

    return intent_mapping.get(intent, "Unknown"), {}
