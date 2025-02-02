import requests

url = "https://api.coinbase.com/v2/prices/spot"

response = requests.get(url)

data = response.json()

if __name__ == "__main__": print(data)