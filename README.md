# Voice-Controlled AI Conversation Agent

## Project Overview

This project is a simple, voice-activated AI conversation agent built using Python. Inspired by a desire to create an accessible AI assistant even on resource-constrained laptops, this agent utilizes speech recognition to take voice input, sends it to a powerful language model (like Gemini), and then speaks back the AI's response. It's designed to be a fun and engaging way to interact with AI, particularly for users who might be new to the technology or have limited access to high-performance devices.

Essentially, you can talk to your computer, and it will talk back! Think of it as a friendly, voice-based chat buddy.

## Features

*   **Voice Input:** Uses your microphone to listen to your commands and questions.
*   **AI-Powered Responses:** Leverages the Gemini API to generate intelligent and conversational replies.
*   **Text-to-Speech Output:** Speaks the AI's responses back to you, making it a fully voice-driven experience.
*   **Conversation History:**  Remembers the ongoing conversation within the current run, allowing for more contextually aware and natural interactions.
*   **Simple Setup:**  Designed to be relatively easy to install and run, even on less powerful machines.

## Getting Started

Follow these steps to get your own voice-controlled AI agent up and running!

### Prerequisites

1.  **Python:** You need Python installed on your computer.  It's recommended to use Python 3.7 or higher. You can download Python from the official website: [https://www.python.org/downloads/](https://www.python.org/downloads/)
2.  **Google Gemini API Key:** This project uses the Google Gemini API to power its AI capabilities. You'll need to obtain an API key from Google.  You can find information on how to get a Gemini API key on the [Google AI for Developers site](https://ai.google.dev/).  *(Look for information about Gemini API and how to set up a project and get an API key.)*

### Installation

1.  **Clone the Repository:**  Download the project files to your computer. If you are familiar with Git, you can clone the repository using:
    ```bash
    git clone https://github.com/prabeshAryal/FUN-AI-Conversational-Bestie.git
    ```
    If you are not using Git, you can download the project as a ZIP file and extract it.

2.  **Navigate to the Project Directory:** Open your terminal or command prompt and go to the folder where you saved the project files.

3.  **Install Required Python Packages:**  This project relies on several Python libraries. Install them using `pip`, the Python package installer. Run the following command in your terminal:
    ```bash
    pip install -r requirements.txt
    ```
    This command will read the `requirements.txt` file (which lists all the necessary libraries) and install them for you.

    **Note on `--break-system-packages`:**  You might see instructions online to use `--break-system-packages`. **It's generally NOT recommended** and can sometimes cause issues with your system.  The command above (`pip install -r requirements.txt`) should be sufficient in most cases. If you encounter issues, please describe them in the issues section of this repository (if applicable).

4.  **Set your Gemini API Key:** The program needs your Gemini API key to connect to Google's AI services. You need to set this as an environment variable named `GEMINI_API_KEY`.

    *   **How to set environment variables:**

        1.  Make a file named `.env` within project directory.
        2.  Place `GEMINI_API_KEY=THE_API_KEY_YOU_RECEIVED` in that file.
        3.  Save it, you're done. Python code will read automatically.
      
### Running the AI Agent

Once you have installed the requirements and set your API key, you can run the agent!

1.  **Navigate to the Project Directory (if you closed your terminal).**
2.  **Run the Python script:** Execute the main Python file (likely named `TestAI.py` or similar based on your description). Use the following command in your terminal:
    ```bash
    python TestAI.py
    ```

    The program should start, and you will see the message "Say something!" in your terminal.

3.  **Start Talking!** Speak into your microphone. The program will transcribe your speech, send it to the Gemini AI, receive a response, print the response in the terminal, and then speak the response back to you.

4.  **End the Conversation:** To stop the agent, say "goodbye". The agent will say "Goodbye!" and the program will exit.

## Usage

After running the script, simply speak naturally to the agent. You can ask questions, have conversations, or give it simple commands.

**Example Interactions:**

*   "Hello, how are you today?"
*   "What is the weather like?"
*   "Tell me a joke."
*   "Write a short poem about friendship."
*   "goodbye" (to end the conversation)

The agent will remember the conversation history within a single run, so you can have more context-aware exchanges.

## Configuration

*   **Gemini API Key:**  As mentioned in the "Installation" section, ensure you have correctly set the `GEMINI_API_KEY` environment variable.
*   **Model Selection (Advanced):** The code currently uses the `"gemini-2.0-flash-thinking-exp-01-21"` model. You can experiment with different Gemini models by changing this line in the `generate_content_with_gemini` function in `TestAI.py`.  Refer to the [Gemini API documentation](https://ai.google.dev/tutorials/python_quickstart) for available models and their capabilities.  For lower-powered laptops, you might want to try models that are optimized for speed and efficiency, but be aware that response quality might vary.
*   **Temperature and other parameters (Advanced):** The `generate_content_config` in the code allows for customization of the AI's response generation. You can adjust parameters like `temperature`, `top_p`, `top_k`, etc., to influence the creativity and randomness of the AI's replies.  Consult the Gemini API documentation for details on these parameters.

## Limitations and Considerations for Limited Memory Laptops

*   **Resource Usage:** While designed to be relatively lightweight, running AI models and speech processing can still consume resources. On very limited memory laptops, you might experience some slowdown or lag, especially during the initial setup or when the AI is generating complex responses.
*   **Model Choice:** The choice of Gemini model can impact performance.  More complex and powerful models generally require more resources. Experimenting with different models might be necessary to find a balance between response quality and performance on a low-memory machine.
*   **Internet Connection:** This agent relies on an internet connection to access the Gemini API.  A stable and reasonably fast internet connection is required for smooth operation.
*   **Background Noise:** Speech recognition can be affected by background noise. Using a good quality microphone and minimizing background noise will improve the accuracy of voice input.

## Contributing

If you'd like to contribute to this project, feel free to fork the repository and submit pull requests with your improvements!  Suggestions for new features, bug fixes, and optimizations are welcome.

## License


This project is of  MIT Licens. 

## Author

- [Prabesh](https://prabe.sh)

## Acknowledgements

*   Thanks to Google for providing the Gemini API.
*   Thanks to the developers of the `speech_recognition`, `pyttsx3`, and `google-generativeai` Python libraries.
*   And a special thank you to my little brother for the inspiration! 😄