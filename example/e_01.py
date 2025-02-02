import requests

url = 'https://www.google.com/'

response = requests.get(url)

if __name__ == "__main__": print (response)