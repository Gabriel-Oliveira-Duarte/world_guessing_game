import requests
import random

URL = "https://restcountries.com/v3.1/all?fields=name,capital,population"


class ServicoAPI:
    def __init__(self):
        self.paises = self.buscar_paises()

    def buscar_paises(self):
        resposta = requests.get(URL, timeout=10)
        resposta.raise_for_status()
        return resposta.json()

    def sortear_pais(self):
        pais = random.choice(self.paises)

        nome = pais.get("name", {}).get("common", "Desconhecido")
        capital = pais.get("capital", ["Sem capital"])[0]
        populacao = pais.get("population", 1)

        return nome, capital, populacao
