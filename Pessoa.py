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

    def get_compras(self):
        item = []
        for itens in self.compras:
           item.append(itens.get_nome())
        return item

    def remover_produto(self, nome):
        for c in self.compras:
            if c.get_nome() == nome:
                self.compras.remove(c)

    def get_caixa(self):
        caixa = []
        for c in self.compras:
            caixa.append(c.get_caixa())
        return caixa