import requests

def extract_dados_bitcoin():
    url = "https://api.coinbase.com/v2/prices/spot"
    response = requests.get(url)
    data = response.json()
    return data

if __name__ == "__main__": print(extract_dados_bitcoin()["data"])