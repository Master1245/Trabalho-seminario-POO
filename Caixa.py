from Pessoa import Pessoa

class Caixa:
    def __init__(self):
        self.clientes = []
        self.nome = ''
        
    def entrar(self, cliente : list):
        for itens in cliente:
            self.clientes.append(itens)

    def sair(self):
        return self.clientes.pop(0)

    def vazia(self):
        return len(self.clientes) == 0

    def set_nome(self, nome):
        self.nome = nome

    def get_nome(self):
        return self.nome

    def __len__(self):
        return len(self.clientes)

