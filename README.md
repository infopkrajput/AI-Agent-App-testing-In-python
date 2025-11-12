# AI-Agent-App-testing-In-python
This repository contains a simple Python application that interacts with Google's Gemini 2.5 Flash model using the `google-genai` library. The application allows users to ask questions and receive responses from the model in an interactive manner.

## Prerequisites
- Python 3.x
- `google-genai` library
- Google API key with access to Gemini models
## Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/infopkrajput/AI-Agent-App-testing-In-python.git
   cd AI-Agent-App-testing-In-python
   ```
2. Install the required library:
   ```bash
   pip install google-genai
   ```
3. Create a `keys.py` file in the same directory with the following content:
   ```python
    GOOGLE_API_KEY = "your_google_api_key_here"
    ```
## Usage
1. Run the application:
   ```bash
   python app.py
   ```
2. Ask questions to the Gemini 2.5 Flash model. Type 'exit' to quit the application.
## Example
```
Ask a question (or type 'exit' to quit): What is the capital of France?
Response: The capital of France is Paris.
```
