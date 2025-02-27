# %%
import os
import speech_recognition as sr
import pyttsx3  # For text-to-speech
from google import genai
from google.genai import types
import dotenv

dotenv.load_dotenv()


# %%
def transcribe_audio():
    """Transcribes audio from the microphone using SpeechRecognition."""
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Say something!")
        recognizer.adjust_for_ambient_noise(source)  # Calibrate microphone
        audio = recognizer.listen(source)

    try:
        text = recognizer.recognize_google(audio)
        print(f"You said: {text}")
        return text
    except sr.UnknownValueError:
        print("Could not understand audio")
        return None
    except sr.RequestError as e:
        print(f"Could not request results from Google Speech Recognition service; {e}")
        return None


# %%
def generate_content_with_gemini(conversation_history):
    """Generates content using the Gemini API with streaming, now with conversation history."""

    client = genai.Client(
        api_key=os.environ.get("GEMINI_API_KEY"),
    )

    model = "gemini-2.0-flash-thinking-exp-01-21"  # or another suitable model

    # Prepare content with conversation history
    contents = []
    for role, text in conversation_history:
        contents.append(
            types.Content(
                role=role,
                parts=[
                    types.Part.from_text(text=text),
                ],
            )
        )

    generate_content_config = types.GenerateContentConfig(
        temperature=0.7,
        top_p=0.95,
        top_k=64,
        max_output_tokens=65536,
        response_mime_type="text/plain",
        system_instruction=[
            types.Part.from_text(
                text="""I want you to give concise response, as I am using this agent as in live chat model. Give humanly response, no astericks and markdowns, you are my bestfriend to share all my rants with. Remember our conversation history and respond accordingly."""
            ),
        ],
    )

    generated_text = ""
    try:
        for chunk in client.models.generate_content_stream(
            model=model,
            contents=contents,
            config=generate_content_config,
        ):
            generated_text += chunk.text
        return generated_text

    except Exception as e:  # Catch more general exceptions for robustness
        print(f"Error generating content with Gemini: {e}")
        return None


# %%
def speak(text):
    """Speaks the given text using pyttsx3."""
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()


# %%
# Main execution
if __name__ == "__main__":
    # Ensure GEMINI_API_KEY is set as an environment variable
    if "GEMINI_API_KEY" not in os.environ:
        print("Error: GEMINI_API_KEY environment variable not set.")
        print(
            "Please set your Gemini API key as an environment variable named GEMINI_API_KEY."
        )
        exit()

    conversation_history = []  # Initialize conversation history

    # 1. Get voice input:
    while True:
        voice_prompt = transcribe_audio()

        if voice_prompt:
            if "goodbye" in voice_prompt.lower() or 'bye' in voice_prompt.lower(): 
                speak("Goodbye!")
                break

            # Add user prompt to conversation history
            conversation_history.append(("user", voice_prompt))

            # 2. Generate content using Gemini with conversation history:
            generated_text = generate_content_with_gemini(conversation_history)

            if generated_text:
                # 3. Output the generated text:
                print("Generated Text:")
                print(generated_text)

                # 4. Speak the generated text:
                speak(generated_text)  # Use text-to-speech

                # Add model response to conversation history
                conversation_history.append(("model", generated_text))

            else:
                print("Failed to generate content.")
        else:
            print("No voice input received.")
