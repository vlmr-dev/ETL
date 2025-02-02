import requests
import json

url = "https://api.openai.com/v1/chat/completions"
headers = {"Content-Type": "application/json", "Authorization": "Bearer $OPENAI_API_KEY"}
data = {"model":"gpt-3.5-turbo", "messages": [{"role":"user", "content": "Qual é a capital da França?"}]}

response = requests.post(url, headers=headers, data=json.dumps(data))

if __name__ == "__main__": print(response.json()['choices'][0]['message']['content'])