from Pessoa import Pessoa

class Caixa:
    def __init__(self, nome):
        self.clientes = []
        self.nome = nome
        self.estado = 'fechado'
        
    def entrar(self, cliente : Pessoa):
        self.clientes.append(cliente)

    def sair(self):
        if len(self.clientes) < 0:
            return "O caixa {} ja está vazio".format(self.nome)
        return self.clientes.pop(0)

    def vazia(self):
        return len(self.clientes) == 0

    def set_nome(self, nome, caixas : list):
        p = False
        for caixa in caixas:
            if caixa.get_nome() == nome:
                print("O caixa {} já existe".format(nome))
                p = True
        if p == False:
            print("O caixa {} foi criado com sucesso".format(nome))
            self.nome = nome

    def get_nome(self):
        return self.nome

    def get_clientes(self):
        return self.clientes

    def abrir(self):
        self.estado = 'aberto'
    
    def fechar_Caixa(self):
        if self.vazia() == True:
            self.estado = 'fechado'
            return "O caixa {} foi fechado com sucesso".format(self.nome)
        else:
            return "O caixa {} não está vazio".format(self.nome)

    def get_estado_Caixa(self):
        return self.estado

    def __len__(self):
        return len(self.clientes)
    
    def __repr__(self):
        return str(self.__dict__)


    def fechar(self, caixas : list, nome_caixa : str):
        count = len(caixas)
        ultimo = caixas[count - 1]
        if ultimo.get_nome() == nome_caixa.get_nome():
            ultimo.fechar_Caixa()
            return "O Caixa {} foi fechado com sucesso".format(nome_caixa.get_nome())
        if ultimo.get_estado_Caixa() == 'aberto':
            return "Favor fechar o caixa " + ultimo.get_nome()

        t = -1
        p = -2
        o = count * 2
        count = count - o - 1
        while p > count:
            if caixas[p].get_nome() == nome_caixa.get_nome():
                if caixas[t].get_estado_Caixa() == 'aberto':
                    return "Favor fechar o caixa : "+ caixas[t].get_nome()
                else:
                    caixas[p].fechar_Caixa()
                    return "O Caixa {} foi fechado com sucesso".format(caixas[p].get_nome())
            p-=1
            t-=1