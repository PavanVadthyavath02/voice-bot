import openai


def text_to_speech(text, output_file="output.mp3"):
    response = openai.audio.speech.create(
        model="tts-1",
        voice="alloy",
        input=text
    )

    audio_content = response['audio']

    with open(output_file, "wb") as out:
        out.write(audio_content)
        print(f"Audio content written to file '{output_file}'")
