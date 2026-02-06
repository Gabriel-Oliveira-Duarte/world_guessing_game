import tkinter as tk
from tkinter import ttk, messagebox
import math
import datetime

from banco_de_dados import BancoDados
from servico_api import ServicoAPI


class JogoApp(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("World Guessing Game - Ranking")
        self.geometry("700x500")
        self.resizable(False, False)

        self.api = ServicoAPI()
        self.banco = BancoDados()

        self.nome_pais = ""
        self.populacao = 0
        self.inicio_tempo = None
        self.jogador = ""

        self.tela_inicial()

    def tela_inicial(self):
        self.frame_inicio = tk.Frame(self)
        self.frame_inicio.pack(expand=True)

        tk.Label(
            self.frame_inicio,
            text="World Guessing Game",
            font=("Arial", 20, "bold")
        ).pack(pady=20)

        tk.Label(
            self.frame_inicio,
            text="Digite seu nome:",
            font=("Arial", 12)
        ).pack(pady=5)

        self.entry_nome = tk.Entry(self.frame_inicio, font=("Arial", 12))
        self.entry_nome.pack(pady=5)

        tk.Button(
            self.frame_inicio,
            text="Iniciar Jogo",
            font=("Arial", 12, "bold"),
            command=self.iniciar_jogo
        ).pack(pady=20)

    def iniciar_jogo(self):
        nome = self.entry_nome.get().strip()
        self.jogador = nome if nome else "Anônimo"

        self.frame_inicio.destroy()
        self.criar_interface()
        self.novo_jogo()
        self.atualizar_ranking()

    def criar_interface(self):
        tk.Label(self, text="Dica (Capital):", font=("Arial", 14)).pack(pady=10)

        self.label_dica = tk.Label(self, font=("Arial", 18, "bold"))
        self.label_dica.pack(pady=10)

        tk.Label(self, text="Digite o nome do país:", font=("Arial", 12)).pack()

        self.entry_palpite = tk.Entry(self, font=("Arial", 12))
        self.entry_palpite.pack()

        tk.Button(
            self,
            text="Chutar!",
            font=("Arial", 12, "bold"),
            command=self.verificar_resposta
        ).pack(pady=10)

        tk.Label(self, text="Top 5 Jogadores", font=("Arial", 14, "bold")).pack(pady=10)

        self.tabela = ttk.Treeview(
            self,
            columns=("Jogador", "Pontuação", "Data"),
            show="headings",
            height=5
        )

        self.tabela.heading("Jogador", text="Jogador")
        self.tabela.heading("Pontuação", text="Pontuação")
        self.tabela.heading("Data", text="Data/Hora")

        self.tabela.column("Jogador", anchor="center", width=200)
        self.tabela.column("Pontuação", anchor="center", width=100)
        self.tabela.column("Data", anchor="center", width=200)

        self.tabela.pack(padx=20)

    def novo_jogo(self):
        self.nome_pais, capital, self.populacao = self.api.sortear_pais()
        self.label_dica.config(text=capital)
        self.entry_palpite.delete(0, tk.END)
        self.inicio_tempo = datetime.datetime.now()

    def verificar_resposta(self):
        palpite = self.entry_palpite.get().strip()

        if not palpite:
            messagebox.showwarning("Aviso", "Digite um país!")
            return

        tempo = (datetime.datetime.now() - self.inicio_tempo).total_seconds()

        if palpite.lower() == self.nome_pais.lower():
            pontos = self.calcular_pontuacao(tempo, self.populacao)
            self.banco.salvar_pontuacao(self.jogador, pontos)

            messagebox.showinfo(
                "Acertou!",
                f"País: {self.nome_pais}\nPontuação: {pontos}"
            )

            self.atualizar_ranking()
        else:
            messagebox.showerror(
                "Errou!",
                f"O país correto era: {self.nome_pais}"
            )

        self.novo_jogo()

    def calcular_pontuacao(self, tempo, populacao):
        base = math.floor(1000 / max(tempo, 1))
        multiplicador = math.log(1_000_000_000 / populacao + 1)
        return math.floor(base * multiplicador)

    def atualizar_ranking(self):
        for item in self.tabela.get_children():
            self.tabela.delete(item)

        for jogador, pontos, data in self.banco.buscar_top5():
            self.tabela.insert("", tk.END, values=(jogador, pontos, data))
