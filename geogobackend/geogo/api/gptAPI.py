import requests
import os

def generateResponse(prompt):

    # OpenAI API endpoint
    api_endpoint = 'https://api.openai.com/v1/chat/completions'

    # Request headers
    headers = {
        'Content-Type': 'application/json',
        'Authorization': f"Bearer {os.environ.get('OPENAI_API_KEY')}"
    }

    # Request payload
    payload1 = {
    'model': 'gpt-4',
    'messages': [{'role': 'user', 'content': prompt}],
    'temperature': 0.8
    }

    response1 = requests.post(api_endpoint, json=payload1, headers=headers)
    l = response1.json()['choices'][0]['message']['content']
    return l

# print(generateResponse())