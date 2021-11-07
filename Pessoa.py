from Produto import Produto

compras = []
class Pessoa:
    def __init__(self, nome):
        self.nome = nome
    
    def __str__(self):
        return self.nome

    def compras(self, Produto : Produto):
        compras.append(Produto)

    def total(self):
        total = 0
        total = str(total)
        for c in compras:
            total += c.get_preco()
        return total

    def set_nome(self, nome):
        self.nome = nome

    def get_nome(self):
        return self.nome

    def get_compras(self):
        item = []
        for itens in compras:
            item.append(itens.get_nome())
        return item

    def remover_produto(self, nome):
        for c in compras:
            if c.get_nome() == nome:
                compras.remove(c)
