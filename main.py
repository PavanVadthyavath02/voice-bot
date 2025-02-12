

from fastapi import FastAPI, File, UploadFile
import shutil
from app.speech_to_text import transcribe_audio
from app.nlu import detect_intent  # Updated to use Hugging Face
from app.response_gen import generate_response
from app.text_to_speech import text_to_speech
from app.database import get_account_balance

app = FastAPI()  # Initialize FastAPI app

@app.post("/process_audio")
async def process_audio(audio: UploadFile = File(...)):
    file_path = "input.wav"
    
    # Save the uploaded file
    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(audio.file, buffer)

    # Step 1: Speech-to-Text
    text = transcribe_audio(file_path)

    # Step 2: NLU - Detect Intent (Using Hugging Face)
    intent, parameters = detect_intent(text)

    # Step 3: Generate Response
    if intent == "Check Account Balance":
        response_text = "Your account balance is $500."
    else:
        response_text = "I'm sorry, I didn't understand that."

    response = generate_response(response_text)

    # Step 4: Convert Response to Speech
    text_to_speech(response, "output.mp3")

    return {"response": response, "audio_file": "output.mp3"}

@app.get("/")
def home():
    return {"message": "Voice Bot is Running!"}
