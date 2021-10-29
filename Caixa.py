
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
        
    def fechar(self, caixas : list, nome_caixa : str):
        count = len(caixas)
        ultimo = caixas[count - 1]
        if ultimo.get_nome() == nome_caixa.get_nome():
            ultimo.fechar_Caixa()
            return "Caixa fechar com sucesso"
        p = 0
        p = count * 2
        count = count - p
        while count < p:
            print(caixas[count].get_nome())
            count+=1
        # i =0
        # emAberto = []
        # for itens in caixas:
        #     i+=1
        #     if itens.get_nome() == nome_caixa.get_nome():
        #         total = count - i
        #         print(total)
        #         while total < count:
        #             print("este é o total",total)
        #             print("este é o p",p)
        #             print(caixas[total].get_nome())
        #             emAberto.append(caixas[total])
        #             total+=1
        #         p = ''
        #         for itens in emAberto:
        #             p = str(itens.get_nome())+": "+ p
        #         if emAberto == []:
        #             nome_caixa.fechar_Caixa()
        #             return "Caixa fechado"
        #         else:
        #             return "Favor fechar esses caixas primeiro"+" "+p

    def fechar_Caixa(self):
        self.estado = 'fechado'

    def get_estado_Caixa(self):
        return self.estado

    def __len__(self):
        return len(self.clientes)
    
    def __repr__(self):
        return str(self.__dict__)