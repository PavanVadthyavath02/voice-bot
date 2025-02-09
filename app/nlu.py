# from google.cloud import dialogflow_v2 as dialogflow

# def detect_intent(text, project_id, session_id, language_code="en-US"):
#     session_client = dialogflow.SessionsClient()
#     session = f"projects/{project_id}/agent/sessions/{session_id}"

#     text_input = dialogflow.TextInput(text=text, language_code=language_code)
#     query_input = dialogflow.QueryInput(text=text_input)

#     response = session_client.detect_intent(session=session, query_input=query_input)
#     return response.query_result.intent.display_name, response.query_result.parameters


# from transformers import pipeline

# # Load DistilBERT-based text classification pipeline
# classifier = pipeline("text-classification", model="distilbert-base-uncased-finetuned-sst-2-english")

# def detect_intent(text):
#     result = classifier(text)
#     intent = result[0]["label"]  # Positive or Negative sentiment (can be adapted)
#     confidence = result[0]["score"]

#     # Map sentiment output to a basic intent system (can be expanded)
#     if intent == "POSITIVE":
#         detected_intent = "greeting_intent"
#     else:
#         detected_intent = "unknown_intent"

#     return detected_intent, {"confidence": confidence}



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
