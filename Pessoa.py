from Produto import Produto

class Pessoa:
    def __init__(self,):
        self.nome = ''
    
    def __str__(self):
        return self.nome

    def compras(self, Produto : list):
        self.compras = Produto

    def total(self):
        total = 0
        for c in self.compras:
            total += c.get_preco()
        return total

    def set_nome(self, nome):
        self.nome = nome

    def get_nome(self):
        return self.nome