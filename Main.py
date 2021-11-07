from types import new_class
from Pessoa import Pessoa
from Caixa import Caixa
from Produto import Produto
from time import sleep

def main():
    caixas = []
    produtos = []
    pessoas = []
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
            "Digite 9 para remover um pessoa do caixa" + "\n",
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
                nome = input("Digite o nome da pessoa que deseja cadastrar")
                pessoa = Pessoa(nome)
                pessoas.append(pessoa)
                print("Pessoa cadastrada com sucesso")
                sleep(2)

            case 6:
                pessoa = input("Digite o nome da pessoa que deseja adicionar um produto")
                produto = input("Digite o nome do produto que deseja adicionar")
                for itens in pessoas:
                    if itens.get_nome == pessoa:
                        for iten in produtos:
                            if iten.get_nome == produto:
                                itens.compras(produto)
                                print("Produto adicionado com sucesso")
                                sleep(2)
                                break
                        else:
                            print("Produto nao existe")
                            sleep(2)
                            break
                else:
                    print("Pessoa nao existe")
                    sleep(2)

            case 7:
                for itens in produtos:
                    print(itens.get_nome())
                    print(itens.get_preco())
                sleep(2)
                
            case 8:
                caixa = input("Digite o nome do caixa que deseja adicionar uma pessoa")
                pessoa = input("Digite o nome da pessoa que deseja adicionar")
                for itens in caixas:
                    if itens.get_nome == caixa:
                        for iten in pessoas:
                            if iten.get_nome == pessoa:
                                itens.entrar(pessoa)
                                break
                        else:
                            print("Pessoa nao existe")
                            break
                else:
                    print("Caixa nao existe")

            case 9:
                caixa = input("Digite o nome do caixa que deseja remover uma pessoa")
                pessoa = input("Digite o nome da pessoa que deseja remover")
                for itens in caixas:
                    if itens.get_nome == caixa:
                        for iten in pessoas:
                            if iten.get_nome == pessoa:
                                itens.sair(pessoa)
                                break
                        else:
                            print("Pessoa nao existe")
                            break
                else:
                    print("Caixa nao existe")

            case _:
                print("Opcao invalida")
    
if __name__ == "__main__":
    main()