import requests
from tinydb import TinyDB

def extract_dados_bitcoin():
    url = "https://api.coinbase.com/v2/prices/spot"
    response = requests.get(url)

    data = response.json()
    return data

def transform_dados_bitcoin(dados):
    valor = dados["data"]["amount"]
    criptomoeda = dados["data"]["base"]
    moeda = dados["data"]["currency"]
    
    dados_transformados = {"valor": valor, "criptomoeda": criptomoeda, "moeda": moeda}
    return dados_transformados

def salvar_dados_tinydb(dados, db_name="bitcoin.json"):
    db = TinyDB(db_name)
    db.insert(dados)
    print("Dados salvos com sucesso!")

if __name__ == "__main__":
     dados_json = extract_dados_bitcoin()
     dados_tratados = transform_dados_bitcoin(dados_json)
     salvar_dados_tinydb(dados_tratados)