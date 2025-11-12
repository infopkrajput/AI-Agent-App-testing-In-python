from google import genai
import keys
# Create a keys.py file in the same directory with the following content:
# GOOGLE_API_KEY = "your_google_api_key_here"

client = genai.Client(api_key=keys.GOOGLE_API_KEY)

while True:
    user_input = input("Ask a question (or type 'exit' to quit): ")
    if user_input.lower() == 'exit':
        break

    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=user_input,
    )
    
    print("Response:", response.text)
    