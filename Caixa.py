
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
        i =0
        for itens in caixas:
            i+=1
            if itens.get_nome() == nome_caixa.get_nome():
                print("Este é o I : ",i)
                print("Este é o count : ",count)
                total = count - i
                print("Este é o total : ",total)
                p =  count
                while total < p:
                    print(caixas[total].get_nome())
                    total+=1
        # if caixas[count-1].get_estado_Caixa() == 'aberto':
        #     caixas[count-1].fechar_caixa()

    def fechar_Caixa(self):
        self.estado = 'fechado'

    def get_estado_Caixa(self):
        return self.estado

    def __len__(self):
        return len(self.clientes)
    
    def __repr__(self):
        return str(self.__dict__)