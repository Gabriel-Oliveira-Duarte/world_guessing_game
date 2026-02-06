
---

# 🌍 World Guessing Game – Ranking Edition

Projeto educacional desenvolvido em **Python**, aplicando **Programação Orientada a Objetos (POO)**, consumo de **API REST**, uso de **bibliotecas nativas** e **interface gráfica com Tkinter**.
O jogo desafia o usuário a adivinhar o nome de um país a partir de uma dica (capital), calculando a pontuação com base no **tempo de resposta** e na **dificuldade do país**, mantendo um **ranking persistente** em banco de dados.

---

## 🚀 Tecnologias Utilizadas

* **Linguagem:** Python 3.x
* **Framework:** Tkinter (Interface Gráfica)
* **Banco de Dados:** SQLite3
* **API Externa:** Rest Countries (API REST)
* **Bibliotecas:**

  * `requests` (requisições HTTP)
  * `math` (cálculo de pontuação)
  * `datetime` (controle de tempo)
  * `random` (sorteio de países)

---

## 🧠 Conceitos Aplicados

* Programação Orientada a Objetos (POO)
* Separação de responsabilidades
* Consumo e tratamento de API REST
* Persistência de dados com SQLite
* Interface gráfica orientada a eventos
* Ranking em tempo real

---

## 🗂️ Arquitetura do Projeto

O sistema foi dividido em classes com responsabilidades bem definidas:

### 📁 Estrutura de Pastas

```
world_guessing_game/
│
├── banco_dados.py      # Persistência e ranking (SQLite)
├── servico_api.py      # Consumo da API de países
├── jogo_app.py         # Interface gráfica e lógica do jogo
├── main.py             # Arquivo principal de execução
└── ranking.db          # Criado automaticamente
```

### 📌 Classes Principais

* **BancoDados**
  Responsável por criar a conexão com o SQLite, gerar a tabela de ranking, salvar pontuações e retornar o Top 5.

* **ServicoAPI**
  Responsável por consumir a API Rest Countries, tratar o JSON retornado e sortear um país aleatório com seus dados.

* **JogoApp**
  Classe principal da aplicação, responsável pela interface gráfica (Tkinter), integração entre API, banco de dados e cálculo de pontuação.

---

## 🎮 Funcionamento do Jogo

1. O sistema sorteia um país aleatório através da API.
2. A capital do país é exibida como dica.
3. O tempo começa a ser contado no momento da exibição da dica.
4. O jogador digita o nome do país e confirma o palpite.
5. Se acertar:

   * A pontuação é calculada com base no tempo de resposta.
   * Um bônus matemático é aplicado conforme a população do país.
   * O resultado é salvo no banco de dados.
6. O ranking dos 5 melhores jogadores é atualizado em tempo real na interface.

---

## 📋 Pré-requisitos

Antes de executar o projeto, você precisa ter instalado:

* **Python 3.x** (marcar *Add to PATH* na instalação)
* **Conexão com a internet** (para consumo da API)
* **VS Code** ou outro editor Python (recomendado)

---

## 🔧 Instalação

### 1️⃣ Clonar ou baixar o repositório

```bash
git clone https://github.com/seu-usuario/world_guessing_game.git
```

### 2️⃣ Instalar dependências

A maioria das bibliotecas já vem com o Python.
Instale apenas a biblioteca de requisições:

```bash
pip install requests
```

---

## ▶️ Como Executar

No terminal, dentro da pasta do projeto:

```bash
python main.py
```

A interface gráfica será aberta automaticamente.

---

## 🧪 Testes Realizados

* Criação automática do banco de dados
* Consumo correto da API
* Cálculo de pontuação baseado em tempo
* Atualização do ranking em tempo real
* Fluxo contínuo do jogo sem reinicialização

---

## 📌 Observações Finais

Este projeto foi desenvolvido com foco educacional, seguindo boas práticas de organização de código, separação de responsabilidades e padrões utilizados em aplicações reais, servindo como base para portfólio acadêmico e profissional.

---

