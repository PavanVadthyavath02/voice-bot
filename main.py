# from flask import Flask, request, jsonify
# from app.speech_to_text import transcribe_audio
# from app.nlu import detect_intent
# from app.response_gen import generate_response
# from app.text_to_speech import text_to_speech
# from app.database import get_account_balance

# app = Flask(__name__)

# @app.route("/")
# def home():
#     return "Voice Bot is Running!"


# @app.route("/process_audio", methods=["POST"])
# def process_audio():
#     if "audio" not in request.files:
#         return jsonify({"error": "No audio file provided"}), 400

#     audio_file = request.files["audio"]
#     audio_path = "input.wav"
#     audio_file.save(audio_path)

#     # Step 1: Speech-to-Text using Whisper
#     text = transcribe_audio(audio_path)

#     # Step 2: Natural Language Understanding
#     intent, parameters = detect_intent(text, "your-project-id", "session-id")

#     # Step 3: Response Generation
#     response = "I'm sorry, I didn't understand that."
#     if intent == "Check Account Balance":
#         user_id = parameters.get("user_id")
#         if user_id:
#             balance = get_account_balance(user_id)
#             response = generate_response(f"The account balance for user {user_id} is ${balance}.")
#         else:
#             response = generate_response("User ID not provided.")

#     # Step 4: Text-to-Speech
#     output_audio = "output.mp3"
#     text_to_speech(response, output_audio)

#     return jsonify({"response": response, "audio_file": output_audio})

# if __name__ == "__main__":
#     app.run(debug=True)


# from fastapi import FastAPI, File, UploadFile
# import shutil
# from app.speech_to_text import transcribe_audio
# from app.nlu import detect_intent
# from app.response_gen import generate_response
# from app.text_to_speech import text_to_speech
# from app.database import get_account_balance
# from fastapi import FastAPI
# from app.nlu import detect_intent

# app = FastAPI()  # Initialize FastAPI app

# @app.post("/process_audio")
# async def process_audio(audio: UploadFile = File(...)):
#     file_path = "input.wav"
    
#     # Save the uploaded file
#     with open(file_path, "wb") as buffer:
#         shutil.copyfileobj(audio.file, buffer)

#     # Step 1: Speech-to-Text
#     text = transcribe_audio(file_path)

#     # Step 2: NLU - Detect Intent
#     intent, parameters = detect_intent(text, "your-project-id", "session-id")

#     # Step 3: Generate Response
#     if intent == "Check Account Balance":
#         user_id = parameters.get("user_id")
#         balance = get_account_balance(user_id)
#         response_text = f"The account balance for user {user_id} is ${balance}."
#     else:
#         response_text = "I'm sorry, I didn't understand that."

#     response = generate_response(response_text)

#     # Step 4: Convert Response to Speech
#     text_to_speech(response, "output.mp3")

#     return {"response": response, "audio_file": "output.mp3"}

# # Default Route
# @app.get("/")
# def home():
#     return {"message": "Voice Bot is Running!"}

# from fastapi import FastAPI, Request
# import io
# from app.speech_to_text import transcribe_audio
# from app.nlu import detect_intent
# from app.response_gen import generate_response
# from app.text_to_speech import text_to_speech
# from app.database import get_account_balance

# app = FastAPI()

# @app.post("/process_audio")
# async def process_audio(request: Request):
#     audio_bytes = await request.body()  # Get raw audio data
    
#     file_path = "input.wav"
    
#     # Save the audio bytes as a file
#     with open(file_path, "wb") as f:
#         f.write(audio_bytes)

#     # Step 1: Speech-to-Text
#     text = transcribe_audio(file_path)

#     # Step 2: NLU - Detect Intent
#     intent, parameters = detect_intent(text, "your-project-id", "session-id")

#     # Step 3: Generate Response
#     if intent == "Check Account Balance":
#         user_id = parameters.get("user_id")
#         balance = get_account_balance(user_id)
#         response_text = f"The account balance for user {user_id} is ${balance}."
#     else:
#         response_text = "I'm sorry, I didn't understand that."

#     response = generate_response(response_text)

#     # Step 4: Convert Response to Speech
#     text_to_speech(response, "output.mp3")

#     return {"response": response, "audio_file": "output.mp3"}

# @app.get("/")
# def home():
#     return {"message": "Voice Bot is Running!"}

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
