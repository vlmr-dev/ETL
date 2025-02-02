import requests

url = "https://api.coinbase.com/v2/prices/spot"
headers = {"Accept": "application/json", "User-Agent": "MinhaAplicacao/1.0"}
params = {"currency":"USD"}
response = requests.get(url, headers=headers, params=params)

data = response.json()

if __name__ == "__main__": print("Preço do Bitcoin (USD):", data["data"]["amount"])