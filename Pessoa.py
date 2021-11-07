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
        total = 0
        total = int(total)
        for c in self.itens:
            soma = int(c.get_preco())
            total += soma
        total = str(total)
        total = "R$" + total
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

    def get_compras_valor(self):
        item = []
        for itens in self.itens:
            item.append(itens.get_nome() + ": " +"R$"+ itens.get_preco())
        return item

    def remover_produto(self, nome):
        for c in self.itens:
            if c.get_nome() == nome:
                self.itens.remove(c)
