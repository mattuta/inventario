import sqlite3 as db


class Produto:

    def __init__(self, descricao, marca):
        self.descricao = descricao
        self.marca = marca

    def cadastrar_produto(self):
        try:
            conexao = db.connect('inventario.db')

            c = conexao.cursor()

            c.execute("INSERT INTO produto (descricao, marca) VALUES (:descricao, :marca)",
                      {'descricao': self.descricao, 'marca': self.marca})

            conexao.commit()
            conexao.close()

        except ImportError:
            print("Ok! Deu alguma merda, mas tenha calma que nós vamos concertar.")

        return "OK"


    def adicionar_produto(self, produto, tamanho, quantidade, valor):
        try:
            conexao = db.connect('inventario.db')

            c = conexao.cursor()

            c.execute("INSERT INTO produto_lista (cod_produto, tamanho, quantidade, valor) VALUES (:cod_produto, :tamanho, :quantidade, :valor)",
                      {'cod_produto': self.produto, 'tamanho': self.tamanho, 'quantidade': self.quantidade, 'valor': self.valor})

            conexao.commit()
            conexao.close()

        except ImportError:
            print("Ok! Deu alguma merda, mas tenha calma que nós vamos concertar.")
        return "OK"
