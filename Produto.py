class Produto:
    def __init__(self):
        self.nome = ''
        self.preco = ''

    def set_nome(self, nome):
        self.nome = nome

    def set_preco(self, preco):
        self.preco = preco

    def get_nome(self):
        return self.nome

    def get_preco(self):
        return self.preco