# %%
import requests
import os
import json
import speech_recognition as sr
import pyttsx3  # For text-to-speech

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
def generate_content_with_gemini(api_key, prompt):
    """Generates content using the Gemini API."""

    url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-2.0-flash:generateContent?key={api_key}"

    headers = {"Content-Type": "application/json"}

    data = {"contents": [{"parts": [{"text": prompt}]}]}

    try:
        response = requests.post(url, headers=headers, data=json.dumps(data))
        response.raise_for_status()
        response_json = response.json()

        if "candidates" in response_json and response_json["candidates"]:
            if (
                "content" in response_json["candidates"][0]
                and "parts" in response_json["candidates"][0]["content"]
            ):
                generated_text = response_json["candidates"][0]["content"]["parts"][0][
                    "text"
                ]
                return generated_text
            else:
                print("Error: 'content' or 'parts' not found in response.")
                return None
        else:
            print("Error: 'candidates' not found in response.")
            return None

    except requests.exceptions.RequestException as e:
        print(f"Request failed: {e}")
        return None
    except json.JSONDecodeError as e:
        print(f"JSON decoding error: {e}")
        print(f"Response text: {response.text}")
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
    
    api_key = os.environ.get("API_KEY") # Replace with your API key
    
    # print(generate_content_with_gemini(api_key,"Who am I"))

    # 1. Get voice input:
    while True:
        voice_prompt = transcribe_audio()
        
        

        if voice_prompt:
            
            if 'goodbye' in voice_prompt:
                break
            
            # 2. Generate content using Gemini:
            generated_text = generate_content_with_gemini(api_key, voice_prompt)

            if generated_text:
                # 3. Output the generated text:
                print("Generated Text:")
                print(generated_text)

                # 4. Speak the generated text:
                speak(generated_text)  # Use text-to-speech
            else:
                print("Failed to generate content.")
        else:
            print("No voice input received.")



