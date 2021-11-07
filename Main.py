from types import new_class
from Pessoa import Pessoa
from Caixa import Caixa
from Produto import Produto
from time import sleep

def main():
    caixas = []
    produtos = []
    pessoas = []
    p=0
    while True:
        print('......')
        print(
            "Digite 0 para criar um caixa" + "\n",
            "Digite 1 para abrir um caixa" + "\n",
            "Digite 2 para fechar um caixa" + "\n",
            "Digite 3 para mostrar os caixas abertos" + "\n",
            "Digite 4 para criar um produto" + "\n",
            "Digite 5 para coloca um nome em uma pessoa" + "\n",
            "Digite 6 para adicionar um produto a uma pessoa" + "\n",
            "Digite 7 para mostrar os produtos cadastrados" + "\n",
            "Digite 8 para adicionar um pessoa ao caixa" + "\n",
            "Digite 9 para Atender um pessoa no caixa" + "\n",
            "\n",
            "Digite um numero acima"
        )
        opcao = int(input())
        match opcao:
            case 0:
                nome = input("Digite o nome do caixa: ")
                for itens in caixas:
                    if itens.nome == nome:
                        print("Nome ja existe")
                        sleep(2)
                        break
                else:
                    caixas.append(Caixa(nome))
                    print("Caixa criado com sucesso")
                    sleep(2)

            case 1:
                for itens in caixas:
                    if itens.get_estado_Caixa() == "fechado":
                        print(itens.get_nome())

                caixa = input("Digite qual caixa deseja abrir: ")
                for itens in caixas:
                    if caixa == itens.get_nome():
                        itens.abrir()
                        print("Caixa aberto")
                        sleep(2)
                        break
                else:
                    print("Caixa nao existe")
                    sleep(2)

            case 2:
                for itens in caixas:
                    if itens.get_estado_Caixa() == "aberto":
                        print(itens.get_nome())
                
                caixa = input("Digite qual caixa deseja fechar")
                for itens in caixas:
                    if caixa == itens.get_nome():
                        print(itens.fechar())
                        break
                else:
                    print("Caixa nao encontrado")

            case 3:
                for itens in caixas:
                    if itens.get_estado_Caixa() == "aberto":
                        print(itens.get_nome())
                sleep(2)

            case 4:
                nome = input("Digite o nome do Produto que deseja cadastrar : ")
                preco = input("Digite o preço do Produto que deseja cadastrar : ")
                for itens in produtos:
                    if itens.get_nome == nome:
                        print("Produto ja existe")
                        sleep(2)
                        break
                else:
                    produtos.append(Produto(nome, preco))

                    print("Produto cadastrado com sucesso")
                    sleep(2)

            case 5:
                nome = input("Digite o nome da pessoa que deseja cadastrar : ")
                pessoa = Pessoa(nome)
                pessoas.append(pessoa)
                print("Pessoa cadastrada com sucesso")
                sleep(2)

            case 6:
                p = 0
                pessoa = input("Digite o nome da pessoa que deseja adicionar um produto : ")
                produto = input("Digite o nome do produto que deseja adicionar : ")
                for itens in pessoas:
                    if p == 1:
                        break
                    if itens.get_nome() == pessoa:
                        for iten in produtos:
                            if iten.get_nome() == produto:
                                itens.compras(iten)
                                print("Produto adicionado com sucesso")
                                print(f"Produto no carrinho do(A) {itens.get_nome()} :",itens.get_compras())
                                sleep(2)
                                p = 1
                                break
                        else:
                            print("Produto nao existe")
                            sleep(2)
                            break

            case 7:
                for itens in produtos:
                    print(itens.get_nome(),itens.get_preco())
                sleep(2)
                
            case 8:
                p = 0
                caixa = input("Digite o nome do caixa que deseja adicionar uma pessoa : ")
                pessoa = input("Digite o nome da pessoa que deseja adicionar : ")
                for itens in caixas:
                    if p == 1:
                        break
                    if itens.get_nome() == caixa:
                        if itens.get_estado_Caixa() == "fechado":
                            print("Caixa esta fechado")
                            sleep(2)
                            break
                        for iten in pessoas:
                            if iten.get_nome() == pessoa:
                                itens.entrar(iten)
                                print("Pessoa adicionada com sucesso")
                                print("Pessoas no caixa :", [i.get_nome() for i in itens.get_clientes()])
                                sleep(2)
                                p = 1
                                break
                        else:
                            print("Pessoa nao existe")
                            sleep(2)
                            break

            case 9:
                caixa = input("Digite o nome do caixa que deseja atende a pessoa : ")
                for itens in caixas:
                    
                    print(itens.get_nome())
                    if itens.get_nome() == caixa:
                        print("Pessoas no caixa")
                        print([i.get_nome() for i in itens.get_clientes()], "\n")

                        print("Voçe esta atendendo o(a)", itens.get_clientes()[0])

                        pessoa = itens.get_clientes()[0]

                        print(f"total de itens do(a) {pessoa} : ", pessoa.get_compras())
                        print("\n")
                        print("Total da venda : ", pessoa.total(), "\n")
                        print("Digite 1 para pagar ou 2 para voltar ao caixa")
                        opcao = int(input())
                        match opcao:
                            case 1:
                                print(f"O(A) {pessoa} pagou com sucesso")            
                                itens.sair()
                                pessoas.pop(0)
                                sleep(2)
                            case 2:
                                print(f"O(A) {pessoa} voltou ao caixa") 
                                sleep(2)
                                break
                        
                        print("Pessoa removida com sucesso")
                        sleep(2)
                    
            case _:
                print("Opcao invalida")
                sleep(2)

if __name__ == "__main__":
    main()