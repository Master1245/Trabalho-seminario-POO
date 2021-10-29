
class Caixa:
    def __init__(self):
        self.clientes = []
        self.nome = ''
        self.estado = ''
        
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

    def get_clientes(self):
        return self.clientes

    def abrir(self):
        self.estado = 'aberto'
        self.caixa = Caixa()
    def fechar(self):
        print(self.caixa)

    def get_estado_Caixa(self):
        return self.estado

    def __len__(self):
        return len(self.clientes)
    
    def __repr__(self):
        return str(self.__dict__)