from Produto import Produto


class Pessoa:

    def __init__(self, nome):
        self.nome = nome
        self.itens = []
    def __str__(self):
        return self.nome

    def compras(self, Produto : Produto):
        
        self.itens.append(Produto)

    def total(self):
        total = ''
        total = str(total)
        for c in self.itens:
            total += c.get_preco()
        return total

    def set_nome(self, nome):
        self.nome = nome

    def get_nome(self):
        return self.nome

    def get_compras(self):
        item = []
        for itens in self.itens:
            item.append(itens.get_nome())
        return item

    def remover_produto(self, nome):
        for c in self.itens:
            if c.get_nome() == nome:
                self.itens.remove(c)
