import requests
import json
import os
from dotenv import load_dotenv

load_dotenv()

url = "https://api.openai.com/v1/chat/completions"
openai_api_key = os.getenv("openai_api_key")
headers = {"Content-Type": "application/json", "Authorization": "Bearer {OPENAI_API_KEY}"}
data = {"model":"gpt-3.5-turbo", "messages": [{"role":"user", "content": "Qual é a capital da França?"}]}

response = requests.post(url, headers=headers, data=json.dumps(data))

if __name__ == "__main__": print(response.json()['choices'][0]['message']['content'])