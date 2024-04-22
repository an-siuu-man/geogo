import requests
import os

def generateResponse(prompt):

    # OpenAI API endpoint
    api_endpoint = 'https://api.openai.com/v1/chat/completions'
    keykey=""
    # for line in open("/home/ubuntu/geogo/geogobackend/geogo/api/apiKeys.txt", "r"):
    #     if "openai" in line:
    #         keykey = (line.split(",")[1].strip())

    file = open('geogo/api/apiKeys.txt', 'r')           #remove
    for line in file:                                   #these
        if 'openai' in line:                            #4
            keykey = line.split(',')[1].strip()         #lines
            
    # Request headers
    headers = {
        'Content-Type': 'application/json',
        'Authorization': f"Bearer {keykey}"
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
