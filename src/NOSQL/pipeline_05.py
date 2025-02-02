import requests
import time
from tinydb import TinyDB
from datetime import datetime

def extract_dados_bitcoin():
    url = "https://api.coinbase.com/v2/prices/spot"
    response = requests.get(url)

    data = response.json()
    return data

def transform_dados_bitcoin(dados):
    valor = float(dados["data"]["amount"])
    criptomoeda = dados["data"]["base"]
    moeda = dados["data"]["currency"]
    timestamp = datetime.now().strftime("%Y/%m/%d %H:%M:%S")
    
    dados_transformados = {"valor": valor, "criptomoeda": criptomoeda, "moeda": moeda, "timestamp": timestamp}
    return dados_transformados

def salvar_dados_tinydb(dados, db_name="bitcoin.json"):
    db = TinyDB(db_name)
    db.insert(dados)
    print("Dados salvos com sucesso!")

if __name__ == "__main__":
     while True:
         dados_json = extract_dados_bitcoin()
         dados_tratados = transform_dados_bitcoin(dados_json)
         print("Dados tratados:")
         print(dados_tratados)
         salvar_dados_tinydb(dados_tratados)
         time.sleep(15)