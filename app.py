import openai
from apikey import APIKEY

openai.api_key = APIKEY

try:
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "user", "content": "Hello, testing API key."}
        ]
    )
    print(response)
except openai.error.AuthenticationError as e:
    print(f"Authentication Error: {e}")
