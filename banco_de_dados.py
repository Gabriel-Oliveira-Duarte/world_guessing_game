import sqlite3
import datetime


class BancoDados:
    def __init__(self):
        self.conexao = sqlite3.connect("ranking.db")
        self.cursor = self.conexao.cursor()
        self.criar_tabela()

    def criar_tabela(self):
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS ranking (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                jogador TEXT,
                pontuacao INTEGER,
                data_hora TEXT
            )
        """)
        self.conexao.commit()

    def salvar_pontuacao(self, jogador, pontuacao):
        data_hora = datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S")
        self.cursor.execute("""
            INSERT INTO ranking (jogador, pontuacao, data_hora)
            VALUES (?, ?, ?)
        """, (jogador, pontuacao, data_hora))
        self.conexao.commit()

    def buscar_top5(self):
        self.cursor.execute("""
            SELECT jogador, pontuacao, data_hora
            FROM ranking
            ORDER BY pontuacao DESC
            LIMIT 5
        """)
        return self.cursor.fetchall()
